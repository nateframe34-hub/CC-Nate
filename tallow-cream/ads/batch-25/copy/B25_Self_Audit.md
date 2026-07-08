# B25 Self-Audit: Real Risks + Fixes

**Date:** 2026-07-07
**Method:** re-read the actual built files (3 liquid listicles, image prompts, headline doc), not the plans about them. Findings below are grounded in what's literally in the code and copy right now.

---

## Risk 1 (biggest): the listicles aren't actually as personalized as the founder decision called for

Diffed the three files directly. Signs 2 through 5, the review block, the guarantee section, and the CTA copy are **100% byte-identical text across all three pages.** Only sign 1 and the opening two lines differ per angle.

That's a real gap against the explicit reasoning for going full-congruence: "the purpose is to test angles end to end... maximizing congruence just raises the likelihood of success if there's a winning angle in there." Right now this is much closer to "one shared listicle with a different opening" (the option that got explicitly rejected) than three genuinely distinct angle-tested pages. If Confrontation wins and 43-vs-4 doesn't, you can't fully credit the winning angle, you're also crediting whatever's different about page 1's first 200 words, which isn't much.

**Fix:** personalize at least sign 4 (the Graveyard/emotional beat) and the closer per angle too, not just sign 1. Cheap to do: reframe sign 4's "half-used products" language through each angle's specific lens (Confrontation: dollar amounts; 43-vs-4: count the labels in the drawer; Legibility: how many of those labels she could actually read). That gets you real congruence without a full rewrite.

## Risk 2: the ad's own curiosity gap isn't paid off where the headline promises it

Angle 1's locked headline ends "...THIS IS THE INGREDIENT MOST CREAMS SKIP..." That's a specific promise: name the ingredient, now. But the listicle's sign 1 is about price vs. ingredients generally, the actual ingredient reveal (water/fat, the mechanism) doesn't land until **sign 3**. A reader who clicked specifically for "which ingredient" has to get through two signs of setup before the promise is kept. That's exactly the kind of mismatch the whole congruence push was supposed to eliminate, just moved one level deeper (page-level congruence is right, but the intro-to-payoff pacing inside the page still has a gap).

**Fix:** move the water/fat mechanism reveal up to sign 1 for the Confrontation page specifically (it's currently sign 3 material), and let "the drawer of half-used products" and "the label you can't finish" follow as supporting evidence rather than leading. The other two angles don't have this problem, their headlines promise a comparison/test, and sign 1 delivers exactly that.

## Risk 3: Confrontation is the account's least-validated angle, and it's the one leading this batch

Your own `B24_Marksman_Brief.md` already flagged Confrontation as having "the weakest research support of the original three" when it got parked out of B24. It's untested, no prior signal either way, sitting at cell 1 of a brand-new expensive-to-build format (3 full landing pages instead of one shared destination). If it underperforms, you won't cleanly know whether that's the angle, the format, or the specific headline, since this is also the first real test of the format itself.

**Fix:** not a change to what's built, just a read on the data honestly: don't let Confrontation's result alone indict the Pubity-format decision. If all 3 cells read weak, look at 43-vs-4 and Legibility before concluding the format failed, those have more research backing behind them.

## Risk 4: the specific numbers in the confrontation claims aren't sourced

"43 ingredients" (used as a direct comparison number in both the ad headline and the listicle body) and the earlier-drafted "70% water" figure (which didn't make it into the final locked headline, worth noting it got dropped along the way, intentionally or not) are illustrative, not pulled from an actual competitor ingredient count. The account's own compliance rule is "no fabricated stats." A specific number stated as if it's a researched fact ("her moisturizer has 43 ingredients") is closer to a fabricated stat than the softer, comparably effective "dozens of ingredients you can't pronounce" framing already used safely elsewhere in your copy.

**Fix:** either soften "43" to something like "40+" framed as a typical range (not a precise found number), or if you have an actual source (a real competitor's real ingredient count you counted), cite that specific product by category, not name, e.g. "the average drugstore moisturizer runs 30-40+ ingredients." Small wording change, real compliance hygiene.

## Risk 5: only one proof point per page, and it's identical across all three

Each page has exactly one customer review, and it's the same review verbatim on all three pages ("I threw out eight products and kept this one..."). With three separate pages now built, this was the moment to spread your review inventory across them if you have more than one real review available, reinforces the "these are genuinely different pages" positioning and avoids a reader who happens to see two of the ads noticing the identical quote.

**Fix:** if there's more than one real, verified review in the account's inventory, assign a different one to each page. If there's only the one, that's fine to leave as-is, just flagging it as a lever if more reviews exist.

## Smaller items, lower priority
- No guarantee/trust signal appears until the very end of each page. The advertorial puts a guarantee-adjacent line earlier; these listicles could add one small mention near the top (even just "60-day guarantee" in the dek or a small badge) to reduce early bounce, since these pages are shorter and have less time to build trust before asking for the click.
- CTA density is lighter than the advertorial (2 touchpoints vs. 3-4), reasonable given these pages are shorter, but worth watching in the data, if scroll depth is good but clicks are low, add a third inline link around sign 4.
- The face-inclusion variable in the image prompts (flagged already in the image-prompts doc) is still genuinely unresolved, worth treating as a real experiment variable once data comes in, not just a footnote.
