import os

DATA = [
  {
    "emoji": "\U0001f321\ufe0f", "id": "thermometer",
    "title": "Meat Thermometers",
    "blurb": "The single most useful grill upgrade. No more cutting into the meat to check \u2014 just perfect results every time.",
    "slots": [1, 2, 3]
  },
  {
    "emoji": "\U0001f525", "id": "grills",
    "title": "Grills & Smokers",
    "blurb": "The heart of the backyard. From classic charcoal kettles to smart pellet smokers \u2014 choose what fits his style.",
    "slots": [1, 2, 3]
  },
  {
    "emoji": "\U0001f9c2", "id": "rubs",
    "title": "BBQ Rubs, Sauces & Seasonings",
    "blurb": "The difference between good and unforgettable comes down to what goes on the meat before it hits the heat.",
    "slots": [1, 2, 3]
  },
  {
    "emoji": "\U0001f9ca", "id": "coolers",
    "title": "Coolers & Drinkware",
    "blurb": "Every great cookout needs something to keep the drinks cold. A quality cooler is the unsung hero of the backyard.",
    "slots": [1, 2, 3]
  },
  {
    "emoji": "\U0001f525", "id": "firepits",
    "title": "Fire Pits & Outdoor Ambiance",
    "blurb": "When the food is finished, a fire pit keeps everyone outside a little longer. Stories, s'mores, and the best summer memories.",
    "slots": [1, 2, 3]
  },
  {
    "emoji": "\U0001f9f0", "id": "tools",
    "title": "Grilling Tools & Accessories",
    "blurb": "Tongs, brushes, aprons, covers \u2014 the little things that make a huge difference every time he fires it up.",
    "slots": [1, 2, 3]
  }
]

def render():
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Backyard BBQ Father's Day Gift Guide 2025 | Grill Gifts for Dad</title>
<meta name="description" content="The Father's Day gift guide built on what dads actually want: grill gear, outdoor tools, and backyard essentials that bring the family together.">
<meta property="og:title" content="Backyard BBQ Father's Day Gift Guide 2025">
<meta property="og:description" content="Grill gifts, smokers, rubs, coolers, fire pits, and tools your dad will actually use.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://mtr587.github.io/fathers-day-grill-guide/">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://mtr587.github.io/fathers-day-grill-guide/">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,700;1,600&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{--brand:#c73e1d;--brand-dark:#a32e12;--bg:#faf8f5;--card-bg:#fff;--text:#1a1a1a;--text-muted:#5a5a5a;--border:#e8e2d8;--accent-green:#2d6a4f;--star:#f4a261;--max-w:1120px}
html{scroll-behavior:smooth}
body{font-family:'Inter',-apple-system,BlinkMacSystemFont,sans-serif;background:var(--bg);color:var(--text);line-height:1.6}
.container{max-width:var(--max-w);margin:0 auto;padding:0 24px}

.hero{background:linear-gradient(135deg,#1a1a1a,#2d2d2d 50%,#1a1a1a);color:#fff;padding:72px 0 56px;text-align:center;position:relative;overflow:hidden}
.hero::before{content:'';position:absolute;inset:0;background:radial-gradient(circle at 20% 50%,rgba(199,62,29,.15) 0%,transparent 50%),radial-gradient(circle at 80% 50%,rgba(45,106,79,.12) 0%,transparent 50%)}
.hero::after{content:'';position:absolute;bottom:0;left:0;right:0;height:5px;background:linear-gradient(90deg,var(--brand),var(--accent-green),var(--star))}
.hero>.container{position:relative;z-index:1}
.hero h1{font-family:'Playfair Display',serif;font-size:clamp(2rem,5vw,3.2rem);font-weight:700;margin-bottom:8px;line-height:1.2}
.hero .subtitle{font-family:'Playfair Display',serif;font-size:clamp(1.1rem,2.5vw,1.4rem);font-style:italic;color:#d4a373;margin-bottom:16px}
.hero p{font-size:clamp(.95rem,1.8vw,1.1rem);color:#ccc;max-width:640px;margin:0 auto 24px}
.hero-badge{display:inline-block;background:var(--brand);color:#fff;font-size:.75rem;font-weight:600;padding:6px 16px;border-radius:20px;text-transform:uppercase;letter-spacing:.06em;margin-bottom:18px}
.hero-stats{display:flex;justify-content:center;gap:24px;flex-wrap:wrap;margin-top:24px;font-size:.82rem;color:#999}
.hero-stats span{background:rgba(255,255,255,.07);padding:8px 16px;border-radius:8px}

.tribute{background:#1a1a1a;color:#e0d5c7;padding:40px 0;text-align:center;border-bottom:1px solid #333}
.tribute .container{max-width:720px}
.tribute h2{font-family:'Playfair Display',serif;font-size:1.6rem;font-weight:700;color:#fff;margin-bottom:8px}
.tribute h2 em{color:#d4a373;font-style:italic}
.tribute p{font-size:.95rem;line-height:1.7;margin-bottom:8px}
.tribute .tagline{font-family:'Playfair Display',serif;font-style:italic;color:#d4a373;font-size:1.05rem;margin-top:16px}

.intro{padding:48px 0 32px}
.intro-grid{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}
.intro-grid h2{font-size:1.6rem;font-weight:700;margin-bottom:16px}
.intro-grid p{color:var(--text-muted);margin-bottom:12px;font-size:.95rem}
.intro-highlight{background:#fff;border:2px solid var(--brand);border-radius:16px;padding:28px}
.intro-highlight h3{font-size:1.15rem;margin-bottom:12px;color:var(--brand)}
.intro-highlight ul{list-style:none}
.intro-highlight li{padding:7px 0;font-size:.9rem;border-bottom:1px solid var(--border)}
.intro-highlight li:last-child{border-bottom:none}
.intro-highlight li strong{font-weight:600}
@media(max-width:700px){.intro-grid{grid-template-columns:1fr}}

.disclosure{background:#f0ede8;border-radius:8px;padding:12px 20px;font-size:.78rem;color:var(--text-muted);text-align:center;margin-bottom:32px}

.section-header{text-align:center;margin-bottom:12px}
.section-header h2{font-size:1.8rem;font-weight:700;position:relative;display:inline-block}
.section-header h2::after{content:'';display:block;width:60px;height:3px;background:var(--brand);margin:10px auto 0;border-radius:2px}
.section-header p{color:var(--text-muted);margin-top:10px;font-size:.95rem;max-width:600px;margin-left:auto;margin-right:auto}

.category-block{margin-bottom:64px}
.category-header{background:linear-gradient(135deg,#1a1a1a,#2d2d2d);border-radius:16px;padding:32px 36px;margin-bottom:28px;color:#fff}
.category-header h3{font-family:'Playfair Display',serif;font-size:1.5rem;margin-bottom:6px}
.category-header .why-emoji{font-size:1.6rem;float:left;margin-right:16px;line-height:1.4}
.category-header p{color:#bbb;font-size:.92rem;line-height:1.6}

.tier-row{display:flex;gap:20px;margin-bottom:20px}
.tier-card{flex:1;min-width:0;background:var(--card-bg);border-radius:16px;border:1px solid var(--border);overflow:hidden;transition:transform .2s,box-shadow .2s;display:flex;flex-direction:column}
.tier-card:hover{transform:translateY(-4px);box-shadow:0 12px 32px rgba(0,0,0,.08)}
.tier-card .img-wrap{width:100%;aspect-ratio:1/1;background:#f5f3ef;display:flex;align-items:center;justify-content:center;padding:16px}
.tier-card .img-wrap img{max-width:100%;max-height:100%;object-fit:contain;display:block}
.tier-card .body{padding:20px;flex:1;display:flex;flex-direction:column}
.tier-card .body h4{font-size:.95rem;font-weight:600;margin-bottom:4px;line-height:1.3}
.tier-card .body .stars{color:var(--star);font-size:.78rem;margin-bottom:6px}
.tier-card .body .desc{font-size:.83rem;color:var(--text-muted);margin-bottom:10px;flex:1;line-height:1.55}
.tier-card .body .price{font-size:1.05rem;font-weight:700;color:var(--brand-dark);margin-bottom:2px}
.tier-card .body .btn{display:inline-block;background:var(--brand);color:#fff;text-decoration:none;padding:9px 18px;border-radius:8px;font-weight:600;font-size:.85rem;text-align:center;transition:background .2s;margin-top:6px}
.tier-card .body .btn:hover{background:var(--brand-dark)}
@media(max-width:820px){.tier-row{flex-direction:column;gap:16px}}

.slot-label{background:var(--accent-green);color:#fff;font-size:.8rem;font-weight:700;padding:8px 18px;border-radius:20px;text-align:center}
.placeholder-title{color:#bbb;font-style:italic}
.placeholder-stars{color:#ddd!important}
.placeholder-price{color:#bbb!important}

.why-section{background:#fff;border-radius:16px;padding:40px;margin-bottom:48px;border:1px solid var(--border)}
.why-section h2{font-size:1.4rem;font-weight:700;margin-bottom:16px}
.why-section p{color:var(--text-muted);font-size:.92rem;margin-bottom:12px;max-width:780px}
.why-section ul{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:16px}
.why-section li{background:var(--bg);padding:12px 16px;border-radius:8px;font-size:.88rem}
.why-section li strong{display:block;margin-bottom:2px}
@media(max-width:600px){.why-section ul{grid-template-columns:1fr}.why-section{padding:24px}}

.faq{padding-bottom:48px}
.faq details{background:#fff;border:1px solid var(--border);border-radius:12px;padding:16px 20px;margin-bottom:12px;cursor:pointer}
.faq summary{font-weight:600;font-size:.95rem;outline:none}
.faq details p{margin-top:12px;color:var(--text-muted);font-size:.9rem;line-height:1.6}

footer{background:#1a1a1a;color:#888;text-align:center;padding:32px 24px;font-size:.8rem}
footer a{color:#aaa;text-decoration:underline}
@media(max-width:700px){.hero{padding:48px 0 36px}.category-header{padding:24px}}
.anchor-offset{display:block;position:relative;top:-80px;visibility:hidden}
</style>
</head>
<body>

<section class="hero">
<div class="container">
<div class="hero-badge">\U0001f525 Father\u2019s Day 2025 Gift Guide</div>
<h1>The Gifts He Deserves,<br>The Gear He\u2019ll Love</h1>
<div class="subtitle">\u2014 Because Dad does more for this family than anyone will ever know.</div>
<p>Skip the tie. Skip the mug. Give him something that says <em>we see everything you do.</em> Tools, gear, and backyard essentials that make his life easier, his weekends better, and the people he loves a little closer.</p>
<div class="hero-stats">
<span>\U0001f3af 65% of dads want quality family time</span>
<span>\U0001f356 Grill &amp; outdoor gear is the #1 growing gift category</span>
<span>\U0001f4e6 Amazon Prime \u00b7 Free returns</span>
</div>
</div>
</section>

<section class="tribute">
<div class="container">
<h2>To the man who <em>gives everything</em> for his family</h2>
<p>He\u2019s the one who leaves before the sun comes up and comes home when everyone else is already winding down. The one who says yes to overtime, who fixes what\u2019s broken on the weekend, who never complains because providing for the people he loves is not a burden \u2014 it\u2019s who he is.</p>
<p>For every early morning and late night, every call he takes and every corner he cuts so his family doesn\u2019t have to. This Father\u2019s Day, he doesn\u2019t need another tie or another mug. He needs something that says <em>we see you. we appreciate you. you are everything.</em></p>
<p>Every gift here is picked with that in mind. Not just things \u2014 but the tools and comfort he deserves after a lifetime of giving. Because no one works harder for this family than Dad. And this year, it\u2019s his turn.</p>
<div class="tagline">Thank you, Dad. You\u2019ve got this.</div>
</div>
</section>

<div class="container">

<div class="intro">
<div class="intro-grid">
<div>
<h2>What Dads Actually Want</h2>
<p>The National Retail Federation\u2019s 2025 survey (8,580 respondents) found that <strong>65% of American dads want quality family time above anything else</strong>. Not ties. Not \u201cWorld\u2019s Best Dad\u201d mugs. Time together, around a flame, sharing good food.</p>
<p>We crossed that data with YouGov\u2019s dad preference polling and Prosper Insights demographic breakdowns to build a gift guide that <strong>closes the gap</strong> between what people buy and what dads actually want.</p>
<p><em>Last updated: May 2025 \u00b7 Sources: NRF, Prosper, YouGov, Ipsos</em></p>
</div>
<div class="intro-highlight">
<h3>The Gift Gap We\u2019re Closing</h3>
<ul>
<li><strong>\U0001f455 What most people buy:</strong> Clothing (55%) \u2014 but only <strong>7% of dads want it</strong></li>
<li><strong>\U0001f525 What dads actually want:</strong> Family time, backyard BBQs, a meal together</li>
<li><strong>\U0001f969 Our focus:</strong> Grill &amp; outdoor gear that brings people together</li>
<li><strong>\U0001f3af Every pick is based on real survey data</strong></li>
</ul>
</div>
</div>
</div>

<div class="disclosure">
<strong>Disclosure:</strong> As an Amazon Associate I earn from qualifying purchases. If you buy through links on this site, I may earn a small commission at no extra cost to you. Every product is independently selected \u2014 thank you for supporting this work.
</div>
"""

    for cat in DATA:
        html += f"""
<!-- {cat['id']} -->
<div class="category-block">
<span class="anchor-offset" id="{cat['id']}"></span>
<div class="category-header">
<span class="why-emoji">{cat['emoji']}</span>
<h3>{cat['title']}</h3>
<p>{cat['blurb']}</p>
</div>
<div class="tier-row">
"""
        for s in cat['slots']:
            html += f"""<div class="tier-card">
<div class="img-wrap">
<div style="text-align:center;padding:30px">
<div class="slot-label">\u2705 Product {s}</div>
</div>
</div>
<div class="body">
<h4 class="placeholder-title">Click to edit</h4>
<div class="stars placeholder-stars">\u2605\u2605\u2605\u2605\u2605 (ratings)</div>
<p class="desc">Add your product name, description, price, image URL, and Amazon link here.</p>
<p class="price placeholder-price">$ --.--</p>
<a class="btn" href="#">Add Link</a>
</div>
</div>
"""
        html += """</div>
</div>
"""

    html += """
<div class="why-section">
<h2>\U0001f4ca Why Grill &amp; BBQ Gifts?</h2>
<p>Based on the National Retail Federation\u2019s 2025 Father\u2019s Day Survey (n=8,580), Prosper Insights data, and YouGov\u2019s dad preference polling:</p>
<ul>
<li><strong>65% of dads</strong> want quality family time above anything else. Backyard BBQs are the most natural fit.</li>
<li><strong>Only 7% of dads want clothing</strong> \u2014 but 55% of shoppers buy it. That\u2019s a massive gift gap to fill.</li>
<li><strong>$24 billion</strong> in total Father\u2019s Day spending expected in 2025 \u2014 the highest ever recorded.</li>
<li><strong>African American &amp; Hispanic dads</strong> index highest on celebration participation; big family cookouts are especially valued.</li>
</ul>
</div>

<div class="faq">
<div class="section-header">
<h2>\u2753 Father\u2019s Day Gift FAQ</h2>
<p>Quick answers to the most common questions about buying grill gifts for Dad.</p>
</div>
<details>
<summary>What\u2019s the best Father\u2019s Day gift under $50?</summary>
<p>Good question! Browse the <strong>Meat Thermometers</strong> and <strong>BBQ Rubs &amp; Seasonings</strong> categories above for budget-friendly options.</p>
</details>
<details>
<summary>Is a new grill worth the investment?</summary>
<p>If Dad\u2019s current grill is rusty, unevenly heated, or more than 8 years old \u2014 absolutely. A quality grill creates years of family dinners and backyard memories.</p>
</details>
<details>
<summary>Do dads actually want BBQ tools as gifts?</summary>
<p>Yes \u2014 when they\u2019re real upgrades. A wireless meat thermometer, competition-grade rub, or quality grilling tool adds real capability he\u2019ll appreciate every time.</p>
</details>
<details>
<summary>What about blue-collar and working-class dads?</summary>
<p>Practical, durable gifts are the way to go. A rugged cooler, heavy-duty grill cover, or tools that make his cookout setup more efficient are always appreciated.</p>
</details>
<details>
<summary>Can I get these delivered in time for Father\u2019s Day 2025?</summary>
<p>Most items on Amazon are <strong>Prime eligible</strong> with 1-2 day shipping. Father\u2019s Day 2025 is June 15. Order by June 12 for standard delivery.</p>
</details>
</div>
</div>

<footer>
<div class="container">
<p><strong>Backyard BBQ Father\u2019s Day Gift Guide</strong> \u2014 Independent recommendations for the dad who loves to cook outdoors.</p>
<p style="margin-top:8px">As an Amazon Associate I earn from qualifying purchases. Prices subject to change.</p>
<p style="margin-top:12px">
<a href="https://mtr587.github.io/fathers-day-grill-guide/">Home</a>
&nbsp;\u00b7&nbsp;
<a href="privacy.html">Privacy Policy</a>
</p>
<p style="margin-top:12px;color:#666">&copy; 2025 &middot; Made for dads who make it happen.</p>
</div>
</footer>
</body>
</html>
"""
    return html

if __name__ == '__main__':
    out = render()
    p = os.path.join(os.environ['USERPROFILE'],
        '.openclaw-autoclaw/agents/agent-9kqve4/workspace/fathers-day-grill-guide/index.html')
    with open(p, 'w', encoding='utf-8') as f:
        f.write(out)
    print(f'Wrote {len(out)} bytes to {p}')
