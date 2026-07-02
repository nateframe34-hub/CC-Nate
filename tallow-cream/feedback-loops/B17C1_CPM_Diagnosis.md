# B17C1 CPM Diagnosis: Why Delivery Costs $200+ and What Might Bring It Under $100

**Date:** 2026-07-02
**Ad:** B17C1 (B9C3 verbatim, The Counter With One Thing). 7 lifetime purchases across both trackings, the account's proven converter.
**Problem:** CPM ranges $160-404 across its June-July run (median ~$200). Whiteboard cells on the same account, same audience settings, same objective run $42-97. Conversion is not the problem ($12-14 CPA on converting days, 3.5-4x ROAS). Delivery cost is.
**Goal:** under $100 CPM without losing the buyer.

## What the data rules OUT first

- **Not noise.** $200+ spend, 19 logged days, CPM never once dipped below $150 except one $76 outlier day (Jun 28). Whiteboard hit sub-$100 in its first week repeatedly.
- **Not account-level.** Whiteboard runs cheap on the same account, same period. Whatever inflates B17C1 is attached to the ad, not the BM or pixel.
- **Not engagement quality.** CTR runs 7-9%, which is very high. Meta is not penalizing this ad for being ignored. People who see it click it.
- **Not frequency fatigue.** Frequency sits at 1.0-1.17. Nobody is seeing it twice.

That combination (high CTR, good conversion, still expensive) matters: it means Meta is not charging more because the ad performs badly. It is charging more for WHO it has decided to show it to, and possibly for WHAT it thinks the ad is about.

## Ranked list of likely CPM inflators

### 1. The audience Meta selects for this creative: women 45-65 are the most expensive impressions on Meta US (MOST LIKELY)

CPM is not a price for "1,000 impressions." It is a price for 1,000 impressions of the specific people Meta predicts will act, and post-Andromeda the creative IS the targeting. Everything in this ad (a 54-year-old narrator, book club, a daughter born in 1998, foundation cracking) tells the delivery system: show this to women 45-65. That demo is among the priciest inventory on the platform: fewer of them than 25-34s, heavily competed for by pharma, insurance, finance, and every menopause-adjacent DTC brand, and they convert at high AOVs so advertisers bid them up. The whiteboard diagrams carry almost no demographic signal, so they deliver into a broader, cheaper mixed pool. Under this hypothesis the CPM gap is mostly the price of the correct audience, and the whiteboard's cheap CPM partly reflects it being shown to people who were never going to buy (consistent with its 1-vs-11 purchase record). Implication: some of the $200 is not an inefficiency to fix but the market rate for the buyer. The realistic play is not to escape the demo but to stop paying a premium ON TOP of it (items 2-4 below).

### 2. Sensitive-category / personal-attribute classification of the copy (VERY LIKELY, AND FIXABLE)

Meta reduces eligible inventory and raises delivery cost for ads it classifies as touching personal health, age, or appearance insecurity, even when no banned word appears. The copy is fully compliant on the banned-phrase list, but a classifier reading 1,500 words will see: "I'm 54," "After about forty, skin makes a lot less of it," "my skin was tight by noon," a narrative about age-related appearance change and being noticed again. That is textbook "implied personal attributes" territory (the pattern Meta's own guidance describes as implying you know the viewer's age or condition). If the ad got quietly bucketed into restricted or reduced-inventory delivery, that alone can multiply CPM. Two diagnostics, both free: (a) in Ads Manager add the Quality Ranking / Engagement Ranking / Conversion Ranking columns for B17C1: a "Below Average" quality ranking with high CTR is the classic fingerprint of a policy-adjacent classification rather than user disinterest; (b) duplicate the ad unchanged and see if the fresh copy clears review into a cheaper delivery bucket (classifications are per-ad, not per-copy). Fix candidates if confirmed: soften the two highest-risk lines ("I'm 54" and "after about forty...") without touching the story beats.

### 3. Primary text length pushing predicted-engagement down for the majority of the pool (LIKELY CONTRIBUTOR)

The 7-9% CTR comes from the minority who start reading. For the majority who do not, a wall of text below a quiet photo predicts zero interaction, and Meta prices an ad partly on predicted total engagement across everyone it could show. A long-copy ad with a plain image gets a low predicted-action rate for most of the pool, which raises the bid needed to win each auction. This is the same mechanism as the founder's "too visually plain" hypothesis but applied to the copy block: the first 3 lines are all a non-reader ever sees. Testable cheaply: run B17C1's exact story with the first 4 paragraphs restructured so the strongest hook lands entirely above the "See more" fold, or a mid-length (500-700 word) cut. B21's image test covers the visual half of this; the copy-length half is untested.

### 4. Purchase optimization on a small budget forces the priciest corner of the pool (STRUCTURAL, PARTLY FIXABLE)

At $10-20/day optimized for purchases, Meta does not spread across the demo; it hunts the handful of users it scores as likeliest buyers right now, and those users are in every competitor's crosshairs too. Small-budget purchase campaigns systematically overpay per impression vs the same ad at higher budget, because the system cannot explore. This is shared with whiteboard in settings, but it compounds multiplicatively with item 1: likeliest-buyer x most-expensive-demo = the priciest inventory on the platform. Partial fixes: higher daily budget once B21/B22 resolve (scaling itself deflates CPM by letting the system explore), or a cost-cap bid to stop Meta from paying whatever it takes.

### 5. Image plainness / low scroll-stop score (POSSIBLE, ALREADY UNDER TEST)

The founder's standing hypothesis, now being tested properly by B21 (problem/outcome imagery). Kept on the list because it is real, but ranked below the audience and classification explanations for one reason: the whiteboard cells with eye-catching diagrams and the SAME demographic-neutral delivery got cheap CPMs, which confounds "bold image" with "broader audience." B21's native problem/outcome images will disentangle it: same story signals (same demo), bolder image. If B21 lands under $100, image was a bigger driver than this ranking gives it credit for; if B21 stays $150+, items 1-2 are doing most of the work.

### 6. Long-copy dwell without click reading as low-quality to the auction (LESS LIKELY)

Some ad buyers report long-form native ads getting priced up because users dwell (read) without any measurable action Meta counts. Plausible but speculative, and partially contradicted by this ad's high CTR. Listed for completeness.

### 7. Banned-phrase or policy strikes (RULED MOSTLY OUT)

The copy passed the full compliance audit (zero strike-list words) and the ad has never been rejected. If item 2's diagnostics come back clean, this is fully dead.

## Recommended action order (cheapest information first)

1. **Today, zero cost:** add Quality/Engagement/Conversion Ranking columns in Ads Manager for B17C1 and read them. Below-average quality ranking = item 2 confirmed as a major driver.
2. **This week, near-zero cost:** duplicate B17C1 unchanged into the same ad set. If the fresh copy delivers materially cheaper in its first days, the original carries a per-ad classification penalty.
3. **B21 (already live):** reads item 5. Same demo signal, bolder image.
4. **Next native test after B21 reads:** a soft-scrub variant of B17C1 copy (remove "I'm 54" and "after about forty," keep every story beat) and/or an above-the-fold hook restructure. Tests items 2 and 3 directly on the proven converter.
5. **If all of the above only gets partway:** accept that item 1 is the floor for this demo and push CPM down structurally instead (budget scale, cost caps), letting a $120-140 CPM ad with a $33 breakeven CPA still scale profitably on its conversion rate.

## The honest bottom line

Realistic expectation: items 2-4 are probably worth a combined 30-50% CPM reduction if they hit, which lands the ad in the $100-140 range. Getting under $100 while keeping the exact 45-65 female buyer probably requires either B21's image swing to work, or accepting whiteboard-style demographic leakage (which is how whiteboard got cheap, and why it does not convert). The one outcome the data has already paid for: do not chase cheap CPM by weakening the demographic signal in the copy. That trade was already run account-wide as the whiteboard test, and it produced $70 CPMs with a $68 CPA. The order of operations that protects the conversion machine: classification fixes first, structure second, demographic dilution never.
