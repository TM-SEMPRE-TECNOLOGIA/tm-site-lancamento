with open('upolitico-clone/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'<div[^>]*class="[^"]*(?:footer|copyrights|section|banner|precos)[^"]*"', text)]
print(f"Total section-like divs: {len(matches)}")
for m in matches:
    print(text[m:m+90].replace('\n', ' '))
