# B17C1 + B26 Structural CPM Audit: Creative and Primary Text, Independent of Origins Doctrine

**Date:** 2026-07-14
**Founder request, explicit:** set aside the native-ad-writer framework's own assumptions and look directly at the actual creative and primary text across B17C1 and all 3 B26 cells to see if the format itself, not just audience cost, is structurally driving the high CPMs. This is a fresh read, not a continuation of the earlier CPM diagnosis's ranked-cause list (`B17C1_CPM_Diagnosis.md`), though it cross-references it where relevant.

**CPM context for both:** B17C1 runs $160-400+. B26's three cells logged so far: B26C1 $131-267, B26C2 $205-247, B26C3 $81-190. All meaningfully above whiteboard's $42-97 baseline on the same account. Different avatars (SA2/SA3/SA4-stacked vs. SA6 Sun-Lived), same expensive delivery pattern. That cross-avatar consistency is itself the strongest signal in this audit: whatever's driving the cost isn't specific to one avatar's audience, it's something shared by the FORMAT.

---

## What all 4 ads structurally share (the format, not the avatar)

| Feature | B17C1 (B9C3) | B26C1 | B26C2 | B26C3 |
|---|---|---|---|---|
| Word count | ~1,500 | ~950 | ~1,050 | ~1,150 |
| Explicit age stated | "I'm 54" | "I'm 48" | "Forty-eight, skin changes" | Not stated directly in body, canon age is 48 |
| Named real place | Vermont, Brattleboro | (Colorado implied via canon, not named in body) | Colorado named directly | Colorado implied |
| Section-break style | `========` (8x) | `-------------` (6x) | `-------------` (6x) | `-------------` (6x) |
| Product/jar visible in image | No | No | No | No |
| Brand/product named in image | No | No | No | No |
| Any human face in image | No | No | No | No |
| Product mentioned in copy before | ~55% mark | ~45% mark | ~45% mark | ~50% mark |
| Image type | Static empty scene (bathroom counter) | Static empty scene (garden) | POV motion scene (trail) | Static empty scene (sideline) |

Every ad in this format family shares the same shape: 900-1,600 words, a real specific age near the opening, a plain unstaged iPhone-style photo with zero product/brand/face visible, and the product itself not named until roughly the halfway point. This is the native-ad doctrine working exactly as designed, camouflage as personal content, not an ad. The question worth actually asking: is that same design choice also the thing making Meta price it as expensive inventory, independent of who it's shown to.

---

## New findings, not in the original CPM diagnosis

### 1. Explicit age-callout is universal across the library, not a one-ad issue

The original CPM diagnosis flagged "I'm 54" and "after about forty" in B17C1 specifically as candidate personal-attribute classification risk. This audit confirms the same pattern in B26C1 and B26C2 too (verbatim age numbers near the top of the ad). This is not a B17C1-specific fix, it's a format-wide pattern. If age-callout classification is real, it's taxing the entire ad library, not one ad, and the fix (removing the specific number while keeping the age-adjacent story beats) should be tested as a format-wide change, not a one-off edit.

### 2. The image style may be scoring low on Meta's own creative-quality signal, not just delivering to expensive people

This is the genuinely new hypothesis from setting the native doctrine aside. The "authentic, unstaged, looks like a real person's photo" image strategy is deliberate camouflage, built to not look like an ad. But Meta's delivery algorithm also scores creative quality directly (this is what the Quality Ranking column the original diagnosis recommended checking actually measures), partly based on predicted stopping power and engagement across the FULL potential audience, not just the segment who'd buy. A plain, empty, deliberately unremarkable photo (a garden with no one in it, a trail with a dog's ear, a near-empty bathroom counter) may read to that scoring system as low-stopping-power creative, exactly the opposite of what the native-ad doctrine intends it to feel like to a human scrolling past. The doctrine optimizes for "doesn't look like an ad to a human," which may be directly in tension with "scores well as an ad to Meta's own delivery algorithm." Nobody has tested this because testing it means deliberately breaking native camouflage, which the account has treated as untouchable. Worth treating as a real, testable hypothesis instead.

### 3. The ASCII section-break characters are an untested variable in their own right

Every ad in the library uses a literal typed divider (`========` or `-------------`) as a pattern-interrupt device, several times per ad. This is presented in the ad-writer skill as a proven readability/pacing tool, and it likely is for the human reader. But nobody has tested whether Meta's text classifier reads repeated non-alphanumeric dividers as a spam-adjacent or low-quality formatting signal, separate from the words themselves. This is cheap to test (duplicate an ad, replace the dividers with a blank line or nothing, compare CPM) and has never been tried.

### 4. Hyper-specific named places may be narrowing predicted relevance geographically

B17C1 names Vermont and Brattleboro specifically (Aunt Winnie's location). B26C2 names Colorado directly. Campaign-level geo-targeting is set separately from ad copy and copy text doesn't change WHO the ad is eligible to show to, but Meta's relevance-prediction models do read ad text, and hyper-local place names could plausibly narrow the model's own prediction of who will find the ad relevant (someone in Texas reading about Vermont farmers markets or Colorado trails may register as a weaker match than a geographically neutral scene would). This is speculative and lower-confidence than items 1-3, but worth listing since it's untested and cheap to isolate (a duplicate with place names genericized).

### 5. The product stays invisible for roughly half the ad, in text AND image, in every cell

No ad in this format shows the jar in the image, and none names the product by name until 45-55% of the way through the copy. This is intentional (Solution-Aware discovery pacing, mechanism-before-reveal), but it also means that for the majority of the potential audience who will never read past the first few lines, the ad gives Meta's classifier almost nothing to categorize as "product ad" versus "personal story post." That ambiguity could be interacting with the auction's own ad-vs-content categorization in ways the account has never tested, since testing it would mean showing the product earlier, which the format currently treats as a hard rule.

---

## What this audit does NOT override

This is not a case for reverting the native strategy generally. B17C1 has 4 confirmed lifetime purchases and B26 is genuinely early data (all 3 cells still under $200 total lifetime spend as of the last log). The CTRs across this whole format family remain strong (8-14%+ on multiple cells), meaning humans who see it respond well. The candidate problem isn't "the story doesn't work," it's "the specific execution choices (age numbers, zero product visibility, plain unbranded imagery, ASCII dividers, hyper-local place names) may be adding a classifier-level cost tax on top of an otherwise-working story," separate from and additive to the already-confirmed expensive-demographic driver.

---

## Recommended tests, cheapest and most isolable first

1. **Age-number strip test.** Duplicate B17C1 and one B26 cell, remove the specific age number ("I'm 54" -> a vaguer age-adjacent line, or cut entirely), keep every other word identical. Compare CPM against the original over the same window. Directly answers finding #1, cheap, fast, minimal creative risk.
2. **Divider-removal test.** Duplicate one ad, replace all `========`/`-------------` dividers with plain paragraph breaks (no visible character), otherwise byte-identical. Answers finding #3.
3. **Bolder image test, deliberately breaking native camouflage.** Take one B26 cell's proven copy and pair it with a genuinely eye-catching, higher-contrast, more designed image (not necessarily a studio product shot, but something with more visual weight than an empty garden/trail/counter), same targeting, same everything else. If CPM drops materially with no CTR collapse, finding #2 is confirmed and the account has been trading delivery cost for authenticity-feel without knowing the price. This is the single highest-value test in this audit because it directly challenges the account's most deeply held creative assumption.
4. **Earlier product-reveal test.** A variant where the jar appears in the image and the product is named in the first third of the copy instead of the mid-point. Answers finding #5. Higher risk to the discovery-pacing mechanic that's proven to convert, so sequence this after 1-3.
5. **Genericized-place test.** Lowest priority, most speculative. Swap Vermont/Brattleboro/Colorado for unnamed equivalents ("a small town a few states over," "the trail near her house") in a duplicate.

Each test isolates exactly one variable, same discipline as the B28 SA-isolation test: own ad set, own budget, never sharing a CBO with a proven converter or with each other.

---

*Analysis only, no ad copy rewritten yet. Cross-references `B17C1_CPM_Diagnosis.md` (audience/classification-level causes) and `B28_SA2_SA3_SA4_Isolation_Angle_Briefs.md` (desire-level causes). This document adds a third, format/execution-level lens.*
