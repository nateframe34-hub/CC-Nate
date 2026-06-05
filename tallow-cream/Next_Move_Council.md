# Next-Move Council — Highest-Leverage Move for the Waiting Period

**Date:** 2026-05-21
**Method:** 5 in-house agents (no external providers — IP stays in-house), each attacking "what's the highest-leverage move while waiting for budget" from a different lens. Goal held constant: profitable ROAS + most sales possible. Constraint held constant: little/no money, founder time is the resource.
**The 5 lenses:** Free-Traffic Operator · CRO · Retention/LTV · Foundation/De-Risk · Brutal Prioritizer

---

## The Headline: 5 of 5 Converged on the POST-CLICK FUNNEL

Every single agent, from its own angle, pointed at the same thing: the problem is not getting the click (the creative already wins that), it's what happens AFTER the click. The break is the landing page + offer + trust + tracking, not the avatars or the ads.

- **Brutal Prioritizer:** "48% CTR / 0 ATC. The market is screaming that the ad works and the destination doesn't. No hook survives a broken landing experience."
- **CRO:** "The story sold a feeling; the PDP sells a product. The emotional thread snaps in the first scroll." (message-match break)
- **Free-Traffic Operator:** "You have a recognition machine, not a sales machine. The fix is capturing the clicks that don't buy into an owned list." (post-click capture)
- **Retention/LTV:** "It's an acquisition-and-conversion problem wearing a retention costume. The highest-leverage retention asset is the one that doubles as conversion-and-trust infra." (post-click trust)
- **Foundation/De-Risk:** "Verify the pixel fires Purchase-with-value — it protects the entire budget AND the learning." (post-click instrumentation)

This is a stronger convergence than the avatar council (which was 4 of 5). And it's triangulated three ways:
1. This council (5/5)
2. The prior avatar council's Red Team (same conclusion)
3. **The founder's own HANDOFF reframe from May 11** ("the bottleneck is differentiation + why-this-$50-vs-$20") — the founder already diagnosed this himself a week ago

When five independent lenses, a prior council, and the founder's own earlier insight all point at the same wall, that's not an opinion. That's the answer.

---

## The Honest Caveat (raised independently by 3 of 5 agents)

At ~6-9 lifetime sales (one a $19.99 pricing error, several from an unattributable banned BM), the funnel "break" is **inferred, not proven**. The cleanest data is ~11-30 landing-page views and one add-to-cart. You cannot statistically distinguish "broken PDP" from "never bought enough traffic to surface a buyer by chance."

But this does not change the move — it sharpens it. The waiting-period fixes are all free and directionally right, and the ONLY way to resolve the uncertainty is **one clean, instrumented, 14-day run into a fixed funnel**. So the highest-value use of the wait is to build exactly the preconditions that make that eventual test legible. Fix the funnel now → the funnel fix is what makes the B16 test tell you the truth instead of more noise.

---

## THE MOVE: Fix the Post-Click Funnel

One project. Make every recovered ad dollar land on a compliant, message-matched, trust-dense page with a working offer and accurate tracking. Everything below is free founder-time.

### The sequence (ranked, with the keystone flagged)

**0. CONFIRM FIRST (5 min) — is BOGO actually built and the pixel actually verified?**
The founder stated earlier these were done; the repo/HANDOFF still lists them as pending and all agents read them as incomplete. Resolve the discrepancy before anything else. If they ARE done, skip steps 2-3 and go straight to the PDP/advertorial work. If NOT, they're top priority.

**1. PDP banned-phrase fix (~35 min) — do this first regardless.**
Section 4 ("up to 60% less" → "a lot less"; drop "After menopause") and Review Block 1 ("I'm 54 and menopausal" → "I'm 54 and my skin changed"). Pure founder-time, removes a Meta ad-policy tail-risk that feeds the very ban pattern killing this brand, and must be true before any traffic hits the page. Flagged by CRO, Retention, Foundation, AND Brutal.

**2. Build the BOGO native discount in Shopify** (Buy-X-Get-Y, no app — already documented) + paste the liquid block. Order matters: discount before liquid, or the live block charges full $99.98. This is the offer lever literally designed to beat the $50-vs-$20 objection, and it's sitting un-built.

**3. KEYSTONE — one real test purchase through the BOGO flow.** This single action validates THREE things at once (per the Foundation agent): (a) cart shows $99.98 → ~$74.99, (b) checkout carries the discount, (c) the pixel fires Purchase with the correct `value` ($74.99, cart-level not per-item) in Events Manager Test Events. Collapses the two biggest foundation risks into one 20-minute test.

**4. PDP conversion edits ($0, a few hours).**
- Swap the order of Sections 3 and 4 — deliver the mechanism ("Your skin isn't dry, it's starving") BEFORE the ingredient spec sheet. A story-warmed visitor needs the next emotional/mechanism beat, not a what's-in/what's-out list.
- Add money-math at the CTA: "One jar lasts 2-3 months. About 55 cents a day." Directly answers the $50-vs-$20 objection at the decision point.
- Pull the 60-day guarantee badge UP next to the hero CTA (currently buried in Section 8).
- Fix the reviews: cut/replace Review Block 4 (the 9-year-old's arm patches — wrong avatar on a $50 face cream for a 55-year-old). Lead with husband-noticed / "threw out 8 products" reviews that match the converter avatars. Make the displayed review count honest.

**5. THE BIGGER SWING — a story-form advertorial / pre-sell bridge page.**
This is the CRO agent's top pick and the root fix for the message-match break. Instead of routing ads straight to the conventional PDP, route them to an advertorial that continues the ad's voice → delivers the mechanism inside the story → handles the price objection in-narrative → THEN hands off to the PDP with the visitor already sold. It can be a lightly-reworked converter ad (B9C3 or B7C1). The PDP's job shrinks to closing the transaction. This is the highest-ceiling fix and the best pure-time use of a long wait.

**6. Turn wasted clicks into owned assets (free, compounds forever).**
- Email-capture popup (the "15% off first order" / "be first when BOGO drops" already specced in the offer sheet). Converts non-buying clickers into a warm list you can launch BOGO to on day one at ~$0 CAC.
- Implement the already-drafted abandoned-cart email.
- Build a review-request flow: turn the ~9 real customers into real, photo-backed reviews that replace the fabricated/non-compliant ones (Retention agent's #1 — it's trust infrastructure, not pure retention).

**7. Stage B16 built-and-paused in Meta** so day-one-of-budget is a single toggle.

---

## The Parallel Track (different risk class): the Ban-Pattern Investigation

Three BM bans is a pattern, not bad luck. A 4th ban during B16 wastes not 30% but 100% of the recovered budget plus everything downstream. The Foundation agent's sharp distinction: this can't be "verified fixed" the way the pixel can, so it's not the highest-leverage VERIFIABLE move for the waiting period — but it IS the highest existential risk overall. It runs as a parallel strategic track that must conclude BEFORE committing the recovered budget. The open question the repo never resolved: is the fresh-FB-per-BM + native-camouflage methodology itself the trigger, not the workaround?

---

## What to STOP Doing

Per the Brutal Prioritizer, stated straight: **freeze the creative/strategy production.** No avatar #12, no Core Desire v3, no B17, no more batches. There are 22+ strategy docs, 11 sub-avatars, 11 narrowed sub-sub-avatars, ~10 written ads, and 4 converters — 6+ months of creative inventory sitting idle behind a broken cart and an empty ad account. Writing more is inventory you can't deploy.

### Reconciling this with the founder's avatar-precision argument (which was right)

The founder's positioning argument — that a no-trust new brand wins through specificity because big brands can't go narrow — is **correct and survives scrutiny as a principle.** It produced the 4 converters. It is the edge.

But here's the reconciliation that makes both things true at once: **avatar precision already did its job.** It got the woman to click at 48%. That IS the precision working. The break is downstream of where avatars operate — no amount of additional avatar precision can fix a cart that converts nobody, because the click already happened. So this isn't "your avatar work was wrong." It's "your avatar work succeeded, and the bottleneck moved past it." Letting the precision pay off requires fixing the thing standing between the click and the sale. You're not abandoning the edge — you're cashing it in.

---

## One-Line Answer

**The single highest-leverage move for the waiting period is to fix the post-click funnel — compliant + message-matched PDP, a live BOGO, a verified pixel, an advertorial bridge page, and an email/review capture layer — so that the moment budget returns, a proven converter (B9C3) launches into a funnel that can actually close, and the 14-day run finally tells you whether you have a business.** Stop producing creative; you have 6 months of it waiting. Run the ban-pattern investigation in parallel.

---

*Synthesis of 5 in-house agents, 2026-05-21. Agents retained for follow-up. Advisory — the founder decides.*
