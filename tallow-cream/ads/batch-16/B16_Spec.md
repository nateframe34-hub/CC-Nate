# B16 Batch Spec — Narrowed v2 + Urgency vs Proven Benchmark

**Date drafted:** 2026-05-21 (supersedes the original single-variable v1-vs-v2 spec)
**Status:** Spec. Awaiting founder green-light on the two narrowed-avatar picks, then ad copy gets written.
**Authority:** `tallow-cream/avatars/Core_Desire_v2.md`, `tallow-cream/sub-avatars/Core_Desire_Remapping.md`, `tallow-cream/sub-avatars/narrowed/`

> **Why this spec was rewritten:** The original B16 tested broad-B5C1-v1 against broad-B5C1-v2. That tests a baseline we've already decided to retire (broad parent avatars). We narrowed the sub-avatars AFTER B5C1 was written, and our actual go-forward strategy is narrow + v2 core desire + urgency anchor. B16 now tests THAT strategy against a proven converter benchmark, instead of re-litigating a broad baseline neither version of the strategy will use.

---

## The Question B16 Answers

Does our new approach — a NARROWED sub-avatar, written on Core Desire v2 ("I want my skin to cooperate again"), with the Urgency Anchor beat — beat our best PROVEN converter in a live head-to-head?

This bundles three changes (narrowing + v2 core + urgency) into the test ads. We accept that a win won't isolate which change drove it. The trade is deliberate: at this stage we need a WINNER more than we need clean attribution. Variable isolation is B17's job, run only on whatever wins here.

---

## Test Design

**One CBO campaign. One ad set. Three ads. Same Relational psychographic pool (keeps the fresh-BM lookalike seed clean).**

| Ad | Role | Sub-Avatar | Core Desire | Urgency Anchor | Notes |
|---|---|---|---|---|---|
| **B16C1** | BENCHMARK | One-Jar Discovery | v1 (as-written) | none (v1) | Exact copy of B9C3. Closest-to-winner converter (13.79% CTR, 4.62x best-day ROAS). The number to beat. We will not keep running it long-term; it exists here as the valid same-auction reference. |
| **B16C2** | NEW BET #1 | **Anniversary Husband-Noticed** (narrowed) | v2 | YES — deadline (milestone anniversary) | Built-in urgency: a real date approaching. Tests whether narrow + v2 + native-deadline-urgency beats the benchmark. |
| **B16C3** | NEW BET #2 | **Reunion One-Jar** (narrowed) | v2 | YES — comparison event (reunion) | Built-in urgency: same-age peer who aged better. Same parent as the benchmark (One-Jar), so C1-vs-C3 is a near-clean read on what narrowing + v2 + urgency does to the One-Jar avatar specifically. |

### Why these two narrowed avatars

Both were chosen because their urgency is NATIVE, not bolted on. The Urgency Anchor element risks feeling artificial if forced. Anniversary (a real deadline) and Reunion (a real comparison event) carry urgency inside the avatar's situation, so the Anchor beat writes itself.

Both are in the Relational pool (per the reach agent's warning not to mix pools during BM warmup). Anti-System avatars (Sebum-Anger, Retinol Burnout) are deliberately excluded from B16 to keep the lookalike seed clean.

**C1 vs C3 is the sharpest internal comparison:** both are the One-Jar avatar. C1 is broad/v1, C3 is narrowed/v2/urgency. If C3 beats C1, that's the cleanest single signal in the test that the new approach works on a held-constant avatar.

---

## What each test ad must contain (v2 11-element skeleton)

Both B16C2 and B16C3 must hit all 11 elements of the v2 converter skeleton (see `Core_Desire_v2.md`), with particular attention to the two NEW-vs-B5C1 things:

1. **Core Desire v2 framing throughout** — the conflict is woman-vs-her-own-skin (the skin is the adversary she fights every morning), NOT woman-vs-absent-validation. The narrator wants her skin to cooperate, not to be noticed.
2. **Urgency Anchor beat** (element #5) — placed between failed-products list and discovery scene. 50-120 words. Native to the avatar's situation:
   - B16C2 (Anniversary): the deadline. "The anniversary is in nine weeks. Every morning between now and then my face is going to do the same thing it did today."
   - B16C3 (Reunion): the comparison + the daily grind. "I've got four months until the reunion and a face that quits by noon."
3. **Self-orientation close** (not external-validation) — the identity payoff is the narrator's own relief from the daily fight. External witnesses (husband, the reunion peer) can appear, but the PAYOFF is internal ("the morning stopped being a fight"), not "someone saw me."

Everything else (peer-adjacent authority, mechanism by discovery character, day markers, habit-cessation, close-mirrors-hook, compliance posture, 1,400-1,600 words) per the locked skeleton.

---

## Campaign Structure

| Setting | Value |
|---|---|
| Campaign | One CBO campaign, "B16 Narrowed v2 Test" |
| Budget | $50/day total (CBO distributes; ~$16/ad if even, but CBO will concentrate) |
| Ad Set | One ad set, all three ads inside |
| Audience | Broad, identical for all three. Creative does the targeting. |
| Optimization | Purchase |
| Placement | Advantage+ Placements |
| Page | Julie Brennan partner page |
| Pixel | New pixel (post-verification) |
| Payment | New virtual Visa Debit |

CBO concentrating budget is itself the first signal — watch which of the three it feeds.

---

## Decision Criteria

**Minimum spend before reading signal:** $250 total. Below that = noise.
**Run length:** 14 days at $50/day = $700. Read at day 14 unless CBO has clearly starved an ad by day 4-5.
**Primary metric:** LPV → Purchase rate (which ad converts the highest % of landing-page views to purchases).
**Secondary:** CPM (auction-classification signal), CTR (hook strength), ATC/LPV (cart commitment), comments-to-LPV (qualitative "that's me" vs "interesting").

| Outcome | Meaning | Next action |
|---|---|---|
| A test ad (C2 or C3) beats benchmark C1 on purchases | New approach (narrow+v2+urgency) validated. We have a winner. | B17: isolate which change drove it (run the winner with one variable reverted), AND expand the winning avatar's frame across the roster |
| Benchmark C1 beats both test ads | New approach did not beat proven broad converter. The narrowing/v2/urgency bundle isn't better — or the execution missed. | Re-examine. Do NOT cascade v2 across the roster. Possibly re-run with different narrowed avatars before abandoning v2. |
| C3 beats C1 but C2 doesn't | The new approach works on the One-Jar avatar (held constant) but the Anniversary/Husband-Noticed execution missed | Winner is the One-Jar v2 direction. Drop Anniversary execution, iterate Reunion. |
| All three convert similarly | Either everything works (unlikely) or the avatar/frame isn't the lever at this spend | Read CPM/CTR for tiebreak; likely need higher spend or the bottleneck is upstream |
| Nothing converts | Upstream problem (CPM, BM, pixel, timing), not creative | Diagnose upstream before re-running |

---

## What B16 deliberately does NOT do

- It does not cleanly isolate v1-vs-v2 (we accepted that trade; B17 isolates on the winner)
- It does not test the Anti-System pool (kept out to protect the lookalike seed)
- It does not test Photo Avoider (held for structural re-frame)
- It does not test more than 2 new avatars (3 ads is the max for a clean $50/day read)

---

## Pre-launch checklist

- [ ] Pixel value attribution verified
- [ ] BOGO automatic discount created in Shopify admin
- [ ] BOGO Custom Liquid block pasted on PDP
- [ ] PDP banned-phrase fix applied (menopause / 60% — per Origins Strategy Audit)
- [ ] B16C1 committed as exact copy of B9C3
- [ ] B16C2 (Anniversary Husband-Noticed, v2 + urgency) written + audited against 11-element skeleton
- [ ] B16C3 (Reunion One-Jar, v2 + urgency) written + audited against 11-element skeleton
- [ ] Images generated for C2 and C3 (C1 reuses B9C3's image)
- [ ] Tracker updated with B16 rows + the 5 new test-variable columns
- [ ] Campaign built in Meta, paused, ready to flip on

---

## Open decision (awaiting founder)

The two narrowed-avatar picks for the test slots. Current proposal: **Anniversary Husband-Noticed (C2)** + **Reunion One-Jar (C3)**, chosen for native urgency + Relational-pool consistency + the clean C1-vs-C3 One-Jar comparison. Alternatives available in `tallow-cream/sub-avatars/narrowed/`: Empty-Nest or Grieving-Daughter (Husband-Noticed); Divorced-Friend or Work-Mentor (One-Jar); Executor / Caregiver / New-Grandmother (Mother's Photo). Founder confirms or swaps before copy is written.

---

*B16 spec v2 locked 2026-05-21. Replaces the original single-variable v1-vs-v2 design. Ad copy written after avatar picks are confirmed and launch infrastructure recovers.*
