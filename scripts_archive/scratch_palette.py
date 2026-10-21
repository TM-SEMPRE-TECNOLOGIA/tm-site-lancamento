import re

css_path = r"C:\Users\mikaa\Downloads\modelo landing page\www.vendatodosantodia.com.br (1)\www.vendatodosantodia.com.br\_next\static\css\d21895c2fbdddc29.css"
with open(css_path, "r", encoding="utf-8", errors="ignore") as f:
    css = f.read()

# Find hex colors
hex_colors = re.findall(r'#(?:[0-9a-fA-F]{3}){1,2}\b', css)
from collections import Counter
counts = Counter(hex_colors).most_common(25)
print("Top 25 Hex Colors in CSS:")
for color, count in counts:
    print(f"  {color}: {count} occurrences")

# Find background gradients
gradients = re.findall(r'linear-gradient\([^)]+\)', css)
print(f"\nGradients ({len(gradients)}):")
for g in set(gradients[:15]):
    print(f"  {g}")
