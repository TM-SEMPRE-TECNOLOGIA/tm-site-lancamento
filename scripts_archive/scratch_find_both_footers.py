with open('upolitico-clone/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'<div class="footer style-2">', text)]
print("Footer positions:", matches)
for m in matches:
    print(text[m:m+200])
