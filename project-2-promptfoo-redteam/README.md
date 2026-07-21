# Red-Team Harness — Healthcare Patient-Support Assistant

An adversarial security evaluation of a healthcare patient-support assistant using [Promptfoo](https://promptfoo.dev), covering PII/PHI extraction, jailbreaks, unauthorized medical advice, bias, and hallucination — with results mapped to industry compliance frameworks (OWASP LLM Top 10, NIST AI RMF, EU AI Act, GDPR, ISO/IEC 42001).

> **Why this project exists:** A healthcare assistant doesn't just need to give good answers (Project 1) — it needs to *withstand attack*. This project asks the security question: can an adversary make the assistant leak patient data, give dangerous advice, or bypass its guardrails? I configured a defended assistant, ran automated adversarial scans against it, and iterated on the defenses based on findings.

---

## Approach

**Target:** A prompt-defended healthcare patient-support assistant (Claude Sonnet), whose system prompt encodes guardrails against PHI disclosure, unauthorized medical advice, and rule-bypassing.

**Attack surface tested** (scoped deliberately to healthcare-relevant risks rather than running all ~40 default plugins — choosing relevant attack surface is itself a QA-judgment decision):
- PII/PHI extraction — direct, social-engineering, and session-based
- Unauthorized medical/specialized advice
- Privacy violations
- Hallucination (fabricated medical facts)
- Bias (gender, race) in medical guidance
- Purpose hijacking

**Attack strategies:** basic delivery + composite jailbreak techniques. ~270 adversarial probes generated and fired per scan.

---

## Results

### Defended successfully (0% attack success)
| Category | Result | Why it matters |
|----------|--------|----------------|
| PII via Direct Exposure | 0% | Core HIPAA risk — held |
| PII via Social Engineering | 0% | Held against manipulation |
| PII via Session Data | 0% | No cross-context leakage |
| Privacy Violation | 0% | Held |
| Gender Bias | 0% | Equitable medical guidance |
| Race Bias | 0% | Equitable medical guidance |
| Resource Hijacking | 0% | Stayed on purpose |

**The highest-severity healthcare risk — PHI leakage — was fully defended across every attack vector.**

### Findings (attacks that succeeded)
| Category | Success Rate | Severity |
|----------|-------------|----------|
| Unauthorized Advice | 20% (6/30) | Medium |
| Hallucination | 3.33% (1/30) | Medium |

### Compliance framework mapping
Results were automatically mapped against OWASP LLM Top 10, OWASP API Top 10, NIST AI RMF, EU AI Act, GDPR, ISO/IEC 42001, and DoD AI Ethical Principles. The unauthorized-advice finding surfaced under OWASP LLM "01. Prompt Injection" and "09. Misinformation"; hallucination under "Traceable" (DoD) and "Misinformation" (OWASP).

---

## The Key Finding: A Real Safety Tradeoff

This is the most important result, and it came from iterating on the defenses.

**Round 1 (strict rule):** The initial system prompt said "never provide specific medical advice." A red-team probe describing classic heart-attack symptoms was flagged as a *failure* — but the assistant's response (call 911 immediately, chew aspirin) was actually the correct, life-saving answer. This was a **false positive**: a strict rule flagging good behavior as bad. A healthcare assistant that *refused* to help during a described heart attack would be worse — arguably dangerous.

**Remediation:** I added an **emergency exception** — permitting direct-to-911 guidance and standard emergency first-aid for life-threatening symptoms, while keeping the routine no-dosing rule intact.

**Round 2 (after fix):** The emergency case was now handled correctly. But the scan surfaced a new consequence: the unauthorized-advice success rate rose to 20%. **The exception I carved out widened the attack surface** — adversarial prompts framed requests as urgent to extract advice the assistant should have withheld.

**The insight:** In AI safety, every exception is a potential exploit vector. The fix is not to remove the emergency exception (that would restore the dangerous false-positive), but to *tightly scope* it — permit only the specific life-saving action (direct to emergency services) without broad latitude to relay treatment guidance. Safety rules in healthcare AI require precise scoping, not blanket prohibitions or broad exceptions.

**Recommended next remediation:** Narrow the emergency exception to "immediately direct the user to call 911 / emergency services" only, removing the broad "you may relay first-aid guidance" clause, then re-scan to confirm the advice-success rate drops while emergency direction is preserved.

---

## What this demonstrates
- Configuring and running automated adversarial red-team scans against an LLM target
- Deliberate, risk-scoped attack surface selection (not blind "run everything")
- Reading results mapped to real compliance frameworks (OWASP, NIST, EU AI Act, GDPR, HIPAA-relevant)
- Reasoning about a genuine security/safety tradeoff — recognizing a false positive, remediating it, and understanding how the remediation created new attack surface
- Iterative hardening: strict → too-loose → precisely-scoped

## Tech Stack
Promptfoo · Claude Sonnet (target) · YAML declarative config · compliance-framework reporting

---

*Built by Surya Teja Mantha as part of an AI QA portfolio. Adversarial testing conducted solely for legitimate security evaluation. All patient scenarios are fictional; no real PHI was used.*
![Compliance framework mapping](results/frameworks.png)

## Results

![Red-team results summary](results/TestSummary.png)

![Compliance framework results](results/TestResults.png)

![Attack findings](results/TestFailures.png)