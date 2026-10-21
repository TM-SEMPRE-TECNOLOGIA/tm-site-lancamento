import re
from html.parser import HTMLParser

file_path = r'C:\Users\mikaa\Downloads\www.empurraodigital.com.br\www.empurraodigital.com.br\marketing-politico-eleicoes-2026.html'

with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Clean tags to extract text
clean_text = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
clean_text = re.sub(r'<style[^>]*>.*?</style>', '', clean_text, flags=re.DOTALL)

print("--- ALL HEADINGS ---")
for m in re.finditer(r'<(h[1-4])[^>]*>(.*?)</\1>', clean_text, re.DOTALL | re.I):
    tag = m.group(1).upper()
    content = re.sub(r'<[^>]+>', '', m.group(2)).strip()
    content = ' '.join(content.split())
    if content:
        print(f"[{tag}] {content}")

print("\n--- CTAs & BUTTONS ---")
for m in re.finditer(r'<a[^>]*class="[^"]*(?:btn|button)[^"]*"[^>]*>(.*?)</a>', clean_text, re.DOTALL | re.I):
    cta = re.sub(r'<[^>]+>', '', m.group(1)).strip()
    cta = ' '.join(cta.split())
    if cta:
        print(f"[CTA] {cta}")

print("\n--- IMAGES USED ---")
for m in re.finditer(r'<img[^>]*src="([^"]+)"', clean_text):
    src = m.group(1)
    if not any(x in src for x in ['facebook', 'turnstile', 'odoo_logo', 'font', 'flags']):
        print(" -", src)
