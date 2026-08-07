# Claude Chrome Research Prompt: Rising-Problem Discovery for Next Product

**Created:** 2026-08-04. Paste everything below the line into Claude in Chrome.
Self-contained — no repo context needed.

**Why this exists.** Tallow Cream was discontinued 2026-08-04 after ~4 months and
~$2,000 for zero profitable weeks. The post-mortem (`tallow-cream/POST_MORTEM.md`)
concluded the binding constraint was the product and the market, not the
marketing: a real-but-not-urgent problem, in a category entered two years late,
undercut on Amazon, with no reorder cadence. This prompt operationalises the
product-selection checklist from section 5 of that document so the next product
is screened before anything is built.

**The screen matters more than the discovery.** Finding rising searches is easy.
The value is in Step 3, where candidates get killed. Expect most to die there.

---

You are a market research analyst finding rising consumer PROBLEMS with
commercial potential in the United States. I sell physical consumer products
direct-to-consumer via Meta ads. I need problems, not product ideas — I will
decide what to build.

## Step 1 — Mine Google Trends for rising problems

Go to **trends.google.com/trends/explore**. For every search below set **Region:
United States** and run **two time ranges: past 12 months and past 5 years.** The
5-year view tells you whether something is genuinely emerging or merely seasonal.

**The critical mechanic:** in the *Related queries* panel, switch the dropdown
from **Top** to **Rising**. "Top" shows established terms — those categories
already have incumbent brands and are what I want to avoid. "Rising" shows
growth, and **"Breakout"** means over 5000% growth. Do the same for *Related
topics*. This is where the actual findings are.

Also check **trends.google.com/trending** (Trending Now) filtered to the US for
anything health, home or personal-care adjacent.

**Seed terms to explore.** Run each, then follow its Rising related queries
outward — the seeds are doors, not answers:

- Symptom-shaped: `hair shedding`, `jaw pain`, `bloating`, `brain fog`,
  `dry eyes`, `night sweats`, `hand pain`, `hip pain`, `tinnitus`,
  `sleep problems`
- Environment-shaped: `hard water`, `mold`, `air quality`, `microplastics`,
  `blue light`, `noise sensitivity`
- Behaviour-shaped: `mouth taping`, `slugging`, `sandwiching`, `cold plunge`,
  `creatine`, `colostrum`, `fiber`
- Life-stage-shaped: `perimenopause`, `postpartum recovery`, `GLP-1 side
  effects`, `caregiver burnout`
- Pet-shaped: `dog itching`, `cat hairball`, `senior dog mobility`

Add your own seeds as patterns emerge. Follow anything with a steep, sustained
curve.

**⚠️ Anchor every candidate for scale.** Google Trends is *relative*, not
absolute — a Breakout term can still have trivial real volume. For each
candidate, use **Compare** against a benchmark term with known large volume
(e.g. `melatonin` or `protein powder`) and report where the candidate lands
relative to it. A term at 2% of `melatonin` is a niche; at 40% it is a market.
**Report this number for every candidate.** Without it a Breakout label is
meaningless.

## Step 2 — Characterise the problem

For each candidate that survives Step 1, find out how people actually talk about
it. Go to Reddit, Amazon 1–3 star reviews of existing solutions, YouTube
comments, and forums.

Collect **verbatim quotes only.** Do not paraphrase, summarise or synthesise.
Ten real quotes beat fifty paraphrases. For each candidate answer:

1. **Is it urgent, or is it a "should"?** The single most important question.
   Urgent = felt today, interferes with today, they would act this week. A
   "should" = they acknowledge it and do nothing. Evidence of urgency looks like
   desperation, sleep loss, quitting something, spending money repeatedly.
   **Quote the desperation or state plainly that you did not find any.**
2. **What do they currently do about it?** List the actual products or hacks
   recommended in those threads, **with prices**.
3. **Does the current solution work?** Find people saying it did not.
4. **Can the problem be named plainly in an ad?** Or is it a diagnosed medical
   condition, a prescription, or something Meta restricts?

## Step 3 — The kill screen

Score every surviving candidate against all seven. **Most should die here. That
is the point. Report the ones that die and why — a well-reasoned kill is as
useful to me as a pass.**

1. **Urgency.** Felt-today problem, or a consumable with a genuine reorder
   cycle. A real-but-not-urgent problem is what killed the last product: it
   produced good click-through and almost no purchases.
2. **Category age — DO THIS ONE FIRST, IT IS THE CHEAPEST KILL.** Go to
   **facebook.com/ads/library**, set country United States, category All ads,
   and search the category's main terms. Sort by longest-running and record:
   how many advertisers, and how long the oldest live ads have been running.
   **If ads have been running 1–2+ years at volume, the urgent buyers already
   have a brand and I am entering late.** This check takes ten minutes and would
   have killed the last product before a dollar was spent.
3. **Amazon exposure.** Search the category on Amazon. Record the price of the
   cheapest credible equivalent and of the best-reviewed one. **If a comparable
   product is materially cheaper on Amazon, that caps my price and kills repeat
   purchase.**
4. **Reorder cadence.** How long does one unit last? **30 days is good, 90 days
   is bad.** No reorder means every sale must be profitable on its own, which is
   very hard at a $3–4 cost per click.
5. **Nameability.** Can the real pain be stated plainly in a Meta ad? If the
   urgent version of the problem is the non-compliant version, the category is a
   trap — that trap is what forced the last product onto its weakest angle.
6. **Price headroom.** What would a product here realistically sell for, and what
   would it cost to make? I need enough contribution margin to absorb a **$3–4
   cost per click**, which I treat as a fixed cost of the platform because it did
   not move across ten creative formats and four months.
7. **The two-of-three rule.** The pattern that works is **existing proven demand
   + a genuinely new mechanism + a specific group with a severe problem.** The
   last product had the first two and lacked the third. **Say explicitly which
   of the three each candidate has and which it lacks.**

## Deliverable

1. **RISING PROBLEMS FOUND.** Every candidate from Step 1, with its Trends
   evidence: search term, growth direction over both time ranges, Breakout status,
   and its scale relative to the benchmark term. Note which are seasonal.
2. **PROBLEM PROFILES.** For each survivor: verbatim quotes with sources,
   current solutions with prices, and evidence of urgency or its absence.
3. **KILL SCREEN TABLE.** All seven criteria scored for every candidate, pass or
   fail, with a one-line reason. Include candidates that died.
4. **SHORTLIST.** The 3–5 that survived, ranked, with the strongest single piece
   of evidence for each and the biggest risk to each.
5. **THE ONE YOU WOULD BET ON**, and why, in one paragraph. Commit to an answer.
6. **WHAT YOU COULD NOT DETERMINE.** Anything that needs primary research or
   supplier quotes before a decision is possible.

## Constraints

- United States market.
- **Never invent a quote, a number, a price or a Trends reading.** If you cannot
  verify something, say so. Fabricated evidence here costs me thousands of
  dollars downstream.
- Give the source URL for every quote and every price.
- **Thin evidence is a finding, not a failure.** Say when a candidate looks
  promising in Trends but has no human evidence behind it — that pattern usually
  means press coverage rather than real demand.
- Do not recommend anything requiring a prescription, a medical claim, or a
  regulated health claim.
- I am not looking for dropshipping listicles or "trending products to sell"
  articles. Those are SEO content, not evidence. Work from Trends data, Ad
  Library, Amazon and primary consumer language only.
