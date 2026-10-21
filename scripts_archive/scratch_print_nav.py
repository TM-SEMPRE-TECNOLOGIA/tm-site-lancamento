with open('upolitico-clone/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
nav_match = re.search(r'<div[^>]*role="banner" class="navbar[^"]*".*?</div>\s*</div>\s*(?=<div[^>]*class="banner)', text, re.DOTALL)
if nav_match:
    print(nav_match.group(0))
