import re

file_path = r'C:\Users\mikaa\Downloads\www.empurraodigital.com.br\www.empurraodigital.com.br\marketing-politico-eleicoes-2026.html'

with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Extract text sections cleanly
html_no_scripts = re.sub(r'<(script|style|svg)[^>]*>.*?</\1>', '', html, flags=re.DOTALL | re.I)

# Let's extract sections and their text
lines = []
for tag in re.finditer(r'<(h[1-4]|p|li)[^>]*>(.*?)</\1>', html_no_scripts, re.DOTALL | re.I):
    tag_name = tag.group(1).lower()
    raw = tag.group(2)
    clean = re.sub(r'<[^>]+>', ' ', raw)
    clean = ' '.join(clean.split())
    if len(clean) > 2 and not any(k in clean.lower() for k in ['cookie', 'turnstile', 'javascript', 'copyright']):
        if tag_name.startswith('h'):
            lines.append(f"\n### [{tag_name.upper()}] {clean}\n")
        elif tag_name == 'p':
            lines.append(f"{clean}\n")
        elif tag_name == 'li':
            lines.append(f"• {clean}")

output_report = '\n'.join(lines)

report_path = r'C:\Users\mikaa\.gemini\antigravity-ide\brain\2a8cfc55-89d0-42be-b82a-a300aaa882d2\analise_empurrao_digital_copy.md'
with open(report_path, 'w', encoding='utf-8') as f:
    f.write("# Análise de Copywriting e Estrutura: Empurrão Digital (Eleições 2026)\n\n" + output_report)

print("Saved report to", report_path)
print(f"Total lines extracted: {len(lines)}")
