# NutriHealth website (nutrihealthai.app), served by Cloudflare Pages from public/.
# Edit content/*.html (policy text) or the HOME / DELETE blocks below, bump EFFECTIVE when a
# policy changes (and list the change in content/privacy.html), then run: python build.py
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'public')
EFFECTIVE = 'September 30, 2026'
CONTACT = 'support@nutrihealthai.app'
# False keeps every page out of search results (noindex) while staying open to visitors and to
# Google Play's reviewers. Set True when the site should appear in Google, then submit a sitemap.
INDEXABLE = False
ROBOTS_META = '' if INDEXABLE else '\n<meta name="robots" content="noindex">'

MARK = '''<svg viewBox="0 0 1000 1000" aria-hidden="true"><g fill="none" stroke="#679459" stroke-width="72" stroke-linecap="round"><path d="M57,236 V142 A88,88 0 0 1 145,54 H244"/><path d="M943,236 V142 A88,88 0 0 0 855,54 H756"/><path d="M57,764 V858 A88,88 0 0 0 145,946 H244"/><path d="M943,764 V858 A88,88 0 0 1 855,946 H756"/></g><path d="M748,756 A356,356 0 1 1 842,412" fill="none" stroke="#1F5150" stroke-width="64"/><g fill="#1F5150"><rect x="633" y="590" width="65" height="130" rx="32.5"/><rect x="733" y="517" width="65" height="203" rx="32.5"/><rect x="830" y="437" width="65" height="280" rx="32.5"/></g><path fill="#679459" fill-rule="evenodd" d="M645,296 C585,330 470,352 400,410 C330,468 305,560 322,640 C330,680 343,700 358,716 L408,730 C505,715 600,650 632,540 C655,460 655,360 645,296 Z M528,466 C470,505 395,590 360,716 L407,729 C415,640 460,540 528,466 Z"/></svg>'''

# Legal links live in the footer on every page (header is logo only, like MyFitnessPal / Cal AI).
LEGAL = [('/privacy/', 'Privacy'), ('/terms/', 'Terms'), ('/health-data/', 'Consumer Health Data'), ('/delete-account/', 'Delete account')]


def page(path, title, description, body):
    links = ''.join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == path else ""}>{label}</a>'
        for href, label in LEGAL
    )
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">{ROBOTS_META}
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap">
<link rel="stylesheet" href="/styles.css">
</head>
<body>
<header class="site"><div class="wrap">
<a class="brand" href="/">{MARK}<span>Nutri<b>Health</b></span></a>
</div></header>
<main><div class="wrap">
{body}
</div></main>
<footer class="site"><div class="wrap">
<nav class="legal" aria-label="Legal">{links}</nav>
<span><a href="mailto:{CONTACT}">{CONTACT}</a> &middot; &copy; 2026 NutriHealth &middot; Ontario, Canada</span>
</div></footer>
</body>
</html>
'''


HOME = f'''
<section class="hero">
{MARK}
<h1>Snap your meal. Know what you ate.</h1>
<p class="lead">NutriHealth is a calorie and nutrition tracker for Android. Take a photo, describe a meal or scan a barcode, and see calories, protein, carbs, fat and fibre against your daily targets.</p>
<span class="badge soon">Coming soon to Google Play</span>
</section>
<div class="features">
<div><b>Photo logging</b><span>AI recognises the foods and portions; nutrition comes from food databases.</span></div>
<div><b>Your targets</b><span>Daily calories and macros from your goal, or set your own.</span></div>
<div><b>Progress</b><span>Streaks, weight trend, water and weekly summaries.</span></div>
</div>
<p class="meta" style="text-align:center;margin-top:28px;">Questions? <a href="mailto:{CONTACT}">{CONTACT}</a></p>
'''

PRIVACY = open(os.path.join(HERE, 'content', 'privacy.html'), encoding='utf-8').read().replace('{EFFECTIVE}', EFFECTIVE).replace('{CONTACT}', CONTACT)

HEALTH = open(os.path.join(HERE, 'content', 'health-data.html'), encoding='utf-8').read().replace('{EFFECTIVE}', EFFECTIVE).replace('{CONTACT}', CONTACT)
TERMS = open(os.path.join(HERE, 'content', 'terms.html'), encoding='utf-8').read().replace('{EFFECTIVE}', EFFECTIVE).replace('{CONTACT}', CONTACT)

DELETE = f'''
<h1>Delete your NutriHealth account</h1>
<p class="meta">NutriHealth &middot; Android app</p>
<p class="lead">You can delete your account and all its data at any time.</p>

<h2>In the app</h2>
<ol class="steps">
<li>Open NutriHealth and go to <b>Profile</b>.</li>
<li>Scroll to the bottom and tap <b>Delete account</b>.</li>
<li>Type <b>DELETE</b> and tap <b>Delete account permanently</b>.</li>
</ol>
<p>Your account is deleted straight away.</p>

<h2>Without the app</h2>
<p>Email <a href="mailto:{CONTACT}?subject=Delete%20my%20NutriHealth%20account">{CONTACT}</a> from the email address you use for NutriHealth, with the subject &ldquo;Delete my account&rdquo;. We&rsquo;ll confirm and delete it within 30 days.</p>

<h2>What is deleted</h2>
<ul>
<li>Your account and profile</li>
<li>Meals, meal photos, favourites, recipes and meal plans</li>
<li>Weight, water, fasting and target history</li>
<li>Activity copied from Health Connect (Health Connect keeps its own data on your phone)</li>
<li>Weekly reviews and problem reports (copies forwarded to our issue tracker are deleted on request)</li>
<li>Your purchase record at our subscription provider</li>
</ul>
<p>Backups are cleared within 30 days.</p>

<p class="note"><b>Have NutriHealth Plus?</b> Deleting your account doesn&rsquo;t cancel your subscription. Cancel it first in Google Play &rarr; Payments &amp; subscriptions &rarr; Subscriptions.</p>
'''

PAGES = {
    'index.html': ('/', 'NutriHealth', 'NutriHealth: snap your meal, know what you ate. A calorie and nutrition tracker for Android.', HOME),
    'privacy/index.html': ('/privacy/', 'Privacy Policy · NutriHealth', 'How NutriHealth collects, uses and protects your data.', PRIVACY),
    'terms/index.html': ('/terms/', 'Terms of Service · NutriHealth', 'The terms for using NutriHealth and NutriHealth Plus.', TERMS),
    'health-data/index.html': ('/health-data/', 'Consumer Health Data Privacy Policy · NutriHealth', "How NutriHealth handles consumer health data, including under Washington's My Health My Data Act.", HEALTH),
    'delete-account/index.html': ('/delete-account/', 'Delete your account · NutriHealth', 'How to delete your NutriHealth account and data.', DELETE),
}

if __name__ == '__main__':
    for rel, (path, title, desc, body) in PAGES.items():
        dest = os.path.join(OUT, rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, 'w', encoding='utf-8', newline='\n') as f:
            f.write(page(path, title, desc, body))
    with open(os.path.join(OUT, 'favicon.svg'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(MARK.replace(' aria-hidden="true"', ' xmlns="http://www.w3.org/2000/svg"'))
    print('wrote', len(PAGES), 'pages')
