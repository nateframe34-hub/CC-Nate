# Listicle B Image Prompts — B5: The Invisible Woman

> **Listicle:** "Why Everything the Wellness Industry Sold You Didn't Work"
> **Batch:** 5 (Specific Pain Point — Invisible Woman)
> **Tool:** Nano Banana Pro (Google Gemini). Also compatible with GPT Image, Midjourney, DALL-E 3, Flux.
> **Critical rule:** These images must feel editorial and slightly confrontational — matching the listicle's angry, frustrated tone. Not aspirational. Not pretty. Real, messy, honest.

---

## Image 1: The Failed Products (Hero Image)

**Placement:** Top of article, below the headline and opening list of products that didn't work.

**Purpose:** Visual proof of the opening paragraph. The reader sees the exact products she's tried — collagen, jade roller, serums — and recognizes her own bathroom cabinet. The image says "I know exactly where you've been" before the copy explains why.

**Prompt:**

```
A photorealistic overhead photograph of a bathroom vanity counter with wellness and beauty products scattered in a frustrated, disorganized arrangement. Visible items: an open jar of collagen powder with a scoop sticking out, a jade roller lying on its side, a tall amber bottle of evening primrose oil, an expensive-looking face serum with a gold dropper cap, a bottle of ashwagandha with the cap half-off, a packet of adaptogenic powder mix torn open, a magnesium bottle, and a small tin of vitamin D gummies with a few spilling out. The counter is white or light marble, but not clean — there's a slight ring of powder residue around the collagen jar, a few drops of serum on the counter, and a used cotton pad nearby. The arrangement looks like someone swept everything to one side of the counter in frustration. Bathroom lighting — slightly cool, overhead, unflattering. No people visible. The mood is: this is what $400 of false promises looks like. Smartphone camera quality, shot from directly above, natural color temperature. 4:5 aspect ratio.
```

**Post-production notes:**
- This is the complement to B5C2's ad creative (supplement graveyard). Same concept, slightly different products (more beauty/wellness focused for the Invisible Woman — jade roller, serum, collagen — vs the general supplement bottles in the ad).
- None of these should look like Baseline or NMN. These are the things she tried BEFORE.
- If any AI-generated labels reference real brands, blur them in post.

---

## Image 2: The Doctor's Office (Dismissal Moment)

**Placement:** Inside "What's Actually Happening After 40" section, after the mention of the doctor saying "fine for your age."

**Purpose:** Puts the reader in the exam room. She's been there. She's heard those words. The image triggers the memory and the frustration — then the copy explains what the doctor missed.

**Prompt:**

```
A photorealistic photograph from a patient's perspective sitting on a medical exam table. The shot looks down at the photographer's own knees and lower legs, wearing dark pants and casual shoes, dangling off the edge of a medical exam table covered in crinkled white paper. In the slightly blurred background: a wall-mounted blood pressure cuff, a computer monitor on a counter showing what appears to be lab results, a jar of tongue depressors, a hand sanitizer dispenser, a rolling stool pushed to the side. The lighting is flat, cool fluorescent — standard medical office. No doctor visible. No other people. The mood is solitary and slightly defeated — the moment after being told "everything looks normal" when nothing feels normal. Smartphone camera quality, shot from eye level looking down, cool color temperature, slight grain. 4:5 aspect ratio.
```

**Post-production notes:**
- This image is similar to B5C3's ad creative (doctor's office POV) but without any text overlay. Pure editorial use.
- The emptiness of the room IS the message — she's alone with a diagnosis that doesn't match her experience.
- Do NOT add any branding or text to this image.

---

## Image 3: NAD+ Decline Graph

**Placement:** Inside "What's Actually Happening After 40" section, after the NAD+ mechanism explanation.

**Purpose:** Makes the invisible visible. The graph transforms "NAD+ declines after 40" from a claim into a visual fact. The dual-timeline message (NAD+ decline separate from hormonal changes) lands harder with a visual.

**Build method:** Canva — same graph style as B4's listicle but with an added visual element.

**Canva specs:**
- **Size:** 1080×720 (3:2) or 16:9
- **Background:** White with subtle gray gridlines
- **Graph:** Single smooth curve in deep teal (#0c3b3f) showing NAD+ decline from age 20-70
- **Addition (unique to B5):** A second subtle dotted line in muted rose (#C4848A) labeled "Hormonal changes" showing a different decline pattern (steeper drop 45-55). Small annotation: "Both are real. Both affect how you feel. Only one gets talked about."
- **Typography:** Plus Jakarta Sans, clean, minimal
- **Bottom:** "Based on published research. Illustration simplified for clarity." in 10pt gray

**Post-production notes:**
- The dual-line graph is the visual version of the listicle's core message: NAD+ decline and hormonal changes are SEPARATE timelines. This is what makes the Invisible Woman's experience make sense — something ELSE is happening that nobody mentioned.
- Keep it clean and editorial. No branding.

---

## Image 4: One Bottle (Product Section)

**Placement:** At the bottom, inside "One Formula That Replaces the Entire Shelf" section, above the CTA.

**Purpose:** The visual payoff. After an article full of failed products and frustration, the reader sees ONE clean bottle. The contrast with Image 1 (cluttered counter of failures) is the message: simplicity after chaos.

**Prompt:**

```
A photorealistic photograph of a single white supplement bottle with subtle purple/violet label accents standing alone on a clean bathroom counter. The counter is the same white or light marble surface as Image 1, but now it's completely clear — no other products, no mess, no residue. Just the one bottle, a glass of water, and two small white capsules placed casually beside it. Soft natural morning light from a window to the left, warm and clean. The mood is the opposite of Image 1: calm, simple, resolved. The bottle is not centered perfectly — it sits slightly to the right, casually placed, as if someone just set it down after taking their morning dose. Shallow depth of field with the bottle sharp and the background (a clean mirror, a small plant) softly blurred. 4:5 aspect ratio.
```

**Post-production notes:**
- This image only works in CONTRAST with Image 1. The same counter, cleaned off, with one bottle replacing the chaos. If you don't use Image 1, this image loses its power.
- The bottle should be recognizable as Baseline but the label doesn't need to be perfectly readable. White bottle + purple accent is enough.
- Add a small caption below: "One bottle. 10 ingredients. 60-day supply." in small gray text.

---

## Image Priority

1. **Failed Products (hero)** — highest impact, instant recognition, sets the confrontational tone
2. **NAD+ Decline Graph (dual-line)** — the Invisible Woman's "aha" moment. Build in Canva.
3. **Doctor's Office** — emotional trigger, secondary but powerful
4. **One Bottle** — product payoff. Only impactful if Image 1 is used (contrast effect).

---

## Usage in Shopify HTML

```html
<!-- Image 1: Failed products — below intro -->
<div style="margin: 30px 0; text-align: center;">
  <img src="YOUR_SHOPIFY_FILE_URL_HERE" alt="Bathroom counter cluttered with supplements and wellness products that didn't work" style="max-width: 100%; border-radius: 8px;">
</div>

<!-- Image 2: Doctor's office — inside mechanism section -->
<div style="margin: 30px 0; text-align: center;">
  <img src="YOUR_SHOPIFY_FILE_URL_HERE" alt="Sitting alone in a doctor's exam room" style="max-width: 100%; border-radius: 8px;">
</div>

<!-- Image 3: NAD+ dual-line graph — inside mechanism section -->
<div style="margin: 20px 0;">
  <img src="YOUR_SHOPIFY_FILE_URL_HERE" alt="Graph showing NAD+ decline and hormonal changes on separate timelines" style="max-width: 100%; border-radius: 4px;">
  <p style="font-size: 12px; color: #999; margin-top: 6px;">Based on published research. Illustration simplified for clarity.</p>
</div>

<!-- Image 4: One bottle — above CTA -->
<div style="margin: 30px 0; text-align: center;">
  <img src="YOUR_SHOPIFY_FILE_URL_HERE" alt="One bottle on a clean counter" style="max-width: 100%; border-radius: 8px;">
  <p style="font-size: 13px; color: #999; margin-top: 8px;">One bottle. 10 ingredients. 60-day supply.</p>
</div>
```

Replace `YOUR_SHOPIFY_FILE_URL_HERE` with the actual file URL from Shopify's file manager after uploading.
