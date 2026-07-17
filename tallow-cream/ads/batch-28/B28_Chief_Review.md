# B28 Chief Review

**Date:** 2026-07-15
**Reviewed against:** the single-angle test constraints (`B28_Test_Skeleton_Single_Angle_Discipline.md`), the 10-element converter skeleton (`Converter_Pattern_Synthesis.md`), the killed-batch Do-Not rules (`Killed_Batch_Failure_Analysis.md`), and the account's compliance strike lists.
**Outcome:** 7 issues found, all fixed directly in the copy files. 2 open items left for founder decision at launch.

---

## Issues found and fixed

### 1. B28C1 contained the banned word "wrinkles" (SEVERITY: HIGH, compliance)
"Not fewer wrinkles. The quiet." The word "wrinkles" is on the account's own banned-phrase list (every B17-family compliance audit reads "Zero banned phrases (menopause, hormones, anti-aging, wrinkles)"). One word could have re-introduced exactly the personal-attribute classification tax this whole batch is trying to remove. Fixed: "Not the skin. The quiet."

### 2. B28C3's mechanism authority was a NURSE (SEVERITY: HIGH, compliance + test integrity)
"Priya's sister-in-law, a nurse, who explained it..." A medical professional delivering the mechanism and recommending tallow is the formally banned medical-endorsement pattern, B1C3 died on exactly this ($175 CPM, 0% CTR), and the killed-batch rules state it flatly: doctor/nurse can be the dismissing foil, never the validator. In a batch built to LOWER CPM, this was directly counterproductive. Fixed: sister-in-law is now "the one in their family who reads the back of every bottle before she buys anything," peer-adjacent, zero credentials, same function.

### 3. B28C1 kept B17C1's Sylvia beats, which are SA1 material, violating the batch's own single-angle rule (SEVERITY: HIGH, test validity)
`Brand_Mastery.md` explicitly credits "the Sylvia beat" (coworker noticing she looks different) to SA1 The Tired-Looking. First draft carried both Sylvia scenes over from B17C1 nearly verbatim, meaning the "single-angle" SA2 cell was actually running SA2 + SA1, quietly reproducing the exact angle-mixing this test exists to remove. Fixed: both Sylvia scenes rewritten SA2-native. Day 9 she asks what product the narrator is testing this month (buying-cycle validation, narrator is the known product-churner with "a review for everything"). Week 5 she asks for the switch because "my cabinet looks like yours used to." Sylvia now validates the inventory change, never the appearance change.

### 4. B28C1's Day 14 beat was SA4 material (SEVERITY: MEDIUM, test validity)
"Foundation cracked around my mouth by 2pm" is SA4 The Tight-by-Noon's signature experience per `Brand_Mastery.md`'s own entry ("foundation cracks by 2pm"). Same class of graft as issue 3. Fixed: Day 14 is now a graveyard-native beat, she bags six of the fourteen for the garage ("Not brave enough for the trash yet. The garage first."), which is arguably a stronger and more original beat than the one it replaced.

### 5. B28C3 opened solo-internal, the exact opener pattern that killed 5+ ads (SEVERITY: HIGH, conversion odds)
First draft opened with the narrator describing her own morning routine, no named person, no dialogue. `Killed_Batch_Failure_Analysis.md` rule 1: "first 3-5 sentences must be a SCENE with a named person and a specific moment," and its Pattern C documents five killed ads whose hooks didn't open loops (including B4C1's internal-state opener, starved to death). Fixed: restructured to open on the Priya Thursday exchange ("Doesn't it seem insane that we do this every single day and it still doesn't hold?"), external dialogue + named person + specific moment + open loop, with the morning-routine inventory moved to section 2.

### 6. B28C3 contained a Cost-Bleed echo, a disproven beat (SEVERITY: MEDIUM)
"I did the math on that once... stopped doing the math when the number got embarrassing" closely mirrored B17C3's Cost-Bleed urgency anchor ("I did the math once. Just once."), the one urgency variant that got real delivery in B17 and cleanly failed to convert ($46 spend, 0 purchases). No reason to carry a disproven beat's fingerprint into a fresh test. Fixed: paragraph removed, low point now rests entirely on the three-backup-tubes system. The later callback line also fixed ("The three backup tubes I hadn't touched in a month" instead of "the math I'd stopped doing").

### 7. Strike-list adverbs scattered through all 3 cells (SEVERITY: LOW, voice discipline)
"actually" x6, "really" x2 across the three bodies. The converter audits hold a zero-strike-adverb standard. All removed or rewritten; C2's "already braced before you've looked" reads tighter than the original anyway. Also softened C2's sharpest shame-diagnostic line ("expecting to be disappointing before anyone's even looked" -> "bracing for nothing"), since the bracing low-point sits right at the ~30% boundary where killed-batch rule 7 starts tolerating shame framing, no reason to run the hottest possible phrasing at the boundary.

---

## Verified clean (checked, no action needed)

- **Single-angle discipline post-fix:** C1 is now SA2 end-to-end (hook, mechanism, validation, habit-cessation, close all inventory/buying-cycle). C2 is SA3 end-to-end (remembered-absence hook, deflection-habit cessation, husband-notice close which is native here). C3 is SA4 end-to-end (shared-ritual dialogue hook, reapplication mechanism framing, backup-tubes cessation, absence-of-maintenance close).
- **No age numbers** in any body (contextual age only: preschool-era friendships, nineteen-year marriage, years at the same desk).
- **No menopause/hormone/anti-aging/wrinkle language** (post-fix).
- **No villain-beat industry-blame** in any cell.
- **Skeptic-convert beat** present in all 3. **Day-numbered transformation** (1/4/9/14/21) in all 3. **Habit-cessation beat** in all 3, each angle-native. **Peer-adjacent non-medical authority** in all 3 (post-fix). **Close mirrors hook** in all 3 (C1 counter->cabinet, C2 October Tuesday->May Saturday, C3 Thursday ritual->"Nothing, that's the whole thing now").
- **Mechanism at ~50% mark** in all 3, same three beats (skin makes oil, water-first labels, water evaporates), delivered by a different character in each.
- **Dividers identical** across cells (`-------------`), word counts in a matched ~1,000-1,100 band.
- **Image prompts:** all three are object-scene, no faces, no text, no logos, consistent with the account's only proven-converting creative family (B17C1's jar-on-counter) and NOT the disproven bold/face direction (B23) or human-presence direction (B21 H1-C).

## Open items for founder at launch (not copy problems)

1. **B28C1's headline is identical to live B17C1's ("One jar. Fourteen down.").** Same locked hook, and B17C1 is still running. Two live ads with the same headline and overlapping story will compete in the same auction pockets and could muddy C1's fresh-object CPM read. Options: pause B17C1 during B28's read window (cleanest), or accept the overlap and read C1 with that caveat. Founder's call, flagging it so it's a decision rather than an accident.
2. **C2's bracing/flinch low point** is compliant per the account's rules as written (functional framing, post-30% shame tolerance, softened per issue 7), but it's the closest of the three cells to the B3C1 "hiding behavior" failure family. If C2 alone comes back with an outlier CPM, this section is the first suspect, noted here so the postmortem doesn't have to rediscover it.

---

*All fixes applied directly to the three copy files in this folder. Zero em-dashes verified post-edit.*
