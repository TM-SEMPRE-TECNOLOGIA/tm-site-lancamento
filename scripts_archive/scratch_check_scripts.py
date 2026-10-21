with open('upolitico-clone/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
scripts = re.findall(r'<script[^>]*>(.*?)</script>', text, re.DOTALL)
for i, s in enumerate(scripts):
    if 'hero' in s or 'rotating' in s or 'vitoriosa' in s:
        print(f"Script {i+1}:")
        print(s[:500])
