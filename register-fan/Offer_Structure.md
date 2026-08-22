# Register Booster Fan — Offer Structure

**Created:** 2026-08-12
**Status:** Locked pending founder override on price. Everything downstream (PDP, creative, kill rules) is built against this.
**Product:** A register/vent cover with built-in fans. Replaces the existing floor or wall register, plugs into a wall outlet, and pulls conditioned air (hot or cold) out of the duct into the room instead of letting it stall in the branch line. **Unit sourced 2026-08-12** carries a **thermostat display, a remote, and mode presets** (winter / cooler / summer / fan / sleep), in **white and bronze**.

---

## 1. The price

> **Two numbers only.** Price gets judged on **CAC room** (the dollars available to buy a customer) and **margin %**. Not on projected CVR, CPC, CPM or CTR — we have no data on any of those for this product, and a projection built on nothing is worse than no projection, because it looks like a reason. Founder call, 2026-08-12.

| | Single | 2-Pack |
|---|---|---|
| Product price | **$89.99** | **$159.99** |
| Shipping | **$9.95** | **Free** |
| Customer pays | **$99.94** | **$159.99** |
| Per unit | $99.94 | **$80.00** |
| Landed COGS | $40.59 | $81.18 |
| Payment processing (2.9% + $0.30) | $3.20 | $4.94 |
| **CAC room** | **$56.15** | **$73.87** |
| **Margin %** | **56.2%** | **46.2%** |

**Supplier: upgraded unit sourced 2026-08-12 at $40.59 landed** (replaces the $46.39 baseline). **Founder call 2026-08-12** — two attempts at a cheaper unit failed (see the sourcing log below), and sourcing cheaper without losing quality is proving hard enough that it is not worth holding the test hostage to it. **The price stays at $89.99 / $159.99 anyway.** The purpose of this test is to find out whether a market exists at a price customers will pay, not to prove profitability at launch COGS. Those are different questions and this is the right one to answer first.

**The bundle returns 1.32x the contribution of a single for the same CAC.** CAC is paid per *order*, not per unit — one click, one customer, one acquisition cost, ~1.3x the money. That is the entire case for pushing the 2-pack, and it is why the bundle is allowed a lower margin % than the single. Margin % is the wrong thing to protect on a bundle.

**Why $89.99 and not $79.99 or $99.**

- **$89.99 + $9.95 is $99.94 at checkout.** The total the customer actually pays stays under $100, shipping included. That is the only real psychological threshold in this range, and this is the highest price that clears it.
- **$79.99 crosses nothing.** $89.94 and $99.94 sit in the same bracket, so dropping to $79.99 gives up $9.71 of CAC room per order and buys no threshold. ($99 + $9.95 = $108.95 *does* break the threshold, in the wrong direction.)
- **$159.99 over $139.99 on the bundle.** At $139.99 the bundle returns only 1.30x a single's contribution — double the fulfilment and double the return exposure for a thin premium. $159.99 holds the ratio at 1.32x while still showing an $80/unit price against a $99.94 single.

**Variant worth keeping on the shelf:** $79.99 + **$14.95** shipping = $94.94 all-in, $57.57 CAC room, 60.6% margin. Shipping is a real cost we are passing through, not a margin grab, and it is the only structure that makes a $79.99 headline affordable. The tradeoff is that visible shipping over ~$10 reads as a trick to some buyers. Test it against the locked pair rather than assuming.

**Anchor:** compare-at $119.99 on the single, $239.98 on the 2-pack. Both real: $119.99 is the intended post-test price and $239.98 is 2 × $119.99.

### The upgraded unit changes the competitive argument, not just the COGS

The unit sourced 2026-08-12 has a **thermostat display, a remote, and mode presets**. That is worth more than the $5.80 of CAC room it added, because it answers the single largest structural risk in this offer.

**The price-check objection now has a real answer.** *"I found one on Amazon for $22"* was the risk that killed tallow, and previously the only response was a brand story. Now it is a specification: that unit has no thermostat, no remote, and runs whenever it is plugged in. This one runs when the duct is actually blowing and stops when it isn't. Different tier, not the same thing marked up.

**It also sharpens the strongest angle.** Angle C — *"you shouldn't have to cool the whole house for one room"* — lands harder on a unit with its own temperature setting. The buyer is not boosting a vent, they are giving one room its own control. That is functionally a second thermostat for a room that never had one, which is exactly the thing angle D says you were quoted $4,500 for.

**Caution: more to set up, and setup is the incumbent's top complaint.** Every bad Amazon review on the category is an instruction failure. Buttons, modes and a remote add ways to conclude the unit is broken when it is only in the wrong mode. The four-photo install card is now more important, not less, and it must cover **the modes**, not just the physical fit.

### Sourcing log — two cheaper units attempted, both failed

**Attempt 1 — $18.25/unit overseas (~$31.75 landed).** Failed to source.

**Attempt 2 — US-based, $34.32 landed. Rejected on terms, 2026-08-12.** VEVOR distribution. Three disqualifiers:

1. **Random logistics.** "The supplier does not support designated logistics shipping." We could not control the carrier, promise a delivery window, or put a transit time on the PDP. Domestic transit speed was the *entire* reason to accept a worse COGS on an urgency purchase, and this clause removes it.
2. **No usable creative assets.** No brand authorization, no use of their images or video, all branding stripped from anything we do use. On a drop-shipped fitment product that means launching with no product photography, no install footage, and no way to shoot the measure-your-vent step — a missing input, not a constraint to write around.
3. **The manufacturer sells this unit on Amazon themselves.** The clause forbidding us to price below their Amazon listing exists because that listing exists. A price-checking customer at a $99.94 checkout doesn't find a substitute, they find the source. This is the tallow failure mode with the volume turned up.

Liability was also one-directional — full responsibility on us, explicit refusal of assistance, termination at their discretion.

**→ New screening question for the product-selection checklist:** *does the supplier sell this unit themselves, under their own brand, on Amazon?* If yes, we compete with our own source and every price-check resolves in their favour. Add this alongside the Meta Ad Library category-age check in `tallow-cream/POST_MORTEM.md`.

### The economics are close to tallow's — this is a demand test, not a margin test

Tallow ran **$41.52** on the single and **$60.71** on the bundle. This runs **$56.15** and **$73.87**. Better, but the same order of magnitude — and tallow died on economics, not on the product.

So everything that has to be different here sits on the demand side: no meaningful Meta competition, an urgent problem, low awareness, higher purchase intent. That is a real difference and it is why this is worth running. But it means:

- **The $600 cap in section 7 is doing more work than it would at a lower COGS. Hold it.** Extending it "for one more read" is exactly the mechanism by which tallow reached $2,000.
- **The 2-pack stays the upsell, not the default selection.** At 1.32x a single it is still worth pushing, but it no longer earns default status.
- **"Store profit funds the MOQ" is a longer runway than it looked.** At $56 of room, if CAC lands near $35 you keep ~$21 an order, putting a $2-3k MOQ ~100-145 orders out rather than 50. Raising to **$119 + $9.95 / $199** post-validation ($68.81 / $102.37 of room) is the lever that shortens it — and it is far easier to raise a price on a product with proof than to launch high without any.

**If a cheaper unit is sourced later**, the pricing does not need to change; the COGS drop goes straight into CAC room. At ~$34 landed the same prices give $62.42 (62.5%) and $86.41 (54.0%).

---

## 2. The bundle framing

The 2-pack is **not** "buy two, save money." That framing invites the objection *I only have one hot room.*

Frame it as **the second register in the same room, or the return path.**

Three true reasons a buyer needs two, in order of how often they'll apply:

1. **Most problem rooms have two registers.** A bedroom over a garage, a bonus room, a converted attic — boosting one and leaving the other is a half fix.
2. **The room at the end of the run is rarely the only one.** Whoever has the hot bedroom usually also has the cold office, or the upstairs that never matches the downstairs.
3. **It is the cheapest second unit you will ever buy.** $80.00 versus $99.94. If a second room turns up later, you paid $20 more for it today than you would have.

**Copy line for the selector:** *"Most problem rooms have more than one vent."*

Do not use "buy 2 get 20% off" as the on-page label. It reads as a discount promotion, which triggers price-checking. Show the per-unit price and let the arithmetic do it.

---

## 3. Sizing — the thing that will break this if we get it wrong

This is a physical-fitment product. It is the highest-friction step in the funnel and it has to be handled **before** the add-to-cart, not after.

**Standard US register sizes, by prevalence:** 4×10, 4×12, 6×10, 6×12. The duct-opening measurement (not the faceplate) is what matters.

**Confirmed 2026-08-12: the supplier offers TWO sizes** — the one quoted originally, plus a wider one. That is good news for the funnel: two options is a two-button choice, not a four-way dropdown, and it lets the measure step be a single yes/no rather than a lookup.

⚠️ **The exact dimensions are still unknown and are a hard gate on launch.** "Wider" is not something a customer can match against a tape measure. On a fitment product a wrong guess becomes a return, a chargeback and a review — the exact failure mode that dominates the incumbent's Amazon reviews. Get both numbers in writing before the size step is built. (Most likely 4×10 and 4×12, but nothing goes on the page on a guess.)

**On the PDP this becomes a required step:**

> **Step 1 — Measure your vent.** Pull the old cover off and measure the *hole*, not the cover. Most are 4×10 or 4×12.

with a photo of a tape measure across an open duct. Making this a numbered step, rather than a dropdown, converts the friction into a sense of competence — it makes the buyer feel they are doing an installation, which is exactly what the "I don't need a contractor" angle is selling.

**Fallback if a size is unavailable:** offer the nearest larger faceplate rather than a no-sale. Do not offer the smaller one.

**Colour: launch white only.** The unit also comes in bronze, and on a visible fixture colour choice genuinely helps conversion — but sizes were already going to multiply SKUs and bronze doubles that again. Every extra variant is another way for the size step to go wrong, and the size step is the highest-friction point in the funnel. Add bronze once a winning angle exists, unless carrying both costs nothing.

---

## 4. Guarantee and returns

**60-day money-back guarantee.** Same window that ran on tallow, for the same reason: the problem is seasonal-adjacent and a buyer needs to live through a hot stretch before they know.

**But the honest version, because this is a ~$100 electrical item and not a $50 jar.** The returns math is different: a returned fan costs us the unit and the return shipping, where a returned jar cost us $8. So the guarantee is written to be *easy to claim and hard to need*:

- **Return shipping is on us only if the unit is faulty.** Otherwise the customer pays return shipping. Say this plainly on the PDP. Hiding it produces chargebacks, which are worse than returns.
- **Keep-it threshold:** below $60 of recoverable value it is cheaper to refund and let the customer keep the unit than to pay return freight and restock a drop-shipped item. Set that as the default support policy from day one. (This threshold is high because the source is overseas; it would drop if a domestic supplier is ever landed.)

**The qualification that prevents most returns.** The dominant Amazon review complaint on the incumbent product is not quality, it is **installation confusion and mismatched expectations**. So the PDP must say, in our own voice, what this does *not* do:

> This works if air comes out of your vent but weakly, or if the room is at the end of a long duct run. It will not fix a vent with no airflow at all — that is a blocked or disconnected duct, and a fan cannot pull air that isn't arriving.

That paragraph costs some conversions and saves more returns than it costs. It also does the credibility work: nobody selling a gimmick tells you when it won't work.

---

## 4b. Imagery — generate the scenes, never the product

Founder call 2026-08-12: imagery is ours to make, with Nano Banana as the tool. One split governs all of it.

**Never generate the product itself.** Nano Banana drifts the physical details of a specific real object — fan count, display layout, screw positions, grille spacing. On a fitment product the customer must recognise what arrives in the box, and a generated hero shot that is subtly wrong is a misrepresentation that converts directly into returns and chargebacks.

| Asset | Source |
|---|---|
| Product gallery, size step, install card | **Real photography only** — supplier assets or a purchased unit. These make a factual claim about what you receive. |
| Room scenes, the hot bedroom, the window, the thermostat, a person at the vent, all ad creative | **Nano Banana.** |

This split also keeps the ads in the register that actually converted on the last brand. Per `tallow-cream/POST_MORTEM.md`, image and copy are independent variables, and the account's best-performing creative (B17C1) never showed the product as a product — it was an authorless object in a domestic scene. Carry that forward. And per the standing rule in `Tallow_Ad_Creative_Principles.md`: **no offer terms in any image** — no price, guarantee, shipping or CTA, as overlay or as diegetic text.

---

## 5. What's in the box

- The register faceplate with integrated fans
- Power adapter and cord
- Thermostat/control module (confirm which the img3 unit ships with)
- **A one-page install card, written by us, not the supplier's.** This is the highest-leverage $0 asset in the whole offer — the incumbent's worst reviews are all instruction failures. Four photos, four steps, no translated English. **On the upgraded unit it must also cover the modes and the remote**, since that is now the larger share of what a confused buyer can get wrong.

**Open supplier questions (do not block the offer, do block launch):**
1. Which register sizes are available?
2. Does the img3 unit support an aroma pad? (Determines whether the SA3 scent upsell is real or has to be dropped.)
3. ✅ **Confirmed: no restrictions on the supplier's images.** The VEVOR problem does not repeat here.
4. Does the adapter carry a UL/ETL/CE mark? Not a gate — it is a plug-in appliance, not a hardwired one — but it is worth one line on the PDP if it does.

---

## 6. Claim discipline — set now, before any copy is written

The nursery/baby trigger is the highest-intensity version of this problem, and it is the same structural trap named in the tallow post-mortem: **the most urgent version of the problem is the least compliant one.**

**Allowed:** room temperature, degrees, the thermostat reading, the monitor reading, the baby waking up, sleeping through, not having to get up and check, comfort, "the room finally matches the rest of the house."

**Banned outright:** SIDS, safe sleep, risk, danger, overheating as a hazard, anything health-framed, anything implying a medical or safety consequence. Never "keep your baby safe."

Same rule for the elderly-parent and the pet variants. Sell the temperature and the not-worrying. Never the risk.

**Also banned, carried over from tallow as a standing rule:** no price, guarantee, return window, shipping terms, discount or CTA in any creative — not as overlay, not as diegetic text.

---

## 7. Kill criteria and spend cap — LOCKED BEFORE LAUNCH

The explicit lesson from the tallow post-mortem is that these were set after the spend, not before. Not repeating that.

**Hard spend cap for the full validation test: $600.** If the product has not produced a profitable cell inside $600, it is dead, the same way tallow should have been dead at $600 instead of $2,000.

**Structure:** ABO, $12.50/day per cell, protected budget. Not CBO — CBO concentrates spend on first-hour noise, which is what produced the account's worst reads.

| Gate | Threshold | Action |
|---|---|---|
| **Per-cell hard kill** | $60 spend, 0 purchases | Kill the cell |
| **Per-cell CTR kill** | $40 spend, under 1.0% CTR | Kill the cell — creative is not stopping anyone |
| **CAC read** | after ~$150 total | Compare actual CAC against the $56.15 / $73.87 room. If nothing is close, stop and reconsider before spending the rest. No CPC target is set here on purpose — we have no basis for one, and inventing a threshold would make a guess look like a rule. |
| **The winner bar** | a cell holding CAC under $56.15 (single) / under $73.87 (bundle) across 3 consecutive days | Scale it. This is the bar tallow never hit. |
| **The product kill** | $600 spent, no cell has held CPA under contribution for 3 days | Kill the product. Write the post-mortem the same day. |

**One thing the cap does not cover:** CPM and CPC on this product are complete unknowns. The research established there *is* strong desire and there *is* almost no Meta competition, which should mean cheaper auction than tallow — but that is a hypothesis, not a number. The $150 CPC read above exists specifically to find out early and cheaply.

---

## 8. What is still needed before launch

| Item | Blocks | Owner |
|---|---|---|
| **Exact dimensions of both sizes** | The size selector, therefore the PDP, therefore everything. Two sizes confirmed; the numbers are not | Founder → supplier |
| Combined 2-pack shipping rate | Whether the 2-pack is default-selected or the upsell | Founder → supplier |
| Aroma pad confirmation | Whether SA3 exists as an upsell | Founder → supplier |
| Scene imagery via Nano Banana | Ads and PDP scenes (never the product itself — see 4b) | Build |
| Shopify: product, variants by size, 2-pack pricing | PDP build | Build |
| PDP with the measure step, the honest qualification, the install card | Ads | Build |
| Install card (4 photos, 4 steps) | Returns rate, not launch | Build |
| Ad batch 1 — angles A and C leading, D closing, B pre-empted | Launch | Build |
