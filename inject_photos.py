#!/usr/bin/env python3
"""Inject NBA headshot images into nba_guide.html for every player card."""

import re

BASE = '/Users/Allenwavekwan/Projects/nba_tutorial'
CDN  = 'https://cdn.nba.com/headshots/nba/latest/260x190/{id}.png'

# Map: exact h3 text snippet  ->  NBA player ID
PLAYERS = {
    # Current Stars
    'Nikola Jokić':              203999,
    'Luka Dončić':               1629029,
    'Giannis Antetokounmpo':     203507,
    'Shai Gilgeous-Alexander':   1628983,
    'Stephen Curry':             201939,
    'LeBron James':              2544,
    'Victor Wembanyama':         1641705,
    # Legends
    'Michael Jordan':            893,
    'Kobe Bryant':               977,
    'Magic Johnson':             77142,
    'Larry Bird':                1449,
    'Kareem Abdul-Jabbar':       76003,
    'Bill Russell':              78049,
    'Wilt Chamberlain':          76375,
    'Shaquille O\'Neal':         406,
    'Tim Duncan':                1495,
    # Great Moments
    'Tracy McGrady':             1503,
    # No-Ring Legends
    'Charles Barkley':           787,
    'Karl Malone':               252,
    'John Stockton':             304,
    'Allen Iverson':             947,
    'Patrick Ewing':             121,
    'Steve Nash':                959,
    'Reggie Miller':             397,
    'Chris Paul':                101108,
}

# CSS to inject (add avatar styles)
AVATAR_CSS = """
/* PLAYER AVATARS */
.av{float:right;width:90px;height:68px;object-fit:cover;object-position:top;border-radius:8px;margin:0 0 10px 14px;border:2px solid var(--or);background:var(--bd);}
"""

html = open(f'{BASE}/nba_guide.html', encoding='utf-8').read()

# 1. Inject CSS before </style>
html = html.replace('</style>', AVATAR_CSS + '</style>', 1)

# 2. For each player, find their <h3> tag and insert <img> right before it
for name, pid in PLAYERS.items():
    img_tag = f'<img class="av" src="{CDN.format(id=pid)}" alt="{name}" onerror="this.style.display=\'none\'">\n  '
    # Match <h3> tag that contains the player name
    # Use regex to find <h3>...name...</h3> and insert img before <h3>
    pattern = r'(<h3>[^<]*' + re.escape(name) + r'[^<]*</h3>)'
    replacement = img_tag + r'\1'
    new_html, count = re.subn(pattern, replacement, html)
    if count:
        html = new_html
        print(f'✅ {name} (ID: {pid})')
    else:
        print(f'⚠️  NOT FOUND: {name}')

with open(f'{BASE}/nba_guide.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'\nDone! Total chars: {len(html)}')
