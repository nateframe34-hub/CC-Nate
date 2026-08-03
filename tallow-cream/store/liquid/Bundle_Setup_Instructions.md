# 2-Pack Bundle — Setup Instructions

**Created:** 2026-08-02
**File:** `store/theme/sections/tallow-pdp-v2-reformulated.liquid` — **everything is in that one file.** No snippets, no `{% render %}`, nothing to coordinate across files. (Two snippets were created and removed during the build; the founder's instruction was to keep it all in the PDP section and that is where it now lives.)

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

## Step 1 — Shopify admin ⬅ THE ONLY THING LEFT TO DO

**Rebuilt 2026-08-03, founder call: quantity-based, not a separate product and not variant IDs.**

Tier 1 always adds **quantity 1** of the balm. Tier 2 adds **quantity 2** (Mode B, the default). Two constraints drive the whole design: **Shopify applies only one product discount**, and **Teemdrop fulfilment makes a new listing expensive to create.**

### 🚨 Shopify applies only ONE product discount — this is what the design works around

Buy-X-Get-Y counts as a product discount, so **"buy 2 = $19.99 off" and "free lip mask" cannot both run.** The section has a **"2-Pack behaviour"** setting with two ways to spend the single discount:

**MODE B — quantity 2 of the balm ← DEFAULT, the fulfilment-safe route**

Founder constraint, 2026-08-03: *"I don't know how I can add a variant of a 2 quantity or make a 2nd product listing with a 2 quantity as all my fulfillment is through Teemdrop."* Mode B needs nothing new created, so nothing new needs supplier mapping.

| | |
|---|---|
| Create | **Nothing.** Tier 2 adds quantity 2 of the SKU Teemdrop already maps |
| Product discount | **Buy X Get Y:** 2 balms in cart → 1 lip mask free |
| Order discount | **Amount off order**, minimum quantity **2** → **−$19.99** ($99.98 → $79.99) |
| Cart reads | `Balm ×2 — $79.99` + `Lip Mask — Free` |

**Two discounts, not one — founder call 2026-08-03.** Shopify caps you at one *product* discount, but a product discount and an **order** discount can run together. Tick **Combinations → combines with order/product discounts** on both, or they won't stack.

**This is also what kills the exploit.** The earlier plan gave the lip mask a $0.00 variant, which is unconditional — a customer could add 2 balms, let the mask auto-add, remove the balms and keep it. Buy-X-Get-Y re-evaluates against cart contents at checkout, so removing the balms re-prices the mask to $20 on its own. No JS guard needed, and the lip mask stays a normal priced product.

**The cost:** an automatic order discount blocks order-level discount *codes* at checkout, so the email-marketing codes stop working. Founder accepted this 2026-08-03 — the email list has produced **1 conversion**, so the leverage being given up is close to zero.

**BXGY does not auto-add the Y item.** The JS still has to put the lip mask in the cart (`addGiftsSilently()`); the discount only zeroes it once it's there. So `free_gift_product` must stay pointed at the **real, priced** lip mask product.

**MODE A — separate 2-Pack product (only if fulfilment allows it later)**

| | |
|---|---|
| Create | A product **"Tallow Honey Balm — 2 Pack"** at **$79.99**, compare-at **$99.98**, containing 2 jars |
| The one discount | **Buy X Get Y:** 2-Pack in cart → 1 lip mask free |
| Price discount needed | **None.** $79.99 is simply the price |
| Cart reads | `2-Pack $79.99` + `Lip Mask FREE` |

Cleaner on paper — it doesn't spend the discount on arithmetic — but it requires a new listing and a new Teemdrop mapping. Park it. If you ever do switch, pick the 2-Pack under *2-Pack product (Mode A only)*.

**Check for stale automatic discounts first.** This section's own header documents a past incident where two automatic discounts stacked and produced a price nobody intended. Adding two more is exactly when that resurfaces — verify the final cart total is $79.99 before going live.

### Then in the theme customizer

Tick **"Show the bundle selector"** (off by default, so nothing changes until you do), leave **2-Pack behaviour** on **Mode B (quantity)** — that is the default — and upload the **real lip mask photo** to *Tier 2 → Gift 1 image*. Shipping and Shipping Protection use built-in line icons and need no upload. No product picker is needed in Mode B.

**Fail-safe:** in Mode A the selector stays hidden until a 2-Pack product is picked, so a half-finished setup can't reach customers. Mode B has no such gate — its guard is the discount, so verify the cart reads $79.99 before you tick the box.

---

## Step 2 — Markup, CSS and JS ✅ DONE (in the section file)

The selector renders between the shipping line and the hero add-to-cart form. CSS is appended to the existing `#tallow-pdp-v2` scoped block. The JS sits immediately above `addGiftsSilently()` and:

- takes ownership of the `id` input on `tlw-form-hero`, `tlw-form-final` and `tlw-form-sticky`, creating it if absent
- rewrites each Add to Cart button's price label while preserving its cart icon
- sets `window.TLW_GIFT_ELIGIBLE`, which gates the gift auto-add
- supports arrow-key navigation and `aria-checked` on a proper radiogroup

**Fail-safe:** the selector is behind a **"Show the bundle selector" checkbox, off by default.** While it's off, Liquid skips the block entirely, `TLW_GIFT_ELIGIBLE` stays `true`, and the page behaves exactly as it does today. Deploy freely; nothing changes until you tick the box.

**Also fixed while in there:** the gift auto-add previously only fired from the hero form (it keyed off a `.tlw-main-flag` input that existed on that form alone), so adding from the sticky bar or the final CTA silently skipped the gift. The selector now adds that flag to all three forms.

---

## Step 3 — Section settings ✅ DONE

Settings added under a **"Bundle selector"** header in the schema, validated as JSON with no duplicate IDs. In Mode B nothing needs picking except the lip mask image — every other field is pre-filled with the intended copy.

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

Modelled on the Grüns PDP (founder reference, 2026-08-03). Theirs hangs off a subscription; ours hangs off the 2-pack. Every gift is **named, priced and shown as a card**, so the value of the extras is visible rather than implied.

| Tier | Gifts | Pill |
|---|---|---|
| Single | Free Shipping $6 | "$6 value" |
| **2-Pack** | **Free Lip Mask $20 · Free Shipping $6 · Shipping Protection $5** | **"$31 value"** |

**Visuals:** each card takes either a built-in line icon (delivery truck, shield, gift box) or an uploaded image, and the image wins if present. Shipping and Shipping Protection use the truck and shield icons. **The lip mask should use a real product photo** — it's a physical $20 item and a photograph sells it far better than a generic gift glyph.

**The stack only renders on the selected tier.** With the 2-pack pre-selected, a visitor lands seeing three gifts and $31 of value; clicking Single collapses it to one gift and $6. That contrast is the persuasion, and it's how Grüns does it.

**The $20 lip mask value is a real listed price** (founder confirmed 2026-08-03), so the claim is straightforwardly true. Shipping Protection at $5 holds on the same basis if it's a real add-on.

---

## What to measure

| Metric | Why |
|---|---|
| **Bundle take rate** | The whole point. Blended contribution at 25% take is ~$46, at 50% ~$51. |
| **LPV→ATC** | Confirms the second option isn't causing choice paralysis. |
| **ATC→purchase** | Where removing the universal gift would show up if it was helping. |
| **Blended AOV** | The number that moves the CPC you can afford. |

**Breakeven CPA moves from $30.16 to $39-41 on the single and $60.71 on the bundle.** Every kill decision made before 2026-08-02 was judged against a bar that was ~30% too strict.
