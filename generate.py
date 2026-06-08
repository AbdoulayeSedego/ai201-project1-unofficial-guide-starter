import os
from groq import Groq
from dotenv import load_dotenv
from embed import retrieve

load_dotenv()

_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "llama-3.3-70b-versatile"

# ── Grounding system prompt ───────────────────────────────────────────────────
# This is the mechanism that prevents the LLM from answering beyond
# the retrieved documents. Two rules enforced here:
#   1. Only use information explicitly present in the provided documents.
#   2. If the documents don't contain enough to answer, say so — don't guess.
SYSTEM_PROMPT = """You are an unofficial student guide for John Jay College of Criminal Justice.

Answer the user's question using ONLY the information in the documents provided below.
Do not use any knowledge from your training data. Do not guess or infer details not stated in the documents.

If the provided documents do not contain enough information to answer the question, respond with:
"I don't have enough information in my documents to answer that question."

At the end of your answer, always list the source documents you used under a "Sources:" heading."""


def ask(question: str, k: int = 7) -> dict:
    """
    Full RAG pipeline: retrieve relevant chunks → build grounded prompt → generate answer.
    Returns {"answer": str, "sources": list[str], "chunks": list[dict]}
    """
    # Stage 4: retrieve top-k chunks
    chunks = retrieve(question, k=k)

    # Build context block — number each chunk and label its source
    context_parts = []
    for i, chunk in enumerate(chunks, 1):
        context_parts.append(
            f"[Document {i} — {chunk['source']}]\n{chunk['text']}"
        )
    context = "\n\n".join(context_parts)

    # Stage 5: grounded generation
    user_message = f"""Documents:
{context}

Question: {question}"""

    response = _client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": user_message},
        ],
        temperature=0.2,   # low temperature = more faithful to source text
        max_tokens=1024,
    )

    answer = response.choices[0].message.content

    # Collect unique source filenames from retrieved chunks
    sources = list(dict.fromkeys(c["source"] for c in chunks))

    return {"answer": answer, "sources": sources, "chunks": chunks}


# ── Quick end-to-end test ─────────────────────────────────────────────────────

if __name__ == "__main__":
    test_questions = [
        # Should answer from federal_work_study.txt
        "What is the most a student can earn per hour through John Jay's "
        "Federal Work-Study program, and what determines eligibility?",

        # Should answer from graduate_rate_retention.txt
        "What is John Jay's 6-year graduation rate, and how does it compare "
        "to its 4-year rate?",

        # Should trigger refusal — not in any document
        "What is the application deadline for John Jay's spring semester?",
    ]

    for q in test_questions:
        print("\n" + "=" * 65)
        print(f"Q: {q}")
        print("=" * 65)
        result = ask(q)
        print(result["answer"])
        print(f"\nSources: {', '.join(result['sources'])}")
