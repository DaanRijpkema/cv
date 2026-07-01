# Critical CV Review and Rewrite Instructions

You are reviewing and restructuring my current CV. Work in plan mode first: inspect the current Markdown CV, identify the major structural and content issues, propose a clear rewrite plan, then apply the changes deliberately. Do not merely polish sentences. The goal is to reposition the CV from “complete biography of everything I have done” toward “focused senior software engineer / staff engineer candidate profile”.

The current CV has strong raw material, but it is too biographical, too uniformly weighted, and insufficiently oriented around technical impact. The rewrite should make the CV easier to scan, more credible for senior engineering roles, and more persuasive for roles involving backend engineering, cloud-native systems, technical leadership, architecture, product-minded engineering, and mentoring.

## Strategic diagnosis

The current CV gives a good first impression visually: it is clean, professional, minimal, and not visually chaotic. The photo is fine for a Dutch or European context, although an international/ATS-friendly variant without photo could also be considered later. The document is two pages, which is acceptable for 10+ years of experience.

The main problem is not lack of experience. The main problem is prioritization. The CV currently treats too many activities as equally important. Older student-association work, volunteering, DJ/music activity, education details, and early leadership roles take up too much space relative to the most commercially relevant engineering experience.

The CV currently reads as: “I have done many interesting things.”
It should read as: “I am a senior software engineer who can design, build, scale, and improve important software systems, while mentoring others and taking product ownership.”

This is the core positioning shift.

## Primary target positioning

Rewrite toward this professional identity:

Senior Software Engineer / Senior Backend Developer with 10+ years of experience building cloud-native, product-facing software systems. Strong in PHP, TypeScript, Node.js, AWS, GraphQL, distributed systems, testing, architecture, and product development. Experienced founder of a SaaS product, senior engineer in a large e-commerce environment, and mentor/technical coach within engineering teams.

Do not over-position as “Staff Engineer” unless the CV makes that claim carefully. It is acceptable to make the CV Staff-ready, but avoid unsupported titles or inflated claims. Use wording like “senior engineer with staff-level trajectory”, “technical leadership”, “architecture”, “mentoring”, and “cross-team impact” only where substantiated by experience.

## Major changes to make

### 1. Replace “Curriculum Vitae” as the dominant title

Do not waste prime header space on “Curriculum Vitae”. The reader already knows what the document is.

Use the top area to communicate role and positioning.

Recommended header direction:

Daan Rijpkema
Senior Software Engineer
Backend • Cloud • Product Engineering • Architecture

Then include contact details compactly:
Email, phone, LinkedIn, location, optionally GitHub/portfolio if available.

Use consistent capitalization:

* LinkedIn, not Linkedin
* February, not february
* TypeScript, not Typescript
* e-commerce or E-commerce consistently
* Full-stack or full stack consistently

### 2. Add a sharp professional summary

The current summary is decent but generic. Rewrite it to emphasize impact, systems, leadership, and product ownership.

Suggested direction:

“Senior Software Engineer with 10+ years of experience designing and building scalable backend and full-stack systems across e-commerce, SaaS, and cloud-native environments. Strong background in PHP, TypeScript, Node.js, AWS, GraphQL, testing, and distributed architectures. Combines hands-on engineering with product ownership, mentoring, and a founder’s mindset from building and operating a SaaS platform used by 60+ organizations.”

Adjust details if the underlying CV contains more precise or more current facts.

Important guardrail: do not invent technologies, metrics, systems, or scale. If a good metric is unavailable, insert a clear TODO marker such as `[TODO: add scale/impact metric if accurate]`.

### 3. Add a “Selected Highlights” or “Career Highlights” section

This is currently missing and should be added near the top, after the summary and before experience. The purpose is to make the first 20 seconds count.

Possible bullets:

* 10+ years of professional software development experience.
* Senior Backend Developer at Coolblue, working on product management, catalog, search/filter/advisory/product-page systems.
* Founder of Codex, a SaaS platform used by 60+ student organizations/businesses across four Dutch cities.
* Experience with AWS, TypeScript, PHP, GraphQL, serverless architecture, databases, CI/CD, and test-driven development.
* Former Google Business Associate Intern focused on fraud detection, anti-abuse strategies, data analysis, and product policy.
* Experienced mentor, coach, and technical contributor in product-oriented engineering environments.

Keep this section short. Maximum 5–6 bullets. It should be a recruiter scanning aid, not a duplicate of the experience section.

### 4. Rename “Activities” to “Professional Experience”

“Activities” undersells the professional experience and makes the CV feel like a student/early-career document. Replace it with “Professional Experience”.

Separate true professional experience from community, volunteering, education, and side interests.

Recommended high-level order:

1. Header
2. Professional Summary
3. Selected Highlights
4. Professional Experience
5. Technical Skills
6. Education
7. Community / Leadership / Selected Earlier Experience
8. Interests, optional and very short

### 5. Rebalance information density

The current CV gives too much space to older or less relevant items. Rebalance based on relevance to future engineering roles.

Recommended relative weighting:

* Coolblue: most important; expand and sharpen.
* Codex / Styx Software: second most important; keep and sharpen strongly.
* Freelance development: keep, but clarify or merge with Codex if overlapping.
* Google internship: keep, but concise.
* Sticky / Enactus / Indievelopment: keep only as leadership/community evidence; shorten drastically.
* DJ/music and EKKO volunteering: optional; keep extremely short or move to Interests.
* High school: remove or reduce to one line at most.
* Personal details: remove date of birth; keep location and driver’s license only if relevant.

The CV should remain two pages. Do not let the second page become a dumping ground.

### 6. Rewrite experience bullets around outcomes, not responsibilities

Current descriptions are mostly responsibility-based. Rewrite them as impact-oriented bullets.

Each major role should use bullets with this structure where possible:

* Context: what domain/system/product?
* Action: what did I design/build/improve/lead?
* Impact: what changed?
* Scale: users, organizations, requests, data volume, teams, systems, revenue, reliability, performance, automation, developer experience.

Use quantified metrics where known. If not known, mark TODOs rather than fabricating.

Example pattern:

Bad:
“Developing and scaling software for the Product Management domain.”

Better:
“Built and maintained backend services for product management, catalog, filtering, advisory, and product-page domains in a large-scale Dutch e-commerce environment.”

Better with metric:
“Built and maintained backend services for product management, catalog, filtering, advisory, and product-page domains supporting [TODO: add scale, traffic, product count, or business impact].”

### 7. Strengthen Coolblue section

This should be the anchor of the CV. The current version is too generic for the most important role.

The Coolblue section should convey:

* Senior Backend Developer / Senior Software Engineer role.
* Large-scale e-commerce context.
* Product Management domain.
* Systems related to catalog, filters, search, advisory, product pages.
* AWS/CDK/serverless/cloud-native work.
* PHP, TypeScript, Java if all still accurate.
* Testing/TDD/quality culture.
* Mentoring, senior competency, process improvement.
* Architecture and scalability.

Recommended format:

Senior Backend Developer — Coolblue
February 2022 – Present | Rotterdam/Utrecht/Remote or Netherlands

Bullets:

* Build and scale backend services for product management, catalog, search/filter, advisory, and product-page domains in a major Dutch e-commerce environment.
* Develop cloud-native systems using AWS CDK, Lambda, S3, DynamoDB, RDS, and related infrastructure.
* Work across PHP, TypeScript, and Java codebases, with a strong focus on maintainability, testing, and operational reliability.
* Contribute to architecture, engineering standards, and process improvements from the senior engineering competency.
* Mentor colleagues through code review, technical coaching, knowledge sharing, and pragmatic engineering practices.
* [TODO: add 1–3 concrete achievements: migration, performance improvement, reliability improvement, cost reduction, team/process improvement, product impact, scale metric.]

Avoid buzzword stuffing. Prefer concrete systems and results.

### 8. Strengthen Codex / founder section

This is a differentiator and should be preserved. It shows product sense, entrepreneurship, ownership, customer understanding, and full lifecycle engineering.

Current version is good, but too paragraph-heavy. Convert it into concise bullets.

Codex should communicate:

* Founder of SaaS platform.
* Built CMS/ERP/HR/CRM/analytics/admin tooling.
* Served 60+ organizations/businesses/associations across four Dutch cities.
* Helped thousands of students or users.
* Integrated third-party services.
* Automated redundant administrative processes.
* Owned product, engineering, support, operations, and customer relationships.

Recommended bullets:

* Founded and built Codex, a web-based administration and analytics SaaS platform for student organizations and small-to-medium associations.
* Designed and developed integrated CMS, ERP, HR, CRM, and analytics functionality with third-party integrations.
* Scaled the platform to 60+ organizations across four Dutch cities, supporting administrative workflows for thousands of students.
* Owned the full product lifecycle: discovery, development, infrastructure, support, customer onboarding, and long-term maintenance.
* Automated repetitive administrative processes and improved reporting, membership, finance, and operational workflows.

If true, add stack details: PHP, MySQL, JavaScript, Linux, etc. If not certain, mark TODO.

### 9. Clarify freelance work

The current freelance item is too vague:
“Freelance Graphic-, Web and App Designer and Developer”

This does not help much because it does not say what kind of clients, systems, technologies, or outcomes.

Either:

* merge it with Codex and broader independent work, or
* rewrite as a concise separate role.

Possible rewrite:

Freelance Software Developer / Product Engineer
September 2008 – Present

Bullets:

* Built websites, web applications, automation tools, and digital products for independent clients.
* Combined software engineering, UX/design, client communication, and delivery ownership.
* [TODO: add 1–2 representative projects, client types, technologies, or outcomes.]

If the CV is targeting senior engineering roles, do not overemphasize graphic design unless applying to product/front-end-heavy roles.

### 10. Keep Google, but concise

The Google internship is valuable brand signal. Keep it, but make it concise.

Recommended bullets:

* Developed fraud detection and anti-abuse strategies using data analysis and policy evaluation.
* Analyzed datasets to improve fraud prevention and product-policy decisions.
* Organized a technical/data-focused meetup and received internal recognition for helping colleagues with data analysis and programming.

Do not let this section dominate. It is old but valuable.

### 11. Shorten Sticky / Enactus / Indievelopment radically

This section currently consumes far too much space. It demonstrates leadership, initiative, communication, event organization, and early technical ownership, but it is too detailed for a senior engineering CV.

Create a “Community & Leadership” or “Selected Earlier Experience” section.

Possible compressed version:

Community & Leadership

* Founding board member and Secretary, Study Association Sticky; led communications, events, alumni initiatives, and internal tooling.
* Designed and developed StickyPay, an RFID/NFC payment system, and StickyAdmin, a PHP-based administration system that digitized internal workflows.
* Founded and organized Indievelopment conference, growing attendance from 140 to 440 visitors and managing budgets up to €20,000.
* Team Captain and Founder, Enactus Utrecht Think Tank; led a creative team developing social enterprise concepts and advising existing ventures.

This keeps the strongest signal and removes excessive operational detail.

### 12. Move DJ/music and EKKO volunteering to Interests or remove

The DJ/electronic music and EKKO volunteering items add personality, but they are not core CV content for a senior software engineering application. Keep them only if there is enough space.

Recommended:
Interests: electronic music production/DJing, endurance sports, yoga, writing, chess.

Do not include the full “ambition to become resident DJ” paragraph in the main experience section. It distracts from the professional story.

EKKO volunteering can be one phrase under interests/community:
“Volunteer bartender at EKKO, Utrecht.”

### 13. Simplify education

Education should be present but much shorter.

Keep:

* BSc Computer Science, Utrecht University.
* MSc Artificial Intelligence, Utrecht University — thesis phase / on hold, if you want to include it.

Be careful with “MSc Artificial Intelligence (thesis phase) — On hold”. It may raise questions. Keep it honest, but phrase neutrally:
“MSc Artificial Intelligence coursework completed / thesis phase paused” only if accurate.

High school should usually be removed. If retained, make it one line:
“Bilingual VWO, Maartenscollege.”

Remove details about prom, yearbook, high school physics/math/chemistry, IB grade, and final research project unless applying for a very early-career or academic context. At 10+ years experience, this is noise.

### 14. Remove or minimize personal information

The current personal information section includes date of birth. Remove date of birth. It is unnecessary and can introduce bias.

Keep only:

* Location: Utrecht, Netherlands
* Work authorization if relevant
* Driver’s license only if relevant to the target role; otherwise omit

Do not include birthplace.

### 15. Rework technical skills into a sharper taxonomy

The current skills section is too generic. Make it more specific and recruiter/ATS-friendly.

Suggested structure:

Technical Skills

* Languages: PHP, TypeScript, JavaScript, Java, Python
* Backend & APIs: Node.js, GraphQL, REST, serverless architectures, event-driven systems
* Cloud & Infrastructure: AWS, CDK, Lambda, S3, DynamoDB, RDS, Docker, Linux, CI/CD
* Databases & Search: MySQL, PostgreSQL, DynamoDB, Redis, OpenSearch/Elasticsearch, Cassandra
* Engineering Practices: TDD, automated testing, architecture, observability, code review, mentoring
* Additional: functional programming, data analysis, cybersecurity, automation

Only include technologies that are true and defensible. Do not add tools just because they sound impressive. If Markdown has more detailed current technologies, prefer those.

### 16. Preserve what is crucial

The following content is crucial and should remain prominent:

* Senior role at Coolblue.
* 10+ years of software development experience.
* Backend/cloud/product engineering identity.
* Codex founder story with 60+ organizations and thousands of users.
* Google internship.
* PHP + TypeScript + AWS.
* Mentoring / coaching / senior competency.
* Product-mindedness and ownership.
* Some evidence of leadership outside formal employment, but compressed.

### 17. Remove or de-emphasize

Remove or heavily reduce:

* “Curriculum Vitae” as a large title.
* Date of birth and birthplace.
* Long high school details.
* Long Sticky operational history.
* Long DJ ambition paragraph.
* Volunteering as separate major professional experience.
* Generic claims without evidence.
* Repeated phrases like “primary responsibility”.
* Anything that sounds like a student CV.

### 18. Tone and style requirements

Use clear, compact, professional English. Avoid corporate cliché. Avoid exaggerated language. Avoid overclaiming.

Prefer:

* “Built”
* “Designed”
* “Led”
* “Maintained”
* “Improved”
* “Automated”
* “Mentored”
* “Scaled”
* “Integrated”

Avoid:

* “Passionate about” repeated too often
* “Crucial aspect”
* “Comprehensive” unless it is genuinely needed
* “And more”
* “Various”
* “Helped with”
* “Responsible for” where a stronger verb is possible

Use bullets, not long paragraphs. Each bullet should ideally fit on one or two lines.

### 19. Formatting instructions for Markdown

Assume the CV will be maintained as Markdown and later exported to PDF.

Use clean Markdown:

* One H1 for the name.
* Short subtitle directly under the name.
* Contact line compactly formatted.
* H2 sections.
* H3 for roles.
* Bullets under each role.
* Avoid nested bullets unless necessary.
* Avoid tables unless the rendering pipeline supports them reliably.
* Keep line lengths readable.
* Keep spacing consistent.

Suggested Markdown structure:

# Daan Rijpkema

Senior Software Engineer
Backend • Cloud • Product Engineering • Architecture
Utrecht, Netherlands | email | phone | LinkedIn | GitHub/website

## Summary

## Selected Highlights

## Professional Experience

### Senior Backend Developer — Coolblue

February 2022 – Present

### Founder — Codex by Styx Software

December 2013 – February 2025

### Freelance Software Developer / Product Engineer

September 2008 – Present

### Business Associate Intern, Product Quality Operations — Google

June 2014 – September 2014

## Technical Skills

## Education

## Community & Leadership

## Interests

### 20. Plan-mode workflow for the agent

Before editing, do this:

1. Inspect the full current Markdown CV.
2. Identify all sections and classify them as:

   * keep and expand
   * keep but rewrite
   * compress
   * move
   * remove
3. Draft a proposed new section order.
4. Identify missing facts or metrics as TODOs.
5. Rewrite the CV in the new structure.
6. Review the final version for:

   * two-page suitability
   * ATS readability
   * truthful claims
   * consistency of dates and capitalization
   * technical keyword coverage
   * senior/staff-level positioning
   * absence of unnecessary personal details
7. Output the final Markdown and a short changelog explaining the main changes.

### 21. Important guardrails

Do not invent metrics, scale, job titles, employers, technologies, or responsibilities.

If a metric would strengthen the CV but is unknown, insert a TODO marker:
`[TODO: add measurable impact, e.g. latency reduction, deployment frequency, traffic scale, cost saving, team size, number of users, or business result]`

Do not remove the entrepreneurial/founder story. It is one of the strongest differentiators.

Do not make the CV sterile. Keep a small amount of personality, but only after the professional signal is strong.

Do not over-index on design. The design is already clean enough. The biggest gains are structural hierarchy, sharper writing, prioritization, and quantified impact.

Do not turn every line into buzzwords. The final CV should feel credible, specific, and grounded.

Do not write as if I am a pure infrastructure engineer. Position me as a product-minded senior software engineer with strong backend/cloud/platform ability.

Do not bury Coolblue and Codex. They should carry the document.

Do not let older association/volunteer work consume space better used for recent engineering impact.

### 22. Desired end state

The final CV should make a hiring manager quickly conclude:

“This is a senior engineer with strong backend and cloud experience, real product ownership, entrepreneurial history, mentoring ability, and enough architectural maturity to be considered for senior/staff-track roles.”

The CV should be concise, specific, scan-friendly, technically credible, and honest.

## Additional semantic update instructions

The current CV is semantically outdated. Before rewriting, incorporate the following career-relevant themes where truthful and appropriate.

Prioritize adding stronger evidence of:

1. Large-scale e-commerce backend engineering
   * product catalog
   * navigation
   * search/filtering
   * advisory flows
   * product pages
   * product-management systems

2. Cloud-native AWS engineering
   * AWS CDK
   * Lambda
   * API Gateway
   * S3
   * SQS/SNS
   * DynamoDB
   * RDS/Aurora MySQL
   * RDS Proxy
   * Redis/ElastiCache
   * OpenSearch
   * CloudFront where relevant

3. API and distributed-systems work
   * GraphQL
   * Apollo Federation / Supergraph patterns
   * REST APIs
   * event-driven architecture
   * queue-based processing
   * service boundaries

4. Data and migration work
   * MySQL/Aurora
   * DynamoDB
   * Redis
   * OpenSearch/Elasticsearch
   * AWS DMS
   * read models / projections
   * data consistency and migration reliability

5. Reliability and engineering maturity
   * TDD
   * integration testing
   * load testing
   * k6
   * Datadog
   * observability
   * production diagnostics
   * CI/CD
   * Docker/local development workflows

6. Technical leadership
   * mentoring
   * code review
   * design discussions
   * architectural decision-making
   * engineering standards
   * pragmatic process improvement

7. Product-minded engineering
   * founder of Codex SaaS platform
   * freelance product/client work
   * internal tooling
   * workflow automation
   * customer/user impact

Also consider adding a short “Selected Projects” section only if space allows. Candidate projects:
* Dictate: local-first voice-to-notes pipeline using Whisper.cpp, Ollama, shell automation, and folder watching.
* Garmin breathing app: independent Garmin Connect IQ product exploration involving breathing guidance, haptics, visual rhythm design, and product documentation.

Guardrails:
* Do not invent metrics.
* Do not expose confidential internal project names or implementation details.
* Prefer domain-level descriptions over internal service names.
* Keep the CV focused on senior software engineering, backend/cloud systems, architecture, product engineering, and technical leadership.
* Avoid making the CV look like a hobby-project portfolio.
* Coolblue and Codex should remain the two strongest anchors.
