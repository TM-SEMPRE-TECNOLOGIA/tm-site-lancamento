with open('upolitico-clone/css/estilo.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

import re
print("--- LOGO RULES ---")
for m in re.findall(r'(\.logo[^{]*\{[^}]*\})', css):
    print(m)

print("--- NAVBAR RULES ---")
for m in re.findall(r'(\.nav[^{]*\{[^}]*\})', css)[:10]:
    print(m)
