with open('khaled_extracted_skills_ui.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.findall(r'skeleton-rage-layer', text)
print("skeleton-rage-layer count in UI:", len(m))

for match in re.finditer(r'skeleton-rage-layer', text):
    pos = match.start()
    print("--- SKELETON RAGE SNIPPET ---")
    print(text[max(0, pos-150):min(len(text), pos+300)])
