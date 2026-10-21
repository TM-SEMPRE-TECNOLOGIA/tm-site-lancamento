import re

html_path = r'c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\upolitico-clone\index.html'
with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Let's locate the boundary
# The duplicate starts at: <div id="Scroll" class="section  w-clearfix"> around pos 56090
# and ends right before <div class="algin-center copyrights"> around pos 65322

dup_start = text.find('</div>\n</div>\n<div id="Scroll" class="section  w-clearfix"><div class="container w-container"><div class="title-wrapper with-margin">\n   <div class="algin-center"><h2>Perguntas frequentes</h2>')
if dup_start == -1:
    # try regex
    m = re.search(r'</div>\s*</div>\s*<div id="Scroll" class="section\s+w-clearfix">\s*<div class="container w-container">\s*<div class="title-wrapper with-margin">\s*<div class="algin-center"><h2>Perguntas frequentes</h2>', text[50000:])
    if m:
        dup_start = 50000 + m.start()

dup_end = text.find('<div class="algin-center copyrights">')

print("dup_start:", dup_start)
print("dup_end:", dup_end)

if dup_start != -1 and dup_end != -1 and dup_start < dup_end:
    # Keep the closing of the previous section, and skip straight to copyrights
    # Notice dup_start starts with </div>\n</div>\n...
    # We want to keep </div>\n</div>\n (closing of footer 1)
    text_cleaned = text[:dup_start + 12] + '\n  ' + text[dup_end:]
    print("Removed duplicate block of length:", dup_end - (dup_start + 12))
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(text_cleaned)
    print("Saved cleaned index.html!")
else:
    print("Could not locate exact duplicate bounds!")
