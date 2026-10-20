# LLM Sentinel AI, Week 1 Dataset Starter
Owner: Husnain Ayyub (AI / ML)

## Your Week 1 task, from slide 6 of the roadmap
Begin collecting and labelling the attack and benign prompt dataset from public sources plus our own samples.

## Labelling schema
File: prompts_starter_v1.csv

Columns:
- id: simple row number, for example D001
- prompt_text: the exact prompt, one row per prompt
- category: benign, jailbreak, direct_injection, or indirect_injection
- attack_type: none, direct, or indirect
- source: team_written, hackaprompt, owasp_example, or other_public. Write the exact source for each row
- notes: short reason for the label, in plain words

Rules we agreed in the brief:
- Keep attack and benign roughly balanced
- Split about 70 / 15 / 15 for train / validation / test. Add the split later, after collection, do not split row by row while collecting
- Categories follow the brief: jailbreak means talking the model out of its safety rules, direct injection means a malicious instruction typed into the chat, indirect injection means a malicious instruction hidden in a document, email or page the model is asked to read
- Do not add a prompt without a source and a label note

## What is in v1
32 team written starter rows, 8 per category, to agree the labelling style before large collection. These are not results and they are not copied from a public dataset. Public source rows should be added in v2 with their source recorded per row.

## Target, decided 2026-10-20
Total: 2,000 prompts.
- benign: 500
- jailbreak: 500
- direct_injection: 500
- indirect_injection: 500

Why equal per category: the classifier predicts one of four categories, so each category needs a similar number of examples or it will favour the larger ones.

Split, applied after collection:
- Train: 1,400 total, 350 per category
- Validation: 300 total, 75 per category
- Test: 300 total, 75 per category

Starter v1 (32 rows) counts towards the team written part of these totals.
