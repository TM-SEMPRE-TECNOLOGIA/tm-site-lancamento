import re
from bs4 import BeautifulSoup

file_path = r'C:\Users\mikaa\Downloads\www.empurraodigital.com.br\www.empurraodigital.com.br\marketing-politico-eleicoes-2026.html'

with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("Title:", soup.title.string if soup.title else "No title")

# Headings
print("\n--- HEADINGS ---")
for h in soup.find_all(['h1', 'h2', 'h3', 'h4']):
    text = h.get_text(strip=True)
    if text:
        print(f"[{h.name.upper()}] {text}")

# Extract all paragraphs and lead texts
print("\n--- KEY COPY BLOCKS ---")
sections = soup.find_all(['section', 'div'], class_=re.compile(r's_|oe_structure|container|snippet', re.I))
print(f"Found {len(sections)} sections/blocks")
