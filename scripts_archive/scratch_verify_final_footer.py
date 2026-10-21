with open('upolitico-clone/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
print("Occurrences of 'Perguntas frequentes':", len(re.findall(r'Perguntas frequentes', text)))
print("Occurrences of 'Solicite um':", len(re.findall(r'Solicite um', text)))
print("Occurrences of 'footer style-2':", len(re.findall(r'footer style-2', text)))
print("Occurrences of 'copyrights':", len(re.findall(r'class="algin-center copyrights"', text)))

# Check for unclosed divs
open_divs = len(re.findall(r'<div\b', text))
close_divs = len(re.findall(r'</div\b', text))
print(f"Div tags: {open_divs} opened, {close_divs} closed. Diff: {open_divs - close_divs}")
