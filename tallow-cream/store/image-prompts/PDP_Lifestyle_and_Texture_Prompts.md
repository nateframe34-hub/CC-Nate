# PDP Image Prompts: Lifestyle (ad-congruence) + Texture Close-Up

**Date:** 2026-07-12
**Why these two:** the PDP currently proves its claims with diagrams (mechanism, label comparison, 14-vs-1 math), which work, but two gaps remained: (1) no visual echo of the ad she just clicked, creating a small congruence gap on landing, (2) no visual proof of the "absorbs in 2 min, no shine" claim. These two images fill both, added as optional `image_picker` settings in `tallow-cream/store/theme/sections/tallow-pdp.liquid` (`lifestyle_image` + `lifestyle_caption`, `texture_image`). Both render conditionally, the page works fine with them left blank.

**Style rule for both, non-negotiable:** honest phone-quality, no studio gloss, no beauty-editorial lighting, no posed model energy. Same standard as the B26 Andromeda ad creatives (real garden, real trail, real sideline). If either image reads as a stock photo, it will hurt more than help on this specific page.

---

## 1. Lifestyle / ad-congruence photo (`lifestyle_image`)

**Placement:** end of the "Sound familiar?" checks section, near the top of the page, right after she's read the relatable pain points and before the mechanism explanation.
**Purpose:** echo the real-context image from whichever ad is driving the most current traffic, so landing on the PDP doesn't feel like a different place than the ad she clicked.

**Which version to generate first:** match it to whichever angle is carrying the most spend right now (check the ad tracker before generating). As of this writing that's the B26 Sun-Lived batch, so lead with the Gardeners version below. Generate the other two as swappable alternates if traffic mix shifts, this setting is built to be swapped per traffic period, not a permanent single image.

### Version A: Gardeners (matches B26C1)
An ultra-realistic iPhone photo of a well-maintained backyard vegetable and flower garden in late spring, raised beds with staked tomato plants, a coiled garden hose, a trowel stuck upright in the soil, worn gloves tossed on the bed edge. Late afternoon natural light, unstyled suburban backyard, ordinary fence and rooftop visible beyond. Slightly imperfect framing, the kind of photo a woman takes proudly of her own garden. No people, no faces, no text, no logos. 4:5 aspect ratio.

### Version B: Walkers (matches B26C2)
An ultra-realistic first-person iPhone photo taken mid-walk on a dirt trail at 6:30am, foothills in soft morning light, long shadows. At the bottom edge of frame, the head and ears of a medium brown mutt on a leash, slightly motion-blurred. Casual, slightly tilted framing, one-handed phone shot. No people, no text, no logos. 4:5 aspect ratio.

### Version C: Bleacher Parent (matches B26C3)
An ultra-realistic iPhone photo shot from a parent's folding chair on the sideline of a youth soccer game, bright late-morning sun, players mid-play in the middle distance (small, not identifiable), a water bottle in the chair's cupholder in the foreground. Slightly overexposed, honest outdoor phone-camera light. No identifiable faces, no text, no logos. 4:5 aspect ratio.

**Suggested caption (optional, small italic text under the image):** none needed for A or B. For C, if used: "Every Saturday, rain or shine."

---

## 2. Texture / absorption close-up (`texture_image`)

**Placement:** bottom of the "Water sits on top. Skin lets fat in." mechanism section, directly under the diagram and the "Not a better cream. A different category." line.
**Purpose:** visual proof of the specific claim made two lines above it (absorbs in, no residue, still there at 2pm). This is a proof shot, not a beauty shot.

**Prompt:**
An ultra-realistic macro/close-up photo of a hand's fingertip pressing a small amount of whipped cream-colored balm into the back of the opposite hand or forearm, mid-absorption, some residue still visible catching the light, some already sunk in. Natural window light, neutral kitchen or bathroom counter blurred in the background, no styled props. Real skin texture, no retouching, no manicure, no jewelry. Shot like a quick phone photo taken to show a friend "look, it actually soaks in," not a commercial product shot. No text, no logos, no product packaging in frame (the jar shouldn't be visible here, this is purely a skin/texture proof shot). 4:5 or 1:1 aspect ratio, tight crop.

---

## Notes
- Both settings are optional (`{%- if ... != blank -%}`), the page degrades gracefully with either or both left empty, no broken layout.
- Once generated, upload via the theme customizer under this section's "Extra photos" settings group, no code changes needed after that.
- If real customer UGC becomes available later (see review-flow status in `tallow-cream/offers/`), swap the lifestyle photo for a real one first, that's a stronger trust move than any generated image once it exists.
