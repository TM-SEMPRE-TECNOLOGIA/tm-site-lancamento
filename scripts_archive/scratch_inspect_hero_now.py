with open('upolitico-clone/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
m = re.search(r'<div[^>]*class="banner style-3".*?<div class="waves-bottom2"></div>', html, re.DOTALL)
if m:
    print("Found hero section:")
    print(m.group(0)[:600])
