# Presell Page: B22C1 Mechanism Bridge

**Purpose:** B22C1 (news-chyron badge graphic, "Why her skin still looks dewy at 2pm and yours doesn't") is getting good CPM and CPC and has produced an initiated checkout, but the ad itself is a single headline image, it has no story to carry someone from curiosity to purchase. This page is the missing middle: click the ad, land here first, then click through to the PDP already convinced.

**URL slug (proposed):** `/pages/why-water-doesnt-hold`
**Traffic source:** B22C1 only, to start. Do not link this from anywhere else in the store nav.
**CTA destination:** PDP (`/products/whipped-tallow-honey-balm` or actual live handle), same product/price/offer as everywhere else.

---

## Page copy (in order, top to bottom)

**Eyebrow:** THE SCIENCE

**H1:** Why her skin still looks dewy at 2pm, and yours doesn't

**Subhead:** It's not your skin. It's what's evaporating by noon.

---

Most moisturizers stop holding by noon. That's not your skin failing. That's water doing what water does.

Water evaporates in about an hour. Every cream that lists it as the first ingredient is gone before lunch, whether the label says so or not. You put it on at 7am and by noon it's gone. That's why nothing holds. That's why your skin feels tight by the time you're eating lunch, why foundation cracks around your mouth by two.

Fat is different. Skin recognizes it as close to what it already makes on its own, so it absorbs in instead of sitting on top.

**[Inline visual: simple two-column comparison graphic, reused/adapted from B19C2's whiteboard diagram style: LEFT "Most Creams" with water droplets evaporating upward, RIGHT "Tallow Balm" with fat absorbing downward. Keep it simple, legible, not busy.]**

Here's the part that isn't on any label. After about forty, skin makes a lot less of its own oil. The drop is real. Most women never connect what's happening to their face to what changed underneath, they just notice their skin doesn't hold the way it used to.

========

A friend of mine, Elaine, figured this out by accident. She'd been using the same jar since her aunt Winnie told her about it at a wedding two summers ago. Winnie is 76, keeps bees in Vermont, and has used the same four ingredients since 1987. "I bought my first one by accident at a farmer's market," she said. Her skin looks like a woman fifteen years younger.

Elaine flipped every bottle in her bathroom over one afternoon and checked. Water. Glycerin second. Something unpronounceable third. Every single one.

The jar Winnie uses doesn't have water as the first ingredient. It's tallow, first. Fat, not water. That's the whole difference.

========

**Sub-head:** What's actually in it

Four ingredients. Grass-fed tallow. Manuka honey. Olive oil. Calendula. Nothing you can't pronounce, nothing that evaporates by noon.

**[Inline visual: the same amber jar, close on the label, calm and simple, not a hero shot]**

========

**Sub-head:** What people notice, not what the label promises

Skin holds instead of going tight by mid-afternoon. Foundation sits flat instead of cracking around the mouth. Some people stop carrying backup lotion in their purse and don't notice for weeks that they've stopped needing to.

Nobody on this page is a doctor. This isn't a medical claim. It's what happens when you stop putting water on your face and start putting on something closer to what your skin already makes.

========

**CTA block:**

**H3:** Try it. $49.99. Free shipping. 60-day money-back guarantee.

If it doesn't do anything in six weeks, email them and get every dollar back.

**[Button: Get the Jar -> links to PDP]**

**Trust strip below button:** 60-Day Guarantee · Free US Shipping · 4 Ingredients · No Subscription

---

## Install (built, ready to ship)

Files: `tallow-cream/store/theme/sections/tallow-presell-mechanism.liquid` + `tallow-cream/store/theme/templates/page.presell-mechanism.json`.

1. Upload both files to the theme (Sections + Templates folders) via the Shopify theme editor's code view, or a theme deploy.
2. In Shopify admin, create a new Page (Online Store -> Pages -> Add page), title it something like "Why Water Doesn't Hold," leave the content blank.
3. On that page, under Theme template, select `page.presell-mechanism`.
4. Update `pdp_url` in the section settings (via theme customizer) to the real live PDP handle if it differs from the default.
5. Point B22C1's ad link to this page's URL instead of the PDP. Every other cell (B22C2, B22C3, B21, B17C1) keeps going straight to the PDP as before, this bridge is B22C1-only for now.

## Build notes

- Reuse the PDP's existing CSS variables and font stack exactly (`--cream`, `--green`, `--amber`, Georgia serif headers, system sans body) so the page feels like the same brand, not a bolted-on ad landing page.
- No product carousel, no reviews section, no nav header with other links, this page has exactly one exit: the CTA button to the PDP. Anything that lets someone wander back into the main site defeats the purpose.
- Keep it shorter than a full native ad (the mechanism story above is roughly 400 words), this is a bridge, not the whole sale, the PDP still has to close it.
- Mobile-first, single column, same as the PDP build.
