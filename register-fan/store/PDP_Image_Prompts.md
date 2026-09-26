# PDP Image Prompts — Nano Banana Pro 2 · ONE-PASS FULL SPEC

**Rebuilt 2026-09-26** to the same standard as the B1C2 ad prompt: every prompt is **self-contained and one-pass**. Attach the reference, paste the whole box, done. No edits, no compositing.

For `theme/sections/evenroom-pdp-sa1.liquid`.

## How to use

- **REF-1** = the supplied product photo (white unit on white, with remote). **Crop the remote out** before attaching for every image except 1f.
- The product description is **written into every prompt in full** so it survives the model ignoring the photo.
- **The display always reads 72°F** (summer). The cold versions use 70°F.
- **Every in-room image uses the same room** (walls `#D9D2C5`, white baseboards, beige carpet `#C9B9A0`) so the gallery reads as one house.
- Real prop branding (tape measure, screwdriver, laptop) stays. Never write "unbranded".
- **It's a floor register.** In a room it sits in the floor, never the wall.

### Gallery order and generation priority

| Slot | Image | Priority |
|---|---|---|
| Gallery 1 | **1c — installed in the floor** | Generate first |
| Gallery 2 | 1a — on white | First |
| Gallery 3 | 1f — what's in the box (unit + remote) | Second |
| Gallery 4 | 1b — display close-up | Second |
| Gallery 5 | 1e — bronze *(only if stocked)* | If needed |
| §5b `out_image` | 5b — the result: that room at 4pm | **First** |
| §7 `fit_image` | 7 — measuring the opening | **First** |
| §8 | 8.1–8.3 — install steps | Optional |

⚠️ **Verify with the supplier:** where the power cord leaves the unit. The prompts assume it runs from beneath the right-hand end of the flange. Change that line if the real unit differs.

---

## 1c. Installed in the floor ⭐ gallery image 1

**Attach:** REF-1 (remote cropped out)

```
Create ONE photograph: a candid, realistic phone photo of the vent cover described
below, installed in the carpeted floor of an ordinary North American home, exactly where
an old floor register used to be. This is the first image on the product page. It must
answer "what will this look like in my house?" at a glance.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. THE ROOM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Walls: flat warm greige paint (#D9D2C5), a couple of faint scuffs.
- Baseboards: white painted MDF (#F2F0EB), about 3.5 inches tall, a thin dust line on
  the top edge.
- Floor: beige low-pile wall-to-wall carpet (#C9B9A0) with visible vacuum tracks.
- Outlets: standard white US duplex outlets in white plates.
- The vent sits in the carpet about 8 inches out from the baseboard of the wall, running
  parallel to it. The carpet is cut and tucked neatly around the vent's flange; the rim
  sits just proud of the carpet pile.
- In frame behind it: the bottom 30% of the wall, the baseboard, and one outlet on the
  baseboard about 18 inches to the right of the vent.
- At the right edge of the frame, one metal leg of a white desk and one black caster
  wheel of an office chair on the carpet — just enough to read as a lived-in office.
  Nothing else in the room is visible.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. THE PRODUCT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Use the attached reference image ONLY for the product's exact appearance.
Do NOT include the remote control from the reference. Do not copy the reference's layout
or background.

THE PRODUCT (match the reference exactly):
- A flat rectangular floor vent cover (register) with two built-in fans. About 2.4 times
  as wide as it is tall. One piece of moulded plastic with a thin raised rim and softly
  rounded outer corners. FINISH: matte bright-white moulded plastic (#F4F4F2), clean and even.
- LEFT about 70% of the face: a rectangular grille opening with rounded inner corners,
  crossed by 18 thin, evenly spaced VERTICAL bars running top to bottom (NOT horizontal
  louvres). Behind the bars, two identical round fans side by side, each with a dark
  charcoal-grey circular shroud and a black five-blade impeller with broad curved blades
  and a small round hub.
- RIGHT about 25% of the face: a vertical glossy black display panel, taller than wide.
  Top: two small white icons with tiny labels. Middle: a large white seven-segment
  digital readout showing exactly "72" followed by a small, clearly formed "°F".
  Bottom: four small white icons in a 2 x 2 grid (flame, snowflake, fan, crescent moon)
  with tiny labels.
- Right of the display: two narrow vertical strips of small square black buttons with
  white symbols — upper strip of three (power at top), lower strip of three (mode, "+",
  "−").
- One round countersunk screw hole at each short end, centred vertically: left of the
  grille, right of the buttons.
- No logo, no brand name, no other text on the product. Exactly two fans.
- THE DISPLAY READS "72°F". Never "188", never garbled, never a stray superscript.
- The vent is ON: the display is lit and reads "72°F".
- A thin white power cord emerges from beneath the right-hand end of the flange, runs
  across the carpet to the baseboard, then along it to the outlet, and is plugged in.
  It lies naturally — a gentle curve, not taped down, not hidden, not perfectly straight.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. CAMERA AND COMPOSITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Shot as if someone crouched in the room and took a phone photo looking down at it:
  camera about 3 feet off the floor, 3 feet back, angled down about 45 degrees.
- ~26 mm equivalent lens, f/1.8. The vent in the middle third of the frame, slightly
  left of centre, about 55% of the frame width, the whole faceplate visible with the
  display end nearer the camera. The display "72°F" is sharp and legible.
- Horizon (baseboard line) very slightly tilted, about 1 degree.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. LIGHT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Ordinary afternoon daylight from a window out of frame to the left, soft and slightly
  warm (about 5000 K), a gentle falloff across the carpet and wall. The display glows
  softly. No flash, no studio lighting.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5. RENDERING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Realistic phone-camera quality (like an iPhone main camera): mild luminance grain in
shadows, natural slightly warm white balance, very slight lens distortion at the edges.
No HDR look, no cinematic grade, no vignette, no bokeh balls, no lens flare.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6. DO NOT INCLUDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- People, hands, pets, plants, fans, space heaters, an old register lying around.
- The remote.
- The vent in the wall. It is IN THE FLOOR.
- Air-flow swirls, wind lines, leaves, snowflakes, sparkles, glow or any effect showing
  air or temperature. Any text, caption, logo, watermark, price, badge, sticker, arrow,
  border or frame added to the image.
- Any logo or text on the product that isn't described above. Horizontal slats, more or
  fewer than two fans, the display on the left side, a product colour other than the one
  specified.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
9. FINAL CHECK BEFORE OUTPUT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
The vent is in the carpeted floor, white, vertical bars, two fans, display on the right reading "72°F". The cord runs visibly to a plugged-in outlet. No people, no remote, no effects, no text.

Aspect ratio 1:1, 1400 x 1400.
```

**If it misses (re-run, don't edit):**

| Miss | Add to the end and re-run |
|---|---|
| Display shows 188 / garbled °F | *"The display digits are the most important detail: exactly 72 then a clean °F, large and legible."* |
| Horizontal slats / wrong fan count | *"Copy the grille from the reference exactly: vertical bars, two fans."* |
| Remote appears when it shouldn't | *"Crop the remote out of the reference before attaching, then re-run."* |
| Vent appears in the wall | *"The vent is set flush into the carpeted floor, 8 inches out from the baseboard, viewed from above."* |

---

## 1a. Product on white · gallery 2

**Attach:** REF-1 (remote cropped out)

```
Create ONE clean e-commerce main product image: the vent cover described below, alone,
on a pure white background, photographed like a professional Amazon main image.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. BACKGROUND
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Pure seamless white (#FFFFFF) edge to edge. No horizon line, no gradient, no texture,
  no props, no text.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. THE PRODUCT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Use the attached reference image ONLY for the product's exact appearance.
Do NOT include the remote control from the reference. Do not copy the reference's layout
or background.

THE PRODUCT (match the reference exactly):
- A flat rectangular floor vent cover (register) with two built-in fans. About 2.4 times
  as wide as it is tall. One piece of moulded plastic with a thin raised rim and softly
  rounded outer corners. FINISH: matte bright-white moulded plastic (#F4F4F2), clean and even.
- LEFT about 70% of the face: a rectangular grille opening with rounded inner corners,
  crossed by 18 thin, evenly spaced VERTICAL bars running top to bottom (NOT horizontal
  louvres). Behind the bars, two identical round fans side by side, each with a dark
  charcoal-grey circular shroud and a black five-blade impeller with broad curved blades
  and a small round hub.
- RIGHT about 25% of the face: a vertical glossy black display panel, taller than wide.
  Top: two small white icons with tiny labels. Middle: a large white seven-segment
  digital readout showing exactly "72" followed by a small, clearly formed "°F".
  Bottom: four small white icons in a 2 x 2 grid (flame, snowflake, fan, crescent moon)
  with tiny labels.
- Right of the display: two narrow vertical strips of small square black buttons with
  white symbols — upper strip of three (power at top), lower strip of three (mode, "+",
  "−").
- One round countersunk screw hole at each short end, centred vertically: left of the
  grille, right of the buttons.
- No logo, no brand name, no other text on the product. Exactly two fans.
- THE DISPLAY READS "72°F". Never "188", never garbled, never a stray superscript.
- The display is lit and reads "72°F".

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. ANGLE, SIZE, POSITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Seen from the front and slightly above: turned about 15 degrees to the left (display
  end nearer the camera) and tilted back about 20 degrees, as if lying on a white table
  photographed from a low front angle. The whole faceplate visible: every vertical bar,
  both fans, the full display. A thin sliver of the housing depth shows along the
  bottom edge and the right end.
- Centred, filling about 80% of the frame width, even white space all round.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. LIGHT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Bright, soft, even studio light from above and front-left (large softbox, 5500 K),
  white fill from the right. The white plastic crisp, gentle grey shading on the rim and
  inside the grille, fans dark behind the white bars, the black display glossy with one
  soft highlight that does not touch the digits.
- A faint mirror reflection beneath the product, about 15% opacity, fading within
  about 50 px. A soft grey contact shadow where it meets the surface.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5. RENDERING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Tack sharp everywhere (90 mm lens, f/11). Realistic matte plastic with fine moulding
  texture and seams. Not a cartoon, not a glossy 3D render, not toy-like.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6. DO NOT INCLUDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- The remote, hands, props, any background other than white.
- Air-flow swirls, wind lines, leaves, snowflakes, sparkles, glow or any effect showing
  air or temperature. Any text, caption, logo, watermark, price, badge, sticker, arrow,
  border or frame added to the image.
- Any logo or text on the product that isn't described above. Horizontal slats, more or
  fewer than two fans, the display on the left side, a product colour other than the one
  specified.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
9. FINAL CHECK BEFORE OUTPUT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pure white background. One white vent cover, vertical bars, two fans, display on the right reading "72°F". No remote, no text, no effects.

Aspect ratio 1:1, 1400 x 1400.
```

**If it misses (re-run, don't edit):**

| Miss | Add to the end and re-run |
|---|---|
| Display shows 188 / garbled °F | *"The display digits are the most important detail: exactly 72 then a clean °F, large and legible."* |
| Horizontal slats / wrong fan count | *"Copy the grille from the reference exactly: vertical bars, two fans."* |
| Remote appears when it shouldn't | *"Crop the remote out of the reference before attaching, then re-run."* |

---

## 1f. What's in the box · gallery 3

**Attach:** REF-1 **with the remote left in**

```
Create ONE clean e-commerce product image showing everything the customer receives:
the vent cover and its remote, together on a pure white background.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. BACKGROUND
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Pure seamless white (#FFFFFF) edge to edge. No text, no props, no packaging.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. THE PRODUCTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Use the attached reference image ONLY for the product's exact appearance.
Include the remote exactly as described below. Do not copy the reference's layout
or background.

THE PRODUCT (match the reference exactly):
- A flat rectangular floor vent cover (register) with two built-in fans. About 2.4 times
  as wide as it is tall. One piece of moulded plastic with a thin raised rim and softly
  rounded outer corners. FINISH: matte bright-white moulded plastic (#F4F4F2), clean and even.
- LEFT about 70% of the face: a rectangular grille opening with rounded inner corners,
  crossed by 18 thin, evenly spaced VERTICAL bars running top to bottom (NOT horizontal
  louvres). Behind the bars, two identical round fans side by side, each with a dark
  charcoal-grey circular shroud and a black five-blade impeller with broad curved blades
  and a small round hub.
- RIGHT about 25% of the face: a vertical glossy black display panel, taller than wide.
  Top: two small white icons with tiny labels. Middle: a large white seven-segment
  digital readout showing exactly "72" followed by a small, clearly formed "°F".
  Bottom: four small white icons in a 2 x 2 grid (flame, snowflake, fan, crescent moon)
  with tiny labels.
- Right of the display: two narrow vertical strips of small square black buttons with
  white symbols — upper strip of three (power at top), lower strip of three (mode, "+",
  "−").
- One round countersunk screw hole at each short end, centred vertically: left of the
  grille, right of the buttons.
- No logo, no brand name, no other text on the product. Exactly two fans.
- THE DISPLAY READS "72°F". Never "188", never garbled, never a stray superscript.
- THE REMOTE (include it, beside the vent): a slim, light-grey (#D9DADB) rounded-
  rectangle remote about as long as the vent is tall-and-a-half, matte plastic. Top
  left: a red power symbol with "ON/OFF" beneath. Top right: a bulb icon, "LIGHT". Centre:
  a tall pill-shaped rocker with "+" above and "−" below and "TEMP" beside it. Left and
  right of the rocker: a padlock icon ("LOCK") and a signal-bars icon ("WIND"). Lower
  rows: flame ("WINTER"), leaf ("IONIZER"), snowflake ("SUMMER"), then fan ("FAN") and
  crescent moon ("SLEEP"). Icons dark grey, labels tiny.
- The vent's display is lit and reads "72°F".

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. ARRANGEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- The vent lies flat, seen from the front and slightly above (tilted back about 25
  degrees), occupying the left and centre of the frame, about 70% of the frame width,
  sitting slightly above the vertical centre.
- The remote lies flat in the lower right, angled about 15 degrees clockwise, its top
  end slightly overlapping the space below the vent's right end, NOT touching the vent.
  About 22% of the frame width. Its buttons and labels face the camera and are legible.
- Balanced white space around both.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. LIGHT AND RENDERING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Bright, soft, even studio light from above and front-left (5500 K). Soft grey contact
  shadows under both items. No reflections.
- Tack sharp, realistic matte plastics. Not a render.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6. DO NOT INCLUDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Hands, packaging, manuals, screws, cables, extra accessories not described.
- Air-flow swirls, wind lines, leaves, snowflakes, sparkles, glow or any effect showing
  air or temperature. Any text, caption, logo, watermark, price, badge, sticker, arrow,
  border or frame added to the image.
- Any logo or text on the product that isn't described above. Horizontal slats, more or
  fewer than two fans, the display on the left side, a product colour other than the one
  specified.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
9. FINAL CHECK BEFORE OUTPUT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Exactly two items: the white vent (display "72°F") and the light-grey remote. Pure white background. No text, no effects.

Aspect ratio 1:1, 1400 x 1400.
```

**If it misses (re-run, don't edit):**

| Miss | Add to the end and re-run |
|---|---|
| Display shows 188 / garbled °F | *"The display digits are the most important detail: exactly 72 then a clean °F, large and legible."* |
| Horizontal slats / wrong fan count | *"Copy the grille from the reference exactly: vertical bars, two fans."* |
| Remote missing or wrong shape | *"Include the light-grey remote from the reference in the lower right, buttons facing the camera."* |

---

## 1b. The display, close · gallery 4

**Attach:** REF-1 (remote cropped out)

```
Create ONE macro product photograph of the display and control end of the vent cover
described below, filling most of the frame. It shows the customer exactly how they set
the room's temperature.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. THE PRODUCT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Use the attached reference image ONLY for the product's exact appearance.
Do NOT include the remote control from the reference. Do not copy the reference's layout
or background.

THE PRODUCT (match the reference exactly):
- A flat rectangular floor vent cover (register) with two built-in fans. About 2.4 times
  as wide as it is tall. One piece of moulded plastic with a thin raised rim and softly
  rounded outer corners. FINISH: matte bright-white moulded plastic (#F4F4F2), clean and even.
- LEFT about 70% of the face: a rectangular grille opening with rounded inner corners,
  crossed by 18 thin, evenly spaced VERTICAL bars running top to bottom (NOT horizontal
  louvres). Behind the bars, two identical round fans side by side, each with a dark
  charcoal-grey circular shroud and a black five-blade impeller with broad curved blades
  and a small round hub.
- RIGHT about 25% of the face: a vertical glossy black display panel, taller than wide.
  Top: two small white icons with tiny labels. Middle: a large white seven-segment
  digital readout showing exactly "72" followed by a small, clearly formed "°F".
  Bottom: four small white icons in a 2 x 2 grid (flame, snowflake, fan, crescent moon)
  with tiny labels.
- Right of the display: two narrow vertical strips of small square black buttons with
  white symbols — upper strip of three (power at top), lower strip of three (mode, "+",
  "−").
- One round countersunk screw hole at each short end, centred vertically: left of the
  grille, right of the buttons.
- No logo, no brand name, no other text on the product. Exactly two fans.
- THE DISPLAY READS "72°F". Never "188", never garbled, never a stray superscript.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. FRAMING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Framed on the right-hand end of the vent: the black display panel fills the centre
  of the frame, about 45% of the frame height; the two button strips to its right are
  fully in frame; on the left edge, the last four or five white vertical grille bars and
  the edge of one fan, softly out of focus.
- Camera looking at the display almost straight on, rotated about 10 degrees, slightly
  above.
- The display lit, reading "72°F" in large white seven-segment digits, razor sharp. The
  four small icons (flame, snowflake, fan, moon) and the two top icons crisp enough to
  recognise.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. LIGHT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Soft, even, diffused daylight (5500 K) from the upper left. The display's glow visible
  but not blooming. One soft reflection on the glossy panel at the top edge, clear of
  the digits.
- Real-world touches: one or two tiny dust specks on the panel and a barely visible
  fingerprint smudge at its lower corner.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. RENDERING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- 100 mm macro, f/4: the display plane tack sharp, the grille falling off smoothly.
  Background behind the product: pure white (#FFFFFF), out of focus.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6. DO NOT INCLUDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Hands, the remote.
- Air-flow swirls, wind lines, leaves, snowflakes, sparkles, glow or any effect showing
  air or temperature. Any text, caption, logo, watermark, price, badge, sticker, arrow,
  border or frame added to the image.
- Any logo or text on the product that isn't described above. Horizontal slats, more or
  fewer than two fans, the display on the left side, a product colour other than the one
  specified.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
9. FINAL CHECK BEFORE OUTPUT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
The display fills the centre and reads "72°F" sharply; both button strips visible; white grille bars soft at the left edge. No text overlays, no effects.

Aspect ratio 1:1, 1400 x 1400.
```

**If it misses (re-run, don't edit):**

| Miss | Add to the end and re-run |
|---|---|
| Display shows 188 / garbled °F | *"The display digits are the most important detail: exactly 72 then a clean °F, large and legible."* |
| Horizontal slats / wrong fan count | *"Copy the grille from the reference exactly: vertical bars, two fans."* |

---

## 1e. Bronze · gallery 5 (only if bronze is stocked)

**Attach:** REF-1 (remote cropped out). The white in the reference is the wrong colour here; the prompt overrides it

```
Create ONE clean e-commerce main product image of the BRONZE version of the vent
cover described below, alone on a pure white background. The reference photo shows the
white version: copy only its shape and details, NOT its colour.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. BACKGROUND
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Pure seamless white (#FFFFFF). No props, no text.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. THE PRODUCT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Use the attached reference image ONLY for the product's exact appearance.
Do NOT include the remote control from the reference. Do not copy the reference's layout
or background.

THE PRODUCT (match the reference exactly):
- A flat rectangular floor vent cover (register) with two built-in fans. About 2.4 times
  as wide as it is tall. One piece of moulded plastic with a thin raised rim and softly
  rounded outer corners. FINISH: dark oil-rubbed bronze (#3B2F28): a deep brown-black with a faint warm metallic sheen, like a bronze door handle. NOT copper, NOT rose-gold, NOT pink, NOT shiny brass, NOT grey. The grille bars are the same bronze.
- LEFT about 70% of the face: a rectangular grille opening with rounded inner corners,
  crossed by 18 thin, evenly spaced VERTICAL bars running top to bottom (NOT horizontal
  louvres). Behind the bars, two identical round fans side by side, each with a dark
  charcoal-grey circular shroud and a black five-blade impeller with broad curved blades
  and a small round hub.
- RIGHT about 25% of the face: a vertical glossy black display panel, taller than wide.
  Top: two small white icons with tiny labels. Middle: a large white seven-segment
  digital readout showing exactly "72" followed by a small, clearly formed "°F".
  Bottom: four small white icons in a 2 x 2 grid (flame, snowflake, fan, crescent moon)
  with tiny labels.
- Right of the display: two narrow vertical strips of small square black buttons with
  white symbols — upper strip of three (power at top), lower strip of three (mode, "+",
  "−").
- One round countersunk screw hole at each short end, centred vertically: left of the
  grille, right of the buttons.
- No logo, no brand name, no other text on the product. Exactly two fans.
- THE DISPLAY READS "72°F". Never "188", never garbled, never a stray superscript.
- The display panel and buttons are black as usual; the display is lit and reads "72°F".

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. ANGLE, SIZE, POSITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Identical to the white main image: turned about 15 degrees left, tilted back about 20
  degrees, centred, about 80% of frame width.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. LIGHT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Bright, soft studio light from above and front-left (5500 K). The bronze shows a soft
  warm sheen along the rim and bars without mirror-like highlights. Faint reflection
  beneath, soft contact shadow.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6. DO NOT INCLUDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- White, copper, rose-gold, pink or grey finish on the faceplate.
- Air-flow swirls, wind lines, leaves, snowflakes, sparkles, glow or any effect showing
  air or temperature. Any text, caption, logo, watermark, price, badge, sticker, arrow,
  border or frame added to the image.
- Any logo or text on the product that isn't described above. Horizontal slats, more or
  fewer than two fans, the display on the left side, a product colour other than the one
  specified.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
9. FINAL CHECK BEFORE OUTPUT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
The vent is dark oil-rubbed bronze, NOT white or copper; vertical bars, two fans, display reading "72°F". White background.

Aspect ratio 1:1, 1400 x 1400.
```

**If it misses (re-run, don't edit):**

| Miss | Add to the end and re-run |
|---|---|
| Display shows 188 / garbled °F | *"The display digits are the most important detail: exactly 72 then a clean °F, large and legible."* |
| Horizontal slats / wrong fan count | *"Copy the grille from the reference exactly: vertical bars, two fans."* |
| Comes out copper/pink | *"Deep brown-black oil-rubbed bronze, like a dark bronze door handle; no copper or pink tones at all."* |

---

## 5b. The result — that room at 4pm · section 5b `out_image`

**Attach:** REF-1 (remote cropped out)

```
Create ONE candid, realistic phone photograph of a small upstairs home office at about
4:00 pm on a very hot, cloudless day in late July. The room has been fixed: someone is
working in it comfortably in the hottest part of the day. This image sells the outcome;
the vent is present but it is NOT the subject.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. THE ROOM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Roughly 10 x 11 feet, a spare bedroom converted to an office, 1990s–2000s suburban
  North American build. Textured white ceiling.
- Walls: flat warm greige paint (#D9D2C5), a couple of faint scuffs.
- Baseboards: white painted MDF (#F2F0EB), about 3.5 inches tall, a thin dust line on
  the top edge.
- Floor: beige low-pile wall-to-wall carpet (#C9B9A0) with visible vacuum tracks.
- Outlets: standard white US duplex outlets in white plates.
- One west-facing window on the far wall, about 4 feet wide, white vinyl frame, white
  horizontal mini-blinds raised halfway, a thin cord dangling. Through it: overexposed
  pale sky and the blurred green top of a tree.
- The white six-panel door with a brass knob stands wide open at the left edge of the
  frame, slightly out of focus.
- A plain white laminate desk with thin grey metal legs against the right-hand wall.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. THE PERSON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- A woman in her mid-40s sits at the desk in a black mesh office chair, seen from behind
  and slightly to her left (three-quarter back view). Her face is NOT visible.
- Shoulder-length brown hair loosely held up with a tortoiseshell claw clip. Heather-grey
  crew-neck t-shirt, navy cotton shorts, bare legs, one bare foot tucked up on the edge of
  the chair seat, the other flat on the carpet.
- Typing on an open silver laptop (its manufacturer logo visible on the lid); the screen
  lit, content soft and unreadable.
- Relaxed and settled: shoulders down, back loose, head tilted toward the screen.
  Completely comfortable. No sweat, no damp patches, no fanning.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. THE DESK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- A tall glass of iced water with visible ice cubes and light condensation on a cork
  coaster. Her phone face-down. A yellow legal pad with a pen. A mug holding pens.
  A charging cable trailing off the back edge.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. THE PRODUCT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Use the attached reference image ONLY for the product's exact appearance.
Do NOT include the remote control from the reference. Do not copy the reference's layout
or background.

THE PRODUCT (match the reference exactly):
- A flat rectangular floor vent cover (register) with two built-in fans. About 2.4 times
  as wide as it is tall. One piece of moulded plastic with a thin raised rim and softly
  rounded outer corners. FINISH: matte bright-white moulded plastic (#F4F4F2), clean and even.
- LEFT about 70% of the face: a rectangular grille opening with rounded inner corners,
  crossed by 18 thin, evenly spaced VERTICAL bars running top to bottom (NOT horizontal
  louvres). Behind the bars, two identical round fans side by side, each with a dark
  charcoal-grey circular shroud and a black five-blade impeller with broad curved blades
  and a small round hub.
- RIGHT about 25% of the face: a vertical glossy black display panel, taller than wide.
  Top: two small white icons with tiny labels. Middle: a large white seven-segment
  digital readout showing exactly "72" followed by a small, clearly formed "°F".
  Bottom: four small white icons in a 2 x 2 grid (flame, snowflake, fan, crescent moon)
  with tiny labels.
- Right of the display: two narrow vertical strips of small square black buttons with
  white symbols — upper strip of three (power at top), lower strip of three (mode, "+",
  "−").
- One round countersunk screw hole at each short end, centred vertically: left of the
  grille, right of the buttons.
- No logo, no brand name, no other text on the product. Exactly two fans.
- THE DISPLAY READS "72°F". Never "188", never garbled, never a stray superscript.
- Set flush into the carpeted floor in front of the desk, between the chair and the
  window wall, running parallel to the wall. Display lit, reading "72°F".
- SMALL in frame: about 12% of the image width. Recognisable (white, vertical bars, black
  display at the right end) but not the focus. In ordinary light, not spotlit.
- Its thin white cord runs across the carpet to an outlet on the baseboard.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5. LIGHT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Hard, low, golden late-afternoon sun (about 4500 K) through the half-raised blinds,
  throwing bright slatted stripes across the desk, her back and shoulder, the carpet and
  the right wall. Obviously the hottest part of the day. Stripes slightly overexposed;
  shadows warm brown, not black. No lamps on.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6. CAMERA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- From the doorway at standing height (about 5 feet), angled slightly down and to the
  right. ~24 mm equivalent, f/1.8, handheld, horizon tilted about 1 degree. Window left of
  centre, woman and desk in the right half, vent in the lower centre.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
7. RENDERING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Realistic phone-camera quality (like an iPhone main camera): mild luminance grain in
shadows, natural slightly warm white balance, very slight lens distortion at the edges.
No HDR look, no cinematic grade, no vignette, no bokeh balls, no lens flare.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
8. DO NOT INCLUDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Her face. Any fan, air conditioner or space heater. Pets, decorative plants, throws.
  The remote. A hand in the foreground.
- Air-flow swirls, wind lines, leaves, snowflakes, sparkles, glow or any effect showing
  air or temperature. Any text, caption, logo, watermark, price, badge, sticker, arrow,
  border or frame added to the image.
- Any logo or text on the product that isn't described above. Horizontal slats, more or
  fewer than two fans, the display on the left side, a product colour other than the one
  specified.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
9. FINAL CHECK BEFORE OUTPUT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Hard 4pm sun; woman comfortable at the desk, face hidden; iced water; door open; no fans; the vent small in the floor reading "72°F". No text, no effects.

Aspect ratio 4:5, 1400 x 1750.
```

**If it misses (re-run, don't edit):**

| Miss | Add to the end and re-run |
|---|---|
| Display shows 188 / garbled °F | *"The display digits are the most important detail: exactly 72 then a clean °F, large and legible."* |
| Horizontal slats / wrong fan count | *"Copy the grille from the reference exactly: vertical bars, two fans."* |
| Vent too large / hero | *"The vent is small in the lower centre, about 12% of the image width, not the subject."* |
| She looks hot or posed | *"She is relaxed and absorbed in her work, like a candid photo taken without her noticing."* |

---

## 7. Measuring the opening · section 7 `fit_image` (no new product in frame)

**Attach:** nothing

```
Create ONE candid, realistic phone photograph looking straight down at a person
measuring the opening of a floor vent with a tape measure. It teaches "measure the hole,
not the cover" at a glance.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. THE OPENING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- A rectangular 4 x 10 inch hole in beige low-pile carpet (#C9B9A0), the old cover
  removed. Inside: the galvanised sheet-metal duct boot, grey with a little dust, dark
  further down.
- Around the hole, a clean rectangular indentation in the carpet and a faint dust
  outline where the old cover sat.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. THE TAPE MEASURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- A yellow-cased retractable tape measure with its manufacturer's name and logo visible
  on the case, exactly like a real hardware-store tape.
- The blade pulled taut across the SHORT side of the opening (the 4-inch side), its hook
  caught on the near edge. The black printed inch numbers and increment marks crisp and
  legible. The far edge of the opening lines up exactly with the "4" mark.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. HANDS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Two ordinary adult hands: one holding the case, one pressing the blade flat at the far
  edge. Short nails, natural skin, a heather-grey t-shirt cuff at one wrist.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. THE OLD COVER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- A plain builder-grade white metal floor register with horizontal louvres (the OLD one,
  not our product) lying face-up on the carpet at the lower right of the frame, a little
  dusty, two loose screws beside it.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5. CAMERA AND LIGHT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- From directly above at chest height, looking straight down. ~24 mm equivalent. Frame
  tilted about 3 degrees. The opening centred.
- Soft, even overhead room daylight, about 5000 K, no hard shadows.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6. RENDERING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Realistic phone-camera quality (like an iPhone main camera): mild luminance grain in
shadows, natural slightly warm white balance, very slight lens distortion at the edges.
No HDR look, no cinematic grade, no vignette, no bokeh balls, no lens flare.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
7. DO NOT INCLUDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Faces. Our new vent cover or any vent with fans or a display.
- Any text, caption, arrow, badge or overlay.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
9. FINAL CHECK BEFORE OUTPUT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Looking straight down; the tape across the short side of the hole reading 4 at the far edge; numbers legible; the old louvred cover set aside. No new product, no text.

Aspect ratio 4:3, 1600 x 1200.
```

**If it misses (re-run, don't edit):**

| Miss | Add to the end and re-run |
|---|---|
| Tape across the long side | *"The tape measure spans the SHORT 4-inch side of the opening, not the 10-inch side."* |
| Numbers illegible | *"The tape's printed inch numbers are large, crisp and readable."* |

---

## 8.1 Install step 1 — take the old cover out

**Attach:** nothing

```
Create ONE candid phone photograph, step 1 of 3 of installing a floor vent cover.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. THE SCENE (identical in all three steps)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Looking down at a rectangular 4 x 10 inch floor vent opening in beige low-pile carpet
  (#C9B9A0), about 8 inches out from a white baseboard (#F2F0EB) and greige wall
  (#D9D2C5). A white US outlet on the baseboard about 18 inches to the right.
- Camera fixed: directly above-and-in-front at about 3 feet, angled down 60 degrees,
  ~26 mm, the opening in the centre. Soft 5000 K daylight from a window to the left.
- Ordinary adult hands, short nails, heather-grey t-shirt cuff.
Realistic phone-camera quality (like an iPhone main camera): mild luminance grain in
shadows, natural slightly warm white balance, very slight lens distortion at the edges.
No HDR look, no cinematic grade, no vignette, no bokeh balls, no lens flare.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. THIS STEP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- An old plain builder-grade white metal floor register with horizontal louvres sits in
  the opening. A hand holds a manual screwdriver with a red-and-black handle (brand
  markings visible) backing out its left screw; the right screw already out, lying on the
  carpet.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. DO NOT INCLUDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Our new vent cover. Faces. Any text, numbers, arrows or overlays.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
9. FINAL CHECK BEFORE OUTPUT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Old louvred register in the floor, screwdriver on the left screw, one screw on the carpet. No new product, no text.

Aspect ratio 4:3, 1600 x 1200.
```

**If it misses (re-run, don't edit):**

| Miss | Add to the end and re-run |
|---|---|

---

## 8.2 Install step 2 — drop the new one in

**Attach:** REF-1 (remote cropped out)

```
Create ONE candid phone photograph, step 2 of 3 of installing the floor vent cover
described below.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. THE SCENE (identical in all three steps)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Looking down at a rectangular 4 x 10 inch floor vent opening in beige low-pile carpet
  (#C9B9A0), about 8 inches out from a white baseboard (#F2F0EB) and greige wall
  (#D9D2C5). A white US outlet on the baseboard about 18 inches to the right.
- Camera fixed: directly above-and-in-front at about 3 feet, angled down 60 degrees,
  ~26 mm, the opening in the centre. Soft 5000 K daylight from a window to the left.
- Ordinary adult hands, short nails, heather-grey t-shirt cuff.
Realistic phone-camera quality (like an iPhone main camera): mild luminance grain in
shadows, natural slightly warm white balance, very slight lens distortion at the edges.
No HDR look, no cinematic grade, no vignette, no bokeh balls, no lens flare.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. THIS STEP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- The old register lies face-up on the carpet at the left edge of the frame.
- Two hands hold the new vent cover by its short ends and lower it into the opening; it is
  about one inch above sitting flush. Display unlit (not plugged in yet).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. THE PRODUCT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Use the attached reference image ONLY for the product's exact appearance.
Do NOT include the remote control from the reference. Do not copy the reference's layout
or background.

THE PRODUCT (match the reference exactly):
- A flat rectangular floor vent cover (register) with two built-in fans. About 2.4 times
  as wide as it is tall. One piece of moulded plastic with a thin raised rim and softly
  rounded outer corners. FINISH: matte bright-white moulded plastic (#F4F4F2), clean and even.
- LEFT about 70% of the face: a rectangular grille opening with rounded inner corners,
  crossed by 18 thin, evenly spaced VERTICAL bars running top to bottom (NOT horizontal
  louvres). Behind the bars, two identical round fans side by side, each with a dark
  charcoal-grey circular shroud and a black five-blade impeller with broad curved blades
  and a small round hub.
- RIGHT about 25% of the face: a vertical glossy black display panel, taller than wide.
  Top: two small white icons with tiny labels. Middle: a large white seven-segment
  digital readout showing exactly "72" followed by a small, clearly formed "°F".
  Bottom: four small white icons in a 2 x 2 grid (flame, snowflake, fan, crescent moon)
  with tiny labels.
- Right of the display: two narrow vertical strips of small square black buttons with
  white symbols — upper strip of three (power at top), lower strip of three (mode, "+",
  "−").
- One round countersunk screw hole at each short end, centred vertically: left of the
  grille, right of the buttons.
- No logo, no brand name, no other text on the product. Exactly two fans.
- THE DISPLAY READS "72°F". Never "188", never garbled, never a stray superscript.
- (Display unlit in this step, so no reading shows.)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. DO NOT INCLUDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Faces. The remote.
- Air-flow swirls, wind lines, leaves, snowflakes, sparkles, glow or any effect showing
  air or temperature. Any text, caption, logo, watermark, price, badge, sticker, arrow,
  border or frame added to the image.
- Any logo or text on the product that isn't described above. Horizontal slats, more or
  fewer than two fans, the display on the left side, a product colour other than the one
  specified.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
9. FINAL CHECK BEFORE OUTPUT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Same framing as step 1; the new white vent being lowered by two hands; old cover set aside; display unlit.

Aspect ratio 4:3, 1600 x 1200.
```

**If it misses (re-run, don't edit):**

| Miss | Add to the end and re-run |
|---|---|
| Horizontal slats / wrong fan count | *"Copy the grille from the reference exactly: vertical bars, two fans."* |
| Remote appears when it shouldn't | *"Crop the remote out of the reference before attaching, then re-run."* |

---

## 8.3 Install step 3 — plug it in

**Attach:** REF-1 (remote cropped out)

```
Create ONE candid phone photograph, step 3 of 3 of installing the floor vent cover
described below.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. THE SCENE (identical in all three steps)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Looking down at a rectangular 4 x 10 inch floor vent opening in beige low-pile carpet
  (#C9B9A0), about 8 inches out from a white baseboard (#F2F0EB) and greige wall
  (#D9D2C5). A white US outlet on the baseboard about 18 inches to the right.
- Camera fixed: directly above-and-in-front at about 3 feet, angled down 60 degrees,
  ~26 mm, the opening in the centre. Soft 5000 K daylight from a window to the left.
- Ordinary adult hands, short nails, heather-grey t-shirt cuff.
Realistic phone-camera quality (like an iPhone main camera): mild luminance grain in
shadows, natural slightly warm white balance, very slight lens distortion at the edges.
No HDR look, no cinematic grade, no vignette, no bokeh balls, no lens flare.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. THIS STEP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- The new vent cover sits flush in the opening, both screws in.
- Its thin white cord runs across the carpet to the outlet on the baseboard; a hand is
  pushing the plug into the outlet.
- The display has just come on and reads "72°F".

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. THE PRODUCT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Use the attached reference image ONLY for the product's exact appearance.
Do NOT include the remote control from the reference. Do not copy the reference's layout
or background.

THE PRODUCT (match the reference exactly):
- A flat rectangular floor vent cover (register) with two built-in fans. About 2.4 times
  as wide as it is tall. One piece of moulded plastic with a thin raised rim and softly
  rounded outer corners. FINISH: matte bright-white moulded plastic (#F4F4F2), clean and even.
- LEFT about 70% of the face: a rectangular grille opening with rounded inner corners,
  crossed by 18 thin, evenly spaced VERTICAL bars running top to bottom (NOT horizontal
  louvres). Behind the bars, two identical round fans side by side, each with a dark
  charcoal-grey circular shroud and a black five-blade impeller with broad curved blades
  and a small round hub.
- RIGHT about 25% of the face: a vertical glossy black display panel, taller than wide.
  Top: two small white icons with tiny labels. Middle: a large white seven-segment
  digital readout showing exactly "72" followed by a small, clearly formed "°F".
  Bottom: four small white icons in a 2 x 2 grid (flame, snowflake, fan, crescent moon)
  with tiny labels.
- Right of the display: two narrow vertical strips of small square black buttons with
  white symbols — upper strip of three (power at top), lower strip of three (mode, "+",
  "−").
- One round countersunk screw hole at each short end, centred vertically: left of the
  grille, right of the buttons.
- No logo, no brand name, no other text on the product. Exactly two fans.
- THE DISPLAY READS "72°F". Never "188", never garbled, never a stray superscript.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. DO NOT INCLUDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Faces. The remote. The old register.
- Air-flow swirls, wind lines, leaves, snowflakes, sparkles, glow or any effect showing
  air or temperature. Any text, caption, logo, watermark, price, badge, sticker, arrow,
  border or frame added to the image.
- Any logo or text on the product that isn't described above. Horizontal slats, more or
  fewer than two fans, the display on the left side, a product colour other than the one
  specified.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
9. FINAL CHECK BEFORE OUTPUT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Same framing as steps 1–2; the white vent flush in the floor reading "72°F"; a hand plugging the cord into the outlet.

Aspect ratio 4:3, 1600 x 1200.
```

**If it misses (re-run, don't edit):**

| Miss | Add to the end and re-run |
|---|---|
| Display shows 188 / garbled °F | *"The display digits are the most important detail: exactly 72 then a clean °F, large and legible."* |
| Horizontal slats / wrong fan count | *"Copy the grille from the reference exactly: vertical bars, two fans."* |
| Remote appears when it shouldn't | *"Crop the remote out of the reference before attaching, then re-run."* |

---

## Notes

- **Don't generate the duct-run diagram.** It's inline SVG in the section file.
- **Check every product image against the reference before uploading.** Wrong fan count, a moved display or an invented logo means re-run. A product that looks different when it arrives becomes a return.
- **Cold versions:** 5b uses flat grey 4 pm winter light, bare tree, oatmeal knit sweater, wool socks and a steaming mug, with no heater. Every display reads 70°F.
