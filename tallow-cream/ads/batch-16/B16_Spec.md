# B16 Batch Spec — The Core Desire v2 Test

**Date drafted:** 2026-05-21
**Status:** Spec only. Writing to begin after BM is ready and budget recovered.
**Purpose:** Head-to-head test of Core Desire v2 ("I want my skin to cooperate again") + Urgency Anchor element against the v1 control (B5C1 as-is).
**Authority:** `tallow-cream/avatars/Core_Desire_v2.md`, `tallow-cream/sub-avatars/Core_Desire_Remapping.md`

---

## The Question B16 Answers

Does re-anchoring the Core Desire from "I want to be seen again" to "I want my skin to cooperate again" — and adding a structural Urgency Anchor beat — lift conversion on the most-validated converter (B5C1)?

If YES (v2 wins): the council's diagnosis is validated. B17 expands v2 across the roster (Mother's Photo close-swap, Sister Visit close-swap, Group Text close-swap). The Principles doc gets formally updated.

If NO (v1 wins or ties): v2's strategic reframe was wrong (or at least premature). We learn that the council's recognition-vs-intent diagnosis was incorrect, the existing v1 framing was already capturing what works, and the avatar work goes back to depth/precision within v1.

If UNCLEAR (mixed signal across the metrics): the test re-runs at higher spend before we change anything.

---

## Test Design

**Single-variable A/B, one sub-avatar, two ad variants.**

The sub-avatar: **Husband-Noticed** (most-validated converter, highest data signal). All other Sub-Avatars stay out of this test.

| Variant | Status | What it is |
|---|---|---|
| **B16C1 — Husband Noticed v2 (CONTROL)** | B5C1 as-written, no changes | The v1 Core Desire baseline. 1,500 words. Every element of the existing 10-element skeleton. Validated converter copy. |
| **B16C2 — Husband Noticed v2 (TEST)** | Rewrite of B5C1 with two specific changes | The v2 Core Desire variant. Same hook, same characters, same mechanism, same day markers, same body length. Two structural changes: (a) Urgency Anchor beat added between failed-products and discovery; (b) close swapped from husband-noticing-as-validation to self-orientation. |

### The two specific changes in the TEST variant

**Change 1: Urgency Anchor beat (added)**

50-120 words inserted between the failed-products list and the discovery scene. Daily-recurrence framing. The narrator names the *labor* of fighting her own skin every morning. Cost-bleed math is allowed but not required. Compliance: no "your skin is getting worse," no fake countdowns.

Draft Urgency Anchor for B16C2 (writer can refine):

> Every morning was the same morning. Foundation at seven. Cracking at eleven. Reapply at one. Useless by four. Wash off at ten. Then again tomorrow. I added it up in February. I had spent ninety-four dollars in the last six weeks on creams that did the same thing. Which was nothing. I wasn't sad about it anymore. I was just tired. Tired of fighting my own face every morning.

**Change 2: Close-swap (existing close replaced)**

Current B5C1 close: "It's the Tuesday. It's the moment someone who's been looking at your face for twenty-six years looks up and notices something changed."

v2 close: a self-orientation moment where the *narrator* notices the change herself, in her own routine, without an external witness validating it. The husband still appears (the hook still mirrors), but the *identity payoff* is internal.

Draft close-swap for B16C2 (writer can refine):

> The Tuesday after that, I was making coffee and I realized I hadn't checked my reflection in the kettle. I'd been doing it every morning for a year. The way you check a wound. I just made the coffee. That was the thing I got back. Not the soft cheek. The not-checking. The not-fighting first thing in the morning. The morning didn't have to be a fight anymore.

(Hook still mirrors: opens with husband-at-kitchen-table. Closes with narrator-at-kitchen-table-alone. The husband noticing earlier in Day 9 stays as a beat; the IDENTITY PAYOFF is the not-fighting.)

### What does NOT change between B16C1 and B16C2

- Same Sub-Avatar (Husband-Noticed)
- Same hook scene (husband at kitchen table)
- Same narrator (Anne, 53, accountant, Pittsburgh, married Dave)
- Same discovery character (Lisa, college friend who texts the selfie)
- Same mechanism explanation (water vs oil, after 40)
- Same day-marker structure (Day 1, 5, 10, 14, 17, 19)
- Same habit-cessation beat (the morning phone-camera check stops)
- Same image prompt (same Tuesday-kitchen-table aesthetic)
- Same Meta Headline ("He never notices anything.")
- Same Meta Description
- Same body length (~1,500 words)
- Same 60-day guarantee placement
- Same price/offer treatment

This isolates two variables (Urgency Anchor added, close swapped) on top of an identical foundation. Cleanest possible A/B given budget.

---

## Campaign Structure

| Setting | Value |
|---|---|
| Campaign | One CBO campaign, "B16 Core Desire Test" |
| Budget | $50/day total ($25/ad) |
| Ad Set | One ad set, both ads inside it |
| Audience | Broad. Identical for both ads. Post-Andromeda; creative does the targeting. |
| Optimization | Purchase |
| Placement | Advantage+ Placements |
| Page | Julie Brennan partner page |
| Pixel | New pixel (post-pixel-verification) |
| Payment | New virtual Visa Debit |

CBO will distribute spend toward whichever ad performs. That distribution itself becomes the first signal.

---

## Decision Criteria

**Minimum spend before reading signal:** $200 total ($100 per ad equivalent). Below that, results are noise.

**Run length:** 14 days at $50/day = $700. Decision read at day 14, unless one ad is clearly starving by day 4 (in which case the CBO has already made the call).

**Primary metric:** Purchase-conversion rate per LPV (LPV → Purchase percentage). Whichever ad converts a higher % of LPVs to purchases wins on this metric.

**Secondary metrics:**
- CPM (which ad delivers cheaper — auction-classification signal)
- CTR (which hook is reading better — surface engagement)
- Adds-to-Cart per LPV (which ad gets the cart commitment)
- Comments-to-LPV ratio (qualitative signal: which ad triggers "that's me" recognition vs "interesting")

**Decision rules:**

| Outcome | What it means | Next action |
|---|---|---|
| B16C2 wins on purchases AND ATC | v2 validated. Council's diagnosis correct. | B17 expands v2 across roster |
| B16C1 wins on purchases AND ATC | v1 was already correct. Council's diagnosis wrong. | Hold v1 framing. Re-examine v2 thesis. |
| B16C2 wins on CTR/CPM but B16C1 wins on purchases | v2's hook is better but its conversion mechanism is weaker — likely the close-swap helped engagement but lost the commitment that "being seen" was driving | Test Urgency Anchor alone (without close-swap) in B17 |
| B16C1 wins on CTR/CPM but B16C2 wins on purchases | v1's hook is better but v2's body is converting — likely the close-swap is doing the work | Test close-swap alone (without Urgency Anchor) in B17 |
| Both ads starve / no conversions | Test failed for non-test reasons (CPM, audience, BM issues). Re-examine upstream before re-running. | Diagnose, then re-run B16 with whatever's fixed |

---

## What B16 does NOT test

- Whether v2 lifts other sub-avatars (that's B17+)
- Whether the v2 close-swap alone would have won (that's an isolated B17 test if needed)
- Whether the Urgency Anchor alone would have won (same — isolated B17 test if needed)
- Whether Photo Avoider can be re-framed to v2 (separate question, separate batch)
- Whether the Anniversary / Reunion / other event-anchored variants outperform the recurrence-anchored Urgency Anchor (later)

The point of B16 is to answer ONE question with the cleanest possible signal. If it answers yes, we know what to expand. If it answers no, we save the cascade work and re-think.

---

## Pre-launch checklist

- [ ] Pixel value attribution verified (carries over from prior pre-launch list)
- [ ] BOGO automatic discount created in Shopify admin
- [ ] BOGO Custom Liquid block pasted on PDP
- [ ] PDP banned-phrase fix applied (carries over from Origins Strategy Audit)
- [ ] B16C1 (control) committed to repo as exact copy of B5C1
- [ ] B16C2 (test) drafted, audited against 11-element v2 skeleton, density-checked
- [ ] Image generated for B16C2 (or reused from B5C1 if visually identical)
- [ ] Tracker updated to include B16 row(s)
- [ ] Campaign built in Meta but paused, ready to flip on

---

## What B16 means for the avatar work

Win or lose, B16 is the test that turns the council's diagnosis from *opinion* into *evidence*. Until B16 runs, v2 is a strategic bet based on convergent adversarial review. After B16, it's either validated or refuted. That's the right way to use the council — not as a substitute for testing, but as a sharper-than-usual hypothesis to test.

*B16 spec locked 2026-05-21. Writing the two ad files (B16C1, B16C2) begins after the launch infrastructure recovers. B16C1 is essentially a re-commit of B5C1; B16C2 is the new copy work.*
