import re

html_path = r'c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\upolitico-clone\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the Hero section markup
# Replace the previous banner-image / hero-text-backdrop with the new layered structure:
# Layer 1: banner-image (with tailored opacity)
# Layer 2: hero-color-overlay (warm gradient / color element)
hero_markup_search = re.search(r'<img src="imagens/hero-war-room\.jpg[^"]*"[^>]*class="banner-image"[^>]*/>\s*(?:<div class="hero-text-backdrop"></div>)?', html)

new_layers = """<img src="imagens/hero-war-room.jpg?v=4" alt="Mesa de Estratégia - Campanha Eleitoral 2026" class="banner-image"/>
  <div class="hero-color-overlay"></div>"""

if hero_markup_search:
    html = html[:hero_markup_search.start()] + new_layers + html[hero_markup_search.end():]
    print("Updated hero markup with hero-color-overlay!")
else:
    print("Could not find exact hero markup search, checking alternative...")

# 2. Update the CSS for Hero War Room Layered Treatment
new_css = """/* Hero Layered Treatment (Transparency & Color Element) */
.banner.style-3 {
  position: relative !important;
  background-color: #fbfbfd !important;
  min-height: 570px !important;
  overflow: hidden !important;
}
.banner-image {
  position: absolute !important;
  left: 0 !important;
  right: 0 !important;
  top: 0 !important;
  bottom: 0 !important;
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  object-position: center 38% !important;
  opacity: 0.28 !important;
  filter: contrast(1.12) saturate(1.15) !important;
  z-index: 1 !important;
  display: block !important;
  pointer-events: none !important;
  mix-blend-mode: multiply !important;
}
/* Elemento de coloração: transição suave e luminosa com toque amarelado/dourado */
.hero-color-overlay {
  position: absolute !important;
  left: 0 !important;
  right: 0 !important;
  top: 0 !important;
  bottom: 0 !important;
  z-index: 2 !important;
  pointer-events: none !important;
  background: linear-gradient(135deg, 
    rgba(255, 255, 255, 0.95) 0%, 
    rgba(255, 255, 255, 0.78) 45%, 
    rgba(255, 248, 220, 0.45) 80%,
    rgba(255, 190, 0, 0.18) 100%
  ) !important;
}
/* Tipografia e contraste 100% nítidos */
.banner.style-3 .dark-color.make-white {
  color: #102234 !important;
  text-shadow: none !important;
  font-weight: 700 !important;
}
.banner.style-3 .paragraph-small2.in-list {
  color: #334155 !important;
  text-shadow: none !important;
  font-weight: 500 !important;
}
.container.banner-style-3 {
  position: relative !important;
  z-index: 3 !important;
}
.waves-bottom2 {
  z-index: 4 !important;
}
@media (max-width: 991px) {
  .banner.style-3 {
    min-height: 520px !important;
  }
  .banner-image {
    opacity: 0.22 !important;
    object-position: center 25% !important;
  }
  .hero-color-overlay {
    background: linear-gradient(180deg, 
      rgba(255, 255, 255, 0.96) 0%, 
      rgba(255, 255, 255, 0.85) 60%, 
      rgba(255, 190, 0, 0.15) 100%
    ) !important;
  }
}
"""

# Replace old hero css block
old_css_match = re.search(r'/\* Hero War Room Style \*/.*?(?=\.button\.btn-yellow|\n</style>)', html, re.DOTALL)
if old_css_match:
    html = html[:old_css_match.start()] + new_css + html[old_css_match.end():]
    print("Replaced CSS with new layered treatment!")
else:
    # Check if Hero Layered Treatment already there or insert before </style>
    if '/* Hero Layered Treatment' in html:
        html = re.sub(r'/\* Hero Layered Treatment.*?(?=\.button\.btn-yellow|\n</style>)', new_css, html, flags=re.DOTALL)
        print("Updated existing Hero Layered Treatment CSS!")
    else:
        html = html.replace('</style>', new_css + '\n</style>', 1)
        print("Injected new Hero Layered Treatment CSS!")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved updated index.html with layered hero treatment!")
