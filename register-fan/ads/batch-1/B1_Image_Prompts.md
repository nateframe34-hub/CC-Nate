# Batch 1 — Nano Banana Pro 2 Image Prompts · FULL SPEC

**Rebuilt 2026-09-26 (founder: "literally as detailed as possible — fonts, colors, everything").**
For `B1_Ads.md` — SA1 The Fan Runner · hot framing. Canvas for every ad: **4:5, 1080 × 1350 px.**

---

## 0. How to use this file

### 0a. Product reference images — attach them every time the product appears

Nate is supplying real photos of our vent cover. **Any prompt that shows the product must be run with those photos attached**, labelled in this order:

| Ref | What it should show | Used for |
|---|---|---|
| **REF-1** | Whole unit, straight on, faceplate facing camera | Shape, proportions, grille pattern, colour |
| **REF-2** | Close-up of the display / control end | Display shape, digit style, icon layout |
| **REF-3** | Three-quarter angle, showing depth / housing | Thickness, how it sits in a wall |
| **REF-4** *(if available)* | Remote, and the cord where it leaves the unit | Cord exit point, remote shape |

Paste this **PRODUCT LOCK** block into any prompt that contains the product (it is already included below where needed):

```
PRODUCT LOCK — the vent cover in this image must be an exact match of the product in
the attached reference images (REF-1 to REF-4). Copy it faithfully: the same overall
rectangular proportions, the same faceplate colour and finish, the same number, spacing
and angle of the grille slats, the same fan hubs and blade count visible behind the
grille, the same position, size and shape of the display panel, the same digit style on
the display, the same icons, the same screw-hole positions, the same corner radius, the
same cord exit point. Do not redesign, simplify, "improve", add features, add a logo,
change the colour, or change the number of fans. Do not invent text on the faceplate
that is not on the reference. If a detail is not visible in the references, keep it
plain and consistent with what is visible. The only thing that may change is the number
shown on the display, which must read exactly as specified in this prompt.
```

### 0b. Brand tokens — the only colours and fonts used on any designed element

| Token | Value | Use |
|---|---|---|
| Terracotta (accent) | **`#B4553A`** · RGB 180/85/58 | Text bands, emphasis |
| Warm off-white (base) | **`#FAF7F2`** · RGB 250/247/242 | Text on terracotta, backgrounds |
| Warm near-black (text) | **`#1C1A17`** · RGB 28/26/23 | Text on light backgrounds |
| Slate (diagram only) | `#5B7185` | Never on ads |
| Headline font | **Archivo**, ExtraBold (800) | All headlines |
| Body font | **Inter**, Regular (400) / Medium (500) / SemiBold (600) | All supporting lines |
| Numbers font | **JetBrains Mono**, Medium (500), tabular figures | Every temperature and every price |

**Fonts in generators drift.** Nano Banana renders type well but cannot guarantee a named font. Every designed ad therefore has two routes:
- **Route A — one-pass composite.** Fast. Check the type against the spec; regenerate if it drifts.
- **Route B — plate + typeset. Preferred for launch.** Generate the photo with empty space, then set the exact type in Figma/Canva/Photoshop using the spec tables. Pixel-exact, on-brand, editable.

### 0c. Standing rules in every prompt

- **Real prop branding stays.** Never write "unbranded", "no logos" or "no brand marks". Fans, laptops, bottles, markers show their normal manufacturer marks.
- **It must look like a real photo, not a render.** Imperfection is specified on purpose: grain, slight tilt, dust, scuffs, lived-in clutter.
- **No added promotional furniture**: no badges, stickers, starbursts, buttons, arrows-as-graphics, countdowns, star ratings. (A price line is allowed where the spec calls for one.)

---

# B1C1 — Native scene image *(no text, no product)*

**Job:** the image above ~1,400 words of Julie's first-person story. It shows the room she gave up on, exactly as she describes it: upstairs home office, west window, hot sun, a box fan on the carpet aimed at the desk, a tower fan by the window, a closed laptop. It must look like she stood in the doorway and took it without thinking.

**Product:** NOT in frame. No vent cover of any kind.

## Prompt

```
A candid, unposed smartphone photograph taken from the open doorway of a small upstairs
home office in an ordinary North American suburban house (1990s–2000s build), at about
3:45 pm on a very hot, cloudless day in late July.

ROOM: Roughly 10 by 11 feet. Walls painted a flat warm greige (close to #D9D2C5), slightly
scuffed at chair height. White painted baseboards (#F2F0EB) with a dust line along the
top edge. Beige low-pile wall-to-wall carpet (#C9B9A0) with visible vacuum tracks and a
slightly flattened path from the door to the desk. White six-panel door, opened inward,
its edge and the doorframe intruding into the left 8% of the frame, slightly out of focus.

WINDOW: One window centred on the far wall, west-facing, about 4 feet wide. White vinyl
horizontal mini-blinds lowered two-thirds of the way and tilted half-open. A thin cord
dangles. Through the gaps: overexposed white-blue sky and the blurred green top of a tree.

DESK: A plain white laminate desk (IKEA-style, simple rectangular top, metal legs) against
the right-hand wall, perpendicular to the window. On it: a closed silver laptop with its
manufacturer logo visible on the lid; a clear drinking glass two-thirds full of water with
heavy condensation, beads running down, and a wet ring spreading on the desk beneath it;
a yellow legal pad with a pen lying diagonally across it; a phone charging cable looping
off the back edge; a mug holding pens. A black mesh office chair pushed back from the
desk and turned slightly toward the door, as if someone just got up.

FAN 1: A black plastic 20-inch box fan standing directly on the carpet about 3 feet from
the desk, angled upward toward the chair. Running — the blades are a soft motion blur.
The manufacturer's name plate and its rotary speed dial are visible and legible on the
front corner, exactly like a real store-bought fan. Its grey power cord trails across the
carpet in a loose S-curve to a white duplex outlet on the baseboard of the right wall.

FAN 2: A white oscillating tower fan, about 40 inches tall, standing on the carpet to
the left of the window, also running, turned to face the desk. Its brand name and
control buttons are visible on the top panel. Its cord runs along the wall to the same
side.

LIGHT: Hard, low, late-afternoon sun (around 4500 K, warm golden-orange) coming through
the blinds, casting bright slatted stripes across the desk surface, the chair, and a wide
patch of carpet. High contrast: the sunlit stripes nearly blow out, the shadows are warm
brown, not black. Fine dust motes visible in the light shaft. No lamps on. The room feels
hot, still and airless.

CAMERA: As if shot on an iPhone 15, main wide lens (~24 mm equivalent), f/1.8, handheld at
chest height (about 4.5 feet) from the doorway, pointing slightly down. The horizon is
tilted about 2 degrees clockwise. Composition not centred: the window sits slightly left
of centre, the desk and chair occupy the right third, the box fan the lower centre. Deep
focus; everything reasonably sharp except the door edge.

RENDERING: Real phone-camera image quality — mild luminance noise in the shadows, a little
highlight clipping in the sunlit stripes, faint chromatic fringing along the window edge,
slight motion blur on both fans' blades, slightly warm auto white balance. No HDR look,
no cinematic colour grade, no vignette, no lens flare effects, no bokeh balls.

MOOD: A room someone has quietly given up on. Nothing styled, nothing arranged for a photo.

EXCLUDE: people, hands, pets; any text, caption, watermark, sticker or graphic overlay;
any air vent, floor register, wall register or vent-mounted device; air conditioner
units; studio lighting; magazine-interior styling; plants arranged decoratively.

Aspect ratio 4:5, 1080 x 1350.
```

## QA before using
- [ ] Two fans, both clearly running (blade blur), box fan on the floor aimed at the desk
- [ ] Laptop **closed**, glass sweating, chair pushed back — she's just left
- [ ] Sunlight is hard and slatted; the room reads hot at thumbnail size
- [ ] No vent visible anywhere
- [ ] Passes the caption test: *"two fans and it's still 84 in here"*

---

# B1C2 — Outcome static · "No more switching rooms because of the heat."

**Job:** show the outcome. The problem room at 4pm, hard sun still coming in, and someone working in it comfortably. The box fan is switched off and retired in the corner. The product can appear small and true-to-reference in the wall. It is not the subject.

## Layout spec (1080 × 1350)

```
┌──────────────────────────────────────────┐  y=0
│  TERRACOTTA BAND  #B4553A  (full width)  │
│  64 px side margins, 64 px top padding   │
│                                          │
│  HEADLINE  (3 lines max)                 │
│  BODY      (3 lines)                     │
│  LINE 3    (2 lines)                     │
│  PRICE                                   │
│                                          │  y≈600 (band bottom, 56 px padding)
├──────────────────────────────────────────┤
│                                          │
│  PHOTOGRAPH (full width, 1080 × 750)     │
│  subject sits in this lower area         │
│                                          │
└──────────────────────────────────────────┘  y=1350
```

## Type spec

| Element | Text (exact) | Font | Size | Line height | Tracking | Colour | Align |
|---|---|---|---|---|---|---|---|
| Headline | **No more switching rooms because of the heat.** | Archivo ExtraBold 800 | 70 px | 1.04 (73 px) | −1% | `#FAF7F2` | Left |
| Gap | — | — | 28 px | — | — | — | — |
| Body | Not a bigger fan — a fan never cooled the room anyway. This pulls the cold air your AC already makes all the way in. | Inter Regular 400 | 29 px | 1.38 (40 px) | 0 | `#FAF7F2` at 92% opacity | Left |
| Gap | — | — | 18 px | — | — | — | — |
| Line 3 | The door stays open. The box fan goes back in the garage. | Inter SemiBold 600 | 29 px | 1.38 | 0 | `#FAF7F2` 100% | Left |
| Gap | — | — | 22 px | — | — | — | — |
| Price | $89 | JetBrains Mono Medium 500, tabular | 30 px | 1.0 | +2% | `#FAF7F2` 100% | Left |

- Text column width: **952 px** (1080 − 2 × 64). Ragged right, no hyphenation, no widows (the headline must not end on a single word — rebreak as *"No more switching rooms / because of the heat."*).
- The em dash in the body is a true em dash (—) with a space either side.
- No drop shadows, outlines, glows or gradients on any text. No logo, no wordmark.
- Band is a flat solid `#B4553A`, no texture, no gradient, square edge where it meets the photo (no curve, no torn-paper edge).

## Route B — photograph plate (preferred)

Generate this at **1080 × 750** (or 1440 × 1000 and scale), then place under the band.

```
[Attach REF-1 to REF-3. Paste PRODUCT LOCK block from section 0a here.]

A candid, unposed smartphone photograph of a small upstairs home office in an ordinary
North American suburban house at about 4:00 pm on a very hot, cloudless day in late July.
The same kind of room as a typical spare bedroom converted to an office: flat warm greige
walls (#D9D2C5) with light scuffs, white baseboards, beige low-pile carpet (#C9B9A0).

LIGHT: The heat of the day is obvious — hard, low, golden late-afternoon sun (around
4500 K) comes through a west-facing window at the left of frame, the white mini-blinds
raised halfway, throwing bright slatted stripes across the desk, the person's back and
the carpet. Warm, high-contrast, a little overexposed in the stripes.

PERSON: A woman in her mid-40s, seen from behind and slightly to her left (three-quarter
back view, face NOT visible), sitting at a plain white desk against the right wall,
typing on an open silver laptop (manufacturer logo visible on the lid). She wears a
heather-grey crew-neck t-shirt and navy shorts, shoulder-length brown hair loosely tied
back with a claw clip. Posture relaxed and settled: shoulders down, one bare foot tucked
up on the seat of her black mesh office chair, the other flat on the carpet. No sweat,
no fanning herself, no tension — she is simply comfortable and working.

DESK: A tall glass of iced water with visible ice cubes and light condensation beside
the laptop, on a cork coaster. A phone face-down. A mug of pens. A yellow sticky note
stuck to the laptop's bezel. A charging cable trailing off the back edge. A light
cardigan hung over the back of the chair.

THE RETIRED FAN: In the far-left corner of the room, below the window, a black plastic
20-inch box fan sits switched OFF (blades perfectly still and sharp), pushed right up
against the wall and slightly angled away from the room, its grey power cord wrapped
around its carry handle. Its manufacturer's name plate is visible. It reads clearly as
put away, no longer in use.

THE DOOR: The white six-panel door behind her, on the far wall, stands wide open to a
softly lit hallway.

THE PRODUCT: Low on the right-hand wall under the desk, just above the baseboard, the
vent cover from the reference images is installed flush in the wall where an old
register would be, its display lit and reading "72°". It is small in the frame (roughly
6–8% of the image width), in natural shadow under the desk, slightly out of focus — a
real object in a real room, not a hero product shot. Its thin white cord runs a short
distance along the baseboard to a white outlet.

COMPOSITION: Shot from the doorway area at standing height (about 5 feet), angled
slightly down and to the right. The person and desk occupy the right half; the window
and the retired fan the left third; the open door visible behind. Keep the TOP 10% of
this plate calm (wall and ceiling line only) because a text band sits directly above it.

CAMERA / RENDERING: As if shot on an iPhone, ~24 mm equivalent, f/1.8, handheld. Horizon
tilted about 1 degree. Mild shadow noise, slight highlight clipping in the sun stripes,
natural slightly warm white balance. No HDR, no cinematic grade, no vignette, no bokeh.

EXCLUDE: her face; any sweat, discomfort or fanning; a running fan; any text, caption,
sticker or overlay in the photo; any logo added to the vent cover that isn't on the
reference; studio lighting; magazine styling; plants arranged decoratively.

Aspect ratio 1080 x 750 (approximately 1.44:1, landscape).
```

## Route A — full composite, one pass

```
[Attach REF-1 to REF-3. Paste PRODUCT LOCK block from section 0a here.]

A vertical 4:5 social advertisement, 1080 x 1350 pixels, made of two stacked parts.

PART 1 — TEXT BAND (top 600 pixels, full width): a flat, solid, untextured terracotta
colour, hex #B4553A. Inside it, 64-pixel margins on the left and right and 64 pixels of
padding at the top, left-aligned text in off-white #FAF7F2:

  Line group 1 — the headline, in a heavy, tight, confident geometric grotesque sans
  serif (Archivo ExtraBold style), about 70 px, tight line spacing, broken exactly as:
      "No more switching rooms
       because of the heat."

  Line group 2 — 28 px below, in a clean neutral sans serif (Inter Regular style), about
  29 px, comfortable line spacing, slightly softer off-white:
      "Not a bigger fan — a fan never cooled the room anyway. This pulls the cold air
       your AC already makes all the way in."

  Line group 3 — 18 px below, same sans serif but semibold, full off-white, about 29 px:
      "The door stays open. The box fan goes back in the garage."

  Line group 4 — 22 px below, in a monospaced typeface (JetBrains Mono style), about
  30 px:
      "$89"

All text crisp, correctly spelled, evenly kerned, fully legible on a phone. No shadows,
outlines, glows or gradients on text. No logo, no wordmark, no badge.

PART 2 — PHOTOGRAPH (bottom 750 pixels, full width, meeting the band with a straight
square edge): [insert the full Route B photograph description here, from "A candid,
unposed smartphone photograph..." through "EXCLUDE"].

STRICTLY EXCLUDE anywhere in the image: badges, stickers, starbursts, ribbons, buttons,
arrow graphics, countdown timers, guarantee seals, star ratings, shipping icons, any
promotional graphic furniture.

Aspect ratio 4:5, 1080 x 1350.
```

## QA before using
- [ ] Headline breaks as *"No more switching rooms / because of the heat."*, all words spelled right
- [ ] Price is `$89` in the mono face, nothing else priced
- [ ] Sun is clearly hot; the person is clearly comfortable; face not visible
- [ ] Box fan is **off** (sharp, still blades) with its cord wrapped
- [ ] Door open
- [ ] Vent cover matches the references and reads `72°`, and it's small and not the hero
- [ ] At thumbnail size the headline reads, and the photo reads "comfortable in a sunny room"

## Cold version (hold for the pivot)
Change: headline → *"No more switching rooms because of the cold."* · light → flat grey 4 pm winter overcast, bare branches through the window, blinds fully up · her clothes → oatmeal chunky knit sweater, leggings, wool socks · iced water → steaming mug of tea · retired device in corner → small oil-filled radiator, unplugged, cord wrapped · display → `70°` · body line → *"…This pulls the warm air your furnace already makes all the way in."*

---

# B1C3 — Whiteboard · "Normal vent" vs "Evenroom vent"

**Job:** a real whiteboard photographed at home, with the same room drawn twice. On the left, a normal vent with the person miserable. On the right, our vent with the person comfortable. The faces carry the ad and the arrows explain why. Our vent is drawn as a **hand sketch that clearly resembles the reference product**, not a photo of it.

## Board layout (as drawn)

```
┌───────────────────────────┬───────────────────────────┐
│      NORMAL VENT          │      EVENROOM VENT        │  ← black, underlined
│  ┌─────────────────────┐  │  ┌─────────────────────┐  │
│  │ [window ☀ red]  81° │  │  │ [window ☀ red]  74° │  │  ← thermometer: red / blue
│  │                     │  │  │                     │  │
│  │   😣 sweating figure │  │  │   🙂 relaxed figure │  │
│  │   at desk, laptop   │  │  │   at desk, iced drink│  │
│  │  ▭ vent  ↑↑ (tiny)  │  │  │ ▭◉◉▣ ⇗⇗⇗ (long,   │  │
│  │                     │  │  │   curling to desk)  │  │
│  └─────────────────────┘  │  └─────────────────────┘  │
│ "barely any air           │ "cold air actually        │
│  coming out" →            │  reaching the room" →     │
├───────────────────────────┴───────────────────────────┤
│   "Same room. Same afternoon. You just stay."         │  ← black, across the bottom
└───────────────────────────────────────────────────────┘
```

## Marker colours (dry-erase, real ink tones, not pure RGB)

| Marker | Approx. ink colour | Used for |
|---|---|---|
| Black | `#1E1E1E`, slightly streaky | Headings, room outlines, figures, desk, labels, bottom line |
| Red | `#C8312B` | Sun, 81° thermometer, sweat drops |
| Blue | `#1F5FAE` | All air arrows, 74° thermometer, ice cubes |

## Prompt

```
[Attach REF-1 and REF-2 so the drawn vent can resemble the real product.]

A candid smartphone photograph of a real white dry-erase whiteboard hanging on the wall
of an ordinary home office, with a hand-drawn marker drawing on it.

THE BOARD: A standard 36 x 24 inch magnetic whiteboard with a thin brushed-aluminium
frame and rounded plastic corner caps, hung slightly crooked (about 1 degree) on a warm
greige painted wall (#D9D2C5). Its surface is glossy white (#F7F7F5) with faint grey
ghosting from older wiped-off writing in the upper right, a few smudges where a hand
brushed the ink, and one small fingerprint smear. An aluminium marker tray runs along
the bottom holding three dry-erase markers with their caps off beside them — black, red
and blue — plus a used grey felt eraser. The markers' manufacturer brand name and
colour band are printed on the barrels and visible, exactly as real markers look.

THE DRAWING — done by an adult, quickly and confidently, in chisel-tip dry-erase marker.
Lines are slightly wobbly and uneven in thickness (about 3–5 mm strokes), with visible
streaking where the marker ran a little dry, overlapping line ends at corners, and
occasional tiny gaps. The style is expressive simple cartoon, like someone explaining
something to their family. Nothing is ruled or perfect. Black ink is #1E1E1E, red ink is
#C8312B, blue ink is #1F5FAE, each with the slightly translucent, streaky look of real
dry-erase ink.

A single vertical black line, drawn freehand down the middle, divides the board into two
equal halves. A horizontal black line about 85% of the way down separates a bottom strip.

LEFT HALF:
- Heading at the top centre in black capital letters, handwritten, about 1.2 inches tall,
  underlined with one quick stroke: "NORMAL VENT"
- Below, a simple room drawn as a square outline with a floor line.
- In the upper left of the room, a small window (rectangle with a cross) with a big red
  sun drawn in it — a circle with eight short red rays blazing out.
- On the right wall of the room, a small drawn thermometer (tube and bulb) with "81°"
  written beside it in red, clearly readable.
- In the middle, a stick-figure-plus person (round head, simple body, arms) sitting on a
  chair at a small desk with an open laptop drawn as an L-shape. The person is clearly
  MISERABLE: eyebrows slanted down and inward, mouth a flat wavy line, three red sweat
  drops flying off the head, two short wavy "heat" lines rising from the shoulders, and
  one hand holding a sheet of paper up and fanning the face (two little motion arcs
  beside the paper).
- On the floor line under the desk, a plain rectangle representing an ordinary vent with
  four short horizontal slat lines inside it. Coming out of it: just TWO tiny, short,
  limp blue arrows that droop sideways and stop after about 2 inches — obviously weak.
- Below the room, a handwritten black label with a short arrow pointing at the vent:
  "barely any air coming out"

RIGHT HALF:
- Heading at the top centre in black capital letters, same size, underlined:
  "EVENROOM VENT"
- The SAME room drawn the same way: same window, same big red blazing sun.
- On the right wall, the same drawn thermometer with "74°" beside it in BLUE, clearly
  readable.
- The SAME person at the SAME desk, now clearly COMFORTABLE: sitting upright, a small
  smile, eyebrows relaxed, both hands on the laptop keyboard (typing), no sweat drops, a
  tall glass on the desk with two little blue ice cubes drawn in it.
- On the floor line under the desk, a simple marker sketch of OUR vent cover based on the
  attached reference photos: a longer rectangle with the same general proportions as the
  reference, horizontal slat lines across it, two circles drawn behind the slats for the
  fans, and a small filled rectangle at the right-hand end for the display panel (matching
  the display's position on the reference). It is a quick sketch, not a detailed drawing,
  but anyone who has seen the product would recognise it.
- Coming out of it: FIVE long, strong, bold blue arrows sweeping up and out of the vent,
  curving across the whole room; three of them curl up to reach the person at the desk.
  These arrows are at least three times longer and bolder than the left side's arrows.
- Below the room, a handwritten black label with a short arrow pointing at the blue
  arrows: "cold air actually reaching the room"

BOTTOM STRIP (spanning both halves, centred, black, slightly larger handwriting):
  "Same room. Same afternoon. You just stay."

ALL HANDWRITING: genuinely handwritten in marker by a real adult, mixed-case except the
two headings, letters slightly uneven in size and baseline, naturally imperfect but
fully legible and spelled exactly as given. NOT a font, NOT a handwriting typeface.
"81°" and "74°" must be clearly readable, each with a proper degree symbol.

PHOTOGRAPH: Taken on a phone from about 5 feet back, nearly straight on but a few
degrees off-axis from the left, so the board is very slightly trapezoidal. The whole
board fills about 85% of the frame, with a strip of greige wall visible around it and,
at the right edge, part of a white bookshelf with a few books (real spines and titles
visible). Ordinary indoor daylight from a window off to the left (about 5000 K), giving
a soft diagonal glare band across the top-left corner of the board that slightly washes
out the ink there but does not cover any words. Mild phone-camera grain, natural white
balance, very slight barrel distortion at the edges, focus sharp across the board.

EXCLUDE: people or hands in frame; any typeset or printed text on the board; any digital
arrows, stickers, badges, price, logo overlays or CTA added over the photo; vector-perfect
or ruled lines; colour fills or shading beyond marker strokes; emoji.

Aspect ratio 4:5, 1080 x 1350.
```

## QA before using
- [ ] Headings read exactly **NORMAL VENT** / **EVENROOM VENT**, and nothing says "before" or "after"
- [ ] At thumbnail size: left figure obviously miserable, right figure obviously comfortable
- [ ] Left arrows tiny and limp, right arrows long, bold and reaching the desk
- [ ] `81°` in red, `74°` in blue, both legible
- [ ] Drawn vent on the right resembles the real product (display at the correct end)
- [ ] Bottom line spelled exactly; handwriting looks human, not a font
- [ ] Marker branding on the tray visible and natural

**If it drifts:** handwriting too neat → add *"messy, rushed handwriting, letters uneven in size and slightly slanted."* Arrows too similar → add *"the left arrows are tiny and faint; the right arrows are three times longer and twice as bold."* Faces unclear → add *"exaggerated cartoon expressions readable from across a room."*

## Cold version (hold for the pivot)
Window: red sun → blue snowflakes and a bare tree · left figure: wrapped in a blanket, shivering lines, teeth-chatter zigzag, `58°` in blue · right figure: t-shirt, relaxed, hot mug with red steam lines, `68°` in red · arrows: **red** warm-air arrows (weak left, strong right) · labels: *"barely any warm air coming out"* / *"warm air actually reaching the room"* · bottom line unchanged.

---

# Cold-weather summary

| | Hot (now) | Cold |
|---|---|---|
| **B1C1** | Two running fans, hard west sun | Small oil-filled radiator glowing next to the desk, grey overcast light, blanket over the chair, laptop closed, mug gone cold |
| **B1C2** | See B1C2 cold version | — |
| **B1C3** | See B1C3 cold version | — |
