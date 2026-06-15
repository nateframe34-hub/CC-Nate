# B17 Pre-Launch Council Log (Round 3)

**Date:** 2026-06-15
**Method:** 5-agent council, third round, focused on Julie-voice authenticity + ad-to-PDP/offer congruence + persuasion flow + image continuity + a mandatory challenger to guard against over-polishing. Triage rule: only fix factual errors, banned phrases, and customer-visible continuity breaks. Defer tonal/identity findings to the post-test iteration.

---

## ACCEPTED FIXES (applied)

**1. PDP banned-phrase fix (the urgent one).** `tallow-cream/store/copy/PDP_Copy_v2.md` lines 132 and 200 still contained "menopause" and "up to 60% less." Meta scrapes landing pages on review; an ad-clean / PDP-not-clean state risks the fresh BM after warmup. Fixed:
- Line 132: "up to 60% less" -> "a lot less"; "After menopause, it can drop even further" -> "After your skin changes, the drop can be bigger."
- Line 200 (Karen M. review): "I'm 54 and menopausal... actually glowing" -> "I'm 54 and my skin changed... soft and actually holding through the day." (Also removes "glowing" which is on the banned list.)

This was a Phase 1 Tier 1 item per the Mastery Council, pending since May 21. Closed.

**2. C3 anchor compression.** The "About thirty-three hundred dollars. Two years." line read as accountant register breaking from the on-the-tub narrator voice. Compressed to a single line so the math feels like a private wince, not a calculation. Anchor-only, isolation preserved.

**3. C4 anchor de-stacking.** Removed "Elaine said that was the line that made her order one." Persuasion-flow agent flagged it as double-stamping Elaine's already-stated nine-months-earlier conversion and creating a premature climax stack right before the mechanism block. Also tightened the framing-line word order. Anchor-only, isolation preserved.

---

## DEFERRED FINDINGS (real, but not for B17)

**1. Ad's "60-day money-back" vs PDP's "keep-it" guarantee mismatch.** The PDP offer block delivers a stronger guarantee than the ad promises. The temptation is to upgrade the ad's close to match. Deferred because the proven converter (C1 = B9C3 verbatim) ran with the weaker "money-back" promise and still converted at ~17%, and changing C1 breaks the test's isolation. **This is the single strongest candidate edit for the post-B17 iteration.** Tested deliberately against the converter, this could be the highest-leverage swing in the next batch.

**2. Julie partner-page identity vs ad narrator mismatch.** Julie's `Partner_Page_Identity.md` documents her as 48, 17-year-old daughter (unnamed in doc), son 21, husband Mark, discovery-via-Denise-at-husband's-holiday-party. The B17/B9C3 narrator is 54, daughter Lily 27, husband unnamed, no son, discovery-via-Elaine-and-Aunt-Winnie. A reader who clicks through Julie's profile lands on a different woman than the ad implied. The right fix: **update the identity doc to match the proven converter, not the other way around.** Schedule during BM warmup, not blocking B17 launch.

**3. PDP_Copy_v2.md bundle/upsell ladder language** (Sections 1 and 10). The live offer block is single-jar (correct), but `PDP_Copy_v2.md` Sections 1 and 10 still reference the Try It / Stock Up / Best Value ladder. Confirm in Shopify admin that the Custom Liquid offer block has replaced those sections on the rendered page. If yes, no action. If the bundle ladder still renders, strip it.

**4. The "Save $20" pill vs "Launch price going to $59.99" framing.** The offer block currently shows the chip. The honest forward-looking line was discussed in the offer council. Optional swap, not blocking B17.

---

## NOTES FOR READING B17 RESULTS

**Urgency-source confound flagged by the persuasion-flow agent:** C2 and C3 deliver urgency from the narrator herself (internal recognition). C4 delivers urgency from Aunt Winnie via Elaine (external elder-permission). This is a real structural difference, not just a mechanism difference. When C4 reads its result, score it carefully:
- If C4 wins, it could be "recoverability urgency works" OR it could be "elder-permission persuasion beats self-realization in this avatar." Different conclusions, different next moves.
- If C2 wins clearly over C4, this confirms internal/self-realization urgency is the lever, not just any urgency.
- The clean way to separate this in a future test is a C4-style ad with the elder voice removed and the narrator delivering the same recoverability beat internally.

---

## IGNORED FINDINGS (challenger-protected)

- The image agent's "two or three ring-marks" tweak (unforced change to a proven image asset).
- Any "Julie would not say it that way" voice flags on the shared B9C3 body (would break control isolation).
- The "Read this part slowly" / "This isn't an ad" / "Saturday night" lines the previous customer-eyes agent flagged. Already logged in `B17_Proofing_Council_Log.md` as post-test candidates. Not relitigating.

---

## VERIFICATION

- Em-dashes across all four files: 0
- Banned phrases in B17 body copy: 0
- Banned phrases in PDP_Copy_v2.md after fix: 0 (verified)
- Isolation: each variant differs from C1 only in the urgency anchor block

**Status: B17 is clean to ship. Pre-launch checklist for the founder:**
1. Confirm the PDP fix renders live on Shopify (PDP_Copy_v2.md changes deployed).
2. Read the C4 garden beat aloud per the long-standing gate.
3. Update Julie's `Partner_Page_Identity.md` to match the narrator during BM warmup (deferred item #2).

---

*Round 3 council, 2026-06-15. The challenger held: only banned phrases and customer-visible continuity breaks shipped. Three tonal/structural findings logged for post-B17 iteration. The next round of polishing is the market.*
