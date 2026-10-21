import re

# 1. Update css/estilo.css to remove the blue gradient on line 2667
css_path = r'c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\upolitico-clone\css\estilo.css'
with open(css_path, 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

# Replace linear-gradient(to left, #79a0d8, #fff) with #ffffff
css_new = css.replace(
    'background-image: linear-gradient(to left, #79a0d8, #fff);',
    'background-color: #ffffff;\n  background-image: none;'
)
with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_new)
print("Updated estilo.css: removed blue gradient!")

# 2. Update index.html
html_path = r'c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\upolitico-clone\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add hero-specific styles inside <style>
hero_css = """
/* Hero Brazil Landmarks & Clean Style */
.banner.style-3 {
  position: relative !important;
  background-color: #ffffff !important;
  background-image: radial-gradient(circle at 85% 15%, rgba(255, 190, 0, 0.07) 0%, rgba(255, 255, 255, 0) 55%), #ffffff !important;
  min-height: 560px !important;
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
  object-position: center bottom !important;
  z-index: 1 !important;
  display: block !important;
  pointer-events: none !important;
}
.hero-text-backdrop {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 56%;
  background: linear-gradient(to right, rgba(255, 255, 255, 0.95) 0%, rgba(255, 255, 255, 0.82) 48%, rgba(255, 255, 255, 0) 100%);
  z-index: 2;
  pointer-events: none;
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
    opacity: 0.88;
    object-position: 70% bottom !important;
  }
  .hero-text-backdrop {
    width: 100%;
    background: linear-gradient(to bottom, rgba(255, 255, 255, 0.94) 0%, rgba(255, 255, 255, 0.82) 65%, rgba(255, 255, 255, 0.2) 100%);
  }
}
"""

if '/* Hero Brazil Landmarks & Clean Style */' not in html:
    html = html.replace('</style>', hero_css + '\n</style>', 1)
    print("Injected hero CSS into index.html!")

# Replace banner-1.png img tag and add hero-text-backdrop
old_banner_tag = re.search(r'<img src="imagens/banner-1\.png[^"]*"[^>]*class="banner-image"[^>]*/>', html)
if old_banner_tag:
    new_banner_html = '<img src="imagens/hero-brasil-pontos.png?v=2" alt="Marketing Político Brasil - Campanhas Eleitorais 2026" class="banner-image"/>\n  <div class="hero-text-backdrop"></div>'
    html = html.replace(old_banner_tag.group(0), new_banner_html)
    print("Replaced banner-image tag with hero-brasil-pontos.png and backdrop!")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved updated index.html successfully!")
