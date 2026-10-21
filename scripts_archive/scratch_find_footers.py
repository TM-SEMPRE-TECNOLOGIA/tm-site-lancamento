with open('upolitico-clone/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'<div class="footer style-2">', text)]
print(f"Footer positions: {matches}")
for i, m in enumerate(matches):
    print(f"\n--- FOOTER {i+1} at index {m} ---")
    print(text[m:m+600])
