# Presell Page: B22C1 Mechanism Bridge

**Purpose:** B22C1 (news-chyron badge graphic, "Why her skin still looks dewy at 2pm and yours doesn't") is getting good CPM and CPC and has produced an initiated checkout, but the ad itself is a single headline image, it has no story to carry someone from curiosity to purchase. This page is the missing middle: click the ad, land here first, then click through to the PDP already convinced.

**URL slug (proposed):** `/pages/why-water-doesnt-hold`
**Traffic source:** B22C1 only, to start. Do not link this from anywhere else in the store nav.
**CTA destination:** PDP, live link: `https://trybasline.com/products/whipped-tallow-honey-balm`, same product/price/offer as everywhere else.

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
4. `pdp_url` already defaults to the live PDP link (`https://trybasline.com/products/whipped-tallow-honey-balm`), confirm it's correct in the theme customizer.
4b. Once the 3 images above are generated, upload them via the theme customizer's image pickers on this section: Hero illustration, Mechanism diagram, Product jar photo. The page renders clean text-only placeholders until images are added, so it's safe to install now and drop images in later.
5. Point B22C1's ad link to this page's URL instead of the PDP. Every other cell (B22C2, B22C3, B21, B17C1) keeps going straight to the PDP as before, this bridge is B22C1-only for now.

## Image prompts (3 needed)

### 1. Hero illustration (top of page, above the H1)

Botanical/apothecary-style illustration, matches the brand's existing "Warm Evidence-Forward Apothecary" visual identity already locked for the PDP, not a photo. This is the non-photographic illustration lever flagged in the creative gap analysis (item 3), untested until now.

```
A vintage-style botanical and scientific illustration in the manner of an old apothecary reference plate, warm cream paper background with subtle age-toned texture. Centered composition: a cross-section diagram of skin rendered in fine ink linework and soft warm watercolor washes (amber, deep green, honey gold), showing a simple, elegant visual of water droplets sitting on the surface and evaporating upward on one side, and small warm golden fat molecules absorbing downward into the skin layer on the other side, labeled simply and legibly in a serif hand-lettered style: "Water" and "Fat," no other text. Small botanical flourishes at the corners, a sprig of calendula, a honeycomb fragment, a simple bee, in the same fine-line vintage illustration style, muted and elegant, not cartoonish. Overall palette: cream, amber, deep forest green, warm gold, matching an old-world scientific field-guide aesthetic. No photorealism, no 3D rendering, no modern infographic look, no additional text beyond the two labels. 16:9 or 3:2 aspect ratio, suitable for a wide page-top banner.
```

### 2. Mechanism diagram (replaces the emoji placeholder mid-page)

Same illustration family as the hero, smaller and simpler, two-column comparison.

```
A simple two-column diagram in the same vintage botanical/apothecary illustration style: fine ink linework, warm watercolor washes in amber and deep green, cream paper background. Left column headed "Most Creams" in elegant serif hand lettering: a small illustrated water droplet sitting on a flat line representing skin's surface, three faint upward arrows above it suggesting evaporation, rendered delicately, not clinical. Right column headed "Tallow Balm": a small illustrated warm golden droplet shown partially absorbed into the same flat surface line, one soft downward arrow, the droplet appears to be sinking in rather than sitting on top. A thin hand-drawn dividing line down the center. No other text, no percentages, no clinical or medical iconography, keep it warm and editorial rather than technical. 4:3 aspect ratio.
```

### 3. Calm product jar shot (replaces the `[ product jar, calm, label-forward ]` placeholder)

Not a hero/glamour shot, matches the same restrained, real-feeling tone as the rest of the presell copy.

```
A calm, softly lit photograph of a single amber glass jar of whipped balm sitting on a warm wood or stone surface, simple label facing the camera and legible but not glossy or over-lit, the lid resting beside it with a small amount of balm visible inside catching soft natural window light. Background softly blurred, warm neutral tones (cream, soft wood, muted sage), no other products in frame, no hands, no people. Gentle, editorial product photography, warm and inviting but understated, not a chrome-and-studio commercial product shot. 4:3 aspect ratio.
```

## Build notes

- Reuse the PDP's existing CSS variables and font stack exactly (`--cream`, `--green`, `--amber`, Georgia serif headers, system sans body) so the page feels like the same brand, not a bolted-on ad landing page.
- No product carousel, no reviews section, no nav header with other links, this page has exactly one exit: the CTA button to the PDP. Anything that lets someone wander back into the main site defeats the purpose.
- Keep it shorter than a full native ad (the mechanism story above is roughly 400 words), this is a bridge, not the whole sale, the PDP still has to close it.
- Mobile-first, single column, same as the PDP build.
