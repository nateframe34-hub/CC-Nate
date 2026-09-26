# PDP Image Prompts — Nano Banana Pro 2 · FULL SPEC

**Rebuilt 2026-09-26 (founder: maximum detail, and real product reference photos supplied).**
For `theme/sections/evenroom-pdp-sa1.liquid`.

---

## 0. Before generating anything

### 0a. Attach the product reference photos to every prompt that shows the product

| Ref | What it is |
|---|---|
| **REF-1** | The only supplied reference: the product straight on, on white, with its remote. White and bronze exist; the bronze look is carried by the text description |

Paste this block into every prompt marked **[PRODUCT LOCK]**:

```
PRODUCT LOCK — one reference image is attached (REF-1: the product on white, with its
remote). Use it ONLY for the product's appearance. Do not copy its white background,
its layout, or the remote unless this prompt asks for the remote.

The product, described precisely so it survives any angle:
- A flat rectangular floor register cover, about 2.4 times as wide as it is tall
  (roughly 12 x 5 inches overall for the 4x10 size), with a thin raised rim and softly
  rounded corners. One piece of moulded plastic.
- FINISH: [WHITE] matte bright white, like a white appliance, #F4F4F2.
  [BRONZE] dark oil-rubbed bronze, a deep brown-black with a faint warm metallic sheen,
  around #3B2F28. Not copper, not rose-gold, not pink, not shiny brass.
- LEFT ~70% OF THE FACE: a rectangular grille opening with rounded inner corners, filled
  by 18 thin, evenly spaced VERTICAL bars (they run top to bottom, not side to side),
  the same colour as the faceplate. Behind the bars, two identical round fans side by
  side, each with a dark charcoal-grey circular shroud and a black 5-blade impeller with
  broad curved blades and a small round hub.
- RIGHT ~25% OF THE FACE: a vertical black glossy display panel, taller than it is wide.
  Top of the panel: two small white icons with tiny labels. Middle: a large white
  seven-segment digital readout of the temperature followed by a small "°F". Bottom:
  four small white icons in a 2x2 grid (a flame, a snowflake, a fan, a crescent moon)
  with tiny labels under each.
- To the right of the display, two narrow vertical strips of small square black
  buttons with white symbols: an upper strip of 3 (power, and two mode buttons) and a
  lower strip of 3 (a mode button, "+", "−").
- Two round countersunk screw holes, one at each short end of the faceplate, centred
  vertically — left of the grille and right of the buttons.
- No logo, no brand name and no other text on the faceplate.
- REMOTE (only when asked for): a slim light-grey rounded-rectangle remote with a red
  power symbol top-left, a pill-shaped +/− temperature rocker in the middle, and small
  grey icon buttons (flame, leaf, snowflake, fan, moon) with tiny labels.

Match this exactly. Do not redesign, add fans, change the bar direction, move the
display, add a logo, or change the colour. The display must read exactly the number
given in this prompt (e.g. "72°F"), not "188".
```

### 0b. Tokens

| | |
|---|---|
| Page base / seamless background | **`#FAF7F2`** warm off-white |
| Accent | `#B4553A` terracotta. Never inside a photo, page UI only |
| Text | `#1C1A17` |
| Display reading, all images | **`72°`** (summer). Cold versions `70°` |
| Room palette, all in-situ images | Walls warm greige `#D9D2C5` · baseboards white `#F2F0EB` · carpet beige `#C9B9A0` |

**Consistency matters on a product page.** Every in-room image uses the **same room palette, same carpet, same baseboard and same display reading**, so the gallery reads as one house.

### 0c. Standing rules
- Real prop branding stays (tape measure, screwdriver, laptop). Never write "unbranded" or "no logos".
- Photos must look like real photographs: grain, true colour, small imperfections.
- No text overlays, badges or graphics inside any photo. The page adds all type.

### 0c-2. What the reference photos showed (2026-09-26)

- **It's a floor register.** Vertical grille bars, two 5-blade fans, black display panel and two button strips on the right, screw holes at both ends.
- (Previously noted: Every in-room image shows it set flush in the **floor**, not the wall.
- The display with its buttons is at the right-hand end, and it comes with a remote.
- **Listing-style references leak their style.** When the references came in, one generation copied their living room, the air swirls, the flying leaves and the hand holding the remote. Every product prompt below therefore ends with the ANTI-LISTING line:

```
Use the reference images ONLY for the product's appearance. Do not copy their
background, room, lighting, props, people, hands, remote, pets, plants, air-flow
swirls, wind lines, leaves or any graphic effects.
```

### 0d. Gallery order
**1c (installed) → 1a (on white) → 1b (display) → 1d (in hand) → 1e (bronze, if stocked).**

---

## 1a. Product on white *(gallery 2)* · [PRODUCT LOCK]

```
[Attach REF-1. Paste PRODUCT LOCK and the ANTI-LISTING line.]

A clean, honest e-commerce product photograph of the vent cover from the reference
images, alone, on a seamless warm off-white background (#FAF7F2) that runs smoothly
from floor to back with no visible horizon line.

ANGLE: Faceplate toward camera, turned about 20 degrees to the left so the right-hand
end (the display end) and a sliver of the housing depth are visible. Camera at the same
height as the product, level, no tilt. Product centred, occupying about 70% of the frame
width, with even space around it.

DISPLAY: Lit, reading "72°F" in the digit style shown on REF-1, crisp and legible.

LIGHT: One large soft source from the upper left (like a big north-facing window,
5500 K), a white fill from the right so shadows are soft and light grey. A soft, natural
contact shadow directly under the product, fading within an inch. No hard speculars, no
rim light, no gradient backdrop, no reflection on the floor.

DETAIL: True-to-reference colour and finish. Fine surface texture, moulding seams,
screw holes and the slight satin sheen of the plastic are visible — this is a real object
photographed plainly, not a glossy 3D render.

CAMERA: 90 mm lens equivalent, f/11, everything tack sharp, no depth-of-field blur.

EXCLUDE: props, hands, text, captions, logos not present on the reference, watermarks,
studio equipment reflections, colour cast.

Aspect ratio 1:1, 1400 x 1400.
```

## 1b. The display, close *(gallery 3)* · [PRODUCT LOCK]

```
[Attach REF-1. Paste PRODUCT LOCK and the ANTI-LISTING line.]

A tight macro photograph of the display / control end of the vent cover from the
reference images, filling most of the frame. The display is lit and reads "72°F", digits
crisp and exactly in the style on REF-1. Any icons or touch buttons are exactly as on
REF-1, in the same positions.

The adjacent faceplate and the first two or three grille slats are visible at the left
edge of the frame, falling gently out of focus. Camera looking at the display straight
on, rotated about 10 degrees for a little depth.

LIGHT: Soft, even, diffused daylight (5500 K) from the upper left. The display's own glow
visible but not blooming. A realistic tiny dust speck or two on the display surface and a
barely-visible fingerprint smudge at one corner — an object that exists and gets touched.

CAMERA: 100 mm macro, f/4, display plane tack sharp, background falling off smoothly.
Background: the same warm off-white #FAF7F2, out of focus.

EXCLUDE: text overlays, logos not on the reference, studio reflections, colour cast.

Aspect ratio 1:1, 1400 x 1400.
```

## 1c. Installed in the wall ⭐ *gallery image 1 — the most important one* · [PRODUCT LOCK]

```
[Attach REF-1. Paste PRODUCT LOCK and the ANTI-LISTING line.]

A candid photograph of the vent cover from the reference images installed in the FLOOR
of an ordinary North American home, exactly where an old floor register would be: set
into beige low-pile carpet (#C9B9A0) about 8 inches out from a white painted baseboard
(#F2F0EB), the carpet tucked neatly around its flange, a visible vacuum line nearby.
Above it, the lower part of a flat warm greige wall (#D9D2C5) with a couple of faint
scuffs.

DISPLAY: Lit, reading "72°F", legible.

THE CORD: A thin white cord leaves the unit at the exit point shown on the references,
runs across the carpet to the baseboard, and along it about 12 inches to a standard white
US duplex outlet on the baseboard, plugged in. It lies naturally and is not hidden or
perfectly tidied. The plug is visible.

CONTEXT: The right edge of the frame shows one wooden leg of a desk and the tip of a
chair's wheel on the carpet, so it reads as a lived-in room. Nothing else.

LIGHT: Ordinary afternoon daylight from a window out of frame to the left, soft and
slightly warm (about 5000 K), with a gentle gradient across the wall. No flash.

CAMERA: Shot as if on a phone at standing-to-crouching height (about 3 feet), looking
slightly down at the floor, ~26 mm equivalent, f/1.8. The unit sits in the middle third,
slightly left of centre. Realistic phone-camera quality: mild grain, natural white
balance, very slight tilt. No HDR, no cinematic grade.

EXCLUDE: people, text overlays, captions, badges, logos not on the reference, a second
vent, any fan in the room.

Aspect ratio 1:1, 1400 x 1400.
```

## 1d. In hand, for scale *(gallery 4)* · [PRODUCT LOCK]

```
[Attach REF-1. Paste PRODUCT LOCK and the ANTI-LISTING line.]

An adult's hand holding the vent cover from the reference images by its left end, the
faceplate toward camera, at chest height in an ordinary hallway. Four fingers wrap round
the back of the housing, the thumb rests on the front of the faceplate near its corner,
so the size is instantly readable against the hand. Ordinary adult hand: short
unpolished nails, natural skin texture and knuckle creases, no rings, no manicure, a
plain grey t-shirt sleeve cuff just visible at the wrist.

DISPLAY: Lit, reading "72°F", legible.

BACKGROUND: A hallway with warm greige walls (#D9D2C5), a white door frame and part of a
framed picture, all softly out of focus.

LIGHT: Soft natural daylight from a window out of frame to the right, 5000 K.

CAMERA: Phone, portrait-style ~50 mm equivalent, f/2.0. Product and hand sharp,
background blurred. Mild grain, slight handheld imperfection, natural colour.

EXCLUDE: face, text, overlays, logos not on the reference, jewellery styling.

Aspect ratio 1:1, 1400 x 1400.
```

## 1e. Bronze colourway *(only if bronze is stocked at launch)* · [PRODUCT LOCK]

Use the 1a prompt exactly, attach REF-1 (white), and add: *"Render the product in the [BRONZE] finish from the PRODUCT LOCK — dark oil-rubbed bronze, deep brown-black with a faint warm sheen. The white in the reference is the wrong colour for this image; copy only the shape."*

---

## 5b. The result photo — `out_image` · [PRODUCT LOCK]

**Job:** the section right after the hand test, captioned *"That room, at 4pm."* It shows the room back in use.

```
[Attach REF-1. Paste PRODUCT LOCK and the ANTI-LISTING line.]

A candid, unposed smartphone photograph of a small upstairs home office in an ordinary
North American suburban house at about 4:00 pm on a very hot, cloudless day in late
July. Walls flat warm greige (#D9D2C5) with light scuffs, white baseboards (#F2F0EB),
beige low-pile carpet (#C9B9A0).

LIGHT: Hard, low, golden late-afternoon sun (about 4500 K) through a west-facing window at
the left, white mini-blinds raised halfway, casting bright slatted stripes across the
desk and carpet. Obviously the hottest part of the day.

PERSON: A woman in her mid-40s seen from behind and slightly to her left (face not
visible), sitting at a plain white desk against the right wall, typing on an open silver
laptop (manufacturer logo visible). Heather-grey crew-neck t-shirt, navy shorts,
shoulder-length brown hair in a claw clip. One bare foot tucked up on her black mesh
chair. Relaxed, settled, comfortable. No sweat, no fanning.

DESK: Tall glass of iced water with visible ice and light condensation on a cork coaster,
phone face-down, mug of pens, yellow sticky note on the laptop bezel, cable trailing off
the back. Cardigan over the chair back.

ROOM: The white six-panel door behind her stands wide open to the hallway. No fan
anywhere in the room.

THE PRODUCT: In the carpet under the desk, near the right-hand wall, the vent cover from the
reference images set flush in the floor, display lit reading "72°F". Small in
frame (about 8% of image width), in the natural shadow under the desk, recognisable but
not the subject. Its thin white cord runs along the baseboard to an outlet.

CAMERA: From the doorway at standing height (about 5 feet), angled slightly down and to
the right, ~24 mm equivalent, f/1.8, handheld, horizon tilted about 1 degree. Mild grain,
slight highlight clipping in the sun stripes, natural warm white balance. No HDR, no
cinematic grade, no vignette.

EXCLUDE: her face, sweat or discomfort, any fan, text, captions, overlays, logos not on
the reference, magazine styling.

Aspect ratio 4:5, 1400 x 1750.
```

**Cold version:** grey overcast 4 pm winter light, bare branches through the window, oatmeal knit sweater and wool socks, steaming mug of tea instead of iced water, display `70°`, no heater in the room.

---

## 7. The measuring photo — `fit_image` *(no product)*

```
A candid overhead photograph of a person's two hands holding a yellow-cased retractable
tape measure, blade pulled taut across the SHORT side of an open rectangular floor duct
opening, with the old register cover removed. The tape's manufacturer name and logo on
the yellow case are visible and natural. The blade's black printed numbers and inch
increments are crisp and legible; the reading at the far edge of the opening is exactly
"4" (four inches).

THE OPENING: A 4 x 10 inch rectangular hole in the floor, the sheet-metal duct boot
visible inside, galvanised grey with a little dust and a dark interior. Beige low-pile
carpet (#C9B9A0) around it, with a clean rectangular indentation and a faint dust outline
where the old cover sat.

THE OLD COVER: A plain builder-grade white metal register with louvred slats, lying face
up on the carpet at the lower right of the frame, slightly dusty, with its two screws
lying loose beside it.

HANDS: Ordinary adult hands, short nails, a grey t-shirt cuff at one wrist, gripping the
tape at either end.

LIGHT: Soft, even overhead room daylight, about 5000 K, no hard shadows.

CAMERA: From directly above at chest height, looking straight down at the hands, ~24 mm
phone equivalent. Framing slightly tilted (about 3 degrees). Mild grain, natural white
balance.

EXCLUDE: faces, text overlays, captions, badges, the new product, any fan.

Aspect ratio 4:3, 1600 x 1200.
```

---

## 8. Install steps — three matched images *(optional, no slot in the section yet)* · [PRODUCT LOCK on 2 and 3]

**These were written for a wall register. The product is a floor register, so shoot these looking down at the floor opening (same framing as §7) when they're generated.** **Identical framing, light and carpet in all three** (the 1c room: greige wall `#D9D2C5`, white baseboard, beige carpet, white US outlet 12 inches to the right). Camera fixed at about 3 feet high, straight on, ~26 mm, 5000 K window light from the left. Phone quality, mild grain. 4:3, 1600 × 1200 each.

```
STEP 1 — A hand holding a manual screwdriver with a red-and-black handle (brand markings
visible), backing out the left screw of an old plain white builder-grade metal wall
register with louvred slats, mounted low on the wall above the baseboard. The second
screw is already out and resting on the baseboard ledge.
```
```
STEP 2 — [Attach REFs. Paste PRODUCT LOCK and the ANTI-LISTING line.] Same framing. The old register is gone and
leaning against the baseboard at the left edge of the frame; the dark rectangular duct
opening is exposed in the wall. Two hands hold the vent cover from the reference images
and are lowering it into the opening, about an inch from flush. Display unlit.
```
```
STEP 3 — [Attach REFs. Paste PRODUCT LOCK and the ANTI-LISTING line.] Same framing. The vent cover is fitted flush
and screwed in, display lit reading "72°F". A hand is pushing its white plug into the
outlet 12 inches to the right; the cord runs along the baseboard between them.
```

---

## Notes

- **Generate first:** 1c, 1a, 5b, 7. The rest can follow.
- **Do not generate the duct-run diagram.** It's inline SVG in the section file.
- Check every product image against the references before uploading. Wrong fan count, a moved display or an invented logo means regenerate. **A product that looks different on arrival is a return.**
