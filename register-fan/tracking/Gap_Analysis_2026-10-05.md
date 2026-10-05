# Gap Analysis: clicks without purchase intent · 2026-10-05

**Data:** Oct 3–4, all 6 ads. $83.07 spend · 1,174 impressions · 36 link clicks · 34 landing page views · **0 ATC, 0 checkouts, 0 purchases.** Tracking confirmed working (founder).

| Ad | Spend | Clicks | LPV | CPC | CTR | What the click knows before landing |
|---|---|---|---|---|---|---|
| B1C2 Relatable Hook | $35.84 (43%) | 11 | 9 | $3.26 | 3.2% | **Everything:** product, features, no price in image (price in post text) |
| B2C3 Pubity | $16.32 | 12 | 12 | $1.36 | 5.0% | **Nothing about a product.** A question, answered in the post text |
| B2C1 native (fight) | $15.40 | 4 | 4 | $3.85 | 1.3% | Product and price late in a long story |
| B2C1b native | $7.35 | 4 | 8 | $1.84 | 3.3% | Product and price late in a long story |
| B1C1 native | $5.44 | 5 | 1 | $1.09 | 4.0% | Product and price late in a long story |
| B1C3 whiteboard | $2.72 | 0 | 0 | n/a | 0% | Not delivering |

## Statistical honesty first
At a typical 5% LPV→ATC rate, zero ATC from 34 visitors happens about **17% of the time** by chance. Zero is a weak signal, not proof. The hypotheses below are ranked by how plausible they are **and** how cheaply we can check them, because we need to know which one to fix before spending more.

## Hypotheses

### H1. Season mismatch: the clicks are curious, not hurting ⭐ most likely
Every live ad is **hot framing** (heat, 81°, AC). It's October. For most of the US the hot room stopped hurting weeks ago. The ads are interesting enough to click (good CTR) but the reader has **no pain today**, so there's no reason to buy today. "Good idea, I'll remember it next summer" is exactly a click with zero intent.
- **Check:** Meta breakdown by region if available; the weather in the top states.
- **Test:** the cold ads (B3, B4) launching Oct 6. If ATC appears on cold ads and not hot ones, this is it.

### H2. Curiosity clicks, not buying clicks ⭐
The two cheapest-click ads (B2C3, B1C1) are the most curiosity-led. B2C3 **never shows a product**: the click is "tell me why my thermostat says 72", and they land on a product page with a price. Readers who wanted an explanation, not a purchase, bounce. High CTR is partly *because* the ad doesn't pre-qualify.
- **Check:** LPV→ATC by ad once there's volume. Shopify: avg session time for these visitors. Clarity: do Pubity visitors scroll at all?
- **Test:** a Pubity variant that shows the product in the circle inset (the swipe's inset is part of the story), so the click already knows it's a product.

### H3. Fitment friction: they can't add to cart without measuring first ⭐
To add to cart you must pick 4x10 or 6x10. Most people don't know their vent size. The honest behaviour is "I'll measure it later", which means leaving, and later rarely comes. Research already logged **two lost sales on fitment**. Separately, many US AC homes have **ceiling or wall registers**, often in other sizes, and every ad image shows a floor vent.
- **Check:** Clarity recordings (do people open the dropdown, then leave?). Ask 3–5 people what size their vents are and where they are.
- **Test:** reduce the fear, not the step. Put "Not sure? Most homes are 4x10, and if it's wrong we swap it free" right at the dropdown, with the 4x10 default. Add a 10-second "how to check your size" line under it.

### H4. They comparison-shop and buy elsewhere
A vent fan is a findable category. A reader who now understands the problem can search "register booster fan" and find $40–70 options on Amazon. Our PDP never names the category, but nothing stops them searching. Zero ATC on our site is consistent with buying elsewhere.
- **Check:** can't be measured directly. Indirect: Shopify sessions with very short time on page, and the share of returning visitors (low = they didn't come back).
- **Test:** value-stack and reasons-to-buy-here at the buy box (free size swap, 60 days, its own thermostat, US plug); a sharper price anchor.

### H5. Trust deficit: new brand, no reviews, a .store domain
An older homeowner, a ~$90 electrical item, a brand they've never heard of, **no reviews** (placeholders correctly off), and a domain they don't recognise. Natives build trust in the story, then drop them on a page with no proof.
- **Check:** Clarity: do people scroll to the guarantee and FAQ, then leave?
- **Test:** real reviews as soon as any exist; until then, make the 60-day guarantee and the free size swap bigger at the buy box. Trust badges stay out (they read as staged).

### H6. Wrong people: Meta found clickers, not homeowners
Broad targeting with a curiosity creative can attract younger renters who click but can't change a vent.
- **Check now, it's free:** Ads Manager → Breakdown → Age and Gender. If most clicks are 18–34, that's this.
- **Test:** nothing to change in targeting (broad stays). Creative fixes it: homeowner cues (the house, the duct run) are already in the copy.

### H7. Something on the page is broken or confusing on mobile
The page was built and changed fast: dropdown inside the cards, a custom drawer, countdown.
- **Check today:** on your own phone, from an ad link: pick a size, pick two vents, add to cart, open checkout. Ask one other person to do the same without help and watch.

## What to do before Oct 6 (cheap checks)
1. **Meta age and gender breakdown** (H6), 2 minutes.
2. **Shopify Analytics:** sessions, average session duration, mobile share, bounce rate for the last 2 days (H2, H4, H5).
3. **Install Microsoft Clarity** if not done. By Oct 7 you'll have recordings of real visits (H2, H3, H5, H7).
4. **A phone run-through** of the buy flow with someone who hasn't seen it (H7).

## What the Oct 6 launch already tests
- **H1 (season):** cold B3/B4 ads against the hot B1/B2 survivors.
- **H2 (curiosity):** natives (pre-sold) against Pubity (curiosity) against designed statics (product shown).

## Proposed changes for the Oct 6 relaunch (pending founder approval)
- **H3:** fitment reassurance line at the dropdown.
- **H2:** the B3/B4 Pubity variants show the product in the circle inset.
- **Season:** lead the CBO with cold ads; keep at most 2 hot ads.
