with open('upolitico-clone/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'Upol', text)]
print("Upol matches:", len(matches))
for m in matches:
    print(text[m-20:m+80])
