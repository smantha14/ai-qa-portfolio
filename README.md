# AI QA Portfolio — Surya Teja Mantha

Evaluation and quality-assurance work for LLM-based systems: eval suites, red-teaming, RAG testing, and CI quality gates.

I'm a Senior QA Engineer with 11+ years testing regulated healthcare software, now focused on **AI system quality** — designing evaluation frameworks that catch the ways LLMs actually fail (hallucination, PHI leakage, bias, prompt injection) and gating them in CI so quality regressions never ship.

---

## Projects

### ✅ Project 1 — Healthcare Chatbot Evaluation Suite
**[→ project-1-chatbot-evals/](./project-1-chatbot-evals/)**

An end-to-end evaluation suite that quality-gates a healthcare patient-support chatbot, built with [DeepEval](https://deepeval.com) and Claude as the judge model, integrated into GitHub Actions CI.

- **Risk-first test strategy** derived from a documented AI Defect Taxonomy — metrics chosen to cover the highest-severity healthcare risks, with deliberate pass thresholds (not defaults).
- **Six metrics:** Answer Relevancy, Faithfulness, Bias, Toxicity, plus two **custom GEval metrics** for PHI/PII safety and safety-disclaimer adherence.
- **28-case golden dataset** spanning normal patient questions and adversarial cases.
- **Regression test** written as a negative test — passes only when the gate *catches* a degraded answer.
- **CI quality gate** via GitHub Actions; 25 individually-named parametrized tests.

*Stack: DeepEval · pytest · Claude · GitHub Actions · Python*

### ✅ Project 2 — Healthcare Assistant Red-Team Harness
**[→ project-2-promptfoo-redteam/](./project-2-promptfoo-redteam/)**

An adversarial security evaluation of a healthcare assistant using [Promptfoo](https://promptfoo.dev) — ~270 automated attacks across PII/PHI extraction, jailbreaks, unauthorized medical advice, bias, and hallucination, with results mapped to OWASP LLM Top 10, NIST AI RMF, EU AI Act, and GDPR.

- **PHI leakage fully defended** — 0% success across direct, social-engineering, and session-based extraction (the critical healthcare risk).
- **Discovered a real safety tradeoff:** a strict "no medical advice" rule produced a false positive on a heart-attack emergency case; adding an emergency exception fixed it but widened the advice attack surface — demonstrating that safety exceptions must be *tightly scoped* or they become exploit vectors.
- **Iterative hardening** documented: strict → too-loose → precisely-scoped.
- Results mapped to industry **compliance frameworks**.

*Stack: Promptfoo · Claude · YAML declarative config · compliance-framework reporting*

### 🔜 Coming next
- **Project 3 — RAG Evaluation** (RAGAS): retrieval-quality testing — context precision/recall, faithfulness, chunking-strategy comparison.
- **Capstone** — production AI quality gates on a live application, with observability.
- **Stretch** — authorization testing for AI agents (intersection of IAM and AI safety).

---

## Background & differentiators
- 11+ years in QA / test automation, primarily **regulated healthcare SaaS** — compliance and patient-safety thinking is native, not bolted on.
- Deep experience in **fine-grained authorization / IAM testing** — a rare intersection with AI: how do you test what an AI agent is *allowed* to access?
- Strengths that transfer directly to AI QA: test strategy, BDD, API validation, and CI/CD integration.

## Foundations
The `day*.py` and `test_day*.py` files at the repo root are foundational Python/pytest exercises from building this skill set — kept for transparency of the learning path.

---

*Contact: [LinkedIn / email — add your preferred contact]*
