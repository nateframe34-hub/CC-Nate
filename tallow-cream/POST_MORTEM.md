# Tallow Cream — Post-Mortem

**Product discontinued 2026-08-04.** ~4 months, ~$2,000 spend, ~26 purchases,
zero profitable weeks, zero repeat purchases.

This document exists so the next product starts from here instead of from
scratch. Everything below is product-agnostic unless marked otherwise.

---

## 1. Why it failed — the arithmetic

**The account's best-ever ad was approximately breakeven, not profitable.**

B17C1 lifetime: ~$640 spend, 10-12 purchases, **~$58 CPA**. Contribution was
$41.52 on a single jar and $60.71 on the 2-pack. So the single best creative we
produced — the one four months of work tried to replicate — landed at about
breakeven, and only if every buyer took the bundle.

Blended: **$3.17 CPC ÷ 3.42% click-to-purchase = $92.69 CPA** against $41.52
contribution. 2.2x off. Profitability required click-to-purchase near 7-8%, or
CPC near $2. Neither ever happened.

**CPC never moved.** $3.09-4.75 across ten formats, two business managers, four
months. Whiteboards, news chyrons, clinical documents, POV photos, vector
illustrations, forum screenshots, text-message screenshots. Creative did not
move the number. That is the single most important fact in this document.

---

## 2. Why it failed — the diagnosis underneath the arithmetic

### The problem was real but not urgent

Our lead avatar (SA2, "too many products on the counter") describes a
dissatisfaction, not a pain. People acknowledge it and do not act today.

**The funnel signature confirms it:** 7.34% CTR with 3.42% click-to-purchase.
High engagement, low action. If the creative were bad, CTR would be bad. If the
offer were bad but the desire urgent, we would see strong add-to-cart and a drop
at checkout. What we saw was people reading 1,500 words and doing nothing —
which is what a non-urgent desire looks like.

Zero repeat purchases fits the same pattern. Low-urgency products do not build
habits. So does price sensitivity: urgency suppresses price shopping, and we had
none to suppress it with.

### We mis-read market sophistication

Documented as Stage 3-4. It was **Stage 4-5**, and the ads themselves prove it:

- Every mechanism-forward creative failed. B19C2 whiteboard, B20C3 label test,
  B22C1 news chyron — all leading with water-vs-fat. **Zero purchases across
  ~1,000+ impressions.**
- The one that converted, B17C1, barely argues the mechanism. It is a story that
  sells "the not-carrying" and being seen across a table. **That is a Stage 5
  response** — identity-level, empathetic.

We wrote the mechanism as if it were new information to a market that had been
hearing it for two years.

### We entered the category late

Tallow had been running hard on Meta and Amazon for ~2 years. The people with
severe dry-skin problems had already found brands and stuck with them. The
audience still available to us was, by definition, the lower-urgency residual.

**This also explains the CPC.** A new BM with no reviews, no pixel history,
bidding into a two-year-old category against established competitors — $3-4 is
the market price of late entry, not a creative failure. No amount of copy work
was ever going to move it.

### Structural disadvantages we never fixed

- **~$20 cheaper on Amazon.** Caps price and caps repeat purchase.
- **One jar lasts 2-3 months.** No reorder cadence to build LTV on.
- **The urgent angles were the non-compliant ones.** Severely cracked/reactive
  skin is a painful-today problem — and it is exactly what Meta restricts. The
  compliant angles were the low-urgency ones. That is a structural trap, not a
  creative failure, and it is worth checking for in any future category.

---

## 3. What we learned that transfers

### 🔑 Attribution is the conversion lever

**The single most valuable finding of the four months.**

The same mechanism sentence appears in four ads:

- Attributed to a named 76-year-old beekeeper, relayed by a friend
  (B17C1, B28C1) → **12 purchases**
- Asserted by the advertiser in short-form
  (B20C3 507 impressions, B22C1 495 impressions) → **0 purchases across ~1,002**

Same claim. Different author. Opposite result.

In the converters, **the advertiser never speaks.** The mechanism is quoted from
someone with no stake. The results are witnessed by people who were not told
anything. The objection is raised by the narrator and answered by a peer. The
product is never named. In the non-converters there is one voice, and it belongs
to whoever wants the money.

**Corollary:** this is why every cheap-format test failed. Whiteboards, chyrons,
documents and diagrams are *authorless surfaces*. Porting the mechanism onto them
stripped out the thing doing the work while preserving the thing that was not.

### 🔑 Image and copy are independent variables

We changed them together for months and learned nothing from either.

**B17C1's image is a jar on a bathroom counter** — authorless, no text, no
person — and it is the best-converting ad in account history. The whiteboard ads
did not fail because of their images. They failed because their **copy** was
60-100 words of brand assertion.

> The image's job is to stop the scroll. The copy's job is to carry the
> attribution. Never trade one for the other.

### 🔑 Check placements before blaming creative

**68-89% of B33's impressions were served into Facebook right column**, a
placement that does not render primary text at all. Our ads were 1,500-word
stories being shown in a slot that could not display one word.

CTR there was not low, it was structurally impossible. It also faked a great CPM:
right column cost $0.31-0.61 against $200-450 in feed, dragging the blended
number down and making it look like we had solved delivery cost.

**Every creative conclusion drawn that week was invalid.** Before diagnosing a
creative, pull the placement breakdown. Exclude right column and Audience Network
at account level on day one of any new account.

### 🔑 Offer terms never go in the creative

B19C2 (whiteboard, $11.35 CPA / 4.40x ROAS, best unit economics we ever posted)
ends its board on "Water sits on top. Skin lets fat in. That's it." No price, no
guarantee, nothing transactional in frame.

B33C3 ran the same format and added "Four ingredients. Sixty days to send it
back" in red, slanted, in terminal position. It read as an ad on sight.

**The test:** could a person with nothing to sell have written this? A mechanism,
a diagram, a symptom, a date — yes. A return window — never.

### 🔑 Never name a doubt in a headline or a pill

An early objection strip titled its rows "Does it smell like beef?" and "Will it
clog my pores?" That hands both objections to every visitor who does not open
them. Handle objections inside a positive frame — the way "Why Grüns?" does.

### 🔑 Post-Andromeda, the creative is the targeting

Vague copy gives the algorithm nothing to work with. Name the topical cluster
explicitly. The safe way to do it is **first person**: "my dermatologist put me
on a retinoid" is a statement about the speaker; "dealing with X?" is an
assertion about the reader, which is the Personal Attributes surface.

### 🔑 Reading beats summarising

Repeatedly, reading a source in full immediately surfaced things summaries had
missed — the B19C2 board that carried no offer terms, the April-21 spike that
invented a fake CTR pattern, the SA9 recommendation sitting unrun for weeks.
Every significant error this account made came from working off a summary.

---

## 4. Process failures worth not repeating

**We optimised the converting avatar instead of testing the highest-urgency
one.** SA9 ("The Actives Casualty") was flagged ⭐ RECOMMENDED NEXT LEAD TEST in
`Brand_Mastery.md` for weeks. B29 through B34 all went to SA2 and SA11 anyway.
The research had already named the answer and we kept iterating on the thing that
was working slightly.

**We ran too many cells on too little budget.** Every batch this month died below
the impression bar. At ~$50/day, CBO concentrates spend on first-hour noise and
starves the rest. B17C1's validating read came from **ABO at $12.50/day on a
protected budget** — that is the config that produced our best data.

**We judged on CPM for too long.** CPM is the metric that moves and does not
matter. CPC is the metric that matters and did not move.

---

## 5. Product-selection checklist for next time

1. **Urgent, felt-today problem** — or consumable economics with a real reorder
   cycle. Grüns is a "should" product that survives on subscription LTV and
   enormous scale; that game needs capital we do not have. Primal Queen is the
   replicable model: a specific group with a severe problem, met with a new
   mechanism.
2. **Check category age in the Meta Ad Library before committing.** Filter the
   category, sort by longest-running. If ads have been live 1-2+ years, the
   urgent buyers already have a brand. Entering early is worth more than any
   amount of copy skill. This check costs ten minutes and would have caught
   tallow.
3. **Not cheaper on Amazon.** Ideally not on Amazon at all.
   **Ask the supplier directly: do you sell this unit yourself, under your own
   brand, on Amazon?** Added 2026-08-12 after a register-fan supplier was
   rejected on exactly this. If the answer is yes, we are competing with our own
   source — a price-checking customer at checkout does not find a substitute,
   they find the manufacturer. Watch for the tell: a distribution agreement that
   forbids pricing below "the official Amazon store price" exists *because* that
   listing exists.
4. **30-day consumption cycle**, not 90.
5. **The real pain must be nameable in an ad.** If the urgent angle is the
   non-compliant one, the category is a trap.
6. **AOV that absorbs a $3-4 CPC.** Treat that as a fixed platform cost, because
   across ten formats and four months it never moved.
7. **Two of three is not enough.** Existing demand + new mechanism + a specific
   group with a severe problem. Tallow had the first two. The third is the one
   that decides it.

---

## 6. What carries forward

Reusable immediately, product-agnostic:

- The native ad architecture and the nine-element converter spine
- The attribution finding (section 3)
- The Origins avatar system and the desire-first SA-numbered method
- The PDP structure, rebuilt on real Clarity scroll data
- The bundle mechanics and two-discount design (product + order discount combine)
- Placement exclusions and the media-buying lessons
- The compliance framework and banned-phrase discipline

**Not carried forward:** the tallow avatars, angles and copy. They are specific
to a product that is discontinued.

---

## 6b. B35 confirmed the diagnosis

**B35 (SA9 The Actives Casualty) was launched after the discontinuation call and
performed badly.** That is worth recording, because it is confirmatory rather
than merely disappointing.

SA9 was the highest-urgency avatar in the research, with the strongest behaviour
evidence the account ever had, written to the full converter spine with the
attribution lever intact, correct placements, and a targeting lexicon built for
post-Andromeda delivery. It was the best shot the account had left.

It did not move. That is evidence the constraint was the product and the market
— price, category age, reorder cadence, Amazon undercut — and not the creative.
A better avatar and better copy could not fix an offer that needed 7-8%
click-to-purchase to break even.

**The transferable point:** when a well-researched, well-executed swing at the
highest-urgency avatar available still fails, stop iterating on creative. The
answer is upstream of the marketing.

---

## 7. The honest summary

We built a legitimate new mechanism and aimed it at a group whose problem was
real but not urgent, in a category we entered two years late, at a price
undercut by Amazon, with no reorder cadence.

The marketing worked. Twenty-six people bought a jar of beef fat off a
1,500-word story. That skill transfers completely.

What did not work was chosen before any of the marketing started.
