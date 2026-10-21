import re

html_path = r'c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\upolitico-clone\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update hero image tag
html = re.sub(
    r'<img src="imagens/hero-brasil-pontos\.png[^"]*"[^>]*class="banner-image"[^>]*/>',
    '<img src="imagens/hero-war-room.jpg?v=3" alt="Sala de Guerra - Estratégia de Campanha Eleitoral 2026" class="banner-image"/>',
    html
)

# 2. Update the Hero CSS block inside <style>
old_css_match = re.search(r'/\* Hero Brazil Landmarks & Clean Style \*/.*?(?=\.button\.btn-yellow|\n</style>)', html, re.DOTALL)

new_hero_css = """/* Hero War Room Style */
.banner.style-3 {
  position: relative !important;
  background-color: #0c1420 !important;
  min-height: 580px !important;
  overflow: hidden !important;
}
.banner-image {
  position: absolute !important;
  left: 0 !important;
  right: 0 !important;
  bottom: 0 !important;
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  object-position: center center !important;
  z-index: 1 !important;
  display: block !important;
  pointer-events: none !important;
}
.hero-text-backdrop {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 60%;
  background: linear-gradient(to right, rgba(12, 20, 32, 0.88) 0%, rgba(12, 20, 32, 0.72) 48%, rgba(12, 20, 32, 0) 100%);
  z-index: 2;
  pointer-events: none;
}
.banner.style-3 .dark-color.make-white {
  color: #ffffff !important;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.7) !important;
}
.banner.style-3 .paragraph-small2.in-list {
  color: #f1f5f9 !important;
  text-shadow: 0 1px 6px rgba(0, 0, 0, 0.7) !important;
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
    display: block !important;
    opacity: 0.92;
    object-position: 50% center !important;
  }
  .hero-text-backdrop {
    width: 100%;
    background: linear-gradient(to bottom, rgba(12, 20, 32, 0.92) 0%, rgba(12, 20, 32, 0.8) 60%, rgba(12, 20, 32, 0.35) 100%);
  }
}
"""

if old_css_match:
    html = html[:old_css_match.start()] + new_hero_css + html[old_css_match.end():]
    print("Replaced old hero CSS with new war room CSS!")
else:
    # If not found, inject before </style>
    html = html.replace('</style>', new_hero_css + '\n</style>', 1)
    print("Injected new war room CSS before </style>!")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved updated index.html with war room hero successfully!")
