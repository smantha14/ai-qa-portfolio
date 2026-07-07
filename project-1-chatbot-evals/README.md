# LLM Evaluation Suite — Healthcare Patient-Support Chatbot

An automated evaluation suite that quality-gates a healthcare patient-support chatbot's responses using [DeepEval](https://deepeval.com), integrated into CI so no change ships without passing the quality bar.

> **Why this project exists:** In healthcare, a chatbot that hallucinates a medication instruction, leaks patient data, or gives biased triage advice isn't a bad user experience — it's a safety and compliance failure. This suite treats LLM outputs the way I'd treat any high-stakes release: define the risk surface, write measurable tests for each risk, and block the build if quality drops.

---

## Test Strategy

This is the part that matters. Anyone can call a metric; the value is in *deciding what to test, why, and where the pass bar sits.* My approach mirrors how I've written test plans across 11 years of regulated-software QA.

### 1. Risk-first, not tool-first
I started from a domain risk analysis (see my [AI Defect Taxonomy](../defect-taxonomy.pdf)), then chose metrics to cover the highest-severity risks — rather than starting from "which metrics does DeepEval have." For a healthcare chatbot, the severity ranking is:

| Priority | Risk | Why it's critical here |
|----------|------|------------------------|
| 1 (Critical) | Hallucination / factual incorrectness | A wrong clinical fact is a patient-safety risk |
| 2 (Critical) | PII / PHI leakage | HIPAA violation — hard release-blocker |
| 3 (High) | Irrelevance / unhelpful answers | Patients don't get the help they need |
| 4 (High) | Bias in advice | Unequal care recommendations across demographics |
| 5 (Medium) | Toxicity / inappropriate tone | Erodes trust in a sensitive setting |
| 6 (Medium) | Instruction adherence (format/safety disclaimers) | Must include "consult a professional" where needed |

### 2. The six metrics and their pass thresholds
Each threshold is a deliberate risk decision, not a default. Higher-severity risks get stricter bars.

| Metric | DeepEval metric | Threshold | Rationale for the bar |
|--------|-----------------|-----------|----------------------|
| Faithfulness | `FaithfulnessMetric` | 0.9 | Near-zero tolerance for unsupported claims in healthcare |
| Answer Relevancy | `AnswerRelevancyMetric` | 0.7 | Answers must address the question; some latitude for phrasing |
| PII/PHI safety | Custom `GEval` | 1.0 | Any leakage is an automatic fail — no partial credit |
| Bias | `BiasMetric` | 0.8 | Strict, given care-equity stakes |
| Toxicity | `ToxicityMetric` | 0.9 | Sensitive setting demands a high bar |
| Safety-disclaimer adherence | Custom `GEval` | 0.8 | Response must advise professional care where appropriate |

*Judge model:* Claude (via DeepEval's `AnthropicModel`) — chosen after getting it running in the foundation phase.

### 3. Golden dataset design
- ~25–30 curated test cases stored in `goldens.json`, each with `input`, `expected_output`, and `context` (trusted facts) where the metric needs it.
- Cases span **normal** patient questions (hours, appointment prep, general symptom guidance) and **adversarial** ones drawn from my taxonomy: PII-extraction attempts, prompt injection, demographically-varied parallel prompts to probe bias.
- The dataset is version-controlled so quality changes are traceable over time — the same discipline as maintaining a regression test bank.

### 4. CI integration (quality as a gate, not an afterthought)
- Evals run via `pytest` + `deepeval test run` on every push through GitHub Actions.
- The build **fails** if any case drops below threshold — mirroring a release quality gate.
- A deliberate regression scenario is included: a degraded prompt that the suite is proven to *catch*, demonstrating the gate actually works.

### 5. What I'm explicitly NOT testing (scope discipline)
- Latency/cost benchmarking — out of scope for a quality suite (would note it as a follow-up).
- Multi-turn conversation state — this suite evaluates single-turn responses; multi-turn is a separate effort.
- Naming what's out of scope is itself a QA-maturity signal.

---

## Tech Stack
- **DeepEval** — evaluation framework
- **pytest** — test runner
- **Claude (Anthropic)** — LLM judge model
- **GitHub Actions** — CI quality gate
- **Python 3.11+**, virtual environment

## Repository Structure (planned)
```
project-1-chatbot-evals/
├── README.md                 # this file
├── goldens.json              # golden dataset (version-controlled)
├── test_chatbot_evals.py     # the eval suite
├── metrics/                  # custom GEval metric definitions
├── .github/workflows/ci.yml  # CI quality gate
└── results/                  # sample run reports (screenshots)
```

## Status
- [x] Test strategy defined (this README)
- [ ] Golden dataset built
- [ ] Core metrics implemented
- [ ] Custom PII + disclaimer metrics
- [ ] CI integration
- [ ] Regression scenario + results documented

---

*Built by Surya Mantha as part of an AI QA portfolio. Test strategy and risk analysis reflect 11+ years of QA experience in regulated healthcare software.*
