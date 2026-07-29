# Reformulated Balm (V2) - Product Photography Image Prompts, IN DEPTH

**Date:** 2026-07-21
**Purpose:** Real product/lifestyle photography prompts for the reformulated balm (new supplier, raw honey + essential oils, 60g, denser-but-still-soft texture), matching the depth/format of the B30 ad-creative prompts. These are for the PDP (`tallow-pdp-v2-reformulated.liquid`'s hero/lifestyle/texture image settings), not ad creative, this is the product photography gap flagged in HANDOFF as still open before the reformulated PDP can go live.
**Note on references:** if generating from a physical sample or the supplier's own product photos as a reference, treat any reference image as a PRODUCT/PACKAGING reference only (jar shape, cap, color, texture), same caution as the Sarah face-reference issue, don't let a reference photo's background/setting/lighting bleed into a scene that's supposed to be different (e.g. the supplier's studio product shot shouldn't drag its studio lighting into a lifestyle bathroom-counter shot).

---

## 1. Hero product shot (jar, standalone)

**Purpose:** Primary PDP gallery image, the main "what you're buying" shot. **Corrected AGAIN 2026-07-29 against founder reference photos:** the 7/21 version described the ROUND LID label as if it were the main body label. The real jar has BOTH: a rectangular black-and-copper-gold body label with the bee, AND a separate round label on the lid top. Prompt 1 now specifies both correctly. **Corrected 2026-07-21:** the first version of this prompt described a kraft-paper label carried over from the OLD product's aesthetic, wrong for this jar. Founder confirmed the supplier's own label/branding is being kept as-is (not relabeled), so this prompt now matches the REAL packaging: amber glass jar, black ribbed screw-top lid, a round label with a black background and a thin gold/orange circular border, a line-art bee illustration at the top, the "wiyun" wordmark, "TALLOW HONEY BALM" title in gold serif caps, a small ingredients line, and "NET: 60G/2.12 OZ" near the bottom. Use the actual supplier product photo as a packaging/label reference (jar shape, cap, label design, exact text), not a scene reference.

```
An ultra-realistic professional product photograph, wide shot, zoomed out slightly, of a squat wide-mouthed amber glass jar with a matte black ribbed screw-top lid, matching the real "wiyun Tallow Honey Balm" packaging. THE BODY LABEL IS RECTANGULAR, not round: a matte black rectangular label wrapping the front of the jar, edged with a thin double-rule copper-gold border dividing it into stacked panels. Upper panel: "TALLOW HONEY BALM" in copper-gold serif capitals, letterspaced, on two centred lines. Centre panel: a single detailed gold line-art honeybee with wings spread, centred, the visual anchor of the label. Lower strip: "wiyun" in white lowercase sans-serif on the right, with a small bordered box beneath reading "NET: 60G/2.12 OZ". Separately, on the flat TOP of the black lid, a round black label with a thin copper-gold ring border containing "wiyun", a small bee, "TALLOW HONEY BALM" in gold serif caps, a small ingredients line, and "NET 60G/2.12 OZ". The jar sits centered on a clean, matte, warm off-white stone or ceramic tabletop. Soft, diffused natural window light from the upper left, gentle shadow falling to the lower right, no harsh reflections on the glass or the label. The jar is closed, lid on, label facing forward and fully legible, shot with enough negative space around the jar that it reads as a real product photo, not a cropped macro shot. Warm, neutral color grade, no cool blue tones, no overly saturated "clean beauty" pastel styling. Real studio-quality but not sterile, the kind of clean e-commerce product shot a small ingredient-forward skincare brand would actually use. No people, no hands, no additional text overlays beyond what's already on the real label, real branding on any object stays visible. Square or 4:5 crop (1080 x 1080 or 1080 x 1350).
```

---

## 2. Open jar, texture visible

**Purpose:** Shows the actual product texture. **Corrected AGAIN 2026-07-29 against founder reference photos:** the 7/21 version described the ROUND LID label as if it were the main body label. The real jar has BOTH: a rectangular black-and-copper-gold body label with the bee, AND a separate round label on the lid top. Prompt 1 now specifies both correctly. **Corrected 2026-07-21:** matched to the real supplier photo, which shows the open jar with a smooth, glossy, pale-gold surface holding a soft swirled peak where it was scooped/filled, a naturally-occurring soft peak from filling, not styled to look airy or whipped-mousse-like. Also updated the lid/label description to match the real black lid and black-and-gold label, plus the jar's dark amber glass showing partial label text around its side.

```
An ultra-realistic close-up professional product photograph of the same amber glass jar, black ribbed lid removed and resting just out of frame to the side, showing the balm's actual surface texture from directly above at a slight angle. The texture reads as a smooth, glossy, pale ivory-to-gold cream with a single soft swirled peak near the center, similar to how a filled product naturally settles, not sculpted or piped, not airy or mousse-like, dense enough to hold its shape without slumping. Warm ivory-to-pale-gold color, consistent with a tallow-honey base, subtle natural color variation, not perfectly uniform (real product, not CGI). Soft, warm side lighting that catches the slight glossy sheen of the balm's surface without blowing out highlights. The jar's own black-and-copper-gold rectangular body label with the line-art bee is partially visible around the side of the glass, out of focus. Background is the same soft, out-of-focus warm tabletop as the hero shot for visual consistency across the gallery. No hands, no additional text overlays. Square or 4:5 crop.
```

---

## 3. Texture on skin, application/absorption proof

**Purpose:** Replaces the old "whipped, melts like warm honey" sensory claim with an accurate one for the denser texture, this shot should show a small amount worked into skin, softening/melting slightly with warmth, without implying the old whipped-mousse consistency.

```
An ultra-realistic close-up photograph of a small dollop of balm on the back of a hand or inner forearm, mid-application, fingertips visible gently working it into the skin. The balm should show a slightly melted, glossy sheen where finger warmth has softened it, translucent at the thinnest edges, still visibly a dense product rather than a light lotion, real skin texture visible (not airbrushed), natural skin tone, no visible jewelry or nail polish to keep focus on the product. Soft, warm, natural window light, slight editorial quality but still candid rather than clinical/lab-style. No face, no identifying features, hand/forearm only. Real iPhone-adjacent photo quality with a touch more polish than the native ad photos (this is PDP/product photography, not ad creative, so slightly more produced is appropriate here). No text, 4:5 (1080 x 1350).
```

---

## 4a. Popup image (email-capture modal, 16:9)

**Purpose:** Fills the `popup_image` setting slot at the top of the welcome/discount popup modal (`.tlw-popup-img`, hardcoded to a 16:9 crop). This is the first thing a visitor sees when the popup fires, needs to be an inviting, clean hero-style shot, wide format, not a tall vertical crop of the other prompts. Same real packaging as the hero shot (black lid, black-and-gold "wiyun" label).

```
An ultra-realistic professional product photograph, wide 16:9 landscape composition, of the amber glass jar with its black ribbed screw-top lid and black-and-copper-gold rectangular "wiyun Tallow Honey Balm" body label (bee illustration, gold serif type), positioned slightly off-center to the left third of the frame per standard product-photography composition, with generous soft-focus warm negative space to the right where a modal's text/button would visually sit if overlaid separately (this image itself has no text baked in). Clean, warm off-white or soft cream backdrop, subtle matte stone or linen texture, soft diffused natural light from the upper left, gentle shadow, no harsh reflections on the glass or label. Real studio-quality but warm, not sterile or clinical. No people, no hands, no additional text overlays beyond what's on the real label, real branding on any object stays visible. 16:9 (1600 x 900).
```

---

## 4. Ingredient flat-lay (raw honey + essential oil emphasis)

**Purpose:** Supports the updated "4 ingredients" label section on the PDP (tallow, olive oil, essential oils, raw honey). Needs to visually communicate the REAL new ingredients honestly, raw honey (not manuka specifically, don't stage it to imply manuka) and a generic/neutral essential-oil visual (don't imply a specific oil like tea tree or citrus unless that's confirmed and you want it named, keep it visually generic if the exact oil composition isn't being called out on the label).

```
An ultra-realistic overhead flat-lay photograph on a warm, matte, light stone surface: a small jar of raw honey with a wooden honey dipper resting across it, a small glass cruet of olive oil, a tiny amber dropper bottle suggestive of essential oil (unlabeled, generic, no specific plant identifiable), and a small mound of rendered tallow or a small dish of the finished balm itself, arranged loosely, not in a rigid grid, natural gaps and slight overlaps like real ingredients set out to be photographed, not a sterile lab layout. Soft, warm, diffused natural light from one side, gentle real shadows. Muted, warm, earthy color palette (honey gold, olive green-gold, cream, amber glass), no bright saturated pops of color, no plastic-looking props. No text, no labels visible on any container beyond the honey jar's plain unbranded look, no people, no hands. This shot needs to read as honest ingredient documentation, not a styled "clean beauty" flat-lay cliche. Square (1080 x 1080).
```

---

## 5. Lifestyle context shot (bathroom counter, matches existing account visual language)

**Purpose:** Matches the account's existing "one jar on a counter" visual identity so the reformulated product still feels continuous with the brand, not a jarring reset. Same amber-glass-on-quiet-counter language used across B9C3/B17C1/B28's image prompts, adapted to the new jar's actual packaging (black lid, black-and-gold circular "wiyun" label, corrected 2026-07-21 from the old kraft-label description).

```
An ultra-realistic iPhone-quality candid photograph of the amber glass jar with its black lid and black-and-copper-gold rectangular body label with the line-art bee, sitting alone on a narrow bathroom counter, real domestic setting, not styled or staged, a folded hand towel and a simple unmarked soap pump softly out of focus at the edges of frame, faint natural counter clutter (a ring-mark from another bottle, a stray hair tie) suggesting a real lived-in space, not a magazine bathroom. Normal indoor bathroom lighting, slightly warm, not dramatic, not a ring light. Real iPhone grain, natural imperfect framing, shot from a slight downward angle as if someone glanced at it while getting ready. No people, no hands, no text overlays beyond the jar's own real label. This should feel continuous with the account's existing "one jar" visual identity, not a hard reset in photography style. 4:5 (1080 x 1350).
```

---

## Notes for whoever generates these

- Do not carry over any reference photo's background, lighting, or setting into a different described scene, same reference-handling rule as the B30C1 ad-image note, reference images are for jar shape/label/texture only, not scene composition.
- Keep the honey visually generic (do not stage it to imply manuka specifically) and the essential oil visually unidentified unless the exact oil composition is confirmed and the founder wants it named on the label and in these photos.
- These are PRODUCT photography (PDP gallery), not ad creative, slightly more produced/clean than the native-ad candid style is appropriate here, but should stay warm and real rather than sterile/clinical, consistent with the brand's existing visual language.
- Once real supplier or in-hand sample photos exist, these prompts can be dropped in favor of the real thing, they exist to fill the gap until then.
