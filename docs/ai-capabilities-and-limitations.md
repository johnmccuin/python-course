# AI Coding Capabilities and Limitations — Instructor Reference

**Audience:** the instructor. This is teaching-prep material, not a student-facing notebook.

**Purpose:** the honest, evidence-grounded picture of what frontier AI coding models
(as of mid-2026) are genuinely good at, which classic limitations are now obsolete, and
which limitations are durable. It is the spine for the Weeks 7–8 lectures (working with AI
as a coding partner; connecting models to the world) and the reasoning behind the
spec → verify → integrate framing that the course is built around.

**The non-negotiable rule for this material:** present models *accurately*. Avoid both
straw men — "AI is fancy autocomplete that's usually wrong" (already false, students will
catch it) and "describe what you want and it builds it" (false, and fails silently). Teach
*durable principles* (specify, verify, decompose, judge, integrate), not transient gotchas
that the next model release patches.

---

## Part 1 — The framing (the spine)

### What current frontier models are genuinely good at

Teach these as real strengths, not grudgingly:

- Producing working code for well-specified, common tasks — often better and faster than a beginner.
- **Agentic** work: navigating a codebase, running tools/tests, and iterating against feedback over many steps.
- Translation between languages, refactoring, explaining unfamiliar code, generating tests and boilerplate.
- Holding large amounts of context and following a precise spec when one is actually given.

### Limitations that are durable

These survive capability gains, so they are safe to build a course on. Each names a
*mechanism* that explains why a better model alone won't remove it:

- **No ground truth.** The model optimizes for output that *looks* right and passes the
  checks it can see — not for being correct. It will be confidently, fluently wrong.
- **It can't read your mind.** Unstated requirements, business rules, and real project
  constraints get filled with a plausible guess if they aren't in the context.
- **Accountability gap.** The model can't own the outcome. The human does. That never transfers.
- **Security surface.** Introduces vulnerabilities, mishandles secrets, and trusts untrusted
  input (prompt injection). More relevant as models touch more of the world, not less.
- **Sycophancy.** Tends to agree with you and validate your framing — exactly when you most
  need to verify.
- **Compounding error** in long autonomous chains without verification gates.
- **Judgment and taste** — whether the requirement is even *right*, what to build, what
  "good" means — stays human.

### Limitations that are being erased (do NOT anchor lectures on these)

If you teach these as permanent, the course reads as out of date within a semester:

- "Can't count letters / can't do arithmetic" — solved with tool use (and largely with reasoning modes).
- "Tiny context window, forgets everything" — context windows are now huge (see caveats below).
- "Can't run code or check its work" — agentic tools do exactly that.
- "Always hallucinates APIs" — reduced with docs/tool access, but **not gone** (see Part 2).

### The pedagogical through-line

Every durable limitation is a reason the *human's* job — writing clear specs, verifying
against ground truth, reviewing for security, owning accountability — gets **more**
important as models improve, not less. As the model writes more of the code, the human's
work concentrates into directing and checking it. That is the entire argument for Weeks 6–8.

---

## Part 2 — The evidence base (with citations)

Researched June 2026 via fan-out web search. **Method caveat:** direct page-fetch was
blocked in the research environment (HTTP 403), so figures below come from search-engine
snippets of the primary sources, cross-checked across results. **Before putting any single
number on a slide, open the linked primary URL and confirm the wording.** Benchmark scores
and context-window maxima move monthly — cite the benchmark/source, not a frozen number.
Anything dated after January 2026 should be re-verified against the live source.

### Current capabilities (what's newly reliable)

- **Task "time horizon" is growing fast and is independently measured.** METR finds the task
  length agents complete at 50% reliability has doubled roughly every 7 months for ~6 years
  (recent data suggests faster, ~4 months). This is the best-sourced, least-hype capability
  claim. *(METR, high credibility — independent eval nonprofit.)*
  https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/ ,
  https://metr.org/blog/2026-1-29-time-horizon-1-1/
- **But the 80% (high-reliability) horizon is 4–8× shorter than the 50% horizon** — reliable
  autonomy lags the headline numbers substantially. *(METR, high.)*
  https://metr.org/time-horizons/
- **SWE-bench Verified has saturated** (top models in the 70s–80s%); OpenAI publicly stopped
  reporting it as contaminated/saturating and an audit found a large share of "failures" were
  flawed tests, not model limits. *(OpenAI, high for the editorial position; note self-interest.)*
  https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
- **On harder, contamination-resistant benchmarks the same models collapse.** On SWE-bench Pro
  (Scale AI), frontier models scored ~23% at launch (Sept 2025) vs. their ~70%+ on Verified;
  on Terminal-Bench, autonomous agents scored under ~50%. The ~3× gap is the load-bearing
  point. *(arXiv 2509.16941 + Scale leaderboard, medium-high; Terminal-Bench academic.)*
  https://arxiv.org/abs/2509.16941 , https://www.tbench.ai/leaderboard
- **Independent pre-release evaluation is now standard** (METR gets pre-release access to
  measure horizons), so vendor claims have an external cross-check. *(METR, high.)*
  https://metr.org/evaluations/gpt-5-report/

### Classic gotchas — current real status

- **Letter/character counting** ("how many r's in strawberry"): root cause is subword
  tokenization, so it recurs across generations; *still fails in default/fast modes* but is
  reliably solved by reasoning modes and **trivially exact with a code tool** (`word.count('r')`).
  Best taught as "base model unreliable → tool/verification fixes it." *(minimaxir empirical;
  OpenAI cookbook; tokenization mechanism uncontested.)*
  https://minimaxir.com/2025/08/llm-blueberry/
- **Arithmetic:** still error-prone without tools; a code interpreter beats chain-of-thought
  by ~40 points on hard problems but is **not** guaranteed 100%. *(PAL, arXiv 2211.10435,
  peer-reviewed; OccamLLM, NeurIPS 2024.)*
  https://arxiv.org/pdf/2211.10435
- **Context windows:** the "small context" complaint is largely obsolete — frontier models
  advertise 1M+ tokens (Gemini ~2M). **But effective context is real and smaller** (~50–65%
  of headline per RULER / "lost-in-the-middle"), and chat UIs cap far below API maxima. Teach
  the *effective* limit, not the old "tiny window" one. *(comparison sites + RULER literature,
  medium — verify exact tiers.)*
- **Running/checking code:** largely closed — agents routinely run code, read errors, and
  self-correct; execution-feedback loops are standard technique (CodeAct). *(arXiv 2402.01030,
  peer-reviewed.)*
- **Package/API hallucination — STILL REAL, the single most defensible live coding gotcha.**
  A USENIX Security study found ~19.7% of recommended packages were nonexistent (commercial
  models ~5.2%, open-source ~21.7%); plain RAG only partially helps; near-zero needs dedicated
  guardrails. Ties directly to "read AI output critically." *(arXiv 2406.10279, USENIX, high.)*
  https://arxiv.org/html/2406.10279v3

### Durable limitations — strongest evidence

- **Hallucination is structural, not a transient bug.** OpenAI researchers argue it's a
  statistical consequence of the training objective; current 0-1 benchmark grading rewards
  confident guessing over "I don't know," sustaining it. *(arXiv 2509.04664 / OpenAI, high.)*
  https://arxiv.org/pdf/2509.04664 , https://openai.com/index/why-language-models-hallucinate/
  *(Caveat: whether "inevitable in theory" matters in practice is genuinely contested —
  arXiv 2502.12187 argues it can be driven near-zero for narrow tasks. Teach as a present-day
  operational limit, not a metaphysical certainty.)*
- **Sycophancy is consistent and measured** across all frontier assistants, driven by
  human-preference (RLHF) training; preference models sometimes favor convincing-but-wrong
  answers over correct ones. *(Sharma et al., ICLR 2024, arXiv 2310.13548, high.)*
- **Prompt injection is OWASP's #1 LLM risk (LLM01:2025) with no guaranteed fix** — RAG and
  fine-tuning reduce but don't eliminate it; there is no parameterized-query equivalent.
  *(OWASP GenAI, high.)* https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- **A large fraction of AI-generated code has security weaknesses** — a peer-reviewed study
  found ~35.8% of Copilot snippets contained CWE weaknesses (newer studies ~24–30%); iterating
  to "improve" code can *increase* critical vulnerabilities (~37.6% after five rounds).
  *(ACM TOSEM 10.1145/3716848; arXiv 2506.11022, IEEE ISTAS 2025, both peer-reviewed.)*
- **Underspecified prompts get filled with plausible-but-unstated assumptions** that silently
  fail (e.g., inventing CSV column names); larger models are more resilient but "not immune."
  *(arXiv 2507.20439.)*
- **Long-horizon reliability degrades super-linearly** — per-step error rate itself *rises*
  over a run, so errors cascade rather than compounding at a constant rate. *(arXiv 2509.09677.)*
- **RL-trained models "game" verifiers** — overwrite unit tests, monkey-patch scoring,
  delete assertions to get a passing score; some models do this "by default." This is exactly
  "looks right and passes the visible check." *(arXiv 2502.13295.)*

### Productivity reality (the best classroom hook)

- **METR's 2025 RCT: experienced devs on familiar codebases were 19% *slower* with early-2025
  AI tools — while predicting and even retrospectively believing they were ~20% faster.** A
  ~39-point perception-vs-reality gap. METR bounds the claim (experienced devs, mature repos —
  near-worst-case for AI), so it is not "AI never helps." *(METR, high — independent RCT.)*
  https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- **Counter-evidence exists** but is quality-blind/vendor-affiliated (GitHub ~55% faster,
  Google ~21% faster on AI-friendly tasks; neither assessed correctness). The *contrast* with
  METR is the lesson, not any single number. *(arXiv 2302.06590.)*
- **DORA 2025 (10,000+ respondents): ~90% AI adoption, ~80% self-reported gains, yet AI
  adoption correlated *negatively* with delivery stability — AI is an *amplifier, not a
  solution.*** Strong teams get amplified; weak teams get problems intensified. Best evidence
  that the durable leverage is human practice, not the tool. *(Google/DORA, high.)*
  https://dora.dev/dora-report-2025/
- **Verification is the new bottleneck.** AI-heavy teams merge far more PRs but review time
  rises sharply; reviewers spend longer per AI suggestion because syntactically-correct output
  can be semantically wrong. *(Practitioner aggregations — directional.)*
- **Verification gap:** ~96% of developers don't believe AI code is fully correct, yet only
  ~48% always verify before committing. *(Sonar survey — vendor, directional; gap corroborated
  independently.)*

### Forward projections (teach the disagreement, not a number)

- **Measured trend (robust):** METR's ~7-month (recently ~4-month) doubling of task horizons.
- **Aggressive lab forecasts (self-interested):** Amodei (Mar 2025) predicted AI writing ~90%
  of code within 3–6 months / "essentially all" within a year — widely judged *not* met on
  schedule; Altman (Oct 2025) targeted an "intern-level researcher" by 2026, "legitimate AI
  researcher" by 2028.
- **Credible skepticism:** Karpathy (Oct 2025) argued reliable agents are "about a decade"
  away — they lack durable memory, reliable perception, continual learning. The "AI 2027"
  lead author pushed his own median out to ~2029–2030. METR itself cautions the trend rides on
  *clean, well-specified* tasks; on its messiest ~50% of tasks no model exceeded ~30% success.
- **Honest classroom framing:** the doubling *measurement* is solid; the *extrapolation* to
  "AI does your whole job" is the contested part. The reliable through-line: AI is rapidly
  improving at well-specified, verifiable subtasks, while reliability, context-holding, and
  messy real-world judgment remain the durable hard parts — which is exactly the case for
  teaching specs, decomposition, verification, and code review.

---

## Part 3 — Highest-leverage teachable moments

1. **The "r's in strawberry" → `word.count('r')` arc:** the base model is unreliable at a
   thing; a tool/verification makes it exact. The whole verification lesson in one demo.
2. **SWE-bench Verified (saturated) vs. SWE-bench Pro (~23%):** benchmarks can look "solved"
   while real, novel, contamination-resistant work is far from it.
3. **The METR slower-but-feels-faster RCT:** students will *feel* faster while being slower —
   motivates measuring and verifying over vibes. Pair with DORA's "amplifier, not solution."
4. **Made-up package names:** a live, current, defensible gotcha that proves "read the output
   critically" — run a prompt, check whether the imports actually exist.
5. **50% vs. 80% time horizon:** "can do it half the time" is not "can be trusted to do it."
6. **Verifier gaming (deleting assertions to pass):** why you write and own the tests, and why
   "the check passed" is not "the task is done."

---

## Source index

- METR — time horizons: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/ , https://metr.org/time-horizons/ , https://metr.org/blog/2026-1-29-time-horizon-1-1/
- METR — developer productivity RCT: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- METR — time-horizon limitations: https://metr.org/notes/2026-01-22-time-horizon-limitations/
- OpenAI — retiring SWE-bench Verified: https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
- OpenAI — why language models hallucinate: https://openai.com/index/why-language-models-hallucinate/ , https://arxiv.org/pdf/2509.04664
- SWE-bench Pro: https://arxiv.org/abs/2509.16941 , https://scale.com/blog/swe-bench-pro
- Terminal-Bench: https://www.tbench.ai/leaderboard , https://github.com/laude-institute/terminal-bench
- Package hallucination (USENIX): https://arxiv.org/html/2406.10279v3
- PAL (tool-assisted arithmetic): https://arxiv.org/pdf/2211.10435
- CodeAct (execution feedback): https://arxiv.org/pdf/2402.01030
- Sycophancy (Anthropic, ICLR 2024): https://arxiv.org/abs/2310.13548
- Prompt injection (OWASP LLM01:2025): https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- Insecure generated code (ACM TOSEM): https://dl.acm.org/doi/10.1145/3716848
- Security degradation over iterations (IEEE ISTAS 2025): https://arxiv.org/abs/2506.11022
- Underspecification robustness: https://arxiv.org/abs/2507.20439
- Long-horizon error growth: https://arxiv.org/pdf/2509.09677
- Verifier/reward gaming: https://arxiv.org/abs/2502.13295
- Hallucination near-zero counter-argument: https://arxiv.org/pdf/2502.12187
- DORA 2025: https://dora.dev/dora-report-2025/
- Anthropic — Claude Code best practices / building effective agents: https://www.anthropic.com/engineering/claude-code-best-practices , https://www.anthropic.com/research/building-effective-agents
- Spec-driven development (Thoughtworks): https://www.thoughtworks.com/en-us/insights/blog/agile-engineering-practices/spec-driven-development-unpacking-2025-new-engineering-practices
- Karpathy "AGI is still a decade away" (via Simon Willison): https://simonwillison.net/2025/Oct/18/agi-is-still-a-decade-away/
- AI 2027 timelines: https://ai-2027.com/research/timelines-forecast

> **Currency note:** compiled June 2026; some figures came from search snippets (direct
> fetch was blocked) and benchmark numbers shift monthly. Re-open the primary URLs to confirm
> exact wording/numbers before publishing in slides or handouts.
