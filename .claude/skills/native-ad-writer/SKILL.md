---
name: native-ad-writer
description: Write long-form native/camouflage Facebook and Instagram ads using the 5-phase Origins framework. This skill should be used when the user wants to write native ads, camouflage ads, long-form primary text ads, or any Meta ad that reads like a personal story instead of a brand pitch. Typical invocations include "write a native ad for [batch/avatar/angle]", "use the native writing skill to make BXCX", "write a camouflage ad", or "write a long-form primary text ad". Produces the body copy, Meta headline, Meta description, and a Nano Banana Pro image prompt as a single deliverable.
---

# Native Ad Writer

## Purpose

Generate complete long-form native primary text ads for Meta (Facebook/Instagram) following the 5-phase Origins native ad framework. Each ad reads like a personal confession from a real person, not a brand pitch, and is engineered to stop the scroll, shift belief, and make the click feel natural.

The skill produces four outputs in a single deliverable:

1. **Body copy** — flexible length (600–1,800+ words, no hard cap; length follows the story, not a target)
2. **Meta headline** — max ~27 characters
3. **Meta description** — max ~27 characters
4. **Nano Banana Pro image prompt** — for the creative that pairs with the ad

## When to Use

Trigger this skill when the user mentions any of:

- "write a native ad"
- "write a camouflage ad"
- "use the native writing skill"
- "write a long-form primary text ad"
- "batch X native ad for [avatar]"
- "write BXCX" (e.g., "write B3C1", "make me B2C2")
- "hey claude I want to start working on Batch X..."

Do NOT trigger for: short-form static ads, video ad scripts, banner copy, VSL scripts, product description copy, landing page copy, or email copy. Those need different formats and frameworks.

## The Prime Directive

The single rule that carries through every decision in every phase:

> **The reader is not evaluating the product. The reader is evaluating the person talking to them.**

Every technique in this skill exists to make the narrator feel like a real person. If the narrator feels real, the product gets trusted by extension. If the narrator feels fake, no copy trick can save it.

## Workflow

Follow these steps in order. Do not skip steps.

### Step 1: Parse the Invocation

Extract from the user's message:

- **Batch and creative number** (e.g., "B3C1")
- **Target avatar** (e.g., "The Invisible Woman", "The Product Graveyard")
- **Angle/direction** (e.g., "dermatologist reveal", "husband noticed", "skeptic convert")
- **Hook direction** (if specified)

If any of these are missing and not derivable from context, ask for them before proceeding.

### Step 2: Auto-Load Research Files

Check the repo for existing research in conventional locations. Use Glob to search these patterns in order:

1. `{current-project}/avatars/**/*.md`
2. `{current-project}/*/avatars/**/*.md`
3. `{current-project}/research/**/Avatar*.md`
4. `{current-project}/*/research/**/Avatar*.md`
5. `{current-project}/*/tracking/Avatar*.md`

Also look for:
- Any file matching the pattern `*Avatar_Language*`, `*Language_Research*`, or `*avatar*blueprint*`
- Any file matching `Sub_Avatar_*` or `sub-avatar*`

When found, Read only the avatar file matching the target sub-avatar and the language research file (if one exists). Do NOT load all avatar files — only the one being targeted.

### Step 3: Confirm Inputs Are Sufficient

Before writing, verify the following inputs exist (from research files or user input):

**Required:**
- Target sub-avatar name and core desire
- Chosen angle (what reason-to-buy drives this specific ad)
- Product name, mechanism (how it works), and offer details
- At least 5 verbatim customer language phrases

**Strongly preferred:**
- Dominant emotion (the 2am thought, not surface complaint)
- Awareness level (Problem Aware / Solution Aware / Product Aware)
- 1–2 "spike moments" (specific situations where the pain hits hardest)

If required inputs are missing, stop and ask the user for them. Do not guess.

### Step 4: Load the Reference Files

Load the reference files for all 5 phases. Each file is ~400 words of actionable rules:

- `references/phase-1-research.md` — audience diagnosis and emotional map
- `references/phase-2-story-elements.md` — character, theme, setting, low point, transformation, dialogue
- `references/phase-3-reader-psychology.md` — pacing, contrast, emotional sequencing, open loops, pattern interrupts, trust ladder
- `references/phase-4-hooks-and-close.md` — hook formats, close formats, awareness matching
- `references/phase-5-image-psychology.md` — 3 image types, POV rule, Reddit caption test
- `references/key-principles.md` — the prime directive and 8 rules that override everything
- `references/compliance-and-readability.md` — **MANDATORY** — the 6 middle-ground rules, vocabulary swap table, 6th-grade reading level mechanics, and worked rewrite example. Load this on every invocation. Health-adjacent categories (skincare, supplements, wellness) will trigger Meta's scanner without it.
- `references/element-density.md` — **MANDATORY** — the 10-element density rule with counting rubric. Every ad must stack 8 of 10 elements before delivery. Load this on every invocation. Under-dense ads can win on engagement OR conversion but not both.
- `references/doctor-ad-example.md` — **MANDATORY** — the canonical fully-annotated reference ad, showing all 10 elements in action. Load this on every invocation as the structural benchmark for density counting.
- `references/self-audit-checklist.md` — the final quality gate before delivering

### Step 5: Plan Before Writing

Before writing a single word of body copy, answer these questions in a brief internal plan. Do not expose this plan to the user unless asked.

1. **Character type:** Peer, Authority, Skeptic Convert, or some combination?
2. **Theme (the 2am question):** What deeper question is this ad answering? State it in one sentence. This stays unspoken in the copy but drives every beat.
3. **Awareness level:** Problem / Solution / Product Aware
4. **Hook format:** Which of the hook formats best matches the awareness level and angle? (See `phase-4-hooks-and-close.md`)
5. **Inciting incident:** What specific moment opens the story? (NOT a summary — a scene)
6. **Low point:** What's the moment of resignation that matches where the reader actually is? **Must use an external witness, not internal shame/hiding behaviors.** (See `compliance-and-readability.md` Rule 2.)
7. **Secondary characters:** Who validates what? **Must have 3–4 named characters, each doing different work** — friend who recommended it, partner/spouse noticing, adult child, different use case. (See `element-density.md` element 5.)
8. **Close format:** How will the close connect back to the hook? **Use social proof ("a lot of women I know say the same thing"), not direct targeting ("if you're X, Y, Z").** (See `compliance-and-readability.md` Rule 5.)
9. **Image type:** Object / Evidence / Isolation?
10. **Compliance pre-write check:** Run the pre-write checklist in `compliance-and-readability.md`. No menopause/perimenopause. No "your body"/"your skin" diagnostic claims. No symptom words in the planned content. No dermatologist/doctor character endorsing the product. No "if you're X" close. If any of these are in the plan, rewrite the plan before writing a word of body copy.
11. **Element density pre-write count:** Before writing, list the 8+ elements from `element-density.md` you plan to include. Name each one specifically:
    - ☐ Multi-mechanism hook (which 3+ mechanisms?)
    - ☐ Specific inciting incident scene (what scene, what characters, what time?)
    - ☐ Product mention placed after belief shift (~50–65% mark)
    - ☐ Escalating stakes (name 3+ escalation beats)
    - ☐ Multiple secondary characters (name each one and what they validate)
    - ☐ Trust ladder (list the 4+ rungs from observable → bigger claim)
    - ☐ Pattern interrupts every 200–300 words (estimate count for planned length)
    - ☐ Skeptic convert frame (what objection, addressed by whom?)
    - ☐ Progressive transformation (timeline beats + unexpected discovery + external validation + identity-level payoff)
    - ☐ Close mirrors the hook (how?)
    
    **If you can't name 8 elements with specifics, rewrite the plan before writing a word of body copy. Under 8 = thin ad. Don't draft thin ads.**

### Step 6: Write the Body Copy

Write the full ad following the Phase 2 story structure and Phase 3 reader psychology principles simultaneously. Key execution rules:

- **Open with a scene, not a summary.** The first 3 paragraphs should place the reader in a specific moment.
- **Belief shift BEFORE product mention.** The new information about why past solutions failed must appear before the product gets named. The product should not appear until roughly 50–65% through the ad.
- **Vary sentence length.** Short fragments for urgency. Longer sentences for mechanism. Read it out loud mentally. **Average under 15 words per sentence** — this is the 6th-grade reading level cap from `compliance-and-readability.md`.
- **Embed contrast throughout.** Not just a before/after at the end — small before/after moments in every section.
- **4–6 emotional alternations.** Low → high → low → high. Not two big blocks.
- **Open loops pulling forward.** Always something unresolved.
- **Pattern interrupt every 200–300 words.** Emotional shift, confession, dialogue, or format change.
- **Build a trust ladder.** Observable truths → common knowledge → new information → bigger claims → biggest claim.
- **3–4 secondary characters minimum.** Each validating something different. **At least one of them is an external witness to the change** (husband, daughter, friend, coworker noticing) — this replaces internal shame/hiding behaviors per `compliance-and-readability.md` Rule 2.
- **Use verbatim audience language** from the research files. Don't paraphrase customer pain into marketing speak. **But never port over flagged phrases** — if a customer quote contains "menopause," "your body stopped," or symptom words, paraphrase around the flag while keeping the emotional core.
- **Transformation must include:** progressive timeline, unexpected discovery, external validation, identity-level change.
- **Functional over physical descriptions.** Describe what the body/skin DOES ("makeup cracking by 11am," "lotion disappearing in an hour") not what it LOOKS LIKE ("crepey," "papery," "flaky"). See `compliance-and-readability.md` Rule 3.
- **First-person discovery over second-person diagnosis.** The narrator learns something; the reader overhears. Drop "your body" / "your skin" entirely and use general observations the reader personalizes themselves. See `compliance-and-readability.md` Rule 4.
- **6th-grade vocabulary throughout.** Cut jargon, adverbs, passive voice. If a 12-year-old wouldn't know a word, replace it. See `compliance-and-readability.md` reading level mechanics.

### Step 7: Write the Meta Headline and Description

Both are max ~27 characters (safe truncation). Neither should feel salesy — they should reinforce the native tone of the body copy.

- **Headline:** Should echo the story's emotional core, not pitch the product. Sound like something a friend would say in passing.
- **Description:** Put practical reassurance here (60-day guarantee, free shipping, no subscription, X ingredients). This is where the offer safety lives.

### Step 8: Write the Nano Banana Pro Image Prompt

Follow `references/phase-5-image-psychology.md`. The image must be one of:

- **Object:** The thing they stare at daily
- **Evidence:** The private proof no one else sees
- **Isolation:** The moment they're alone with the problem

NEVER generate prompts for:
- Beauty photography or editorial skincare shots
- Faces performing emotion (crying, frustrated posing)
- Product hero shots with styled lighting
- Stock-photo composition
- Images with text overlays or labels

The image must pass the **Reddit caption test**: would it make sense posted to Reddit with "dealing with this shit again" as the caption? If not, rewrite the prompt.

Default aspect ratio: **4:5 (1080 × 1350)** for Meta feed.

### Step 9: Self-Audit Before Delivering

Run the full deliverable against `references/self-audit-checklist.md`. Silently check every item. If any item fails, fix it before delivering. If a failure cannot be fixed without more information, flag it to the user.

### Step 10: Deliver

Output all four pieces as a single deliverable in this exact structure:

```
# [BXCX — Ad Name]

**Sub-Avatar:** [name]
**Angle:** [one-line description]
**Character type:** [Peer / Authority / Skeptic Convert / etc.]
**Hook format:** [format name]
**Awareness level:** [Problem / Solution / Product Aware]

---

## Body Copy

[Full ad copy here — flexible length, no hard cap]

---

## Meta Headline
[max ~27 chars]

## Meta Description
[max ~27 chars]

---

## Image Prompt (Nano Banana Pro)

**Type:** [Object / Evidence / Isolation]
**POV:** [first-person / observer]

[Full prompt — ready to paste into Nano Banana Pro]

**Aspect ratio:** 4:5 (1080 × 1350)
```

## Critical Reminders

1. **Length follows density, not the other way around.** Stacking 8+ elements at sufficient depth requires 1,200–1,800 words. Ads significantly shorter than this cannot structurally fit 8 elements. Do not pad a short story to hit word count — fix the density instead. Do not truncate a dense story to fit a cap.

2. **The product should not appear until the belief shift lands.** In most ads, this is around 50–65% through the copy. Before that, the reader should be getting new information about why their past solutions failed, not being sold to.

3. **Confession tone, not testimonial tone.** The narrator is sharing because they wish someone had told them sooner. They are not reviewing a product.

4. **Specificity = credibility.** Numbers, timeframes, real product names of things that failed, sensory details, names of secondary characters.

5. **Don't exaggerate the pain.** The reader should think "that's my skin" not "thank god my skin isn't that bad." Normal dry skin, not a medical condition. Normal frustration, not crisis.

6. **Never break native tone in the close.** The click should feel like a natural next step, not a sales pitch interruption.

7. **Compliance is craft, not censorship.** Meta's 2026 scanner penalizes direct diagnostic claims ("your body stopped making X"), negative self-perception framing (hiding/avoiding/shame behaviors), symptom-based descriptions ("crepey," "papery," "flaky"), second-person health assertions ("your skin is starving"), hormonal/menopause language, and indirect targeting ("if you're X"). None of these are what makes native copy convert. Specificity, external witnesses, functional observations, and first-person discovery are. The constraints make the copy better, not worse. See `compliance-and-readability.md` for the 6 middle-ground rules, vocabulary swap table, and worked rewrite example.

8. **6th-grade reading level always.** Average sentence under 15 words. No jargon ("sebum," "transepidermal," "fatty acid profile"). No adverbs on the strike list ("actually," "basically," "literally," "really," "very"). Active voice. One idea per sentence. Concrete nouns. If a 12-year-old wouldn't know a word, replace it. Read the copy out loud mentally — if you stumble, simplify.

9. **Element density is the single highest-leverage structural rule.** Every ad must stack 8 of 10 elements from `element-density.md`. The course's reference ad (Doctor Ad) stacks all 10. Our historical best has been 5. The gap between 5 elements and 10 elements is not "polish" — it's a structural rewrite. Thin ads fail on either engagement (CPMs) or conversion (ROAS), sometimes both. Dense ads win on both. **Count elements during planning AND after drafting.** Under 8 = rewrite, not fix. See `element-density.md` for the full rubric and `doctor-ad-example.md` for the annotated reference.
