import re

with open('khaled_extracted_skills_ui.js', 'r', encoding='utf-8') as f:
    code = f.read()

print("File length:", len(code))

# Find words related to line, laser, bezier, svg, connecting
keywords = ['M ', 'C ', 'svg', 'path', 'stroke', 'bezier', 'chakra', 'laser']
for kw in keywords:
    count = code.count(kw)
    print(f"Keyword '{kw}': {count} occurrences")

# Find where chakra nodes or lines are built
for m in re.finditer(r'chakra', code, re.IGNORECASE):
    pos = m.start()
    print("Snippet:", code[max(0, pos-40):min(len(code), pos+120)])
    break
