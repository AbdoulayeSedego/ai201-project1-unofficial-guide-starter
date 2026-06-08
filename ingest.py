import os
import re
import random

# ── Stage 1: Load ────────────────────────────────────────────────────────────

def load_documents(folder="documents"):
    """Read every .txt file in folder. Returns list of {source, text} dicts."""
    docs = []
    for filename in sorted(os.listdir(folder)):
        if not filename.endswith(".txt"):
            continue
        filepath = os.path.join(folder, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            raw = f.read()
        docs.append({"source": filename, "text": raw})
    return docs


# ── Stage 2: Clean ───────────────────────────────────────────────────────────

# Lines that are pure navigation / boilerplate — remove them entirely.
BOILERPLATE_PATTERNS = [
    r"skip to (main )?content",
    r"john jay college of criminal justice logo",
    r"\(opens in (a )?new (window|tab)\)",
    r"^donate now$",
    r"we use cookies",
    r"privacy policy",
    r"cookie policy",
    r"skip to main content",
    r"^share$",
    r"^tweet$",
    r"^print$",
    r"^email$",
    r"^search$",
    r"read more",
    r"^sign (in|up)$",
    r"^log (in|out)$",
    r"^menu$",
    r"^navigation$",
    r"^\s*\|\s*$",           # lone pipe characters (nav separators)
    r"^(about|academics|admissions|research|student life|alumni|giving)$",
    # footer patterns
    r"©\s*\d{4}",                          # copyright line
    r"annual security report",
    r"student consumer information",
    r"website.*social media policies",
    r"guest speaker",
    r"^\d{3,5}\s+\w+.*,\s+[A-Z]{2}\s+\d{5}",  # address lines like "524 W 59th St, NY 10019"
    r"@jjay\.cuny\.edu",                   # email addresses
]
_BOILERPLATE_RE = re.compile(
    "|".join(BOILERPLATE_PATTERNS), re.IGNORECASE
)


def clean_text(text):
    """
    Remove navigation boilerplate, normalize whitespace.
    Returns cleaned plain text.
    """
    lines = text.splitlines()
    cleaned = []
    for line in lines:
        stripped = line.strip()
        # drop empty lines (we'll re-add single separators below)
        if not stripped:
            continue
        # drop known boilerplate
        if _BOILERPLATE_RE.search(stripped):
            continue
        # drop very short lines that are almost certainly nav links (< 3 words)
        if len(stripped.split()) < 3 and len(stripped) < 25:
            continue
        cleaned.append(stripped)

    # collapse runs of blank lines to a single newline
    result = "\n".join(cleaned)
    result = re.sub(r"\n{3,}", "\n\n", result)
    return result.strip()


# ── Stage 3: Chunk ───────────────────────────────────────────────────────────

def chunk_text(text, chunk_size=500, overlap=75):
    """
    Split text into overlapping chunks of up to `chunk_size` characters.
    Boundaries snap to the nearest whitespace so chunks never start or
    end mid-word. Each consecutive chunk starts `overlap` characters back
    from where the previous chunk ended.
    Returns list of non-empty strings.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        if end < len(text):
            # snap end backward to the nearest whitespace
            snap = text.rfind(" ", start, end)
            if snap > start:
                end = snap
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start += (end - start) - overlap  # step = chunk_length - overlap
        if start <= 0:
            break
    return chunks


# ── Main: run the full pipeline and inspect ──────────────────────────────────

if __name__ == "__main__":
    print("Loading documents...")
    docs = load_documents("documents")
    print(f"  Loaded {len(docs)} documents\n")

    all_chunks = []   # each entry: {"source": filename, "chunk": text}

    for doc in docs:
        cleaned = clean_text(doc["text"])
        chunks  = chunk_text(cleaned)
        for chunk in chunks:
            all_chunks.append({"source": doc["source"], "chunk": chunk})
        print(f"  {doc['source']:45s}  raw={len(doc['text']):>6} chars  "
              f"cleaned={len(cleaned):>6} chars  chunks={len(chunks)}")

    print(f"\nTotal chunks across all documents: {len(all_chunks)}")

    # ── Inspection: print 5 random chunks ────────────────────────────────────
    print("\n" + "="*60)
    print("SAMPLE CHUNKS (5 random)")
    print("="*60)
    sample = random.sample(all_chunks, min(5, len(all_chunks)))
    for i, item in enumerate(sample, 1):
        print(f"\n--- Chunk {i} | source: {item['source']} ---")
        print(item["chunk"])
        print(f"[length: {len(item['chunk'])} chars]")

    # ── Sanity checks ─────────────────────────────────────────────────────────
    print("\n" + "="*60)
    print("SANITY CHECKS")
    print("="*60)
    oversized   = [c for c in all_chunks if len(c["chunk"]) > 500]
    empty       = [c for c in all_chunks if not c["chunk"].strip()]
    print(f"  Chunks exceeding 500 chars : {len(oversized)}")
    print(f"  Empty chunks               : {len(empty)}")
    if oversized:
        print("  WARNING: some chunks are too long — check chunk_text()")
    if empty:
        print("  WARNING: empty chunks found — check clean_text()")
    if len(all_chunks) < 50:
        print("  WARNING: fewer than 50 chunks — documents may be too short "
              "or chunks too large")
    if len(all_chunks) > 2000:
        print("  WARNING: more than 2000 chunks — chunks may be too small")
    print("\nDone. Inspect the sample chunks above before moving to Milestone 4.")
