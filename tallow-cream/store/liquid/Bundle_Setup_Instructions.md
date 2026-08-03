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

## Step 1 — Shopify admin: create the variant

The PDP hardcodes *displayed* price via section settings, but the **cart charges the real variant price**, so the variant must be created properly.

On the Tallow Honey Balm product, add an option (e.g. `Size` or `Pack`) with two values:

| Variant | Price | SKU suggestion | Inventory |
|---|---|---|---|
| 1 Jar | **$49.99** | TLW-60G-1 | tracked |
| 2 Jars + Lip Mask | **$79.99** | TLW-60G-2GIFT | tracked |

Notes:
- Set **compare-at $99.98** on the 2-pack so Shopify's own discount display is consistent with the struck-through price in the selector.
- The 2-pack is **one variant that ships two jars plus a lip mask**. Do not model it as quantity 2, or the per-unit price maths and the gift logic both break.
- Make sure the **2-pack variant is not excluded** from any existing automatic discounts. Check for leftovers — the PDP file notes a past incident where two automatic discounts stacked and produced an unintended price.

Copy both **variant IDs** (Products → variant → the `variant=` number in the URL).

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

## What to measure

| Metric | Why |
|---|---|
| **Bundle take rate** | The whole point. Blended contribution at 25% take is ~$46, at 50% ~$51. |
| **LPV→ATC** | Confirms the second option isn't causing choice paralysis. |
| **ATC→purchase** | Where removing the universal gift would show up if it was helping. |
| **Blended AOV** | The number that moves the CPC you can afford. |

**Breakeven CPA moves from $30.16 to $39-41 on the single and $60.71 on the bundle.** Every kill decision made before 2026-08-02 was judged against a bar that was ~30% too strict.
