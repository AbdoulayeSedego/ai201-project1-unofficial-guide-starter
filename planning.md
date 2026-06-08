# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

**Domain: The unofficial student-experience guide to John Jay College of Criminal Justice (CUNY).**

This guide covers what it's actually like to be a John Jay student — the activities and clubs you can join, the academic and research opportunities you can pursue, what current/past students say about the school and its professors, how well students actually do (graduation and retention outcomes), and the concrete ways students find work and launch careers (career/internship fairs, on-campus jobs, Federal Work-Study).

Within that domain, the corpus is organized around six question themes:

1. **Extracurricular activities** — clubs, organizations, and campus events open to students.
2. **Student opportunities** — research programs, honors, and scholarships.
3. **Student reviews** — first-hand opinions on academics, professors, campus life, and the commuter experience.
4. **Graduation & retention outcomes** — official and third-party statistics on how students fare.
5. **Career-fair opportunities** — CareerCon / Career & Internship Fairs and what they offer.
6. **On-campus jobs** — Federal Work-Study and student employment on campus.

**Why this knowledge is valuable and hard to find officially:** A prospective or current John Jay student has to stitch this picture together from a dozen disconnected places — the official site buries clubs, career fairs, and work-study under different departments, while the honest "is this school worth it / which professors are good / is it just a commuter school" perspective lives on Niche, Rate My Professors, and Reddit, and the real outcome numbers live on third-party data sites. No single official channel answers "what's it actually like, and what can I get out of it?" This guide consolidates official facts with unofficial student sentiment so one question can be answered from one place.

> **Scope note:** This is a deliberately broad "experience guide" domain rather than a single narrow topic (e.g., only professor reviews). The benefit is wide question coverage; the risk is that retrieval has to discriminate between very different document types (statistics vs. opinion vs. event listings). The chunking and retrieval sections below address that.

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| #   | Source                                        | Description                                                                                          | URL or location                                                                                                                                                                        |
| --- | --------------------------------------------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | John Jay — Student Organizations              | Official list/description of clubs & student orgs (ALPFA, Law Society, Environmental Club, etc.)     | https://www.jjay.cuny.edu/student-life/center-student-involvement-leadership/student-organizations                                                                                     |
| 2   | John Jay — Activities & Events                | Official page on campus activities and events run by the Center for Student Involvement & Leadership | https://www.jjay.cuny.edu/student-life/center-student-involvement-leadership/activities-events                                                                                         |
| 3   | John Jay — PRISM Research Program             | Undergraduate research opportunity in science/math (eligibility, stipends, programs)                 | https://www.jjay.cuny.edu/research/student-research/program-research-initiatives-science-math                                                                                          |
| 4   | John Jay — Honors & Achievement Programs      | Honors program and achievement opportunities for high-performing students                            | https://www.jjay.cuny.edu/academics/undergraduate-programs/honors-achievement-programs                                                                                                 |
| 5   | John Jay — Research & Creativity Scholarships | $1,000 OSRC scholarships for undergrad/grad student research with faculty                            | https://www.jjay.cuny.edu/research/student-research/office-student-research-creativity/research-creativity-scholarships/undergraduategraduate-researchcreativity-assistant-scholarship |
| 6   | Niche — Reviews                               | First-hand student reviews of academics, value, and campus                                           | https://www.niche.com/colleges/cuny-john-jay-college-of-criminal-justice/reviews/                                                                                                      |
| 7   | Niche — Campus Life                           | Student opinions on safety, food, party scene, commuter experience                                   | https://www.niche.com/colleges/cuny-john-jay-college-of-criminal-justice/campus-life/                                                                                                  |
| 8   | Rate My Professors — John Jay (School #227)   | Aggregated professor ratings and student comments                                                    | https://www.ratemyprofessors.com/school/227                                                                                                                                            |
| 9   | College Factual — Graduation & Retention      | Third-party breakdown of 4-yr/6-yr grad rates and retention vs. peers                                | https://www.collegefactual.com/colleges/cuny-john-jay-college-of-criminal-justice/academic-life/graduation-and-retention/                                                              |
| 10  | Data USA — John Jay profile                   | Enrollment, graduation, demographics, and outcome statistics                                         | https://datausa.io/profile/university/cuny-john-jay-college-of-criminal-justice                                                                                                        |
| 11  | John Jay — Quick Facts 2023 (PDF)             | Official institutional retention/graduation numbers and degrees awarded                              | https://www.jjay.cuny.edu/sites/default/files/2024-05/QUICK%20FACTS%202023.pdf                                                                                                         |
| 12  | John Jay — Career Building & Job Search       | Career Learning Lab, Handshake, VMock, employer connections overview                                 | https://www.jjay.cuny.edu/student-life/career-building-job-search                                                                                                                      |
| 13  | John Jay — Spring Career & Internship Fair    | Event page for the recruitment fair (CareerCon)                                                      | https://www.jjay.cuny.edu/news-events/events/spring-career-internship-fair                                                                                                             |
| 14  | John Jay — Career Fair news story             | Student perspective on networking at the Career & Internship Fair                                    | https://www.jjay.cuny.edu/news-events/news/career-internship-fair-gives-students-invaluable-networking-opportunities                                                                   |
| 15  | John Jay — Federal Work-Study                 | On-campus/off-campus FWS jobs, eligibility, pay ($ up to ~$17/hr)                                    | https://www.jjay.cuny.edu/admissions/tuition-financial-aid/federal-work-study                                                                                                          |
| 16  | CUNY Jobs — John Jay campus                   | Live listing of campus job openings (incl. student positions)                                        | https://cuny.jobs/campus/john-jay-college/jobs/                                                                                                                                        |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**
500 characters
**Overlap:**
75 characters
**Final chunk count:** 347 chunks across 16 documents
**Reasoning:**
I have decided to use 500 chars because it is large enough to hold a complete short review or a full official-page paragraph as a unit, but small enough to keep one chunk = one topic.If chunk A ends mid-review and chunk B starts with a different student's take, retrieval might return a chunk that answers two different questions poorly instead of one question well.

I use 75 char for overlap to give the LLM enough context from chunk A and chunk B without wasting space or making exact copies of chunks. Without overlap, a fact that falls at a chunk boundary won't appear complete in either chunk, so retrieval returns an incomplete answer.

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**
all-MiniLM-L6-v2
**Top-k:**
5
k=1 risks missing the answer if it ranked second; k=10 floods the LLM with off-topic noise. k=5 balances enough context with focused retrieval across my six document types.
**Production tradeoff reflection:**
MiniLM's 256-token limit is fine for my 500-char chunks, but if I wanted larger chunks (say 1500 chars ≈ 375 tokens), text would get silently truncated and the embedding would only represent the first half. A production model with a higher limit (e.g., 8,000 tokens) removes that ceiling. Since MiniLM is general-purpose, it might not rank criminal-justice or university-specific terms as precisely as a model fine-tuned on that kind of text — but a domain-specific model is harder to find and may miss broader questions.
In production, I might consider an API-hosted model (e.g., OpenAI text-embedding-3-large) which is more accurate — but it costs money per embedding, adds network latency, and sends my documents to a third-party server. MiniLM avoids all three of those downsides by running locally.

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| #   | Question                                                                                                                                     | Expected answer                                                                                                                                                                                                                  |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | What is the most a student can earn per hour through John Jay's Federal Work-Study program, and what determines eligibility?                 | Pay ranges from minimum wage up to ~$17.00/hour; eligibility is based on financial need and requires completing the FAFSA (checking the FWS box), awarded first-come, first-served. _(Source #15 — Federal Work-Study)_          |
| 2   | What is John Jay's 6-year graduation rate, and how does it compare to its 4-year rate?                                                       | ~54% 6-year graduation rate vs. ~38% 4-year rate (retention ~81% full-time). _(Sources #9 / #11 — College Factual, Quick Facts 2023)_                                                                                            |
| 3   | How often does John Jay hold its career/internship fairs, and roughly how many employers does the Career Learning Lab work with?             | John Jay runs CareerCon ~5 times per academic year (industry-aligned fairs in fall and spring); the Career Learning Lab maintains connections with 4,400+ employers. _(Sources #12 / #13 — Career Building, Spring Career Fair)_ |
| 4   | Name two student clubs or organizations a John Jay student can join, and what one of them focuses on.                                        | Any two of, e.g., ALPFA (accounting/finance career opportunities), Law Society, Environmental Club, Habitat for Humanity (affordable-housing/homelessness awareness), Legally Conscious. _(Source #1 — Student Organizations)_   |
| 5   | According to student reviews, what is the most common criticism of the social scene at John Jay, and how do students describe campus safety? | It's frequently described as a commuter school where social interaction is harder; on safety, ~97% of students say they feel extremely safe/secure on campus. _(Sources #6 / #7 — Niche Reviews & Campus Life)_                  |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1.The retrieval mechanism cannot make the difference between opinion and fact especially from Niche and Rate My Professors, where student opinions and actual statistics live in the same corpus.

2.once I ingest the documents there is no way the ingestion mechanism can later on refresh to new data, it might answer question with outdated data for example, if John Jay updates the Federal Work-Study pay cap or career fair schedule after ingestion, the system will still return the old figures.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

---

┌─────────────────────────────────────────────────────────────────────┐
│ THE UNOFFICIAL JOHN JAY GUIDE │
└─────────────────────────────────────────────────────────────────────┘

[1] INGESTION [2] CHUNKING [3] EMBED + STORE
documents/\*.txt,.pdf → chunk_text() → all-MiniLM-L6-v2
(Python, pdfplumber) ~500 chars / 75 ovlp → vectors → ChromaDB
│
▼
┌─────────────────────────────────────────────────────┐
│ user question │
│ │ │
│ ▼ │
│ [4] RETRIEVAL: embed question (MiniLM) │
│ → ChromaDB similarity search → top-k=5 chunks │
│ │ │
│ ▼ │
│ [5] GENERATION: chunks + question → grounded prompt │
│ → Groq (Llama) → answer + cited sources │
└─────────────────────────────────────────────────────┘

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**
I will give Claude my Documents section (16 sources, mix of .txt and one .pdf) and my Chunking Strategy section (500 chars / 75 overlap) and ask it to implement two functions: `load_documents()` that reads all files from the documents/ folder, and `chunk_text(text, chunk_size=500, overlap=75)` that returns a list of string chunks. I will verify the output by printing 5 chunks and confirming: no chunk exceeds 500 characters, the overlap text from the end of one chunk appears at the start of the next, and there are no empty strings or HTML artifacts in the output.

**Milestone 4 — Embedding and retrieval:**
I will give Claude my Retrieval Approach section (all-MiniLM-L6-v2, top-k=5) and the Architecture diagram from this file and ask it to implement `embed_and_store()` (embeds all chunks with SentenceTransformer and writes them to ChromaDB with source metadata) and `retrieve(query, k=5)` (embeds the query and returns the top-5 matching chunks with their source names and distance scores). I will verify by running 3 of my 5 evaluation questions and checking that the returned chunks visibly relate to each question and that distance scores are below 0.5.

**Milestone 5 — Generation and interface:**
I will give Claude my grounded generation requirement (answer only from retrieved context, cite sources, refuse if documents don't contain the answer) and the Gradio skeleton from the milestone instructions and ask it to implement an `ask(question)` function that combines retrieval with a Groq/Llama API call using a grounding system prompt, plus an `app.py` with a Gradio interface. I will verify grounding by asking one question my documents don't cover and confirming the system says it doesn't have enough information rather than generating a plausible-sounding answer from general knowledge.
