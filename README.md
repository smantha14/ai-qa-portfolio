# AI QA Portfolio — Surya Teja Mantha

Evaluation and quality-assurance work for LLM-based systems: eval suites, red-teaming, RAG testing, and CI quality gates.

I'm a Senior QA Engineer with 11+ years testing regulated healthcare software, now focused on **AI system quality** — designing evaluation frameworks that catch the ways LLMs actually fail (hallucination, PHI leakage, bias, prompt injection) and gating them in CI so quality regressions never ship.

---

## What's here

### ✅ Project 1 — Healthcare Chatbot Evaluation Suite
**[→ project-1-chatbot-evals/](./project-1-chatbot-evals/)**

An end-to-end evaluation suite that quality-gates a healthcare patient-support chatbot, built with [DeepEval](https://deepeval.com) and Claude as the judge model, integrated into GitHub Actions CI.

- **Risk-first test strategy** derived from a documented [AI Defect Taxonomy](./project-1-chatbot-evals/) — metrics chosen to cover the highest-severity healthcare risks, with deliberate pass thresholds (not defaults).
- **Six metrics:** Answer Relevancy, Faithfulness, Bias, Toxicity, plus two **custom GEval metrics** for PHI/PII safety and safety-disclaimer adherence — domain requirements no built-in metric covers.
- **28-case golden dataset** spanning normal patient questions and adversarial cases (PII-extraction, prompt injection, demographic bias probes).
- **Regression test** written as a negative test — it passes only when the gate successfully *catches* a degraded answer, proving the suite blocks quality drops.
- **CI quality gate:** structural validation runs on every push via GitHub Actions; full LLM evaluation documented as a scheduled/manual step (deliberate cost & secret-management tradeoff).
- **[Findings & results writeup →](./project-1-chatbot-evals/)** including a lesson learned distinguishing faithfulness (contradiction detection) from unsupported-claim detection.

*Stack: DeepEval · pytest · Claude (Anthropic) · GitHub Actions · Python*

### 🔜 Coming next
- **Project 2 — Prompt Regression & Red-Team Harness** (PromptFoo): adversarial testing, jailbreak/injection scans, multi-model cost/quality comparison.
- **Project 3 — RAG Evaluation** (RAGAS): retrieval-quality testing — context precision/recall, faithfulness, chunking-strategy comparison.
- **Capstone** — production AI quality gates on a live application, with observability.

---

## Background & differentiators
- 11+ years in QA / test automation, primarily **regulated healthcare SaaS** — so compliance and patient-safety thinking is native, not bolted on.
- Deep experience in **fine-grained authorization / IAM testing** (a rare intersection with AI: how do you test what an AI agent is *allowed* to access?).
- Strengths that transfer directly to AI QA: test strategy, BDD, API validation, and CI/CD integration.

## Foundations
The `day*.py` and `test_day*.py` files at the repo root are foundational Python/pytest exercises from building this skill set — kept for transparency of the learning path.

---

*Contact: [[LinkedIn](https://www.linkedin.com/in/surya-teja-mantha-721355209/) / .[email(teja.mantha@gmail.com)]*
