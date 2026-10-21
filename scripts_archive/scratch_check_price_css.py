with open('upolitico-clone/css/estilo.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

import re
matches = re.findall(r'(\.price[^{]*\{[^}]*\})', css)
for m in matches:
    print(m)

print("--- PRECO CLASSES ---")
matches2 = re.findall(r'(\.preco[^{]*\{[^}]*\})', css)
for m in matches2:
    print(m)

print("--- TOP-PRICE ---")
matches3 = re.findall(r'(\.top-price[^{]*\{[^}]*\})', css)
for m in matches3:
    print(m)

print("--- FROM-TEXT ---")
matches4 = re.findall(r'(\.from-text[^{]*\{[^}]*\})', css)
for m in matches4:
    print(m)
