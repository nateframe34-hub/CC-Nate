# PRODUCT IMAGE REFERENCE — canonical spec

**Date:** 2026-07-29
**Status:** SINGLE SOURCE OF TRUTH. Built from founder-supplied product reference photos.

> **Rule:** any image prompt that puts our product in frame must paste one of the blocks below **verbatim**. Do not paraphrase the packaging, do not invent label copy, do not simplify it to "amber jar with a plain label." The packaging is real and specific, and the whole reason it works is that it looks like a real product.
>
> **Real branding stays.** Per `Tallow_Ad_Creative_Principles.md`, branding tests neutral on CPM and makes a shot read as real. Never write "unbranded," "no logos," or "no readable text" about our own product or anyone else's.

---

## BLOCK A — The main product (Tallow Honey Balm, 60g)

Paste verbatim into any prompt where the balm appears:

```
THE JAR (reproduce exactly, this is a real product):
A squat, wide-mouthed amber glass jar, roughly 60ml, warm honey-brown translucent glass that glows where light passes through it.

LID: a matte black screw-on lid, slightly wider than the jar body, with a finely ribbed / knurled vertical texture around its outer edge. On the flat top of the lid, a circular black label with a thin copper-gold ring border set just inside its edge. Inside that ring, from top: the word "wiyun" small in white lowercase; a small gold line-art bee; "TALLOW HONEY BALM" in gold serif capitals across two lines; two lines of very small ingredient text; and "NET 60G/2.12 OZ" at the bottom.

BODY LABEL: a rectangular matte black label wrapping the front of the jar, edged with a thin double-rule copper-gold border that divides the label into stacked panels.
  - Upper panel: "TALLOW HONEY BALM" in warm copper-gold serif capitals, generously letterspaced, on two centred lines.
  - Centre panel: a single detailed gold line-art honeybee, wings spread, drawn in fine copper-gold linework, centred. This is the visual anchor of the label.
  - Lower strip, split in two: on the left, empty black; on the right, "wiyun" in white lowercase sans-serif, and beneath it a small bordered box reading "NET: 60G/2.12 OZ".

PALETTE: amber glass, matte black, copper-gold foil. Nothing else.
```

**Quick description** for prompts where the jar is small, distant, or out of focus (a full label spec would waste tokens and confuse the generator):
> *"a squat amber glass jar with a matte black ribbed screw lid and a black-and-copper-gold label bearing a line-art bee"*

---

## BLOCK B — The free gift (YURHERSU Tallow Overnight Lip Mask, 20g)

Paste verbatim into any prompt where the gift appears:

```
THE LIP MASK (reproduce exactly, this is a real product):
A small squat round jar, roughly 20g. The body is translucent golden-amber plastic with a soft vertical gradient, lighter at the base. The lid is a glossy, domed, saturated orange plastic cap, taller than the body, giving the whole object a rounded pill-like silhouette.

PRINTING on the jar body, all in deep navy blue: "YURHERSU" in small sans-serif capitals at the top; "Tallow" beneath it, large, in a flowing navy italic script; then "OVERNIGHT LIP MASK" in white sans-serif capitals reversed out of a solid navy bar; and at the bottom "20g/0.7oz" inside a thin navy outlined oval.

THE BOX (include only when the box is called for):
A rectangular tan-beige kraft-toned carton standing beside the jar. Front face, top to bottom: "YURHERSU" in navy sans capitals; "Tallow" very large in navy italic script with a faint swirl motif behind it; "OVERNIGHT LIP MASK" in white capitals on a solid navy bar; "Deeply nourishes the lips" in navy script; and "20g/0.7oz" in a thin navy outlined oval. The visible side panel carries small dense body text.

PALETTE: golden amber, saturated orange, deep navy, tan kraft.
```

---

## 🚨 THE GOVERNING PRINCIPLE: if the story says she bought it, SHOW it

Added 2026-07-29, founder call.

Every native ad on this account tells the same basic story: **she bought this specific product and it worked.** So the product has to be in the frame, wearing its real label. A generic amber jar with a blank cream band is not our product; it's a prop that looks like our product, and it quietly contradicts the story the copy is telling.

This is the same failure as stripping third-party branding, pointed at ourselves. **A blank label is a tell.** It says "staged" to exactly the reader we need to believe this is real.

**The balance, per `Tallow_Ad_Creative_Principles.md` (2026-07-03):** the real label is visible and legible, but **the product is not hero-lit or centred like a commercial.** It sits in the scene the way a real object sits on a real surface. Legible label, ordinary placement. Both at once.

- ✅ Right: our jar, real label readable, sitting off-centre on a cluttered shelf in ordinary light.
- ❌ Wrong: a blank or generically-labelled jar (contradicts the story).
- ❌ Also wrong: our jar centred, hero-lit, shallow depth of field, hand-placed (that's a product ad, and the camouflage collapses).

## What NOT to do with these

- **Do not restyle the packaging to match a mood.** If a prompt calls for a cool clinical bathroom, the jar is still amber, black and copper-gold. The product does not change to suit the scene.
- **Do not put the lip mask in a native/object-discovery shot.** It belongs in the offer creative only. In a native scene it reads as a second product and breaks the one-jar story that every converter runs on.
- **Do not add badges, starbursts, price flashes, or overlay text.** Real branding on a real object is good; added design furniture is a different thing and still kills the native read.
- **Do not describe the label as "plain," "simple," or "unbranded."** It is none of those.

## Where this is used

| File | Block |
|---|---|
| `batch-31/copy/B31C1` | A (quick description — jar is one of two objects) |
| `batch-31/copy/B31C2` | A (quick description) |
| `batch-31/copy/B31C3` | A (quick description) |
| `batch-31/copy/B31C5` | **A + B in full** — the offer creative, both products hero |
| `batch-32/copy/B32C1-C3` | A (quick description, only if a jar appears on the desk) |
| `batch-30/copy/Reformulated_Balm_Image_Prompts.md` | A in full |
