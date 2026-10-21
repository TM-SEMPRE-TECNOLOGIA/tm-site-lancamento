with open('upolitico-clone/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'class="banner style-3"', text)]
print("Banner matches:", matches)
for m in matches:
    print("--- SNIPPET ---")
    print(text[m-50:m+400])

for s in re.findall(r'<style[^>]*>.*?</style>', text, re.DOTALL):
    if 'banner' in s or 'style-3' in s:
        print("--- STYLE ---")
        print(s)
