with open('khaled_extracted_skills_shader.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.finditer(r'\.jsx\)\s*\(\s*["\']([a-zA-Z0-9_-]+)["\']\s*,\s*(\{.*?\})\s*\)', text)
for i, m in enumerate(matches):
    tag = m.group(1)
    props = m.group(2)[:180]
    print(f"[{i}] <{tag}>: {props}...")
