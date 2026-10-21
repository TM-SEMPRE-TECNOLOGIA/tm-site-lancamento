import re

html_path = r'c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\upolitico-clone\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the jumping words script (Script 17)
html = re.sub(r'<!-- Hero Rotating Word Script -->\s*<script>.*?document\.querySelectorAll\(\'\.hero-rotating-word\'\).*?</script>', '', html, flags=re.DOTALL)
print("Removed rotating words script to prevent awkward text jumps!")

# 2. Fix Slide 1 and Slide 2 buttons to use btn-yellow instead of button line
html = re.sub(
    r'<div class="top-margin medium"><a href="orcamento\.html" class="button line w-hidden-tiny w-button">Or.*?Online</a></div>',
    '<div class="top-margin medium"><a href="orcamento.html" class="button btn-yellow w-button">Orçamento Online</a></div>',
    html
)
print("Updated slider buttons to btn-yellow!")

# 3. Fine-tune Hero CSS Layered Treatment
layered_css = """/* Hero Layered Treatment (Tailored Opacity & Warm Color Element) */
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
  object-position: center 36% !important;
  opacity: 0.22 !important;
  filter: contrast(1.10) saturate(1.15) !important;
  z-index: 1 !important;
  display: block !important;
  pointer-events: none !important;
  mix-blend-mode: multiply !important;
}
.hero-color-overlay {
  position: absolute !important;
  left: 0 !important;
  right: 0 !important;
  top: 0 !important;
  bottom: 0 !important;
  z-index: 2 !important;
  pointer-events: none !important;
  background: linear-gradient(135deg, 
    rgba(255, 255, 255, 0.94) 0%, 
    rgba(255, 255, 255, 0.76) 45%, 
    rgba(255, 245, 214, 0.40) 80%,
    rgba(255, 190, 0, 0.16) 100%
  ) !important;
}
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
    opacity: 0.18 !important;
    object-position: center 25% !important;
  }
  .hero-color-overlay {
    background: linear-gradient(180deg, 
      rgba(255, 255, 255, 0.95) 0%, 
      rgba(255, 255, 255, 0.82) 60%, 
      rgba(255, 190, 0, 0.15) 100%
    ) !important;
  }
}
"""

if '/* Hero Layered Treatment' in html:
    html = re.sub(r'/\* Hero Layered Treatment.*?(?=\.button\.btn-yellow|\n</style>)', layered_css, html, flags=re.DOTALL)
    print("Updated Hero Layered Treatment CSS in index.html!")
else:
    html = html.replace('</style>', layered_css + '\n</style>', 1)
    print("Injected Hero Layered Treatment CSS into index.html!")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved index.html successfully!")
