# Free Lip Balm Gift + Cart Upsell: Setup Guide

**Date:** 2026-07-19, REVISED same day.
**2026-07-19 revision:** founder reconsidered. The free lip balm now goes to **every customer automatically**, not gated behind popup email signup (16% of visitors was the wrong ceiling to optimize under). The popup reverted to the original 10% FIRST10 discount, repositioned as an email-capture/cart-recovery tool, not the primary incentive. The gift card also changed from every-order to a scarcity "next 100 customers" mechanic. This doc now covers the universal free-gift mechanism; see `Gift_Card_Flow_Setup.md` for the scarcity gift card. `Welcome_Free_Gift_Email.html` is superseded/reference-only, the popup email is `Welcome_Discount_Email_FIRST10.html` again.

**Delivery mechanism, updated:** since the gift is now universal, it no longer needs a discount code at all for the customer to enter. `tallow-pdp.liquid`'s JS now **auto-adds the lip balm to the cart silently** the moment the main balm is added (see `addGiftsSilently()`), using the same Buy X Get Y discount underneath (still needed so the item rings up at $0, see below) but with zero manual steps for the customer. The cart-drawer upsell block described further down is now a fallback only, for anyone who removes the free item and wants to re-add it (at the real $7.99 cross-sell price, since removing signals they don't want the freebie).

---

## The core problem this answers: how to give it away free without setting the price to $0.00

If the lip balm's actual product price is set to $0.00, anyone can add it to their cart alone and check out for free, no balm purchase required, pure loss. **The fix is Shopify's native "Buy X, Get Y" discount type**, not a price change, now set up as an AUTOMATIC discount (no code) since it applies to every order:

1. Shopify admin -> **Discounts -> Create discount -> Buy X get Y**.
2. **Method: Automatic discount** (not a code, since every customer qualifies now).
3. **Customer buys:** specific product, Whipped Tallow & Honey Balm, quantity 1.
4. **Customer gets:** specific product, the Lip Balm, quantity 1, discounted **100% off**.
5. **Usage limit:** none needed (it's per-order, automatic, not per-customer).
6. **Active dates:** leave open-ended/always-on, this is now a standing offer, not a time-limited one.

This way the lip balm keeps its real list price ($14.99 recommended, see below) everywhere except at checkout when the balm's also in the cart. Nobody can buy it standalone for free, since the automatic discount only fires when both items are present.

**The one remaining UX catch, already solved in code:** Buy X Get Y does not automatically add the free item to the cart on its own. `tallow-pdp.liquid`'s cart JS now handles this for you, the moment the balm is added via any of the 3 main Add to Cart buttons (hero, final CTA, sticky), it silently also adds the lip balm (and the gift-card token, if configured) via a background `/cart/add.js` call, no second click required. The cart-drawer upsell block (below) still exists as a visible fallback/manual re-add path, not the primary delivery mechanism anymore.

---

## Pricing recommendation

Landed cost on the lip balm (unit cost + packaging/pick-pack, conservatively) is roughly **$2.50-3.50 per unit** at any real order volume (the $1.46 unit price you sampled at gets cheaper per-unit at bulk MOQs, and freight-in amortizes down from the $5.67 single-sample shipping quote).

- **List price (PDP + upsell "value" reference): $14.99.** High enough that "$14.99 value, free" reads as a real gift, not a throwaway. Comparable tallow lip balms on the market run $8-14, so this is defensible, not inflated.
- **Cart upsell price for people who DON'T have the free code (straight cross-sell): $7.99.** Roughly half off list, still ~60%+ margin at a $3 landed cost, priced to feel like a deal on its own rather than needing the free-gift context to make sense.
- These two numbers are already wired into the code (`tallow-lipbalm-pdp.liquid` defaults to $14.99, the cart upsell block defaults to "+ $7.99"), change both together in the theme customizer if you land on different numbers.

---

## What's built and where

1. **`tallow-cream/store/theme/sections/tallow-lipbalm-pdp.liquid`** - lightweight product page section for the lip balm. Far less detailed than the main balm PDP on purpose (no traffic being driven here directly), but on-brand: same color/type system, real Add to Cart form, ingredients block, trust line. Create the lip balm as its own product in Shopify admin, assign this section to its page.

2. **`tallow-pdp.liquid` auto-add JS** - new `addGiftsSilently()` function fires after any of the 3 main balm Add to Cart forms (hero/final/sticky, matched by form ID) succeeds, adds the lip balm and gift-card token variants in the background if their variant IDs are configured, skips anything already in the cart, fails silently (never blocks checkout on a free-gift hiccup).

3. **`tallow-pdp.liquid` PDP callouts, under the Add to Cart button** - two separate lines now: an always-on "Free Tallow Lip Balm ($14.99 value) with every order" callout (shows whenever `lipbalm_upsell_variant_id` is set), and a scarcity gift-card callout with a LIVE remaining count pulled directly from the gift-card token product's real inventory (`gift_token_product_handle` setting), auto-hides once inventory hits 0, no manual updating ever needed.

4. **`tallow-pdp.liquid` cart drawer upsell block** - still present, now a fallback/manual re-add path only (e.g. if someone removes the free lip balm and wants it back, they'd see it at the real $7.99 cross-sell price). Schema settings under "Cart lip balm upsell (optional)."

5. **Popup + `Welcome_Discount_Email_FIRST10.html`** - reverted to the 10% off ENTIRE ORDER framing (copy tightened from vague "10% off" to explicit "your entire order," which reads as a bigger, clearer offer). Repositioned purpose: this is now the account's email-capture/cart-recovery tool, not the primary conversion incentive, that job moved to the universal free gift above. `Welcome_Free_Gift_Email.html` kept as reference only, not wired into the live Flow.

---

## Before this goes live, in order

1. Create the lip balm as a real Shopify product (real inventory, real $14.99 price), assign the new lip balm PDP section to it. Grab its variant ID.
2. Build the automatic Buy X Get Y discount per the steps above (no code, always-on).
3. Paste the lip balm's variant ID into `lipbalm_upsell_variant_id` in the theme customizer (this both shows the "free with every order" callout AND enables the auto-add JS). Upload a thumbnail for the fallback cart-drawer block.
4. Separately, follow `Gift_Card_Flow_Setup.md`'s 2026-07-19 update to build the scarcity gift-card token product and wire `gift_token_variant_id` + `gift_token_product_handle`.
5. Preview end to end before sending traffic: add the balm from the PDP, confirm the lip balm (and gift-card token, if configured) land in the cart automatically with no second click, confirm the lip balm rings up at $0.00, confirm the "X remaining" count on the PDP matches the token product's real inventory.
