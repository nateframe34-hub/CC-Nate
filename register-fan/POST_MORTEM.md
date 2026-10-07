# Post-Mortem: Register Fan (Evenroom Vent Thermostat)

**Discontinued 2026-10-07** (founder call). Launched 2026-10-03. About 4 days of paid traffic plus one relaunch.
**Read alongside:** `tallow-cream/POST_MORTEM.md`. The two together are the product-selection rulebook for whatever comes next.

---

## The one-line verdict

**People clicked cheaply and nobody showed buying intent, and even if they had, the margin needed a ROAS this product was unlikely to reach.** With Q4 starting, seasonal products with better economics are a better use of the same money and time.

## What happened, in numbers

| | |
|---|---|
| **Days 1–2 (Oct 3–4), ABO, 6 ads** | $83 spend · 1,174 impressions · 36 link clicks · ~34 landing page views · **0 ATC · 0 checkouts · 0 purchases** |
| **Best click costs** | B2C3 Pubity $1.25–1.36 CPC (5–6% CTR) · B2C1b native $1.44–1.84 · blended ~$2.30 |
| **Tallow, for comparison** | $3.09–4.75 CPC across four months, never moved |
| **Relaunch (Oct 6–7)** | One CBO ad set, 9 ads, cold-season batches, gift-stack offer, fall sale countdown, fitment line. Still no buying intent. Budget-sink ads killed (spend past ~$57 CPA with no purchase, or CPM >$200 after $20) |
| **Total spend** | *Founder to fill in from Ads Manager* |

## Why it didn't work (ranked by what we believe)

### 1. The unit economics left no room ⭐ the deciding reason
COGS **$39.83** on an **$89.99** price (+$9.95 shipping) left ~$57 to acquire a customer: **breakeven ROAS 1.76×**, scale ROAS ~2.25×. At cold-traffic conversion rates that needs a 2.5–4% click-to-purchase on $1.30–2.50 clicks, with no room for returns on a ~$100 electrical item with a sizing step. **Even a working ad would have been a thin, fragile business.** The founder's call: not worth the time in Q4.

> **Rule:** COGS at or under ~25–30% of price before launch. A product that needs a 2×+ ROAS just to scale is a bad bet for a new store with no pixel history.

### 2. Clicks were curiosity, not intent
The cheapest-click ads were the most curiosity-led. B2C3 never showed a product, so people clicked to learn *why the thermostat says 72* and left when they hit a price. High CTR was partly *because* the ads didn't pre-qualify buyers. **Interrupt traffic rewards interesting; it doesn't create need.**

### 3. Season mismatch at launch
Batches 1 and 2 were hot framing, launched in October. The pain had gone for the year for most of the US. The cold batches (3, 4) came in the relaunch, but by then the decision window was 1–2 days.

> **Rule:** launch a pain product while the pain is live, with at least 6–8 weeks of season ahead.

### 4. Fitment friction before ATC
The buyer had to know their vent size (4x10 or 6x10) to add to cart. Most don't, so "I'll measure later" means leaving. Many US AC homes have ceiling or wall registers in other sizes. Research had already logged two lost sales on fitment before launch.

> **Rule:** the product can be bought in one decision, without measuring, fitting or checking anything at home first.

### 5. Category is searchable and cheaper elsewhere
Once the ad taught the problem, a "register booster fan" was one search away at $40–70. We were the education, not the store.

### 6. Trust, at the margin
New brand, no reviews, a .store domain, a ~$90 electrical item, an older audience. Not proven to matter, but it stacked on the rest.

## What worked (carry forward)

| What | Evidence |
|---|---|
| **Pubity-style static** | Cheapest clicks in the account ($1.25 CPC, 6% CTR). Worth testing first on the next product |
| **Research-backed natives over invented frames** | B2C1b (evidenced: turning the thermostat down never reaches the room) 3.3–5.5% CTR vs B2C1 (invented thermostat fight) 0.74–1.9%. Same characters and product beat. **The evidence-based frame won by 3–5×** |
| **Copying swipe templates closely** | Every ad that matched its swipe's structure (Pubity, Relatable Hook, Nutella, Carepod) came out cleaner than the formats we invented |
| **One-pass image prompts with a product lock** | Written product spec + reference image + explicit orientation. Fixed the "product doesn't look like what ships" problem after several misses |
| **Objection-led offer stacking** | Every bonus must answer an objection (the install kit answers "do I need anything else"). The thermometer idea was rejected for that reason. Good rule for any offer |

## Process lessons (what to do faster next time)

1. **Check unit economics before any creative work.** Margin is the first gate, not the last.
2. **Check the calendar before writing angles.** We wrote a full hot-season batch for an October launch.
3. **Decide the kill rule by ads tested, not just dollars.** At a ~5% ad hit rate, 7 ads is a ~30% chance of finding a winner. Plan for 15–20 ads tested inside the budget, and cut losers at ~$25–40.
4. **Pre-qualify in the ad.** Show the product (or a clear "it's a product" cue) in curiosity formats so clicks arrive expecting a store.
5. **Store polish is not the bottleneck at day 1.** We spent heavily on PDP detail before knowing if anyone wanted to buy. Build a solid, fast page, launch, and polish what the data points at.

## Product-selection checklist additions (on top of tallow's)

- [ ] **COGS ≤ ~30% of price.** Breakeven ROAS under ~1.5×
- [ ] **In season at launch, with 6+ weeks of runway**
- [ ] **One-decision purchase:** no measuring, sizing or compatibility check at home
- [ ] **Not easily found cheaper by searching the category name**
- [ ] **Q4: giftable or seasonal demand** (Christmas, cold weather, holiday hosting) so the calendar works for us, not against us

## Assets that survive (reusable)

- `register-fan/store/theme/sections/evenroom-pdp-sa1.liquid`: a full Shopify PDP section (dropdowns inside bundle cards, mixed 2-packs, built-in cart drawer, gift stack, countdown, sticky bar, carousel, reviews block). **Reskin it for the next product rather than rebuilding.**
- `evenroom-home.liquid`: a short homepage section that sends everyone to the PDP.
- The one-pass prompt structure in `ads/batch-2/B2_Image_Prompts.md` and the product-lock block.
- `M4_Method_Analysis.md`: the post-winner scaling playbook.
