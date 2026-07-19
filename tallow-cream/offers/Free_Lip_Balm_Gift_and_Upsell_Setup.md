# Free Lip Balm Gift + Cart Upsell: Setup Guide

**Date:** 2026-07-19
**What this replaces:** the popup email's discount code (FIRST10) mechanic, per founder direction. The popup, welcome email, PDP, and cart drawer all updated to support a free-gift-with-purchase instead.

---

## The core problem this answers: how to give it away free without setting the price to $0.00

If the lip balm's actual product price is set to $0.00, anyone can add it to their cart alone and check out for free, no balm purchase required, pure loss. **The fix is Shopify's native "Buy X, Get Y" discount type**, not a price change:

1. Shopify admin -> **Discounts -> Create discount -> Buy X get Y**.
2. **Customer buys:** specific product, Whipped Tallow & Honey Balm, quantity 1.
3. **Customer gets:** specific product, the Lip Balm, quantity 1, discounted **100% off**.
4. **Code:** `FREELIP` (matches the email already written).
5. **Usage limit:** check "Limit to one use per customer."
6. **Active dates:** set a 7-day window to match the email's urgency copy, or longer if you want it always-on, just keep the email's copy and the code's real expiry in sync.

This way the lip balm keeps its real list price ($14.99 recommended, see below) everywhere. It is only ever free when the code is applied AND the balm is in the same cart. Nobody can buy it standalone for free.

**The one UX catch:** Buy X Get Y does not automatically add the free item to the cart. The customer has to add the lip balm themselves for the discount to kick in. That's exactly what the new cart-drawer upsell block is for, see below, it's not just a nice-to-have cross-sell, it's the mechanism that actually delivers the free gift.

---

## Pricing recommendation

Landed cost on the lip balm (unit cost + packaging/pick-pack, conservatively) is roughly **$2.50-3.50 per unit** at any real order volume (the $1.46 unit price you sampled at gets cheaper per-unit at bulk MOQs, and freight-in amortizes down from the $5.67 single-sample shipping quote).

- **List price (PDP + upsell "value" reference): $14.99.** High enough that "$14.99 value, free" reads as a real gift, not a throwaway. Comparable tallow lip balms on the market run $8-14, so this is defensible, not inflated.
- **Cart upsell price for people who DON'T have the free code (straight cross-sell): $7.99.** Roughly half off list, still ~60%+ margin at a $3 landed cost, priced to feel like a deal on its own rather than needing the free-gift context to make sense.
- These two numbers are already wired into the code (`tallow-lipbalm-pdp.liquid` defaults to $14.99, the cart upsell block defaults to "+ $7.99"), change both together in the theme customizer if you land on different numbers.

---

## What's built and where

1. **`tallow-cream/store/theme/sections/tallow-lipbalm-pdp.liquid`** - new, lightweight product page section for the lip balm. Far less detailed than the main balm PDP on purpose (no traffic being driven here directly), but on-brand: same color/type system, real Add to Cart form, ingredients block, trust line. Create the lip balm as its own product in Shopify admin, assign this section to its page.

2. **`tallow-pdp.liquid` cart drawer** - new optional "Cart lip balm upsell" block, sits between the item list and the checkout button. Shows a small thumbnail, title, price, and its own Add button (uses the same AJAX add-to-cart pattern as the rest of the drawer). New schema settings under "Cart lip balm upsell (optional)" in the section customizer: paste the lip balm's real variant ID, upload a thumbnail, set title/price text. **Leave the variant ID blank and the block hides itself automatically**, so nothing breaks if this isn't set up yet.

3. **Popup** - heading/subtext/button copy changed from the discount framing to the free-gift framing ("Unlock a free tallow gift" / "Reveal my gift"), both the inline Liquid defaults and the schema settings updated so customizer and code agree.

4. **`tallow-cream/store/email/Welcome_Free_Gift_Email.html`** - new email, replaces `Welcome_Discount_Email_FIRST10.html` for this flow (old file kept as reference, not deleted). CTA sends them to the balm's product page with the FREELIP code auto-applying, then the cart upsell block is what gets the lip balm actually into their cart.

---

## Before this goes live, in order

1. Create the lip balm as a real Shopify product (real inventory, real $14.99 price), assign the new lip balm PDP section to it.
2. Build the FREELIP Buy X Get Y discount per the steps above.
3. Grab the lip balm's variant ID (Shopify admin -> Products -> the lip balm -> variant details, or via the product page's URL/API), paste it into the cart drawer's upsell settings in the theme customizer, upload a thumbnail.
4. Preview the popup -> email -> PDP -> cart drawer flow yourself once, end to end, before sending it to real customers. Specifically confirm: clicking the email CTA lands on the balm PDP with the code active, adding the balm shows the lip balm upsell in the drawer, adding the lip balm from there actually zeroes its price at checkout.
5. Set the FREELIP code's real expiry to match whatever the email says.
