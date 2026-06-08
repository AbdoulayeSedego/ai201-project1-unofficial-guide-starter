import chromadb
from sentence_transformers import SentenceTransformer
from ingest import load_documents, clean_text, chunk_text

# ── Constants ─────────────────────────────────────────────────────────────────

COLLECTION_NAME = "john_jay_guide"
EMBED_MODEL     = "all-MiniLM-L6-v2"
TOP_K           = 5

# ── Shared model + collection (loaded once) ───────────────────────────────────

print("Loading embedding model...")
_model  = SentenceTransformer(EMBED_MODEL)

_client = chromadb.PersistentClient(path="chroma_db")

# cosine distance: 0 = identical, 1 = completely different
# milestone checkpoint asks for top results below 0.5
_collection = _client.get_or_create_collection(
    COLLECTION_NAME,
    metadata={"hnsw:space": "cosine"}
)


# ── Stage 3: Embed + Store ────────────────────────────────────────────────────

def embed_and_store():
    """
    Load → clean → chunk all documents, embed every chunk with MiniLM,
    and write to ChromaDB with source metadata.
    Clears any existing data first so re-runs don't create duplicates.
    """
    global _collection
    # wipe existing data so this function is safe to re-run
    existing = _collection.count()
    if existing > 0:
        print(f"  Clearing {existing} existing chunks from collection...")
        _client.delete_collection(COLLECTION_NAME)
        # recreate with same settings
        _collection = _client.get_or_create_collection(
            COLLECTION_NAME,
            metadata={"hnsw:space": "cosine"}
        )

    print("Loading and chunking documents...")
    docs = load_documents("documents")

    ids, texts, metadatas = [], [], []
    for doc in docs:
        cleaned = clean_text(doc["text"])
        chunks  = chunk_text(cleaned)
        for i, chunk in enumerate(chunks):
            ids.append(f"{doc['source']}::{i}")
            texts.append(chunk)
            metadatas.append({"source": doc["source"], "chunk_index": i})

    print(f"  Embedding {len(texts)} chunks with {EMBED_MODEL}...")
    embeddings = _model.encode(texts, show_progress_bar=True, batch_size=64)

    print("  Writing to ChromaDB...")
    # ChromaDB add() has a limit per call — batch in groups of 500
    batch = 500
    for start in range(0, len(texts), batch):
        _collection.add(
            ids        = ids[start : start + batch],
            embeddings = embeddings[start : start + batch].tolist(),
            documents  = texts[start : start + batch],
            metadatas  = metadatas[start : start + batch],
        )

    print(f"  Stored {_collection.count()} chunks in '{COLLECTION_NAME}'.\n")


# ── Stage 4: Retrieve ─────────────────────────────────────────────────────────

def retrieve(query: str, k: int = TOP_K) -> list[dict]:
    """
    Embed `query` and return the top-k most similar chunks.
    Each result dict has: text, source, distance.
    Lower distance = more similar (cosine distance, range 0–1).
    """
    query_vec = _model.encode([query])[0].tolist()
    results   = _collection.query(
        query_embeddings = [query_vec],
        n_results        = k,
        include          = ["documents", "metadatas", "distances"],
    )

    chunks = []
    for text, meta, dist in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    ):
        chunks.append({
            "text":     text,
            "source":   meta["source"],
            "distance": round(dist, 4),
        })
    return chunks


# ── Main: embed everything, then test retrieval ───────────────────────────────

if __name__ == "__main__":
    embed_and_store()

    # 3 of the 5 evaluation-plan questions
    test_queries = [
        "What is the most a student can earn per hour through John Jay's "
        "Federal Work-Study program, and what determines eligibility?",

        "What is John Jay's 6-year graduation rate, and how does it compare "
        "to its 4-year rate?",

        "How often does John Jay hold its career/internship fairs, and roughly "
        "how many employers does the Career Learning Lab work with?",
    ]

    print("=" * 65)
    print("RETRIEVAL TEST — top-5 chunks per query")
    print("=" * 65)

    for q in test_queries:
        print(f"\nQUERY: {q}\n")
        results = retrieve(q)
        for rank, r in enumerate(results, 1):
            print(f"  [{rank}] distance={r['distance']}  source={r['source']}")
            # print first 200 chars of chunk so you can judge relevance
            print(f"      {r['text'][:200]}...")
        print()
