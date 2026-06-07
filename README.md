# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
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

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | John Jay — Student Organizations | Official (clubs) | https://www.jjay.cuny.edu/student-life/center-student-involvement-leadership/student-organizations |
| 2 | John Jay — Activities & Events | Official (events) | https://www.jjay.cuny.edu/student-life/center-student-involvement-leadership/activities-events |
| 3 | John Jay — PRISM Research Program | Official (opportunity) | https://www.jjay.cuny.edu/research/student-research/program-research-initiatives-science-math |
| 4 | John Jay — Honors & Achievement Programs | Official (opportunity) | https://www.jjay.cuny.edu/academics/undergraduate-programs/honors-achievement-programs |
| 5 | John Jay — Research & Creativity Scholarships | Official (opportunity) | https://www.jjay.cuny.edu/research/student-research/office-student-research-creativity/research-creativity-scholarships/undergraduategraduate-researchcreativity-assistant-scholarship |
| 6 | Niche — Reviews | Unofficial (reviews) | https://www.niche.com/colleges/cuny-john-jay-college-of-criminal-justice/reviews/ |
| 7 | Niche — Campus Life | Unofficial (reviews) | https://www.niche.com/colleges/cuny-john-jay-college-of-criminal-justice/campus-life/ |
| 8 | Rate My Professors — John Jay (#227) | Unofficial (reviews) | https://www.ratemyprofessors.com/school/227 |
| 9 | College Factual — Graduation & Retention | Third-party (stats) | https://www.collegefactual.com/colleges/cuny-john-jay-college-of-criminal-justice/academic-life/graduation-and-retention/ |
| 10 | Data USA — John Jay profile | Third-party (stats) | https://datausa.io/profile/university/cuny-john-jay-college-of-criminal-justice |
| 11 | John Jay — Quick Facts 2023 (PDF) | Official (stats) | https://www.jjay.cuny.edu/sites/default/files/2024-05/QUICK%20FACTS%202023.pdf |
| 12 | John Jay — Career Building & Job Search | Official (careers) | https://www.jjay.cuny.edu/student-life/career-building-job-search |
| 13 | John Jay — Spring Career & Internship Fair | Official (career fair) | https://www.jjay.cuny.edu/news-events/events/spring-career-internship-fair |
| 14 | John Jay — Career Fair news story | Official (career fair) | https://www.jjay.cuny.edu/news-events/news/career-internship-fair-gives-students-invaluable-networking-opportunities |
| 15 | John Jay — Federal Work-Study | Official (campus jobs) | https://www.jjay.cuny.edu/admissions/tuition-financial-aid/federal-work-study |
| 16 | CUNY Jobs — John Jay campus | Official (campus jobs) | https://cuny.jobs/campus/john-jay-college/jobs/ |

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**

**Overlap:**

**Why these choices fit your documents:**

**Final chunk count:**

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**

**Production tradeoff reflection:**

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**

**How source attribution is surfaced in the response:**

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

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

**What the system returned:**

**Root cause (tied to a specific pipeline stage):**

**What you would change to fix it:**

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**

**One way your implementation diverged from the spec, and why:**

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

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*

**Instance 2**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*
