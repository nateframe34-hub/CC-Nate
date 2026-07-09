# Review Request Email (Flow + Shopify Email)

**Date:** 2026-07-07
**Context:** Judge.me's free tier didn't give founder control over request timing/copy, so review collection is being built manually with Shopify Flow (trigger on fulfillment, delay 10-14 days, tag customer) + Shopify Email (the "Send marketing email" Flow action, same one already used for the gift-card reminder). Founder is building the Flow side; this is the email content.

**Collection point:** since neither Flow nor Shopify Email can capture structured review data, the email links out to a plain Google Form (2 fields: star rating + written review). Founder reviews submissions manually and hands strong ones over to drop into the `review_quote` settings across the PDP, advertorial, and 3 listicles, no fabricated reviews, ever.

---

## Subject line
```
How's your skin doing? (30 seconds, means a lot)
```

## HTML (if Shopify Email has a code/HTML editing option)
```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin:0;padding:0;background:#F6F1E9;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#F6F1E9;padding:32px 0;">
  <tr>
    <td align="center">
      <table role="presentation" width="100%" style="max-width:520px;background:#FBF8F2;border-radius:16px;overflow:hidden;border:1px solid #D8CDBC;">

        <tr>
          <td align="center" style="background:#22351F;padding:24px;">
            <span style="font-family:Georgia,'Times New Roman',serif;font-size:20px;font-weight:600;color:#F2EAD9;letter-spacing:.02em;">Baseline</span>
          </td>
        </tr>

        <tr>
          <td style="padding:36px 32px 8px;text-align:center;">
            <p style="font-family:Georgia,'Times New Roman',serif;font-size:24px;font-weight:600;color:#23291F;margin:0 0 12px;">You've had it a couple weeks now.</p>
            <p style="font-size:15px;color:#46503c;line-height:1.55;margin:0 0 24px;">We'd genuinely love to know how your skin's doing with it. Good, bad, in between, all of it helps, and it helps other people trying to figure out if this is right for them too.</p>
          </td>
        </tr>

        <tr>
          <td align="center" style="padding:0 32px 32px;">
            <a href="{{REVIEW_FORM_LINK}}" style="display:inline-block;background:#2E4731;color:#ffffff;text-decoration:none;font-weight:700;font-size:16px;padding:16px 32px;border-radius:14px;">Leave a Quick Review</a>
          </td>
        </tr>

        <tr>
          <td align="center" style="padding:0 32px 32px;">
            <p style="font-size:12.5px;color:#8a8472;margin:0;">Takes about 30 seconds. No account or sign-in needed.</p>
          </td>
        </tr>

        <tr>
          <td style="border-top:1px solid #D8CDBC;padding:20px 32px;text-align:center;">
            <p style="font-size:11px;color:#9a927d;margin:0;line-height:1.6;">
              Thanks for trying it. Whatever you tell us, we read every one.
            </p>
          </td>
        </tr>

      </table>
    </td>
  </tr>
</table>
</body>
</html>
```

## Block-by-block breakdown (if Shopify Email's editor is drag-and-drop instead of raw HTML)
- **Header/logo block:** "Baseline"
- **Heading block:** "You've had it a couple weeks now."
- **Text block:** "We'd genuinely love to know how your skin's doing with it. Good, bad, in between, all of it helps, and it helps other people trying to figure out if this is right for them too."
- **Button block:** label "Leave a Quick Review", link -> the Google Form URL
- **Small text block:** "Takes about 30 seconds. No account or sign-in needed."
- **Footer text block:** "Thanks for trying it. Whatever you tell us, we read every one."

## Still open
- `{{REVIEW_FORM_LINK}}` needs the real Google Form URL once founder builds it.
- Founder still building the Flow side (trigger, delay, tag, Send marketing email action). Not yet confirmed which fulfillment-related trigger name actually exists in the account's Flow trigger list.
