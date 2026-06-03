# BOGO "The Pair" — Setup Instructions

The Custom Liquid block (`BOGO_The_Pair.liquid`) only **shows** the offer and adds 2 jars to the cart. The actual discount is a separate native Shopify setting. Both pieces are required. If you paste the liquid but skip the discount, customers adding 2 jars get charged the full **$99.98**.

---

## Step 1 — Create the automatic discount (do this FIRST)

Shopify Admin → **Discounts** → **Create discount** → **Buy X Get Y**

- **Title:** `The Pair (BOGO 50%)`
- **Customer buys:** Minimum quantity of items → **1** → Specific products → **Whipped Tallow & Honey Balm**
- **Customer gets:** Quantity **1** → Specific products → **Whipped Tallow & Honey Balm** → at a discounted value of **Percentage 50%**
- **Maximum number of uses:** check "Limit number of times this discount can be used in total per order" and set it so a 2-jar cart discounts exactly one jar. (If you want a 4-jar cart to be 2 full + 2 half, leave it uncapped. Decide based on whether you want stacking.)
- **Discount type:** **Automatic** (no code needed — applies the moment 2 are in cart)
- Set **Active**.

Save.

## Step 2 — Add the liquid block to the product page

Shopify Admin → **Online Store** → **Themes** → **Customize** (Shrine Pro 1.3.0)

- Open the **product template**
- **Add block** (or **Add section** → **Custom Liquid**) where you want the offer to appear, e.g. right under the buy button
- Paste the entire contents of `BOGO_The_Pair.liquid`
- Save

## Step 3 — Test before you trust it

1. Open the product page, click **Add Both Jars**.
2. In the cart, confirm: 2 jars, subtotal $99.98, discount applied, total ~$74.99.
3. Go to checkout and confirm the discounted total carries through.
4. Do one real test purchase (you can refund yourself) so you also confirm the pixel fires a Purchase event with the correct value. (The pixel value-attribution check is still on the pre-launch list.)

---

## Notes and gotchas

- **Single-variant product:** The balm is one size (120g), so `selected_or_first_available_variant.id` always resolves to the only variant. No variant-picker wiring needed.
- **Cart drawer vs cart page:** The form does a plain POST and lands on `/cart`. Reliable on any theme. If you want Shrine Pro's slide-out drawer to open instead, the button needs to be wired to the theme's AJAX cart JS — skip that for now, the plain version works.
- **Penny rounding:** 50% of $49.99 is $24.995. Shopify rounds, so the checkout total may show **$74.98 or $74.99**. Marketing says $74.99; the 1-cent variance is normal. If you ever want it exact, switch the discount from "50%" to a fixed "$24.99 off," but 50% is the cleaner mechanic.
- **This replaces** the old Try It / Stock Up / Best Value selector from PDP v2. The Ritual and Transformation bundles were killed (zero sales) and replaced by The Pair per the offer sheet (Apr 27).
- **Value attribution:** When BOGO is live, make sure the pixel reports the actual cart value ($74.99), not per-item, so Meta can optimize toward higher-AOV buyers later.

---

*Created 2026-05-21. Pairs with `BOGO_The_Pair.liquid` and the offer sheet row "The Pair (2x Tallow Balm — BOGO 50%)" in `tallow-cream/offers/Offer_Planning_Sheet.csv`.*
