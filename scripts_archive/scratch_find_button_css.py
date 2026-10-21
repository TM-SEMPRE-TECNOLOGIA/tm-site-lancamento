with open('upolitico-clone/css/estilo.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

import re
matches = re.findall(r'(\.button[^{]*\{[^}]*\})', css)
for m in matches[:15]:
    print(m.strip())
    print('---')
