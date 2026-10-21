with open('upolitico-clone/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# check top-title-wrapper in index.html
m = re.search(r'<div class="top-title-wrapper">.*?</div>\s*</div>\s*<div class="w-slide">', text, re.DOTALL)
if m:
    print(m.group(0))
