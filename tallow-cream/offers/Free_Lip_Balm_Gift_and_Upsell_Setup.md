# Free Lip Balm Gift + Cart Upsell: Setup Guide

**Date:** 2026-07-19, REVISED same day.
**2026-07-19 revision:** founder reconsidered. The free lip balm now goes to **every customer automatically**, not gated behind popup email signup (16% of visitors was the wrong ceiling to optimize under). The popup reverted to the original 10% FIRST10 discount, repositioned as an email-capture/cart-recovery tool, not the primary incentive. The gift card also changed from every-order to a scarcity "next 100 customers" mechanic. This doc now covers the universal free-gift mechanism; see `Gift_Card_Flow_Setup.md` for the scarcity gift card. `Welcome_Free_Gift_Email.html` is superseded/reference-only, the popup email is `Welcome_Discount_Email_FIRST10.html` again.

**Delivery mechanism, updated:** since the gift is now universal, it no longer needs a discount code at all for the customer to enter. `tallow-pdp.liquid`'s JS now **auto-adds the lip balm to the cart silently** the moment the main balm is added (see `addGiftsSilently()`), using the same Buy X Get Y discount underneath (still needed so the item rings up at $0, see below) but with zero manual steps for the customer. The cart-drawer upsell block described further down is now a fallback only, for anyone who removes the free item and wants to re-add it (at the real $7.99 cross-sell price, since removing signals they don't want the freebie).

**2026-07-19, third revision (design overhaul + product-picker + upsell removed):**
- **Cart-drawer upsell removed entirely, per founder: "no point in an upsell for something we are giving as a free gift."** Correct call, cross-selling a free item is incoherent. Markup, CSS, and the 3 dead schema settings (`lipbalm_upsell_title`, `lipbalm_upsell_price`, the old `lipbalm_upsell_image`) all removed.
- **Free gift and gift-card token now reference real Shopify products, not raw variant IDs.** New schema settings `free_gift_product` and `gift_token_product` are native `product` pickers, founder selects the actual product from a dropdown in the customizer instead of copy-pasting a variant ID. Image, title, and price all pull from the real product automatically (with optional override fields if a different photo/title is wanted just for this card). The JS auto-add logic and the live remaining-count logic both read the variant ID and inventory directly off the selected product, nothing to keep in sync manually.
- **Free-gift card redesigned** (invoked the frontend-design skill per founder's request): a torn-ticket motif, small green "FREE" tab hanging off the top edge, a real 64px product-image slot (falls back to a gift-icon glyph if no photo is set yet, never renders empty), a dashed perforated divider between the image and the copy (mimics a ticket stub tear), Georgia serif title matching the rest of the page's headers instead of plain body text, a green pill "$X value" tag pulled from the product's real price, and a subtle fade-up entrance animation on page load (respects `prefers-reduced-motion`). Meant to read as a genuine claimed-gift moment rather than another beige alert box.

**2026-07-19, second revision (design + cart display + timing):**
- **PDP visual redesign:** the free gift now gets its own real card (`free-gift-card`) with a product photo, eyebrow label, title, and value line, placed directly under the main Add to Cart button, the most prominent real estate on the page. New `free_gift_image` setting for the lip balm photo.
- **Gift card scarcity DEMOTED on purpose, pushback from Claude, founder agreed:** the "too good to be true" risk isn't about pixel styling, it's about offer count. Stacking a boxed gift-card callout next to a boxed free-gift callout makes the page read as pile-on regardless of how clean either box looks individually. The gift card moved to (a) the top announcement bar (`anno_text` default updated to mention it) and (b) a small plain-text line under the free-gift card with no background/border, deliberately lower visual weight, not competing for the same attention as the one offer that should dominate the page.
- **Cart drawer now labels the free item explicitly.** Any line item where `final_line_price` is 0 but `original_line_price` is not (i.e. discounted to free by the automatic Buy X Get Y) gets a green "FREE GIFT" tag next to its name, and its price column shows the word "FREE" instead of "$0.00". This was flagged as a real conversion lever (seeing "free" explicitly in the cart, not just a zero, should lift ATC->Checkout), not just cosmetic.
- **Gift card cap:** founder will track and manually turn off the `gift_card_active` toggle once 100 units are given out, no live-inventory-counter build needed for this one (the code still supports an optional live count via `gift_token_product_handle` if that's wanted later, just leave it blank for the manual-tracking approach).
- **Popup delay: 5s -> 8s.** Deliberate: gives already-decided visitors enough time to reach checkout before the popup interrupts them (so they convert at full price with their email still captured at checkout, no discount cost), while still catching genuinely undecided visitors who are still reading past the 8-second mark.

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

3. **`tallow-pdp.liquid` free-gift card, under the Add to Cart button** - the primary visual focus of the page's incentive stack (ticket-motif card, see the design note above). Driven entirely by the `free_gift_product` setting, a native product picker, image/title/price all pull from the real product automatically.

4. **`tallow-pdp.liquid` gift-card line** - deliberately minimal plain-text line below the free-gift card, LIVE remaining count pulled directly from `gift_token_product`'s real inventory, auto-hides once inventory hits 0.

5. **Cart drawer upsell block: REMOVED**, no longer exists in the code as of the third revision above.

6. **Popup + `Welcome_Discount_Email_FIRST10.html`** - reverted to the 10% off ENTIRE ORDER framing (copy tightened from vague "10% off" to explicit "your entire order," which reads as a bigger, clearer offer). Repositioned purpose: this is now the account's email-capture/cart-recovery tool, not the primary conversion incentive, that job moved to the universal free gift above. `Welcome_Free_Gift_Email.html` kept as reference only, not wired into the live Flow.

---

## Before this goes live, in order

1. Create the lip mask as a real Shopify product (real inventory, real $14.99 price), assign the lip mask PDP section to it.
2. Build the automatic Buy X Get Y discount per the steps above (no code, always-on).
3. In the theme customizer, select that product in the new `free_gift_product` picker (this alone shows the free-gift card AND enables the auto-add JS, no manual ID entry). Optionally set an override photo/title if you want the card to show something different than the product's own listing.
4. Separately, follow `Gift_Card_Flow_Setup.md`'s 2026-07-19 update to build the scarcity gift-card token product, select it in the new `gift_token_product` picker.
5. Preview end to end before sending traffic: add the balm from the PDP, confirm the lip mask (and gift-card token, if configured) land in the cart automatically with no second click, confirm it rings up at $0.00 with the "FREE GIFT" tag showing, confirm the "X remaining" count on the PDP matches the token product's real inventory.
