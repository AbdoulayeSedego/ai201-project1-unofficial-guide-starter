# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section _after_ you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

**The unofficial student-experience guide to John Jay College of Criminal Justice (CUNY).**

The system answers "what's it actually like, and what can I get out of it?" for John Jay students across six themes: extracurricular activities and clubs, student opportunities (research/honors/scholarships), student reviews, graduation & retention outcomes, career-fair opportunities, and on-campus jobs.

This knowledge is valuable but scattered: official facts are buried across unrelated departmental pages, honest sentiment about professors and the commuter experience lives on Niche/Rate My Professors/Reddit, and real outcome numbers live on third-party data sites. No single official channel combines them — this guide does, pairing official facts with unofficial student opinion so one question can be answered from one place.

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| #   | Source                                        | Type                   | URL or file path                                                                                                                                                                       |
| --- | --------------------------------------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | John Jay — Student Organizations              | Official (clubs)       | https://www.jjay.cuny.edu/student-life/center-student-involvement-leadership/student-organizations                                                                                     |
| 2   | John Jay — Activities & Events                | Official (events)      | https://www.jjay.cuny.edu/student-life/center-student-involvement-leadership/activities-events                                                                                         |
| 3   | John Jay — PRISM Research Program             | Official (opportunity) | https://www.jjay.cuny.edu/research/student-research/program-research-initiatives-science-math                                                                                          |
| 4   | John Jay — Honors & Achievement Programs      | Official (opportunity) | https://www.jjay.cuny.edu/academics/undergraduate-programs/honors-achievement-programs                                                                                                 |
| 5   | John Jay — Research & Creativity Scholarships | Official (opportunity) | https://www.jjay.cuny.edu/research/student-research/office-student-research-creativity/research-creativity-scholarships/undergraduategraduate-researchcreativity-assistant-scholarship |
| 6   | Niche — Reviews                               | Unofficial (reviews)   | https://www.niche.com/colleges/cuny-john-jay-college-of-criminal-justice/reviews/                                                                                                      |
| 7   | Niche — Campus Life                           | Unofficial (reviews)   | https://www.niche.com/colleges/cuny-john-jay-college-of-criminal-justice/campus-life/                                                                                                  |
| 8   | Rate My Professors — John Jay (#227)          | Unofficial (reviews)   | https://www.ratemyprofessors.com/school/227                                                                                                                                            |
| 9   | College Factual — Graduation & Retention      | Third-party (stats)    | https://www.collegefactual.com/colleges/cuny-john-jay-college-of-criminal-justice/academic-life/graduation-and-retention/                                                              |
| 10  | Data USA — John Jay profile                   | Third-party (stats)    | https://datausa.io/profile/university/cuny-john-jay-college-of-criminal-justice                                                                                                        |
| 11  | John Jay — Quick Facts 2023 (PDF)             | Official (stats)       | https://www.jjay.cuny.edu/sites/default/files/2024-05/QUICK%20FACTS%202023.pdf                                                                                                         |
| 12  | John Jay — Career Building & Job Search       | Official (careers)     | https://www.jjay.cuny.edu/student-life/career-building-job-search                                                                                                                      |
| 13  | John Jay — Spring Career & Internship Fair    | Official (career fair) | https://www.jjay.cuny.edu/news-events/events/spring-career-internship-fair                                                                                                             |
| 14  | John Jay — Career Fair news story             | Official (career fair) | https://www.jjay.cuny.edu/news-events/news/career-internship-fair-gives-students-invaluable-networking-opportunities                                                                   |
| 15  | John Jay — Federal Work-Study                 | Official (campus jobs) | https://www.jjay.cuny.edu/admissions/tuition-financial-aid/federal-work-study                                                                                                          |
| 16  | CUNY Jobs — John Jay campus                   | Official (campus jobs) | https://cuny.jobs/campus/john-jay-college/jobs/                                                                                                                                        |

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**
500 characters
**Overlap:**
75 overlap
**Why these choices fit your documents:**
I have decided to use 500 chars because it is large enough to hold a complete short review or a full official-page paragraph as a unit, but small enough to keep one chunk = one topic. If chunk A ends mid-review and chunk B starts with a different student's take, retrieval might return a chunk that answers two different questions poorly instead of one question well.

I use 75 chars for overlap to give the LLM enough context from chunk A and chunk B without wasting space or making exact copies of chunks. Without overlap, a fact that falls at a chunk boundary won't appear complete in either chunk, so retrieval returns an incomplete answer.

Before chunking, `clean_text()` removes navigation menus ("Skip to main content", "Donate now"), cookie banners, page footers (copyright lines, email addresses), and very short nav-link lines. Chunk boundaries are snapped to the nearest whitespace so no chunk starts or ends mid-word.

**Final chunk count:** 347 chunks across 16 documents

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**
all-MiniLM-L6-v2
it's free, runs locally (no API key), fast, and solid for English text.
**Production tradeoff reflection:**
 MiniLM's 256-token limit is fine for my 500-char chunks, but if I wanted larger chunks (say 1500 chars ≈ 375 tokens), text would get silently truncated and the embedding would only represent the first half. A production model with a higher limit (e.g., 8,000 tokens) removes that ceiling. Since MiniLM is general-purpose, it might not rank criminal-justice or university-specific terms as precisely as a model fine-tuned on that kind of text — but a domain-specific model is harder to find and may miss broader questions.
 In production, I might consider an API-hosted model (e.g., OpenAI text-embedding-3-large) which is more accurate — but it costs money per embedding, adds network latency, and sends my documents to a third-party server. MiniLM avoids all three of those downsides by running locally.
---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**
The system prompt in `generate.py` enforces grounding with two explicit rules:

```
You are an unofficial student guide for John Jay College of Criminal Justice.

Answer the user's question using ONLY the information in the documents provided below.
Do not use any knowledge from your training data. Do not guess or infer details not stated in the documents.

If the provided documents do not contain enough information to answer the question, respond with:
"I don't have enough information in my documents to answer that question."

At the end of your answer, always list the source documents you used under a "Sources:" heading.
```

The context is structured so each retrieved chunk is labeled `[Document N — filename]` before its text. This makes attribution explicit in the prompt itself rather than relying on the model to invent citations.

Temperature is set to 0.2 (near-minimum) to reduce the chance of the model elaborating beyond the provided text.

**How source attribution is surfaced in the response:**
Source filenames are collected programmatically from the retrieved chunks — not generated by the LLM. After the model responds, `ask()` builds a `sources` list from the metadata of the top-k chunks and returns it alongside the answer. The Gradio UI displays this in a separate "Retrieved from" panel so the user always sees which documents were used, independent of what the model chose to cite in its text.

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| #   | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
| --- | -------- | --------------- | ---------------------------- | ----------------- | ----------------- |
| 1   | What is the most a student can earn per hour through John Jay's Federal Work-Study program, and what determines eligibility? | Pay up to ~$17/hr; eligibility based on financial need + FAFSA, first-come first-served | "I don't have enough information in my documents to answer that question." — refused even though federal_work_study.txt was retrieved | Partially relevant — correct document retrieved but the chunk with the $17/hr figure ranked outside top-7 | Inaccurate — answer exists in corpus but wrong chunk surfaced |
| 2   | What is John Jay's 6-year graduation rate, and how does it compare to its 4-year rate? | ~54% 6-year vs ~38% 4-year | "46% at 6 years (first-time/full-time), 52% overall; 23% at 4 years (first-time/full-time), 38% overall" — correctly distinguishes two cohorts | Relevant — all top results from graduate_rate_retention.txt, distances 0.20–0.24 | Accurate |
| 3   | How often does John Jay hold its career/internship fairs, and roughly how many employers does the Career Learning Lab work with? | ~5 times per year (CareerCon); 4,400+ employers | "Each semester; 101 employers at one event" — frequency roughly correct, employer count from one event only | Partially relevant — career_fair.txt retrieved but the career_building.txt chunk containing 4,400+ employer figure did not rank in top-7 | Partially accurate |
| 4   | Name two student clubs or organizations a John Jay student can join, and what one of them focuses on. | Any two clubs with one described (e.g. ALPFA, Law Society, Habitat for Humanity) | "Food Security Advocates Club (addresses food insecurity) and English Honor Society/Sigma Tau Delta" — specific and accurate | Relevant — all top results from student_organizations.txt | Accurate |
| 5   | According to student reviews, what is the most common criticism of the social scene at John Jay, and how do students describe campus safety? | Commuter school = social interaction harder; ~97% feel safe | "Overcrowding during community hour is the main criticism; no campus safety information found in documents" — different valid criticism, safety stat not retrieved | Partially relevant — campus_life.txt and nich_review.txt retrieved but the 97% safety figure was not in the surfaced chunks | Partially accurate |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**
"What is the most a student can earn per hour through John Jay's Federal Work-Study program, and what determines eligibility?"

**What the system returned:**
"I don't have enough information in my documents to answer that question." — even though `federal_work_study.txt` appeared in the retrieved documents at rank 1 and 3.

**Root cause (tied to a specific pipeline stage):**
This is a retrieval failure. The `$17.00 per hour` figure lives in chunk 7 of `federal_work_study.txt`, which is a paragraph about payment procedures and timesheets. The surrounding context ("Your FWS supervisor must submit timesheets…", "you can only be paid for hours you have worked…") dilutes the semantic signal, so the embedding for that chunk is closer to "payment administration" than "how much can I earn." With k=7, the two chunks from `federal_work_study.txt` that did surface were the intro paragraph (chunk 0) and a freshmen eligibility paragraph (chunk 3) — neither contains the pay rate. The model correctly refused rather than hallucinating, which means grounding worked, but retrieval did not bring the right chunk.

**What you would change to fix it:**
Two options: (1) increase k to 10–12 so more chunks from the same document compete — this increases the chance the pay-rate chunk surfaces but also adds noise. (2) At ingestion time, split the Q&A-formatted sections of `federal_work_study.txt` by question boundary rather than fixed character count, so the pay rate and eligibility rules each become their own chunk with a cleaner semantic signal. A hybrid chunker that respects paragraph/Q&A structure would prevent this fact from being buried in procedural context.

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**
Organizing the domain into six specific question themes in planning.md directly shaped how I collected documents. Because I had written down "on-campus jobs" and "career-fair opportunities" as separate themes, I knew I needed distinct sources for each rather than relying on one general page. When I ran the retrieval tests, I could check each query against the theme it belonged to, which made it much easier to spot that Q3 was failing because the 4,400-employer figure lived in the career-building page (source #12), not the career-fair news story (source #14) — two documents I collected precisely because the spec listed them as separate subtopics.

**One way your implementation diverged from the spec, and why:**
The spec set top-k=5 based on reasoning that five chunks would give the LLM enough context without adding noise. During Milestone 4 testing, retrieval showed that some answers — particularly multi-part questions about a single document like the Federal Work-Study page — required more than one chunk from the same source to surface the complete answer. I increased k to 7 after seeing that the graduation-rate question needed multiple chunks from the same file to give the full breakdown (first-time/full-time vs. overall). The spec's k=5 reasoning was sound in theory but didn't account for documents structured as long Q&A pages where a single answer spans several 500-character chunks.

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- _What I gave the AI:_ My Documents section (16 sources, mix of .txt files) and my Chunking Strategy section (500 chars / 75 overlap, reasoning about mixed document types) from planning.md.
- _What it produced:_ `ingest.py` with `load_documents()`, `clean_text()`, and `chunk_text()`. The initial `chunk_text()` used a simple fixed-character slice (`text[start:end]`) that cut at exactly 500 characters regardless of word boundaries.
- _What I changed or overrode:_ I inspected 5 sample chunks and found two started mid-word (e.g., `"ion at CUNY..."`, `"reer plans?"`). I directed Claude to fix the boundary logic using `rfind(" ")` to snap each chunk end to the nearest whitespace. I also found that the footer pattern `"© 2026 John Jay College"` was surviving cleaning and added it to `BOILERPLATE_PATTERNS`.

**Instance 2**

- _What I gave the AI:_ My Retrieval Approach section (all-MiniLM-L6-v2, top-k=5) and the Architecture diagram from planning.md, plus the grounded generation requirement (answer only from documents, refuse if not found, cite sources).
- _What it produced:_ `embed.py` with `embed_and_store()` and `retrieve()`, and `generate.py` with `ask()` using a system prompt that instructed the model to answer only from provided documents. It also produced `app.py` with a Gradio interface.
- _What I changed or overrode:_ After running the 5 evaluation questions, Q1 (Federal Work-Study) failed because the $17/hr chunk wasn't surfacing. I directed Claude to investigate and then increased k from 5 to 7 in both `embed.py` and `generate.py`. I also verified that the `temperature=0.2` setting was appropriate for faithful grounding — the default would have been higher and more likely to generate beyond the source text.
