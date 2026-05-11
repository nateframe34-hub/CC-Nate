# Killed Batch Failure Pattern Analysis

**Date:** 2026-05-11
**Scope:** Batches 1-6 (15 killed ads + 2 converters for contrast), plus B8 and B10 high-level
**Purpose:** Failure analysis to inform new batch writing for Friday May 15 launch

> **Note:** This document is paired with `Converter_Pattern_Synthesis.md` — that doc captures "what works," this one captures "what fails and why." Use both as design constraints for new ad writing.

---

## 1. Per-Ad Failure Summary Table

| Ad ID | Hook Format | Funnel Break Point | Identified Cause | Lessons Captured |
|---|---|---|---|---|
| **B1C1** Desert Dry | Menopause-specific state change | Never delivered (starved) | Compliance violation: "menopause" + "hormones" in hook. CPM $99, but only 11 impressions, 18.18% CTR on noise. CBO avoided. | Strip menopause/hormonal language entirely. Externalizing the whiplash experience doesn't require naming the cause. |
| **B1C2** Husband Noticed | External dialogue (husband comment) | ATC→Purchase (0 sales despite 100% LPV-to-ATC) | $166 CPM unsustainable; 2 LPV→2 ATC was promising but no conversion at price point. 5-element density predates density rule. | Hook locked. Structure rebuilt as B5C1. Densification moved CTR up and converted 1 sale at full price. |
| **B1C3** Dermatologist | Authority-endorsed mechanism discovery | Click→LPV (0 clicks on 47 impressions, 0% CTR) | Doctor/dermatologist character violates 2026 Meta compliance rules. Meta penalizes medical-authority product endorsement separate from other health claims. Hook reads like ad (question-based thesis) not personal story. | Medical authority discovery is formally banned. Replace with peer authorities (sister, friend, older woman). Open with scene, not conversation summary. |
| **B2C1** Cow Fat | Hook as unique pattern interrupt | Never delivered (starved despite low CPM) | Best CPM in batch ($65) but CBO chose B2C2 ($213) instead. Ad had 1 LPV / 0 ATC on 42 impressions. Never tested at scale due to budget prioritization. | "Cow fat" hook is unique differentiator. Needs densification (8-of-10 elements). Low CPM signal suggests this hook may bypass audit penalties — worth revisiting. |
| **B2C2** All The Same | LPV→ATC (4 LPV, 0 ATC — worst funnel in batch) | 7 clicks was engagement bait; thesis given away in first sentence. $213 CPM despite 3.93% CTR proves auction problem upstream. 57% click-to-LPV drop-off; argument-based ads attract argument-based clickers, not buyers. | Bury thesis inside story. Open with scene. Add external character who delivers insight. Build to identity-level payoff, not intellectual payoff. Mechanism works; delivery structure doesn't. |
| **B2C3** Daughter | Click→LPV (0 clicks on 32 impressions, 0% CTR) | Hook is punchline, not hook — resolution arrived before conflict. Daughter validates inventory absence, not skin change. CBO immediately deprioritized (0 engagement signal). | Open with scene, not punchline. Daughter should validate SKIN change, not bottle absence. Minimalism angle is real but underbuilt. Reworked as B5C3. |
| **B3C1** Caught In Bad Light | LPV→ATC (0 ATC, never logged full data) | Hiding-behavior low point is compliance liability. "In bad light" frame implies shame about being seen. Compliance rules 2 & 4 now ban this structure. Hook slower than B1C2's proven "He never notices anything." | Invert structure — validation first, backstory second. Replace hiding behaviors with external observations. Hope before shame. Rebuilt as B5C1. |
| **B3C3** The Questions She Never Read | Click→LPV (0 clicks, data unlogged) | Three compliance violations in first 3 sentences: "menopause," "dermatologist," anti-medical anger frame. List-format structure slows scroll-velocity reading. Dermatologist as antagonist reads combative. | Menopause is permanently banned. Medical dismissal anger is valid but needs softer framing (systemic failure, not individual doctor antagonism). Replace 7-question list with 2-3 embedded in narrative. |
| **B4C1** The 30-Day Mirror | Never converted (0 ATC despite early high CTR) | Day-1 CPM $70 on 13 impressions was noise. Day-2 CPM spiked to $686 — CBO starved ad (0 engagement signal on larger sample). Internal decision-moment urgency doesn't earn delivery. Mechanism ("compounding damage clock") intellectually correct but emotionally cold. | Hook template ("I'm [age]. It's [time]. I [action].") is strong. Internal urgency fails. Externalize urgency through other characters. Move close from internal decision to relational outcome. |
| **B4C2** I Wanted To Throw Up | Never delivered ($1,000 CPM on 14 impressions — auction penalty, not CBO starvation) | "Active harm" framing + visceral disgust language ("throw up") is a separate Meta penalty category not covered by original compliance rules. Anti-competitor framing ("your cream is harming you") trips wellness-conspiracy filters. | Active-harm framing is structurally banned. Disgust language added to strike list. Differentiation = "different category," not "harmful." Humectant mechanism (valid) must frame as educating, not warning. |
| **B4C3** Six Weeks From Saturday | Never converted (9 impressions across 2 days, 0 engagement) | External calendar urgency is sound but too narrow. "Six weeks / high school reunion" may have been classified as low-relevance for broad targeting. Hyper-specific event doesn't translate urgency for non-attendees. | Calendar anchor mechanism is valid. Broaden from single event to event category. Add 2-3 named external characters to externalize urgency. Replace singular deadline with sequence of relational moments. |
| **B5C2** I Haven't Told Anyone | Never delivered (15 impressions, 0 engagement) | Confession-opener is slow for cold paid placement — works in known-audience Facebook post, struggles with stranger. CBO sampled, saw no early clicks, pulled back. 4 impressions at $325 vs 11 impressions at $59 shows tiny-sample noise (CPM not reliable). | Confession beat works as MID-AD pattern interrupt, not opener. Move to 30-50% mark after scene-based hook. Don't claim signal under 50 impressions. 10-element body is solid; hook is the problem. |
| **B5C3** I Gave Up On Moisturizer | Never delivered (20 impressions, 0% CTR across 2 days) | Time-reversal opener ("I gave up") is counter-intuitive for scroll velocity — promises nothing to the reader. CBO sampled lightly, saw zero engagement, pulled back. Body is 10/10 density (strongest in project) but never read. | Rebuild hook as scene (November morning without product on face). Add curiosity promise to first 3 sentences. Port body forward intact. Scene-based hook on 10/10 body = stronger test. |
| **B6C1** Silent Touch | Never converted (5 impressions, 20% CTR is statistical noise, $18 CPM artifact) | 1 click on 5 impressions = 95% confidence interval 1%-72%. Treated as signal when it was noise (same trap as B1C1, B4C1). CBO never committed budget ($0.09 spend). Wordless-touch hook concept sound; budget deprioritization meant untested. | Hard rule: no engagement claim under 50 impressions, no CPM claim under 100 impressions. Wordless-touch survives as candidate for fresh-campaign test. Husband-dialogue hook outperformed all variants. |
| **B6C2** Unposed Photo | Never converted (13 impressions, 0% CTR) | Photo-as-validation too subtle for hook — requires reader to translate why candid photo matters. Generational mismatch: Gen X avatar doesn't experience phone photos as romantic gesture. B6 hypothesis test proved verbal-comment mechanism is load-bearing. | Don't lead with interpretive gestures. Verbal-comment mechanism is doing the work. B6C2/B6C3 failures together prove this. Photo moment could survive as mid-ad pattern interrupt in a different structure. |
| **B6C3** Spoken Compliment | LPV→ATC (1 click, 0 LPV on 37 impressions, 2.70% CTR) | Generic "you look beautiful" ≠ skin-specific noticing. B5C1's "your skin looks different" has load-bearing specificity. Reader can't extrapolate "product → generic compliment." CBO funded this more than B6C1/B6C2 but still only $6.36 spend. | Verbal-comment mechanism requires SKIN-SPECIFIC noticing. "Your skin looks different" beats "you look beautiful." Generic compliments must be locked out. B6 hypothesis proven: the comment content is load-bearing. |

---

## 2. Cross-Cutting Failure Patterns

**Pattern A: Sub-50-Impression CTR Noise (5 ads affected: B1C1, B4C1, B6C1, implicit in B1C3, B2C3)**

B1C1 (18.18% CTR on 11 impressions), B4C1 (15.38% CTR on 13 impressions), B6C1 (20% CTR on 5 impressions) all read as winners initially, then failed to scale or convert. Each was a regression-to-mean trap. Hard threshold needed: no claim under 50 impressions.

**Pattern B: Compliance Violations in First 3 Sentences (4 ads: B1C1, B1C3, B3C3, B4C2)**

Menopause language (B1C1, B3C3), doctor-character endorsement (B1C3), visceral disgust + active-harm (B4C2). Each triggered separate Meta penalty buckets. B1C3 got $175 CPM, B4C2 got $1,000 CPM — algorithm decided before body copy could matter. Compliance own-goals.

**Pattern C: Hooks That Don't Open Loops (5 ads: B1C3, B2C3, B5C2, B5C3, B6C2)**

B1C3 thesis opener, B2C3 punchline opener, B5C2 slow inward confession, B5C3 counter-intuitive claim ("I gave up"), B6C2 subtly meaningful gesture. None earned the first click. B5C3 had 10/10 density and 0% CTR — body work means nothing if the hook doesn't open a loop.

**Pattern D: Upmarket Price Resistance (2 ads: B1C2, B5C1)**

B1C2 (5-element) generated 100% LPV-to-ATC but 0 purchases at $19.99 until densified. B5C1 (10-element) converted 1 full-price sale at $49.99. Thin ads carry users to ATC; dense ads convert checkout to purchase at full price.

**Pattern E: Intellectual Engagement Without Purchase Intent (1 ad: B2C2)**

Opening with the thesis attracts evaluators, not buyers. The Invisible Woman buys when she feels SEEN, not when she feels SMART. Story beats > thesis beats.

**Pattern F: The Husband-Variant Test Produced Negative Results (3 ads: B6C1, B6C2, B6C3)**

Wordless touch, candid photo, generic compliment all underperformed vs. "your skin looks different." The VERBAL COMMENT about SKIN-SPECIFIC change is the load-bearing element. Variants fail because they lose specificity.

**Pattern G: CBO's Early-Sample Behavior Predicts Failure**

Ads that got starved in the first day (< $2 spend across 1-2 days) are telling the algorithm they don't have engagement signal. CBO's funding decision is itself diagnostic data. Hard-starved ads consistently had hooks that didn't open loops.

**Pattern H: Density Rule Falsified CPM Hypothesis**

B1C2 (5-element, $166 CPM) vs B5C1 (10-element, $228 CPM). Densification did NOT lower CPM. The CPM problem is upstream of creative density. Conversion benefit ≠ CPM benefit.

---

## 3. Density Gaps: Killed Ads vs 10-Element Converter Skeleton

| Element | Missing in Killed Ads | Notes |
|---|---|---|
| 1. External noticing as hook | 5/15 | Killed ads open with narrator state, thesis, doctor conversation, internal decision, or visceral disgust |
| 2. Skin-specific noticing language | 2-3/15 | B6C3 generic compliment, B6C2 subtle gesture |
| 3. Named peer-adjacent authority | 7/15 | Most killed ads either no secondary character or abstract/generic |
| 4. Mechanism explained by discovery character | 7/15 | Most killed ads either don't explain or do it narrator-as-expert |
| 5. Progressive day-marker transformation (Day 1, 4, 9, 14, 21) | **15/15** | **Zero killed ads use specific day numbers. Universal in converters.** |
| 6. Unexpected habit-cessation beat | **15/15** | **Zero killed ads include "I didn't notice I stopped..." Present in 3/4 converters.** |
| 7. Close mirrors hook | **15/15** | **Killed ads don't loop back. Universal in converters.** |
| 8. Identity-level payoff | **15/15** | **Killed ads close on product features or internal state. Converters close on relational outcomes.** |
| 9. Solution-aware + accidental discovery | 6/15 | Early killed ads adopt problem-education posture instead of solution-aware |
| 10. Zero medical authority, zero shame framing | 5/15 | Menopause language, dermatologist endorser, hiding-behavior shame, active-harm framing |

**Key takeaway:** Killed ads average 3-4 of 10 elements. Converters have 9-10/10. **Day-marker transformation, habit-cessation beat, close-mirrors-hook, and identity-level payoff are 100% absent from killed ads** — these are the highest-leverage individual elements.

---

## 4. CBO Algorithmic Signal

**Starved immediately (< $2 spend, < 50 impressions):** B1C1, B1C3, B2C1, B2C3, B4C3, B5C2, B5C3, B6C1, B6C2

Pattern: Engagement-signal rejection. CBO sampled, saw zero clicks or low clicks, decided not to scale. **HIGH CONFIDENCE: CBO's starvation is accurate feedback.**

**Funded slightly more ($2-$10 spend):** B4C1 ($6.41), B6C3 ($6.36)

Pattern: CBO saw early signal, committed small budget, then engagement failed to scale.

**Funded significantly ($10+ spend):** B2C2 ($37.99), B1C2 ($11.65), B5C1 ($22.92)

Pattern: CBO believed in these. Engagement was real; conversion was the missing piece.

**Meta audit penalties (high CPM, low impressions):** B1C3 ($175 CPM on 47 imp), B4C2 ($1,000 CPM on 14 imp)

Pattern: Compliance triggers. Meta priced these out of desirable inventory.

**Key insight:** Meta's algorithm is not arbitrating creative quality; it's arbitrating compliance and engagement. The campaign-level CPM problem is upstream (pixel, page, product, account) not at the creative layer.

---

## 5. Specific Framings That Consistently Failed

**Banned outright:**
- "Menopause" / "perimenopause" / "hormones" — Meta 2026 health-claim scanner trigger
- Doctor/dermatologist as endorser — separate Meta penalty
- Visceral disgust language ("throw up," "wanted to vomit") — content moderation trigger
- Active-harm framing ("your cream is hurting you") — wellness-conspiracy filter trigger

**Failed structurally (multiple ads, 0 engagement):**
- Opening with thesis or claim statement
- Opening with punchline or resolution
- Opening with slow inward emotional beat
- Opening with subtle interpretive gestures
- Generic compliments (not skin-specific)

**Conditional bans (work in body, fatal in opening):**
- Hiding behaviors / shame framing — only after hope established (40%+ mark)
- "Compounding damage" / urgency-via-fear language — replace with relational urgency

---

## 6. Design Constraints for New Batch — "Do Not" Rules

1. **Do not open with a thesis, claim, or problem-diagnosis.** First 3-5 sentences must be a SCENE with a named person and a specific moment.
2. **Do not use menopause, perimenopause, hormones, or estrogen language anywhere in first 150 words.**
3. **Do not use a doctor or medical professional as the person recommending or endorsing the product.** Doctor can be the dismissing foil, never the validator.
4. **Do not open with a punchline, quip, or the resolution to the story.** Opening must create an open loop.
5. **Do not lead with disgust/illness/visceral-reaction language** ("throw up," "gross," "disgusting," "sick to my stomach").
6. **Do not frame competitor products as "actively harming"** the reader. Differentiate as "wrong category" not "this is hurting you."
7. **Do not include hiding behaviors or emotional shame as the opening low point.** Low points must be functional ("foundation cracks by noon") not emotional ("I couldn't leave the house"). Shame framing only acceptable AFTER 30-40% mark.
8. **Do not lead with slow, introspective, inward emotional beats.** For cold paid placement, open with external moment first.
9. **Do not use subtle or interpretive gestures as the proof of the change.** Noticing must be explicit and skin-specific.
10. **Do not make noticing or compliments generic.** External witness must comment SPECIFICALLY on skin/face. "Your skin looks different" works. "You look beautiful" doesn't.
11. **Do not read engagement signal under 50 impressions or CPM under 100 impressions.** Hard threshold for noise vs signal.
12. **Do not use internal-decision urgency without external validation.** Urgency must be externalized through characters, calendar anchors, or habit-cessation discovery.
13. **Do not skip any of the 10-element converter skeleton.** Particularly do not skip: day-marker transformation, habit-cessation beat, close-mirrors-hook, identity-level payoff.
14. **Do not use generic "transformation" language without specific day numbers.** Day 1, Day 4, Day 9, Day 14, Day 21.
15. **Do not write under 1,400 words.** The Invisible Woman needs the full relational arc, not a functional summary.

---

## 7. What B8 Specifically Taught Us (NMN-Mirror Falsification)

B8 was built on theory that "NMN ads are short and mechanism-focused and convert on functional benefits — so tallow ads should mirror that format." Every B8 ad was killed. CBO didn't fund them. No conversions.

**Why short functional ads work for NMN but not tallow:**
- NMN buyer is analytical. Wants mechanism. Shorter copy is cleaner.
- Tallow buyer solves a RELATIONAL problem (being seen again, being touched the way he used to). The mechanism is required but not sufficient. Story is the conversion engine.
- B3C2 (converter that used mechanism-frontloading + intellectual register) worked but only generated 1 sale on the analytical sub-segment. The broader avatar needs ~1,500 words of story + mechanism + relational close.

**Operational lesson:** Don't transpose winning structures from product category to product category. Tallow's conversion threshold is relational, not functional.

---

## 8. What B10 Specifically Taught Us (Homesteader Mom Avatar Failure)

B10 tested the Homesteader Mom avatar. Hypothesis: "If Invisible Woman works, a completely different avatar should also work when written to the same 10-element skeleton." Result: B10 got delivered at brutal CPM ($116-184) and 0 conversions despite structurally sound ads.

**Competing interpretations:**
1. **Avatar hypothesis:** Homesteader Mom is NOT a tallow-cream buyer. She wants functional payoff ("hands that work"), not relational ("being seen"). Wrong audience for the product framing.
2. **CPM hypothesis:** Homesteader targeting triggered a different Meta audience classification. Smaller lookalike pool = higher CPM floor.
3. **Hybrid (most likely):** Both. Wrong avatar psychology AND higher CPM floor combined.

**What this tells us about avatar selection going forward:**
- Not every woman-over-40 buyer persona works for tallow cream
- The Invisible Woman avatar (women whose husbands/partners have stopped visibly noticing them) is the validated buyer
- Avatar-switching without sufficient converter volume is a CPM-tax
- Stick with Invisible Woman until 10+ converters; then systematically test other avatars with confidence

---

## Final Summary for Execution

**The killed ads in B1-B6 teach us:**

1. Hooks decide everything. Perfect 10-element body means nothing if the hook doesn't earn the first click.
2. Compliance violations are lethal and need pre-write auditing.
3. Density matters for conversion but not for CPM — density thesis was partially proven (better funnel, full-price sales) and partially falsified (CPM went up).
4. Scene openers beat thesis/punchline/confession/subtle openers. External noticing beats internal processing.
5. The 10-element skeleton is real. Every converter has it. Every killed ad is missing 3+ elements.
6. CBO is a good algorithm. It correctly starves low-engagement ads. The CPM problem is upstream.
7. Specific > generic. "Your skin looks different" beats "you look beautiful." Day numbers beat "works fast." Named characters beat abstract.

**For the new Friday May 15 batch:**

- Write to the 10-element skeleton. Don't experiment with structure.
- Lock the hook to one of the proven patterns (external noticing, accidental discovery, generational mirror, object discovery) and only vary the character/setting.
- Pre-audit every ad for compliance violations in first 150 words.
- Aim for 1,400-1,600 words.
- Stay with Invisible Woman avatar.
- Bake in the Pond's preempt from B7C1 comment analysis.
- Don't read engagement signal under 50 impressions.
