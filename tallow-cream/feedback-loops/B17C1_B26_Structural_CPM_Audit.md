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

## Second pass: 5 more findings from a line-by-line re-read of the actual copy

### 6. Real, named competitor brands appear directly in the primary text - untested brand-safety risk

**Correction, 2026-07-14, founder:** overstated. B17C1, the ad with the highest and longest-running CPM problem in the account, does NOT contain any competitor brand names at all, it's purely internal (Elaine, Winnie, the fourteen-things list is unbranded). Since the worst-CPM ad in the library doesn't have this feature, competitor brand naming can't be a primary driver of the CPM problem, whatever role it plays for B26 specifically is secondary at best. Downgraded from a real finding to a low-priority, low-confidence side note: still fine to strip brand names from B26 copy opportunistically since it costs nothing, but not worth spending a dedicated isolated test slot on.

### 7. Skin-condition language density is a parallel risk to the age-callout finding, not just age

**Correction, 2026-07-14, founder:** also overstated. Earlier ads (B9C3/B17C1 and others) ran with high CPMs and carried zero "sun damage"/"sun spots" language, that phrasing is B26-specific (Sun-Lived avatar naturally talks about sun exposure). Since ads without this language show the same high-CPM pattern as ads with it, condition-language density is not a primary driver either. Downgraded to the same low-priority side-note status as finding #6.

### 8. The softened "villain beat" is the same framing family that got a killed ad flagged for wellness-conspiracy filters

`Killed_Batch_Failure_Analysis.md` documents B4C2 dying at a $1,000 CPM specifically for "active-harm" / anti-competitor framing that "trips wellness-conspiracy filters." The current live copy has since softened that same instinct into what the B26 briefs call a "villain beat," present in every ad: "the industry lets you conclude you weren't applying it often enough," "a customer who blames herself buys another bottle," "the industry never corrected me, because me blaming myself was the business model." This is meaningfully softer than B4C2's "your cream is actively harming you," and hasn't caused an outright rejection, but it's the same underlying idea (the industry profits from your confusion) delivered at a lower volume. Worth testing whether even the softened version is adding a small, ongoing classification tax, since this beat is now locked into every cell rather than being a one-off failed experiment.

### 9. Second-person imperative breaks the native frame at exactly the highest-leverage moment

**Founder read, 2026-07-14: worth testing but considered unlikely to be a major driver.** Kept as a low-cost, low-priority test rather than a strong hypothesis. Almost the entire body of every ad stays in strict first-person past-tense diary voice, which is core to the camouflage effect, but the mechanism-reveal section in multiple ads breaks that frame directly: "Go flip yours over. I'll wait." (B26C1) is a direct, present-tense, second-person command aimed at the reader. A version that keeps this beat in first-person reported voice ("I flipped mine over. I'll bet yours says the same thing.") would preserve the persuasive function while staying inside the diary frame. Cheap enough to test alongside something else rather than as a standalone priority.

### 10. Zero human presence in any creative image across the entire account

**Correction, 2026-07-14, founder: already tested and disproven.** B21's H1-C cell ("Outcome Visualized: Product In Use") ran B17C1's exact copy with a hand/arm-in-use image, real human presence, product texture visible. Per `Ad_Performance_Tracker.csv`, that cell's CPM ran $132-315+ across its test window, no cheaper than the empty-scene baseline and at points worse. Human presence in the image has already been tried on this exact ad and did not lower CPM. This finding is dead, not just downgraded, don't re-test it without a genuinely different execution (this ranking assumed empty-scene photography was untested; it wasn't).

## What this audit does NOT override

This is not a case for reverting the native strategy generally. B17C1 has 4 confirmed lifetime purchases and B26 is genuinely early data (all 3 cells still under $200 total lifetime spend as of the last log). The CTRs across this whole format family remain strong (8-14%+ on multiple cells), meaning humans who see it respond well. After the founder's corrections, the remaining live hypotheses are narrower than the first draft suggested: age numbers (finding #1), plain-vs-bold image treatment specifically (finding #2/#3, not human-presence, which is already disproven), ASCII dividers (finding #3), the softened villain-beat framing (finding #8), and the second-person mechanism breaks (finding #9, low confidence). Competitor brand names, condition-specific language, and human-presence imagery are ruled out by the account's own existing data.

---

## Recommended tests, revised 2026-07-14 after founder correction

Findings #6, #7, and #10 were disproven or downgraded by the founder against real account history (B17C1 has no competitor brand names or condition language and still runs high CPM; B21's H1-C already tested human-presence imagery on this exact ad and it didn't help). Test list cut down accordingly, ranked by remaining confidence.

1. **Age-number strip test.** Duplicate B17C1 and one B26 cell, remove the specific age number ("I'm 54" -> a vaguer age-adjacent line, or cut entirely), keep every other word identical. Directly answers finding #1, cheap, fast, minimal creative risk. Still the strongest untested single-variable hypothesis in this doc.
2. **Divider-removal test.** Duplicate one ad, replace all `========`/`-------------` dividers with plain paragraph breaks, otherwise byte-identical. Answers finding #3.
3. **Bolder image test, deliberately breaking native camouflage.** Take one B26 cell's proven copy and pair it with a genuinely eye-catching, higher-contrast, more designed image (not a human-presence swap, that's already been tried per finding #10's correction, but a bolder/more graphic treatment of an empty scene, or a different visual approach entirely). If CPM drops materially with no CTR collapse, this is confirmed as a real driver. Still the highest-value remaining test since it challenges the deepest creative assumption and hasn't actually been isolated yet (B21's human-presence test answered a different, narrower question than pure visual boldness).
4. **Villain-beat softened/removed test.** Duplicate an ad with the industry-blame lines cut or rewritten as pure personal reflection with no industry-motive claim. Founder: worth testing. Medium priority since the current version hasn't caused an outright rejection, but it's the same framing family as a previously-killed ad.
5. **First-person-only mechanism rewrite test.** Duplicate an ad with the "Go flip yours over. I'll wait." style second-person commands rewritten into first-person reported voice. Founder: worth testing but considered unlikely. Cheap enough to bundle with test 1 or 2 rather than run standalone.
6. **Earlier product-reveal test.** A variant where the jar appears in the image and the product is named in the first third of the copy instead of the mid-point. Higher risk to the discovery-pacing mechanic that's proven to convert, sequence last.

**Dropped entirely:** competitor-brand-name swap, condition-language strip, and human-presence image tests. Not worth a test slot, the founder's own account history already answers them.

Each remaining test isolates exactly one variable, same discipline as the B28 SA-isolation test: own ad set, own budget, never sharing a CBO with a proven converter or with each other.

---

*Analysis only, no ad copy rewritten yet. Cross-references `B17C1_CPM_Diagnosis.md` (audience/classification-level causes) and `B28_SA2_SA3_SA4_Isolation_Angle_Briefs.md` (desire-level causes). This document adds a third, format/execution-level lens.*
