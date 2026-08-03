# 2-Pack Bundle — Setup Instructions

**Created:** 2026-08-02
**File:** `store/theme/sections/tallow-pdp-v2-reformulated.liquid` — **the bundle is built directly into the PDP section.** There is no separate snippet; an earlier one was removed on founder's call, since `{% render %}` doesn't inherit `section` and the settings live in this file's schema anyway.

**Code is already written and committed. Steps 2, 3 and 4 below are DONE — they are kept as a record of what changed. Only Step 1 (Shopify admin) still needs doing.**

---

## Why this exists

At the new COGS ($10.81 for balm + lip mask, $8.47 for the balm alone):

| Offer | Price | COGS | Contribution | Supports a CPC of |
|---|---|---|---|---|
| 1 jar (no gift) | $49.99 | $8.47 | **$41.52** | ~$1.42 |
| 2 jars + lip mask | $79.99 | $19.28 | **$60.71** | ~$2.08 |

*(at the account's real 3.42% click→purchase)*

**Actual account CPC is $3.17.** The 2-pack roughly halves the gap, and it does it without needing anything from Meta.

It also hedges retention. There are **0 repeat purchases**, but only **3-4 customers are past a 6-8 week reorder window** as of 2026-08-02, so that is absence of data rather than proof of a problem. The 2-pack captures the second unit at peak intent instead of betting on a return visit — which matters more than usual here, because **the product is ~$20 cheaper on Amazon**, so a satisfied customer reordering may not reorder from us.

**No subscription.** Founder call, 2026-08-02: subscribe-and-save depresses CVR and isn't worth it while the messaging is still unproven. Revisit once a winning ad exists.

---

## Step 1 — Shopify admin: create the 2-Pack as its own PRODUCT ⬅ THE ONLY THING LEFT TO DO

**Founder call 2026-08-03: configured by product, not variant IDs.** The 2-pack is a separate Shopify product with its own images, inventory and URL — not a variant of the balm.

| Product | Price | Compare-at | Contains |
|---|---|---|---|
| Tallow Honey Balm | **$49.99** | — | 1 jar |
| Tallow Honey Balm — 2 Pack | **$79.99** | **$99.98** | 2 jars + lip mask |

- The compare-at makes Shopify's own discount display agree with the struck price in the selector.
- **Ship the lip mask inside the 2-pack SKU** rather than relying on the cart auto-add. One SKU, no cart trickery, and the cart can never hold the gift without the bundle. (The auto-add still works if you'd rather — it's gated to this tier.)
- **Check for stale automatic discounts before going live.** This file's parent section documents a past incident where two automatic discounts stacked and produced a price nobody intended. A new product is exactly when that resurfaces.

Then in the theme customizer, under **"Bundle selector + free gifts"**, pick both products. Everything else is pre-filled.

---

## Step 2 — Markup, CSS and JS ✅ DONE (in the section file)

The selector renders between the shipping line and the hero add-to-cart form. CSS is appended to the existing `#tallow-pdp-v2` scoped block. The JS sits immediately above `addGiftsSilently()` and:

- takes ownership of the `id` input on `tlw-form-hero`, `tlw-form-final` and `tlw-form-sticky`, creating it if absent
- rewrites each Add to Cart button's price label while preserving its cart icon
- sets `window.TLW_GIFT_ELIGIBLE`, which gates the gift auto-add
- supports arrow-key navigation and `aria-checked` on a proper radiogroup

**Fail-safe:** if either variant ID is blank the whole block is skipped by Liquid, `TLW_GIFT_ELIGIBLE` stays `true`, and the page behaves exactly as it did before. Nothing breaks if you deploy before creating the variants.

---

## Step 3 — Section settings ✅ DONE

Nineteen settings added under a **"Bundle selector"** header in the schema, validated as JSON with no duplicate IDs. Set the two variant IDs in the theme customizer; every other field is pre-filled with the intended copy.

---

## Step 4 — Free gift moved to the 2-pack ✅ DONE

**This is the part that changes existing behaviour, so read it.**

Today the lip mask auto-adds to every order via the script around line 709 of the PDP file. Founder decision 2026-08-02: it moves to the 2-pack, both to remove the *"I'm paying $50 for a lip mask I don't want"* read and to take $2.34 out of every single-jar order.

`addGiftsSilently()` now opens with:

```js
if(!window.TLW_GIFT_ELIGIBLE) return Promise.resolve();
```

so the lip mask (and the gift-card token) auto-add on the 2-pack tier only.

**Recommended simplification:** if the 2-pack physically ships with the lip mask inside, remove the lip mask from `free_gift_product` entirely and let the SKU carry it. Fewer moving parts, and the cart can never hold the gift without the bundle.

⚠️ **Watch ATC→purchase after this change.** The 7/22 note says the universal gift *appeared* to lift CVR but was never confirmed on volume. You are removing something unproven, not something known-good, but it's the metric where a regression would surface.

---

## Step 5 — Update the ads before they run

**All five B33 cells state `$49.99` in their closes**, and several imply a single jar. Once the bundle is live the copy isn't wrong, but it undersells. Options in order of preference:

1. **Leave the ads alone for now.** $49.99 is still the entry price and the selector does the upsell on the page. No copy edits, no delay to launch.
2. Later, once a winning ad exists, add a bundle line to that ad's close only.

Do **not** rewrite all five closes before launch. The batch's job is finding a scroll-stopper; changing the offer copy mid-test adds a variable.

---

## The free-gift stack ✅ DONE

Modelled on the Grüns PDP (founder reference, 2026-08-03). Their version hangs off a subscription; ours hangs off the 2-pack. Every gift is **named and priced** and shown as a card, so the value of the extras is visible rather than implied.

| Tier | Gifts | Pill |
|---|---|---|
| Single | Shipping $6 | "$6 value" |
| **2-Pack** | **Lip Mask $20 · Shipping $6 · Shipping Protection $5** | **"$31 value"** |

**The stack is only visible on the selected tier.** With the 2-pack pre-selected, a visitor lands seeing three gifts and $31 of value; clicking Single collapses it to one gift and $6. That contrast is the persuasion, and it's how Grüns does it too.

⚠️ **One thing to make true rather than drop.** "$20 value" on the lip mask is only defensible if the lip mask is actually sold somewhere at ~$20. Right now it isn't sold at all, which makes the number an assertion rather than a fact. **The fix costs nothing: list the lip mask as a real product at $19.99 on the store.** Then the claim is simply true, the gift reads as a genuine $20 item, and there's nothing to argue about. Same logic for Shipping Protection at $5 — if it's a real add-on you'd otherwise charge for, the number holds.

---

## What to measure

| Metric | Why |
|---|---|
| **Bundle take rate** | The whole point. Blended contribution at 25% take is ~$46, at 50% ~$51. |
| **LPV→ATC** | Confirms the second option isn't causing choice paralysis. |
| **ATC→purchase** | Where removing the universal gift would show up if it was helping. |
| **Blended AOV** | The number that moves the CPC you can afford. |

**Breakeven CPA moves from $30.16 to $39-41 on the single and $60.71 on the bundle.** Every kill decision made before 2026-08-02 was judged against a bar that was ~30% too strict.
