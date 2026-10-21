with open('upolitico-clone/css/estilo.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

import re
print("--- LINK-BLOCK ---")
for m in re.findall(r'(\.link-block[^{]*\{[^}]*\})', css):
    print(m)

print("--- FOOTER ---")
for m in re.findall(r'(\.footer[^{]*\{[^}]*\})', css)[:10]:
    print(m)

print("--- FOOTER COLUMN ---")
for m in re.findall(r'(\.footer-column[^{]*\{[^}]*\})', css):
    print(m)
