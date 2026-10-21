import re

html_path = r'c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\upolitico-clone\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Let's check how the navbar is structured
nav_match = re.search(r'<div[^>]*role="banner" class="navbar[^"]*".*?</nav>', html, re.DOTALL)
if nav_match:
    print("Found navbar in index.html, length:", len(nav_match.group(0)))
