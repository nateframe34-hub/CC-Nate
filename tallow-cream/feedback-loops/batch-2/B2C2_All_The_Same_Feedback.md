# Feedback Loop: B2C2 — All The Same

**Ad Name:** B2C2 — All The Same
**Batch:** 2 (The Product Graveyard)
**Angle:** A2 — Every moisturizer is water + glycerin in different bottles
**Status:** Killed April 9 (Soft kill triggered at $37 with 0 ATC)
**Verdict:** Loser. CBO's pick of the batch — and it consumed 60% of B2 spend without converting. The most expensive lesson in the launch.

---

## Performance Summary (1 Day — April 8)

| Date | Spent | Impressions | CPM | CTR | CPC | LPV | ATC | Purchases |
|------|-------|-------------|-----|-----|-----|-----|-----|-----------|
| Apr 8 | $37.99 | 178 | $213.43 | 3.93% | $5.43 | 4 | 0 | 0 |
| **Total** | **$37.99** | **178** | **$213** | **3.93%** | **$5.43** | **4** | **0** | **0** |

**Kill trigger:** Soft kill at $37 spend with 0 ATC (per `Kill_Rules_and_Decision_Framework.md`)

---

## Step 1: Hypothesis

### What this ad got right

**1. CBO voted heavily for it (HIGH CONFIDENCE)**

$37.99 of campaign spend on day 1 = ~60% of the entire B2 ad set budget. Meta's algorithm saw the engagement signal — 7 clicks, 4 LPVs — and decided this was the creative most likely to drive a conversion event. The algorithm was wrong, but the signal it was reading wasn't fake. Click engagement was real.

**2. The thesis is correct and shareable (HIGH CONFIDENCE)**

"Every moisturizer is water + glycerin in different bottles" is a powerful frame. It taps into the avatar's lived experience (drawer of failed products) and gives them a satisfying explanation for why nothing has worked. It's the kind of statement a friend repeats at brunch. Shareable thesis = good native ad ingredient.

### Why it failed catastrophically

**1. The thesis IS the entire ad — there's nothing left to discover (HIGH CONFIDENCE)**

The hook gives the punchline away in sentence one: "I lined up every moisturizer I've ever bought. Then I looked at the ingredients. They were basically all the same thing in different bottles." The reader gets the belief shift in 30 seconds and feels intellectually satisfied. Then there's nowhere for the story to go. There's no progressive transformation, no characters validating, no specific scene of using the new product — just a thesis statement looking for a destination. The 7 clicks were curiosity ("really? all the same?"), the 4 LPVs were verification ("let me check the brand"), and the 0 ATCs were the inevitable result of an ad that argued instead of stories.

**2. 4 LPV → 0 ATC is the worst LPV-to-ATC rate in the batch (HIGH CONFIDENCE)**

Compare to B1C2: 2 LPV → 2 ATC = 100%. B2C2 sent the most traffic to the PDP and converted the LEAST. This is a behavioral red flag. The ad attracted the wrong KIND of click — analytical/skeptical readers who came to evaluate the claim, not emotionally-moved readers who came to buy a solution. Argument-based ads attract argument-based clickers. They don't buy.

**3. Click-to-LPV gap is yellow flag (HIGH CONFIDENCE)**

7 clicks / 4 LPVs = 57% click-to-LPV. The other ads in B1/B2 with measurable clicks all hit ~100% click-to-LPV. A 57% drop-off means people clicked, then bailed before the page loaded — likely confused about where they were going (the CTA didn't signal a product page, just a brand) or bouncing from a slow LCP. PDP page-load performance is a separate diagnostic.

**4. $213 CPM despite high engagement signal (HIGH CONFIDENCE)**

The most damning data in the campaign. Even with 3.93% CTR — which is excellent — Meta charged $213 per thousand. This is the clearest evidence the CPM problem is upstream of the creative. We had a creative Meta liked enough to fund, generating click engagement Meta values, and Meta still charged premium auction prices. Whatever's setting the auction floor isn't the ad — it's the page, pixel, product, or category.

**5. No emotional anchor — the ad is purely intellectual (HIGH CONFIDENCE)**

There's no character to root for, no specific moment of pain, no scene where the avatar feels seen. The ad reads like a Reddit explainer post. Reddit explainer posts get upvotes. They don't get purchases. The Invisible Woman avatar buys when she feels SEEN. B2C2 makes her feel SMART. Wrong emotional outcome for the conversion goal.

---

## Step 2: Action — What Changes Going Forward

### Keep
- The "all the same — water + glycerin" mechanism. It's the cleanest belief shift in our library and it WILL stay in the toolbox. But it has to be DELIVERED through a story, not stated as a thesis.
- The instinct to expose the category. The avatar wants someone to validate that her drawer of failed products wasn't her fault.

### Change
- **Bury the thesis inside a story, don't lead with it.** B5C3 "I Gave Up" demonstrates the right pattern: the same "every cream is water" insight appears at the 50% mark, AFTER a low point and a discovery character set it up. By that point the reader is emotionally invested and the thesis lands as a relief, not as an argument.
- **Open with a scene, not a list.** "I lined up every moisturizer" is a tableau, not a moment. Replace with a specific incident: "My friend was in my bathroom looking for hand cream and asked why I had eight of the same thing on the counter."
- **Add an external character who delivers the insight.** The thesis has more weight when it comes from a peer (a sister, a friend, a stranger at the makeup counter) than when the narrator self-delivers it.
- **Build to identity-level payoff.** "She was right" is intellectual. "And then my husband touched my face the way he used to" is identity-level. The ad needs to land somewhere emotional, not somewhere argumentative.

### Test Next
- The "water vs oil" mechanism is currently being delivered effectively in B5C3. That's the live test. Do not re-run B2C2 as-is.
- A future test could pair the "drawer of failed products" inciting incident with a friend or sister character who delivers the water/glycerin insight at the 50% mark. Different avatar entry, same mechanism payoff.

---

## Decision

Killed correctly. This ad burned 60% of B2's day-1 budget and converted no one. The kill threshold ($37 with 0 ATC) was the right call and validated the soft-kill rule in `Kill_Rules_and_Decision_Framework.md`. The biggest learning isn't about THIS ad — it's about what its data tells us about the campaign-wide CPM problem. A creative this engaging at $213 CPM means the auction is broken, not the writing. That insight is what's now driving the proposed fresh-campaign duplicate test.

---

*Feedback loop created: April 13, 2026*
