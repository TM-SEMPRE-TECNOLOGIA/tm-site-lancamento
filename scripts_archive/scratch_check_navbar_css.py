with open('upolitico-clone/css/estilo.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

import re
matches = re.findall(r'(\.navbar[^{]*\{[^}]*\})', css)
for m in matches:
    print(m)

print("--- BRAND ---")
for m in re.findall(r'(\.brand[^{]*\{[^}]*\})', css):
    print(m)

print("--- NAVLINK ---")
for m in re.findall(r'(\.navlink[^{]*\{[^}]*\})', css):
    print(m)
