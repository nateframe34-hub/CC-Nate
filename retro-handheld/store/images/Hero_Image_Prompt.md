# PocketArcade: PDP Hero Image Prompt (one template, every color)

**Written 2026-11-02**, using the competitor's PDP (RetroSnap) as reference.
**What we keep from the comp:** a cozy Christmas living room, a warm bokeh tree, falling snow, a hand holding the unit up with a bright game title on screen, and a gift object on the left.
**What we change:** they have a branded retail box next to the unit. **We have no branded box**, so the left side is a **wrapped present with its paper half torn open**. The gift reads as "this is what's inside", with no packaging to fake.

**How to use:** upload a real photo of that color as the product reference (front view, screen on), paste the prompt, and swap the two `{…}` fields. Keep everything else word for word so every color comes out as a matching set.

---

## The prompt (Nano Banana Pro)

```
Create a photorealistic, high-end product lifestyle photo for an online store.
Use the attached reference photo as the exact product. PRODUCT LOCK: reproduce the
handheld exactly as in the reference: same shape, proportions, button layout,
colors and finish. Do not redesign it.

THE PRODUCT: a vertical retro handheld game console, about the size of a phone
but thicker, in {COLOR DESCRIPTION}. Layout from top to bottom: a 3.5-inch
bright color screen in a black bezel at the top; below it a D-pad on the left,
four round A/B/X/Y face buttons on the right, a small speaker grille and
start/select buttons in the middle; two small analog thumbsticks at the bottom
corners; shoulder buttons on the top edge. Upright, portrait orientation,
screen facing the camera. Never rotated sideways, never a phone, never a
console with a cartridge slot on the front.

THE SCREEN: switched on and glowing, showing the colorful title screen of
{GAME ON SCREEN}, crisp and readable, slightly brighter than the room.

COMPOSITION: a woman's hand with a natural, light manicure enters from the
right and holds the handheld up at chest height, slightly angled toward the
camera, filling the right 45% of the frame. On the left, resting on soft white
faux snow, a gift box wrapped in glossy red paper with a gold satin ribbon,
the paper half torn open at the front as if just unwrapped, a few scraps of
paper on the snow. No logos or printing on the gift box.

SETTING: a cozy living room on Christmas morning. Behind, out of focus: a
decorated Christmas tree with warm white fairy lights forming large round
bokeh, a red stocking hanging on a fireplace mantel, warm amber light. Gentle
falling snowflakes drift across the foreground, softly blurred.

CAMERA: shot on a full-frame camera with an 85mm lens at f/2. Sharp focus on
the handheld and the screen, background melted into soft bokeh. Warm white
balance, soft natural highlights on the plastic, true-to-life colors of the
product. Clean, premium, festive, inviting. No text, no captions, no badges,
no price tags, no added graphics or overlays, no watermarks.

Aspect ratio 1:1, 2048 x 2048.
```

---

## Per-color fill-ins

Fill `{COLOR DESCRIPTION}` from the real unit. Use the same game for every color so the set matches, or a different game per color for variety (founder's choice).

| Color (Shopify variant) | `{COLOR DESCRIPTION}` | `{GAME ON SCREEN}` |
|---|---|---|
| Transparent purple | translucent see-through purple plastic showing the circuit board inside, black D-pad and sticks, colored A/B/X/Y buttons | Pokemon FireRed |
| Transparent teal | translucent see-through teal-green plastic showing the circuit board inside, black D-pad and sticks, colored A/B/X/Y buttons | Crash Bandicoot |
| Black | solid matte black plastic, black buttons with colored A/B/X/Y lettering | Super Mario World |
| White | solid glossy white plastic, grey D-pad, colored A/B/X/Y buttons | Kirby's Adventure |
| Pink | solid pastel pink plastic, pink buttons, white sticks | Kirby |
| _(add each color you stock)_ | _(describe exactly what the real unit looks like)_ | |

## Extra gallery shots (same scene, one change each)
1. **Hero:** the prompt above.
2. **Pair shot (for the duo):** "two handhelds, {COLOR A} and {COLOR B}, held side by side by two hands" in the same scene.
3. **Stocking shot:** the handheld peeking out of the red stocking on the mantel, screen on.
4. **Under the tree:** the handheld on top of wrapped presents under the tree, screen on, no hand.
5. **Case shot:** the handheld next to its silicone case on the snow (for the case upsell and the bundles).

## Checklist before using an image
- [ ] Button layout matches the real unit (count the face buttons and the sticks)
- [ ] Portrait orientation, not sideways
- [ ] Color matches the real variant. Customers will compare it to what arrives
- [ ] Screen readable and lit
- [ ] No fake box, logo, text or price added

---

## Color-swap prompt (founder workflow, 2026-11-02)
Make the first hero with the full prompt above. After that, for each color, attach **Image 1 = the finished hero** and **Image 2 = a real photo of the color**, and use:

```
Recreate Image 1 exactly: same scene, Christmas background, snow, lighting,
camera angle, crop, hand pose, gift box and game on the screen. Change ONLY the
handheld's body and button colors to match the handheld in Image 2 exactly:
same plastic color, transparency or finish, and the same button and thumbstick
colors. Keep the handheld's shape, size, position and button layout identical
to Image 1. Do not change anything else. No added text or graphics.
Aspect ratio 1:1, 2048 x 2048.
```

If it drifts (new pose, a different background), regenerate rather than edit. If the color comes out wrong, add one line describing it, e.g. "The body is translucent purple, see-through, showing the circuit board inside."

---

## Silicone case image (2026-11-02)
**Used in:** the drawer upsell (shown at 40px, so it must read at a glance), the "Free with your bundle" box, and the case product page.
**Reference:** the supplier's flat-lay (front, back, sides, lanyard), one per color.

### Master case image: attach Image 1 = our handheld hero (any color), Image 2 = the case reference in BLACK
```
Create a photorealistic product photo for an online store.
Image 1 shows our handheld game console. Image 2 shows the silicone case made
for it, laid out flat (front, back, side pieces and a wrist lanyard).

Show ONE handheld from Image 1 fully fitted INSIDE the silicone case from
Image 2, as if the case is snapped on: soft matte silicone hugging the edges
and back, every cut-out in the case lining up exactly with the screen,
D-pad, buttons and thumbsticks, exactly as in Image 2. Reproduce the case's
shape, thickness, cut-outs and texture exactly. Do not invent a different case.
The braided wrist lanyard from Image 2 is attached at the bottom corner and
lies in a loose curve beside it.

The handheld is upright, portrait orientation, front facing the camera,
slightly angled, screen on and showing the same game as Image 1.

Setting: resting on soft white faux snow, with the same warm Christmas
living-room bokeh as Image 1 (tree lights, warm amber glow) behind, gently
blurred. The handheld in its case fills about 60% of the frame and is
centered, so it reads clearly even as a small thumbnail.

Soft, even light that shows the silicone's matte texture; true-to-life case
color. No text, no labels, no "Black" heading, no badges, no extra parts
floating around, no hands.
Aspect ratio 1:1, 2048 x 2048.
```

### Color swap for each case color: Image 1 = the finished master case image, Image 2 = that color's case reference
```
Recreate Image 1 exactly: same handheld, same pose, same snow, background,
lighting, crop and lanyard. Change ONLY the silicone case color to match the
case in Image 2 exactly (same color, same matte finish). Keep the handheld
itself and everything else identical. No added text.
Aspect ratio 1:1, 2048 x 2048.
```

**Tips**
- Keep the handheld the same color in every case image (e.g. white or translucent purple) so the case color is the only thing that changes.
- If the model puts the handheld *next to* the case instead of *inside* it, add: "The handheld is wearing the case; the case is not empty."
- The supplier's flat-lay is still useful as a 2nd image on the case product page (it shows the lanyard and what's included).
