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

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | John Jay — Student Organizations | Official list/description of clubs & student orgs (ALPFA, Law Society, Environmental Club, etc.) | https://www.jjay.cuny.edu/student-life/center-student-involvement-leadership/student-organizations |
| 2 | John Jay — Activities & Events | Official page on campus activities and events run by the Center for Student Involvement & Leadership | https://www.jjay.cuny.edu/student-life/center-student-involvement-leadership/activities-events |
| 3 | John Jay — PRISM Research Program | Undergraduate research opportunity in science/math (eligibility, stipends, programs) | https://www.jjay.cuny.edu/research/student-research/program-research-initiatives-science-math |
| 4 | John Jay — Honors & Achievement Programs | Honors program and achievement opportunities for high-performing students | https://www.jjay.cuny.edu/academics/undergraduate-programs/honors-achievement-programs |
| 5 | John Jay — Research & Creativity Scholarships | $1,000 OSRC scholarships for undergrad/grad student research with faculty | https://www.jjay.cuny.edu/research/student-research/office-student-research-creativity/research-creativity-scholarships/undergraduategraduate-researchcreativity-assistant-scholarship |
| 6 | Niche — Reviews | First-hand student reviews of academics, value, and campus | https://www.niche.com/colleges/cuny-john-jay-college-of-criminal-justice/reviews/ |
| 7 | Niche — Campus Life | Student opinions on safety, food, party scene, commuter experience | https://www.niche.com/colleges/cuny-john-jay-college-of-criminal-justice/campus-life/ |
| 8 | Rate My Professors — John Jay (School #227) | Aggregated professor ratings and student comments | https://www.ratemyprofessors.com/school/227 |
| 9 | College Factual — Graduation & Retention | Third-party breakdown of 4-yr/6-yr grad rates and retention vs. peers | https://www.collegefactual.com/colleges/cuny-john-jay-college-of-criminal-justice/academic-life/graduation-and-retention/ |
| 10 | Data USA — John Jay profile | Enrollment, graduation, demographics, and outcome statistics | https://datausa.io/profile/university/cuny-john-jay-college-of-criminal-justice |
| 11 | John Jay — Quick Facts 2023 (PDF) | Official institutional retention/graduation numbers and degrees awarded | https://www.jjay.cuny.edu/sites/default/files/2024-05/QUICK%20FACTS%202023.pdf |
| 12 | John Jay — Career Building & Job Search | Career Learning Lab, Handshake, VMock, employer connections overview | https://www.jjay.cuny.edu/student-life/career-building-job-search |
| 13 | John Jay — Spring Career & Internship Fair | Event page for the recruitment fair (CareerCon) | https://www.jjay.cuny.edu/news-events/events/spring-career-internship-fair |
| 14 | John Jay — Career Fair news story | Student perspective on networking at the Career & Internship Fair | https://www.jjay.cuny.edu/news-events/news/career-internship-fair-gives-students-invaluable-networking-opportunities |
| 15 | John Jay — Federal Work-Study | On-campus/off-campus FWS jobs, eligibility, pay ($ up to ~$17/hr) | https://www.jjay.cuny.edu/admissions/tuition-financial-aid/federal-work-study |
| 16 | CUNY Jobs — John Jay campus | Live listing of campus job openings (incl. student positions) | https://cuny.jobs/campus/john-jay-college/jobs/ |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**

**Overlap:**

**Reasoning:**

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**

**Top-k:**

**Production tradeoff reflection:**

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is the most a student can earn per hour through John Jay's Federal Work-Study program, and what determines eligibility? | Pay ranges from minimum wage up to ~$17.00/hour; eligibility is based on financial need and requires completing the FAFSA (checking the FWS box), awarded first-come, first-served. *(Source #15 — Federal Work-Study)* |
| 2 | What is John Jay's 6-year graduation rate, and how does it compare to its 4-year rate? | ~54% 6-year graduation rate vs. ~38% 4-year rate (retention ~81% full-time). *(Sources #9 / #11 — College Factual, Quick Facts 2023)* |
| 3 | How often does John Jay hold its career/internship fairs, and roughly how many employers does the Career Learning Lab work with? | John Jay runs CareerCon ~5 times per academic year (industry-aligned fairs in fall and spring); the Career Learning Lab maintains connections with 4,400+ employers. *(Sources #12 / #13 — Career Building, Spring Career Fair)* |
| 4 | Name two student clubs or organizations a John Jay student can join, and what one of them focuses on. | Any two of, e.g., ALPFA (accounting/finance career opportunities), Law Society, Environmental Club, Habitat for Humanity (affordable-housing/homelessness awareness), Legally Conscious. *(Source #1 — Student Organizations)* |
| 5 | According to student reviews, what is the most common criticism of the social scene at John Jay, and how do students describe campus safety? | It's frequently described as a commuter school where social interaction is harder; on safety, ~97% of students say they feel extremely safe/secure on campus. *(Sources #6 / #7 — Niche Reviews & Campus Life)* |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1.

2.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

---

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

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
