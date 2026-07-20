# Batch 30 Plan - SA1 "The Tired-Looking," Single-Angle Deep Dive + Awareness-Bridge Isolation Test

**Date:** 2026-07-19
**Status:** PLAN ONLY. No copy written yet, this is the strategy document for founder sign-off before writing begins.
**Trigger:** B28 confirmed the account has a top-of-funnel problem it can already solve (B28C1's CTR/CPC were strong) but a down-funnel conversion problem it hasn't solved (1 ATC total across the batch, 0 purchases). This batch is designed specifically to attack the conversion leak, not to find another hook.

---

## Why this batch is structured the way it is (read this before the per-cell breakdowns)

Two outside ideas came in alongside the "we need conversions" directive, and both check out against this account's own data rather than being taken on faith:

**1. The awareness-level mismatch idea.** The claim: every buyer converts at Most-Aware (the PDP, since it's where they see your brand/product/offer together), and an ad that's Problem- or Solution-Aware but sends the click straight to a Most-Aware page breaks the journey mid-stream. Checked against this account: our native ads are NOT the problem here, they already walk the reader up through awareness inside the copy itself (scene → mechanism reveal → skeptic-convert/product intro → transformation → price/guarantee close, which is Solution-Aware opening to a Most-Aware close, all within the ad). But the CLICK still dumps the reader from that finished narrative onto a generic commerce page (hero image, price, Add to Cart button) with zero continuity of voice or story. That's the actual mismatch moment, at the click, not in the copy. And it lines up exactly with B28's data: strong CTR (people are engaged and clicking) but the funnel breaks right after (LPV happens, ATC barely happens, purchase doesn't). **Real, previously-unused infrastructure already exists for this fix:** `tallow-cream/store/theme/sections/tallow-advertorial.liquid` is a full advertorial page, built, styled, on-brand, and its DEFAULT content is literally headlined "She Uses One Jar. Her Skin Doesn't Look Tired Anymore." with a hero image alt-text of "one jar on an empty bathroom counter." It was built for this exact angle and has never been sent a single visitor. Cell 4 below tests it directly.

**2. The single-angle-depth idea.** The claim: pick one angle, prove it converts, then squeeze it across different EMOTIONAL PATHWAYS into the same core trigger for different people, rather than burning budget testing many shallow angles and abandoning most of them. Checked against this account's own `Killed_Batch_Failure_Analysis.md`: that's close to a documented lesson already, "test 10 angles, drop 8" is exactly the pattern that produced 15 killed ads in batches 1-6 with only 3-4 of 10 skeleton elements present each, versus the converters that share a dense, consistent skeleton. `Brand_Mastery.md` also independently names one sub-avatar, SA1 The Tired-Looking, as "⭐ STRONGEST," backed by 3 verbatim-validated real-language hooks, and flags it as **completely untested as a lead angle** (every batch to date has tested SA2/SA3/SA4/SA6 instead). Between the account's own strongest-rated, most-validated, never-tried angle and the discipline of going deep instead of wide, SA1 is the correct next bet on the numbers alone, independent of the friend's framework.

**How the two ideas combine into this batch:** 3 cells test SA1's ONE core trigger ("surface dryness reads as tired to other people and to yourself, fixing hydration fixes the read") through 3 different emotional entry pathways drawn directly from SA1's own 3 already-researched angles in `Brand_Mastery.md` (self-recognition, external-comment accumulation, identity-reclaiming). All 3 keep the proven 10-element skeleton fully intact and route straight to the PDP, exactly like every prior converter, so this is NOT an unproven format, it's the account's best untapped angle run the way angles have always been proven to work here. A 4th, budget-isolated cell reuses the strongest of those 3 pathways verbatim but changes exactly one variable, the landing destination, native ad → advertorial → PDP, instead of native ad → PDP directly, to test the awareness-bridge hypothesis in isolation without touching angle, hook, or copy at all.

---

## Batch structure

| Cell | Pathway (same core trigger, different entry) | Landing destination | Purpose |
|---|---|---|---|
| B30C1 | Self-Recognition | PDP direct | Primary SA1 lead test |
| B30C2 | External-Comment Accumulation | PDP direct | Primary SA1 lead test |
| B30C3 | Identity-Reclaiming | PDP direct | Primary SA1 lead test |
| B30C4 | Self-Recognition (= B30C1's copy, verbatim) | **Advertorial → PDP** | Isolated awareness-bridge test, single variable change from B30C1 |

**Budget protocol, matching the account's own locked discipline:** each cell in its own ad set, protected/floored budget, no CBO starvation risk (per the standing CBO-starvation lesson from the killed-batch analysis and the B28 15%-floor precedent). B30C4 in particular needs true isolation since it's the one genuinely new structural variable in this batch, not sharing budget or learnings with C1-C3. Apply the existing governing kill rule (2x Ideal Scaling CAC, $40 no-purchase since launch) per cell, unproven regime, same as B28's read.

---

## B30C1 - Self-Recognition Pathway

**1. What we are testing:** SA1 Angle 1 ("Stops your skin from looking tired"), entered through a self-recognition moment, the narrator sees herself somewhere unflattering (a video call screenshot, a photo someone else took) and doesn't recognize the tiredness as fatigue, only as her own face.

**2. Why we are testing it:** SA1 is the account's own top-rated, completely untested-as-lead sub-avatar. Every other batch has tested SA2/3/4/6. This is the highest-research-confidence angle in the account that has never been given a real shot as a lead.

**3. Why high chance of success, from avatar research:** `Brand_Mastery.md` rates SA1 "⭐ STRONGEST" of all 8 sub-avatars researched, and its Angle 1 hook is verbatim-validated (added 2026-07-06 specifically because it plays off a real, already-existing cultural phrase, "it's just my face," rather than inventing a new claim). Verbatim-validated language is the account's highest bar for research confidence, most angles in the doc are hooks written FROM research, this one is a hook FOUND IN research.

**4. Why high chance of success, from data:** Two independent data points support the mechanism this angle relies on. First, B28's just-completed comparative analysis found the account's best-performing creative element is a genuinely ambiguous, voyeuristic visual moment (the empty-counter jar shot), not a straightforward before/after or lifestyle photo, this angle's video-call-screenshot hook has the same structural quality, a private, unposed, "caught off guard" moment. Second, the existing (unused) advertorial page was already built with this exact angle's headline and imagery as its DEFAULT content before this plan existed, meaning a previous pass at this account independently converged on SA1/self-recognition as the strongest creative bet without today's research pass referencing it.

**5. Awareness level:** Solution-Aware. She already knows something is making her look tired that isn't sleep (she's ruled out the obvious explanation), she just hasn't connected it to her skin specifically yet. This matches the proven posture of every converter to date, this batch is not experimenting with awareness level in the copy, only (in C4) at the click-through moment.

**6. Hook:** "It's not 'just my face.' It was my skin." (verbatim-validated, `Brand_Mastery.md` SA1 Angle 1) opening on the video-call-screenshot scene.

**7. Why this will convert, reasoning from research and data:** The killed-batch analysis identifies "external noticing as hook" and "skin-specific noticing language" as 2 of the top-3 highest-leverage elements separating converters from killed ads (present in 100% of converters, largely absent in killed ads). This hook IS the skin-specific noticing, self-directed rather than said by someone else, which is a variation the account hasn't run before (all prior converters use an external character delivering the noticing). Testing whether the reader can deliver her own noticing to herself, in her own words, converts as well as hearing it from a husband or friend is itself useful data regardless of pathway.

**8. What creative and why:** A phone held up, showing a paused video-call frame or a photo just taken by someone else, on a kitchen counter or in a car, unstaged, the narrator's own hand in frame holding the phone. Ambiguous enough that a scroller has to look for a half-second to understand what they're looking at (the B28-validated principle), NOT a mirror selfie (that reads as generic beauty-ad content per B28C2's dead-CTR lesson).

**9. Story arc:**
- **Hook/scene (0-10%):** She's scrolling through photos from a birthday dinner the next morning and stops on one someone else took of her mid-laugh. She looks exhausted. She wasn't. She'd slept nine hours.
- **Externalized noticing, specific (10-20%):** She starts noticing it in every recent photo, at her kid's game, at a work lunch. Not a bad-lighting problem, it's consistent. Names the exact "you look tired" comment she's gotten from a specific person recently and how it didn't match how she felt.
- **Peer-adjacent authority introduced (20-35%):** A named friend or family member (new character, not reused from B28) who she confides in, who's noticed the same thing about her own face in the past and has an answer.
- **Mechanism reveal via that peer, discovery-style (35-50%):** Skin makes its own oil; most products are water-first and evaporate; the "tired" read is surface dryness pulling light flat, not fatigue. Same locked, proven mechanism language as every prior converter.
- **Skeptic-convert + product intro (50-60%):** "Cow fat, on my face" beat, unchanged, cross-cutting proven material.
- **Day-numbered transformation (60-80%):** Day 1 texture note, Day 4 waking-up noticing, a specific day where she looks at a new photo of herself and doesn't flinch.
- **Habit-cessation beat (80-85%):** Something she used to do without noticing (over-correcting with makeup around the eyes, avoiding video calls, a concealer routine) that she realizes she's quietly stopped.
- **Close mirrors hook (85-100%):** Another photo moment, this time she looks at it and doesn't see tired, she sees herself. Identity-level payoff: not younger, just accurately herself again, tying to SA1 Angle 3's compliance-safe framing without needing a full separate angle for it.

---

## B30C2 - External-Comment Accumulation Pathway

**1. What we are testing:** SA1 Angle 2 ("Ends the 'are you okay?' comments"), entered through a specific, counted accumulation of unwanted comments rather than a single moment.

**2. Why we are testing it:** Second entry pathway into the same SA1 trigger, testing whether an accumulation/tally structure (multiple people, multiple moments) converts differently than a single self-recognition scene (C1) or a single identity moment (C3).

**3. Why high chance of success, from avatar research:** `Brand_Mastery.md`'s Angle 2 hook, "Three people asked if I was tired this month. I was fine. My skin wasn't," is drawn from the same verbatim-validated research pass as Angle 1, same confidence tier, different entry emotion (external social friction vs. private self-recognition).

**4. Why high chance of success, from data:** The account's own converter pattern research (`Converter_Pattern_Synthesis.md`) established that the husband-notice verbal-comment mechanism is load-bearing and skin-specific noticing beats generic compliments (B6 hypothesis test, `Killed_Batch_Failure_Analysis.md` Pattern F). This pathway extends that proven mechanism from a single close-beat (SA3's "he stopped mid-sentence") into the OPENING hook itself, testing it as a lead rather than only a close.

**5. Awareness level:** Solution-Aware, same posture as C1, she's aware something is wrong (repeated comments) but hasn't connected it to a fixable cause yet.

**6. Hook:** "Three people asked if I was tired this month. I was fine. My skin wasn't." Cold open on the tally itself, no throat-clearing.

**7. Why this will convert, reasoning from research and data:** This is the only one of the 3 primary cells that opens on other people's words rather than the narrator's own observation, giving the batch genuine internal variance to read (does hearing it from others land harder than seeing it herself, per the friend's "different emotional pathways to the same trigger" framing) while keeping every other structural element, mechanism, day-markers, close, identical and controlled.

**8. What creative and why:** A candid group setting, not posed, where the concern-comment would plausibly happen, a lunch table, a school pickup line, from behind/beside so the specific commenter isn't the focus, she is. Object-discovery-adjacent: the viewer sees a normal social scene and has to find the tension in it (why does this photo feel slightly awkward), rather than an obvious "concerned friend" stock-photo setup.

**9. Story arc:**
- **Hook/scene (0-10%):** Cold open on the tally: three specific people, three specific settings this month (a coworker at coffee, her sister on a call, a stranger complimenting her "fun" scarf while asking if she was doing okay). She wasn't tired any of those days.
- **Externalized noticing, specific (10-20%):** She starts keeping an unintentional running count in her head. Names the exact phrasing that stuck ("you look tired" vs. "are you feeling okay," which one she got more).
- **Peer-adjacent authority introduced (20-35%):** A named friend/family member she vents to about the pattern, who's been through the same accumulation.
- **Mechanism reveal via that peer (35-50%):** Same locked mechanism language as C1/C3, delivered through this cell's own character.
- **Skeptic-convert + product intro (50-60%):** Same proven beat.
- **Day-numbered transformation (60-80%):** Reframed around the SAME people who'd been commenting, does anyone say it again by day 21, does she brace for it and it doesn't come.
- **Habit-cessation beat (80-85%):** She stops pre-empting the comment (the rehearsed "oh I know, I look tired" deflection line she used to keep ready), same structural beat validated in B28C2, reused here since it's proven material, not because it's unique to this cell.
- **Close mirrors hook (85-100%):** The tally resets to zero. Nobody's asked in weeks. Identity payoff: not that she looks different, that she stopped bracing for the question.

---

## B30C3 - Identity-Reclaiming Pathway

**1. What we are testing:** SA1 Angle 3 ("Look like yourself again, not younger"), entered through a specific not-recognizing-myself moment rather than an external comment or a general tired-look complaint.

**2. Why we are testing it:** Third entry pathway, testing the account's most explicitly compliance-safe SA1 framing (no anti-aging adjacency at all) as a full lead rather than only a closing line, which is how "not younger, just like myself" language has mostly been used to date.

**3. Why high chance of success, from avatar research:** `Brand_Mastery.md` flags this specifically as "compliance-safe framing," meaning it was written with the account's locked banned-phrase rules already in mind (no age-adjacent language, no anti-aging claim), reducing compliance risk relative to angles that have to be carefully worded to avoid the line versus angles built to never approach it.

**4. Why high chance of success, from data:** Identity-level payoff is one of the 4 elements the killed-batch analysis found 100% absent in every killed ad and universal in converters. This pathway makes identity the OPENING frame, not just the closing payoff, testing whether leading with it (rather than earning it structurally across the ad) changes performance, while every other skeleton element stays locked and comparable across C1-C3.

**5. Awareness level:** Solution-Aware, consistent with C1/C2.

**6. Hook:** "Not younger. Just like myself again." as the opening line, paired immediately with a concrete scene (see story arc) so it doesn't read as a bare claim, avoiding the exact "opens on thesis, not scene" failure pattern documented in `Killed_Batch_Failure_Analysis.md` Pattern C.

**7. Why this will convert, reasoning from research and data:** This pathway most directly answers the account's own Stage-5-market-sophistication requirement (`Brand_Mastery.md` Part 8, rule 2: a hook the reader has heard before doesn't ship without a mechanism/information/identity layer). "Look younger" is a claim she's heard a thousand times and is numb to; "look like yourself" is a distinct, less-used identity claim in this exact vertical, giving it real differentiation in a saturated auction even before the mechanism section does its work.

**8. What creative and why:** A specific found-object or reflection moment that isn't a mirror-selfie, an old photo held next to a reflection, or a candid caught-off-guard shot in natural light where she's comparing something (a passport photo, a photo from a few years back) against how she looks now, ambiguous enough to require a beat of parsing, consistent with the B28-validated creative principle.

**9. Story arc:**
- **Hook/scene (0-10%):** Cold open on the identity line paired with a scene, cleaning out a drawer and finding an old ID or photo, holding it next to her reflection, feeling the gap without being able to name it as anything other than "different."
- **Externalized noticing, specific (10-20%):** Not a compliment or comment this time, a private, specific realization about what changed (not wrinkles, not gray hair, something about how her face holds light or expression, staying identity-focused not age-focused).
- **Peer-adjacent authority introduced (20-35%):** A named friend/family member with a parallel realization of her own.
- **Mechanism reveal via that peer (35-50%):** Same locked mechanism.
- **Skeptic-convert + product intro (50-60%):** Same proven beat.
- **Day-numbered transformation (60-80%):** Framed around the identity thread specifically, day she catches her reflection and it's just her face again, no gap to parse.
- **Habit-cessation beat (80-85%):** She stops doing the thing she didn't realize she'd started, avoiding photos, over-scrutinizing video calls, whatever the specific private habit was.
- **Close mirrors hook (85-100%):** Returns to the old photo/ID beat from the hook, this time holding it up and the gap is gone. "Not younger. Just like myself again," now earned rather than asserted.

---

## B30C4 - Awareness-Bridge Isolation Test

**1. What we are testing:** Whether inserting the existing (unused) advertorial page between the ad click and the PDP improves conversion, holding angle, hook, and copy completely constant. Reuses B30C1's copy and creative verbatim, changes exactly one variable: the destination URL.

**2. Why we are testing it:** B28's data shows engaged clicks (strong CTR/CPC on C1) failing to convert past LPV. The advertorial page already exists, was already built with this exact angle's headline and imagery as its default content, and has never been sent a single visitor. This is close to a free test, no new copy, no new creative, one link change.

**3. Why high chance of success, from avatar research:** N/A directly (this cell tests a structural/funnel variable, not an avatar-language variable), but indirectly: the advertorial's existing default copy already demonstrates someone on this account previously identified SA1/self-recognition as the strongest fit for a bridge page, independent of this current research pass.

**4. Why high chance of success, from data:** This is the direct, controlled answer to the specific gap this batch was commissioned to close: B28C1 proves the click-quality isn't the problem (strong CTR/CPC), so the remaining unexplained variable is what happens between the click and the add-to-cart decision. A native long-form ad ends on a fully resolved, Most-Aware narrative voice; the PDP it currently links to has no narrative continuity, generic commerce layout, different voice entirely. The advertorial preserves the narrator's voice, repeats the mechanism in condensed form, and includes a real review quote before ever presenting the "Add to Cart" moment, closer to how the ad copy itself is already structured. If the hypothesis is right, C4 should show a measurably better LPV-to-ATC rate than C1 despite byte-identical top-of-funnel creative and copy.

**5. Awareness level:** Same Solution-Aware ad copy as C1. The variable being tested is what happens to that awareness state AFTER the click, not the ad's own awareness level.

**6. Hook:** Identical to C1: "It's not 'just my face.' It was my skin."

**7. Why this will convert, reasoning from research and data:** Isolates the single cleanest, lowest-cost hypothesis this account can currently test for the specific failure mode it's experiencing (LPV without ATC), with an existing, already-built asset, and a true single-variable comparison against C1 as its own control, no separate ad set full of confounds needed.

**8. What creative and why:** Byte-identical to C1. Any creative change here would break the isolation.

**9. Story arc:** Byte-identical ad copy to C1. The advertorial page itself (already built) re-states the mechanism in condensed form, includes a real customer review quote, and ends on 2 CTA moments before the PDP link, extending the narrative bridge described in the reasoning above rather than cutting straight to commerce.

---

## What NOT to do in this batch (carried forward from `Killed_Batch_Failure_Analysis.md`)

- No menopause/perimenopause/hormone language, no medical/dermatologist authority, no disgust language, no active-harm framing, no stated age numbers, no villain-beat industry-blame language.
- No opening on a bare claim or thesis, every hook above pairs with a concrete scene within the first 1-2 lines.
- No generic compliments in the noticing beat, must stay skin-specific per the B6 hypothesis finding.
- No claiming CTR/CPM signal under 50/100 impressions respectively (Pattern A, hard rule).
- C4 specifically: do not let the advertorial page's copy drift from C1's ad copy once built, that drift would break the single-variable isolation this cell exists to test.

## Before this launches

1. Founder sign-off on the 4-cell structure and which pathway (if any) gets deprioritized if budget only supports 3 cells at real floors.
2. Full ad copy written for C1/C2/C3 (C4 reuses C1's copy once written).
3. Advertorial page (`page.advertorial.json` / `tallow-advertorial.liquid`) populated with real settings, real product photo, real review quote (never fabricated, matches the section's own schema warning), pdp_url confirmed pointing at the live balm product.
4. Compliance pass on all 3 new ads against the banned-phrase list before any spend.
5. Isolated ad sets/protected budgets per cell, per standing CBO-starvation lesson.
