# Advertorial V1 — Image Generation Prompts (Nano Banana Pro)

> **Advertorial:** "The Thing Nobody Told Me About Energy After 40"
> **Batch:** 1 (Reluctant Decliner)
> **Tool:** Nano Banana Pro (Google Gemini). Also compatible with GPT Image, Midjourney, DALL-E 3, Flux.
> **Critical rule:** These images must look editorial, not commercial. No product-forward shots. No studio lighting. No marketing polish. Every image should look like something a real health writer would use in a real article.

---

## Image 1: Sarah's Author Photo

**Placement:** Below the intro paragraph, after "the thing that actually explained what was happening."

**Purpose:** Puts a face to the voice. Builds immediate trust. This is the most important image — people read articles from people, not from logos.

**Prompt:**

```
Candid portrait photo of a woman, age 44, sitting at a light wood kitchen table in natural morning light. She has warm brown hair, pulled back loosely, wearing a simple cream linen top. She's looking slightly off-camera with a calm, thoughtful, approachable expression — not smiling big, not serious, just present. One hand loosely wrapped around a ceramic coffee mug. The kitchen behind her is real and lived-in — a few items on the counter, a small plant, natural light from a window. No makeup-ad perfection — she looks like a real person, a mom, someone you'd trust. Warm natural color palette: cream, soft wood tones, muted sage green. Shot with natural window light, no flash, no studio setup. Editorial portrait style, like a health magazine profile photo. 35mm lens, f/2.0, shallow depth of field with background softly blurred, ultra-realistic, 4:5 aspect ratio, 8K resolution.
```

**Post-production notes:**
- This is Sarah Lawson. She should look like a real health practitioner and mom in Austin — warm, grounded, intelligent. Not an influencer. Not a stock photo model.
- If the AI gives you someone too polished or too "wellness influencer," regenerate. She should look like someone you'd meet at school pickup.
- Add a subtle caption below: "Sarah Lawson, Functional Health Practitioner" in small gray text.

---

## Image 2: NAD+ Decline Graph

**Placement:** Inside the ~50% stat callout box, replacing or accompanying the stat number.

**Purpose:** Makes the science visual. The 50% decline stat is the "I didn't know that" moment — a graph makes it land harder and feel more credible than text alone.

**Prompt:**

```
Clean, minimal scientific infographic showing NAD+ decline with age. A simple line graph on a white background with subtle grid lines. The x-axis shows age from 20 to 70 in decade intervals. The y-axis shows "Relative NAD+ Levels" from 0% to 100%. A single smooth curve starts high at age 20-30 (near 100%), holds relatively steady until about age 35, then begins a clear downward trajectory, declining steeply through ages 40-60, ending near 50% by age 60. The curve is drawn in a deep purple/violet color (#5b4a8a). A subtle shaded area under the curve in light lavender (#f0edf5). Small text annotation at age 40 with a dotted vertical line: "Decline accelerates here." Clean sans-serif typography. No clutter, no 3D effects, no gradients on the background. The style of a research paper figure or a high-quality health journalism graphic — informative, not flashy. Flat design, vector-style, 16:9 aspect ratio.
```

**Post-production notes:**
- AI models struggle with precise graph rendering. Best approach: use this prompt to generate the overall aesthetic, then recreate in Canva or Figma with exact data points.
- Keep it dead simple. One line, one color, one annotation. The simpler it is, the more credible it looks.
- Add small source text at bottom: "Based on published NAD+ research. Illustration simplified for clarity."
- Do NOT add a Baseline logo or any branding to this image. It should look like editorial content.

---

## Image 3: Casual Morning Counter (Product Incidental)

**Placement:** In the "What I actually take now" section, after "Two capsules with my morning coffee."

**Purpose:** Shows the product in context without making it the subject. The lesson from B1C2's feedback loop: the product must be incidental, one item among many in a real-life scene. This image should feel like Sarah snapped a photo of her morning counter — not a product photo.

**Prompt:**

```
Ultra-realistic overhead POV photograph of a lived-in kitchen countertop in warm morning light. The scene is a real morning — slightly messy, human, authentic. Items scattered naturally across a light granite or quartz counter: a half-drunk ceramic coffee mug with steam visible, an open laptop showing a blurred article, a pair of reading glasses folded beside a small stack of papers, a set of car keys, a small potted succulent, a phone face-down, and among all of this — partially obscured by the laptop — a white supplement bottle with subtle purple label accents. The bottle is NOT centered, NOT the focal point. It is one item among many, pushed slightly to the side as if it was just used and set down. Two small white capsules sit on the counter near the coffee mug, casually placed, not arranged. The entire scene is bathed in warm golden morning window light from the left side. The composition feels accidental — like someone looked down at their counter and snapped a photo. Color palette: warm whites, natural wood, cream, soft green from the succulent, muted purple from the bottle label barely visible. No studio lighting. No artificial arrangement. Shot from directly above (flat lay) with a slight casual angle. iPhone-quality aesthetic, not commercial. 35mm lens, f/4, everything in focus, ultra-realistic, 4:5 aspect ratio, 8K resolution.
```

**Post-production notes:**
- **Critical:** The supplement bottle must NOT be the visual focus. If the AI centers it or makes it prominent, regenerate or crop/reposition in post.
- The bottle should be partially hidden — behind the laptop, next to the keys, not front and center. If someone glanced at this image, they should see "a morning counter" not "a supplement ad."
- The two loose capsules near the coffee mug tell the story without the bottle needing to be visible. That's the subtle detail that works.
- This image directly applies the lesson from the B1C2 187Days feedback loop — product visible but incidental, not the subject.
- Do NOT add any text overlays or branding.

---

## Usage in Shopify HTML

To add these images to the advertorial, upload them to Shopify (Settings → Files → Upload files) and insert them into the HTML at the specified placement points using:

```html
<!-- Image 1: Sarah's author photo — after intro -->
<div style="margin: 30px 0; text-align: center;">
  <img src="YOUR_SHOPIFY_FILE_URL_HERE" alt="Sarah Lawson, Functional Health Practitioner" style="max-width: 100%; border-radius: 8px;">
  <p style="font-size: 13px; color: #999; margin-top: 8px;">Sarah Lawson, Functional Health Practitioner</p>
</div>

<!-- Image 2: NAD+ decline graph — inside stat callout box -->
<div style="margin: 20px 0;">
  <img src="YOUR_SHOPIFY_FILE_URL_HERE" alt="Graph showing NAD+ decline with age" style="max-width: 100%; border-radius: 4px;">
  <p style="font-size: 12px; color: #999; margin-top: 6px;">Based on published NAD+ research. Illustration simplified for clarity.</p>
</div>

<!-- Image 3: Morning counter — in "What I actually take" section -->
<div style="margin: 30px 0;">
  <img src="YOUR_SHOPIFY_FILE_URL_HERE" alt="Morning routine" style="max-width: 100%; border-radius: 8px;">
</div>
```

Replace `YOUR_SHOPIFY_FILE_URL_HERE` with the actual file URL from Shopify's file manager after uploading.

---

## Image Priority

If you're generating in order of importance:

1. **Sarah's author photo** — highest impact on trust and readability
2. **NAD+ decline graph** — makes the science tangible, could build in Canva faster than generating
3. **Morning counter** — nice to have but the advertorial works without it. Only add if the image genuinely looks incidental and casual. If it looks like a product photo at all, skip it.
