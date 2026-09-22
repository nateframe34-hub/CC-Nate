# ⛔ PLACEHOLDER REVIEWS — DESIGN MOCKUP ONLY — DO NOT PUBLISH

> **These are invented. Every name, rating, date and sentence below is fabricated.**
> They exist for one reason: to see how the reviews module looks and how the page flows with proof in it.
>
> **Rules:**
> 1. **Never deploy this content to a live store**, a staging site with a public URL, an ad, or any asset a customer could see. Fabricated reviews presented as real are an FTC problem and a chargeback problem, independent of anything else.
> 2. Every entry carries the marker `[PH]` in the handle field. **Grep for `[PH]` before any deploy** — if it appears anywhere in the theme, the build is not shippable.
> 3. Delete this file's content from the theme the moment real reviews exist. Per `Brand_and_PDP_Outline.md` §B4, the reviews module ships the week the first real review lands.

---

## Summary block (for the layout)

```
★★★★☆   4.6 out of 5        [PH]
Based on 38 reviews         [PH]

5 ★  ████████████████████░░  26
4 ★  █████░░░░░░░░░░░░░░░░░   8
3 ★  ██░░░░░░░░░░░░░░░░░░░░   3
2 ★  ░░░░░░░░░░░░░░░░░░░░░░   1
1 ★  ░░░░░░░░░░░░░░░░░░░░░░   0
```

**Why 4.6 and not 5.0 in the mockup:** a perfect score reads as fake and the layout needs to handle a mixed distribution anyway. Design the module against an imperfect set — it's the realistic case and it's the more useful stress test.

---

## Reviews

Deliberately varied in length so the module is tested at one line, one paragraph, and long. Includes a 4★ and two 3★, because a real set has them and the layout must not fall apart when a review isn't glowing.

---

**★★★★★ · Dana R. `[PH]` · Verified Buyer · 4×10 White**
**"Hallway 69, bedroom 63. Now they're within a degree."**

Back bedroom is over the garage and has always been the cold one. Put one of these in three weeks ago. It isn't magic — the room still runs a touch cooler than the rest of the house — but the gap went from six degrees to about one, and that's the difference between usable and not. Took maybe ten minutes with a screwdriver.

---

**★★★★★ · Marcus T. `[PH]` · Verified Buyer · 6×10 White**
**"The space heater is in the basement now."**

Had a little oil radiator running in that room every night from October to April. Haven't plugged it in once since this went in.

---

**★★★★☆ · Priya N. `[PH]` · Verified Buyer · 4×10 White**
**"Works. Took me a minute to figure out the modes."**

The fan itself does what it says. The instructions that came with it were not great and I had it on the wrong setting for the first two days, which made me think it was broken. Once I sorted that out it's been fine. Four stars because the setup could be clearer.

---

**★★★★★ · Jen W. `[PH]` · Verified Buyer · 4×10 White**
**"My daughter stopped asking to sleep in our room."**

Her room is at the end of the hall and it was always the coldest. I'd been putting an extra blanket on her every night and still checking on her at 2am. Room sits about four degrees warmer than it used to. I stopped checking.

---

**★★★☆☆ · Robert K. `[PH]` · Verified Buyer · 6×10 White**
**"Helped a little. My problem was bigger than a vent."**

Honest review — it moved my office up about two degrees, which I can feel but isn't what I was hoping for. Turns out I've got a duct issue that needs a real fix. That's on me, not the product; their own site did say to check the airflow first and I skipped that part.

---

**★★★★★ · Alison M. `[PH]` · Verified Buyer · 4×10 Bronze**
**"Bought a second one a week later."**

Did the bonus room first. Worked well enough that I ordered another for the guest room, which I should have done in the first order.

---

**★★★★★ · Tom H. `[PH]` · Verified Buyer · 4×10 White**
**"Two screws. That's the whole install."**

I got a quote for just under $3,000 to rebalance the ductwork for one room and put it off for two winters. This was eighty-something dollars and a screwdriver. Wish I'd tried the cheap thing first.

---

**★★★★★ · Carla D. `[PH]` · Verified Buyer · 6×10 White**
**"Finally understand why that room was cold."**

The explanation on their site about the room being last on the duct run was the first time anyone had explained it to me. Two HVAC guys looked at it and neither said that. The fan helped, but honestly the explanation was worth something on its own.

---

**★★★★☆ · Nathan B. `[PH]` · Verified Buyer · 4×10 White**
**"You can hear it. Doesn't bother me, might bother you."**

It's a fan, so it makes fan noise. I sleep with it on the low setting and it's fine, kind of like white noise. My wife noticed it the first two nights and then stopped noticing. Worth knowing before you buy if you're a light sleeper.

---

**★★★☆☆ · Sandra P. `[PH]` · Verified Buyer · 4×10 White**
**"Measure first. I ordered wrong."**

My fault entirely — I measured the cover instead of the hole and got a size that didn't fit. Support sorted out the exchange without any fuss, but I lost a week. The instructions do say to measure the opening. Read that part.

---

**★★★★★ · Greg A. `[PH]` · Verified Buyer · 6×10 White**
**"Upstairs office went from 64 to 68."**

That's it. That's the review.

---

## Notes for whoever builds the module

The set above is shaped to stress-test the layout, not to flatter it:

- **One-line reviews and long ones** sit next to each other — the card must not break when a review is eleven words.
- **Two reviews mention noise and fitment.** A real set for this category will contain them (the incumbent's reviews are dominated by setup confusion and noise), so the module should look right with them, not only with praise.
- **Ratings are mixed.** If the design only reads well at five stars, it's the wrong design.
- **Variant is shown per review** (4×10 / 6×10, white / bronze), which is genuinely useful on a fitment product and worth building in now.
- **Outcomes are partial, not total** — degrees closed, not "fixed." That matches the claim rule in `Brand_Mastery.md` Part 8 rule 1b, and it's what real reviews for this product will actually say.

**When real reviews arrive:** keep the structure, drop this content, and sort so that a mixed distribution stays visible. Burying the 3★ reviews is what makes a review set read as bought.
