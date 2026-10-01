# nutrihealth-website

The public website for the NutriHealth Android app: **https://nutrihealthai.app**

| Page | URL | Used by |
|---|---|---|
| Home | `/` | Play Store listing (website) |
| Privacy Policy | `/privacy/` | Play Console → App content → Privacy policy; the app |
| Terms of Service | `/terms/` | The app (sign-up, paywall, Profile) |
| Consumer Health Data Privacy Policy | `/health-data/` | Washington / Nevada / Connecticut health-data laws |
| Delete your account | `/delete-account/` | Play Console → Data safety → Data deletion |
| Invite | `/invite/?code=…` | The app's Share invite link (refer a friend) |

Static HTML and CSS only: no build step on the host, no analytics, no cookies.

**Search indexing is off for now:** every page carries `noindex` (`INDEXABLE = False` in
`build.py`). To go public in search, set it to `True`, rebuild, add a sitemap, switch Cloudflare's
AI Crawl Control to `search=yes`, and submit the sitemap in Google Search Console.

## Editing

1. Policy text lives in `content/` (`privacy.html`, `terms.html`, `health-data.html`); the home and
   delete-account pages are in `build.py`.
2. When a policy changes, update `EFFECTIVE` in `build.py` and note the change under the date in
   `content/privacy.html`. Significant changes must also be announced in the app.
3. Run `python build.py`, check `public/`, commit and push. Cloudflare Pages deploys on push.

The app's data collection and this policy must stay in step: any change to what the app collects,
who processes it, or how long it's kept needs a matching update here.

## Hosting

Cloudflare Pages, connected to this repo: no build command, output directory `public`, custom
domain `nutrihealthai.app`.
