import re

# 1. Update css/estilo.css to add .button.btn-yellow
css_path = r'c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\upolitico-clone\css\estilo.css'
with open(css_path, 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

btn_yellow_css = """
.button.btn-yellow {
  background-color: #FFBE00 !important;
  color: #102234 !important;
  font-weight: 700 !important;
  box-shadow: 0 4px 14px rgba(255, 190, 0, 0.32);
}
.button.btn-yellow:hover {
  background-color: #102234 !important;
  color: #ffffff !important;
  box-shadow: 0 4px 14px rgba(16, 34, 52, 0.35);
}
"""

if '.button.btn-yellow' not in css:
    css = css + '\n' + btn_yellow_css
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print("Added .button.btn-yellow to estilo.css!")
else:
    print(".button.btn-yellow already in estilo.css")

# 2. Update index.html
html_path = r'c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\upolitico-clone\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add to <style> block in index.html as well for instant rendering
if '.button.btn-yellow' not in html:
    html = html.replace('</style>', btn_yellow_css + '\n</style>', 1)
    print("Added .button.btn-yellow to index.html <style>!")

# Find the target button:
# <div class="top-margin"><a href="orcamento.html" class="button w-button">Oramento Online</a></div>
# around line 335

old_btn = '<div class="top-margin"><a href="orcamento.html" class="button w-button">Or'
new_btn = '<div class="top-margin"><a href="orcamento.html" class="button btn-yellow w-button">Or'

# Also check line 823 or keep targeted
count = html.count(old_btn)
print(f"Occurrences of target pattern: {count}")

# Replace the first occurrence (line 335, matching xpath /html/body/div[6]/div[2]/div/div[1]/div/div/div[3]/a)
html = html.replace(old_btn, new_btn, 1)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html button successfully!")
