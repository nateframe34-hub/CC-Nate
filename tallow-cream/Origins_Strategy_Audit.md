# Origins Strategy Audit — Holistic

**Date:** 2026-05-21
**Scope:** Current state of all tallow project work assessed against the Origins framework
**Pairs with:**
- `tallow-cream/avatars/Origins_Framework_Audit.md` (avatar-level audit, 2026-05-13)
- `tallow-cream/sub-avatars/Sub_Avatar_Roster.md` (Sub-Avatar documentation)
- `tallow-cream/Tallow_Ad_Creative_Principles.md` (locked ad principles)

---

## Executive Summary

The core strategy is well-aligned with Origins. Where we deploy the framework explicitly (ad creative, Sub-Avatar building, mechanism delivery), we follow it correctly. The gaps are mostly in adjacent surfaces (PDP, partner page positioning, identity strategy) where the work predated the Origins audit and hasn't been brought into alignment yet.

**Big-picture finding:** We are deploying two of the three Stage 4-5 strategic responses well (New Mechanism + New Information). We are not yet deploying the third (New Identity) in a deliberate way. That's probably correct for our scale.

**Biggest specific risk:** PDP copy uses "menopause," "menopausal," and "60% less" in body and reviews. These are banned in ad creative per `Tallow_Ad_Creative_Principles.md`. If Meta re-reviews ad-to-landing-page consistency, this could blow back on the ads even though the ads themselves are clean.

---

## Where We Are Aligned With Origins

### 1. Mass Desire Identification — STRONG

Origins: "Mass Desire = the public spread of a private want. You cannot CREATE desire. You can only CHANNEL existing desires onto your product."

Our work: "I want to be seen again" is a real, pre-existing desire that millions of women 45-65 share. It maps to Origins' permanent forces of Relationships (primary) and Status (secondary). It existed before us. We channel it.

### 2. Two-Product Reality (Physical vs Functional) — STRONG IN ADS, PARTIAL IN PDP

Origins: "People don't buy your physical product. They buy what your product DOES for them."

Our ads: Identity-level payoffs close on functional outcomes (being seen, not-checking, not-carrying), not physical features. All 4 converters + B15 batch follow this. Strong alignment.

Our PDP: Hero section says "For skin that changed and nothing else works." Functional. Good. But Section 3 leans heavy on physical features (ingredients list, "What's In / What's Out"). This is a feature-led section in a Stage 4-5 market — defensible if the features support the mechanism, but worth checking whether the proportion of physical-features to functional-outcomes feels right.

### 3. Mechanism Deployment — STRONG (Stage 4-5 strategic response)

Origins: "Stage 3-5 dominate modern eCommerce. Success requires introducing new mechanisms explaining HOW products work differently."

Our work: Tallow-as-skin's-own-oil-structural-match is a New Mechanism. "Skin makes oil, after 40 makes less, water can't replace oil" is the New Information layer. Both deployed in ads. PDP Section 4 ("Your skin isn't dry. It's starving.") delivers the same mechanism content.

Alignment is strong because we use BOTH New Mechanism AND New Information together. Most brands deploy one or the other. We deploy the combination.

### 4. Avatar Building (5 Categories, in Order) — STRONG (per recent audit + Sub-Avatar work)

Origins: "Start with Desire, NEVER demographic. More categories combined = more specific Sub-Avatar."

Our work: 11 Sub-Avatars documented (`tallow-cream/sub-avatars/`), each with all 5 categories layered. Demographics-led avatars deprioritized (Postpartum Mom, Tween Daughter's Mom parked). Desire-first targeting is the standard. ✓

### 5. Sub-Avatar Discipline — STRONG (recent)

Origins: "At $0-100k/month: ONE Core Desire, MANY Sub-Avatars."

Our work: Core Desire locked to "I want to be seen again." 11 Sub-Avatars built around it. 5 other Core Desires (Working Hands Man, Eczema Fighter, Postpartum Mom, etc.) parked. This was a deliberate alignment move on 2026-05-13.

### 6. Permanent Forces / Mass Instincts Hit — STRONG

Origins ranking: Health > Status > Relationships > Comfort > Control > Belonging.

Our positioning:
- **Relationships** (primary) — being seen by spouse, sister, friends
- **Status** (secondary) — being respected as still-visible inside relationships
- **Health** (background) — skin functioning correctly is an implicit Health benefit

These are three of the top three Origins-ranked permanent forces. Strong fit for purchase-motivation strength.

### 7. Verbatim Language Alignment — STRONG IN CONVERTERS

Sub-Avatar files pulled verbatim language directly from validated ad copies. Each Sub-Avatar has documented "Words she'd embrace" and "Words she'd reject" lists. The killed-batch failure analysis enforces "tight," "cracking," "rested," "different" while banning "anti-aging," "wrinkles," "luxurious," etc. ✓

---

## Gaps and Risks Against Origins

### 1. PDP Compliance Inconsistency — RISK

`Tallow_Ad_Creative_Principles.md` bans these phrases in ad creative:
- "menopause," "perimenopause," "hormones," "estrogen"
- Body stats with percentages ("a lot less" not "60% less")

The PDP (`store/copy/PDP_Copy_v2.md`) uses all of these:
- Section 4: "After menopause, it can drop even further." + "After 40, your body produces up to 60% less of it."
- Review Block 1 (Karen M.): "I'm 54 and menopausal."

**Origins angle:** This is less an Origins problem and more a brand-voice-consistency problem. But it has a real-world consequence: Meta's ad-policy review looks at landing-page content when evaluating ad approvals and ongoing ad delivery. A clean ad pointing at a PDP that uses banned language can trigger ad-policy strikes after the ad is already running. That's a hidden risk to the upcoming launch.

**Fix:** Audit and rewrite PDP Section 4 + review block 1 to mirror ad-creative voice. "After 40 your skin makes a lot less of it" instead of "60% less." Remove "menopausal" from reviews (or edit the review to say "I'm 54 and my skin changed" with similar impact).

### 2. PDP Mass-Reach Hero Line — MILD WEAKNESS

The hero says "For skin that changed and nothing else works."

Origins at $0-100k/month: "The lower the revenue, the MORE specific you need to be."

The hero is broad enough that it works for the entire Invisible Woman Core, but it doesn't speak to any specific Sub-Avatar. Per Origins, broad positioning is something brands EARN. We haven't earned it.

**Mitigation:** This is probably fine because the PDP is the destination after the ad does the avatar-narrowing work. The ad targets a specific Sub-Avatar (Husband-Noticed, Photo Avoider, etc.). The PDP can be broader because the avatar has already self-selected by clicking through.

**But:** if you ever test sub-avatar-specific PDPs (e.g., a Photo Avoider PDP that opens with "you're not in the family photos anymore"), that would lift conversion meaningfully per Origins logic.

### 3. New Identity Strategy — GAP, BUT NOT URGENT

Origins: "The New Identity strategy creates emotional connections through lifestyle movements, focusing on WHO customers become rather than what products do."

We're using New Mechanism + New Information. We're NOT really deploying New Identity. Julie Brennan as the partner page is identity-adjacent but isn't a movement. There's no "join the women who chose less" tribal positioning.

**Per Origins:** "Identity strategies fail when positioning feels inauthentic, values misalign with actual brand behaviour, or attempts to appeal to everyone result in meaningless positioning. New Identity demands brand strategy expertise, influencer relationship building, and authentic storytelling capabilities."

**Fix:** Don't fix this yet. Building a real New Identity movement requires resources we don't have at <$1k in lifetime sales. Stay locked on New Mechanism + New Information until 10+ converters validate the path. Then consider an identity move (anti-influencer simple-skincare movement, "real woman" brand, etc.).

### 4. Forces of Change Underused — MINOR GAP

Origins: "Forces of Change = What Changes How The Permanent Desires Are Fulfilled. Style Trends (what becomes fashionable) and Mass Education (what society learns)."

We use Mass Education well (the "skin makes its own oil" reframe is education). We use Style Trend somewhat (ingredient transparency, anti-routine simplicity).

**The gap:** We could lean harder on the Style Trend of "ingredient simplicity" and "anti-skincare routine" as cultural movements. The 4-ingredient framing is Origins' Style Trend + Mass Education combined ("Why are you still using 14 products in 2026?" type framing). Not currently deployed.

**Fix:** Possibly worth a future ad concept. Hook: cultural critique of the 14-product routine. But this is more an opportunity than a fix.

### 5. Avatar-Market Sophistication Gap — RESOLVED IN ADS, UNTESTED ELSEWHERE

Origins: "Even though your avatar is perfectly defined, the desires are crystal clear, and your product actually delivers — you fail to communicate with those avatars in a way that breaks through the sophistication level."

Our ads have addressed this through density (10-element converter skeleton), Sub-Avatar specificity, and mechanism layering. Per the killed-batch failure analysis, this is the primary mechanism by which our killed ads failed and our converters succeeded.

**Untested:** Whether the PDP, abandoned-cart email, and partner-page content also pass the Avatar-Market Sophistication Gap. The PDP probably mostly does because it inherits the ad's voice. The partner-page warmup content is generic pet-photo engagement (which is correct for warmup but doesn't address the gap). The abandoned-cart email is drafted but unimplemented.

### 6. Beliefs Treatment — PROBABLY CORRECT

Origins: "Beliefs are derivative of Experience + Emotion + Behaviour. Not a separate category."

Our work: We don't have a "beliefs" category in our Sub-Avatar templates. ✓ Aligned.

We do have a `Clean Eater` avatar that was flagged in the avatar audit as belief-led (food/skincare consistency). The recommendation was to re-derive it from E+E+B or kill it. Currently parked. ✓ Aligned with Origins.

### 7. Mechanism Overcomplication — RISK TO MONITOR

Origins: "The biggest mistakes people make with this are over-technical communication that alienates audiences, claiming false uniqueness for industry-standard processes, and explaining mechanisms without connecting to customer value."

Our ads keep the mechanism at ~100-150 words and connect it to customer value (the day-marker transformation and habit-cessation beats). ✓

The PDP's Section 4 ("Your skin isn't dry. It's starving.") delivers the same mechanism. Length is appropriate. Connection to customer value is the line "That's the difference between a moisturizer that disappears by noon and one that lasts all day."

**Watch for:** any future creative that turns the mechanism into a lecture. The "I'm still angry about it" B3C2 variant skirts this risk — it's mechanism-heavy and was killed for low ROAS. We need to keep mechanism delivery character-driven, not narrator-driven.

---

## Specific Recommendations

### Priority 1 — Fix Before Launch (~May 27)

1. **PDP Section 4 rewrite.** Remove "menopause" and "60% less." Replace with ad-voice equivalents ("after 40," "a lot less"). 30 minutes of work.
2. **Review Block 1 rewrite.** Karen M.'s review says "I'm 54 and menopausal" — rewrite to "I'm 54 and my skin completely changed" or similar. Keeps the avatar signal without the banned phrase. 5 minutes.
3. **Verify ad-landing-page voice consistency before Meta upload.** When you upload the B15 ads, click through to the PDP from each ad and read it as the avatar would. Make sure nothing on the PDP undoes what the ad established.

### Priority 2 — Strategic, Pre-Scale

4. **Decide on a Sub-Avatar-specific PDP test for the post-validation phase.** Once one Sub-Avatar consistently converts (say, Husband-Noticed gets 10+ sales on the new Portfolio), build a Sub-Avatar-specific PDP that opens with that Sub-Avatar's verbatim language. Test against the broad PDP. This is the next-level Origins move.
5. **Defer New Identity strategy until 10+ converters.** Don't try to build a "women who chose less" movement now. Stay on New Mechanism + New Information through B15-B18.

### Priority 3 — Watchlist (Future Work)

6. **Forces of Change opportunity.** Future B16/B17 batch could test a Style Trend + Mass Education hook: "Why are we still using 14 products in 2026?" Cultural-critique angle. Not yet, but flagged.
7. **Partner page content evolution.** Julie's page currently runs warmup content (pet photos). After the engagement campaign serves its purpose, Julie's content should evolve toward "what I've figured out at 48" type content that aligns with the simple-skincare positioning. This is unrelated to Origins but flagged for completeness.
8. **Identity-aware customer service.** When customers buy, the post-purchase emails could use Sub-Avatar-aware language. Different welcome series for Photo Avoider buyers vs Husband-Noticed buyers. Premature now, valuable later.

---

## What's NOT Worth Fixing Right Now

Origins-adjacent concerns that are real but premature at our scale:

- **Influencer relationship building** (New Identity prerequisite)
- **Cultural movement positioning** (New Identity prerequisite)
- **Sub-Avatar-segmented email automation** (post-purchase optimization)
- **Multi-PDP testing** (requires meaningful conversion volume first)
- **Tribal community building** (requires sustained engagement first)

All of these become important at $10k/month and beyond. Not now.

---

## Origins Alignment Summary

| Origins concept | Alignment | Notes |
|---|---|---|
| Mass Desire identification | Strong | "Be seen again" is real, pre-existing, mapped to top permanent forces |
| Two-Product Reality | Strong in ads, partial in PDP | PDP has more feature-focus than functional-focus in some sections |
| New Mechanism | Strong | Tallow-as-skin-oil-structural-match deployed in ads + PDP |
| New Information | Strong | "Skin makes oil, water can't replace it" reframe deployed in ads + PDP |
| New Identity | Not deployed | Probably correct for our scale; defer until post-validation |
| Avatar building (5 categories, in order) | Strong | Sub-Avatar roster locked, demographics deprioritized |
| Sub-Avatar discipline (one Core, many Subs) | Strong | 11 Sub-Avatars under "Be Seen Again" Core Desire |
| Permanent forces hit | Strong | Relationships + Status + Health background |
| Verbatim language alignment | Strong | Sub-Avatar files pulled from actual ad copies |
| Avatar-Market Sophistication Gap closure | Strong in ads | 10-element converter skeleton addresses this in ads. PDP and email less audited. |
| Beliefs as derivative (not a category) | Aligned | No "beliefs" category in our templates. |
| Mechanism overcomplication risk | Watchlist | B3C2 skirted this; killed. Watch for future creative that lectures. |
| Forces of Change deployment | Partial | Mass Education used well. Style Trend underutilized. |
| Compliance / banned-phrase consistency across touchpoints | RISK | PDP uses "menopause" + "60% less" in body + reviews. Banned in ads. Worth fixing before launch. |

---

## Bottom Line

Where we deploy Origins explicitly, we do it correctly. Where we deploy it implicitly (PDP written before the Origins audit, partner page warmup content), there are small inconsistencies worth fixing.

The biggest concrete item to fix before launch: PDP Section 4 + Review Block 1 use phrases banned in ad creative. Quick rewrite eliminates a real risk to ad delivery.

Everything else is either already aligned or premature optimization.
