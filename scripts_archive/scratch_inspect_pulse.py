import re

with open('khaled_extracted_skills_ui.js', 'r', encoding='utf-8') as f:
    code = f.read()

# find animate-chakra-pulse context
for m in re.finditer(r'animate-chakra-pulse', code):
    pos = m.start()
    print("--- PULSE SNIPPET ---")
    print(code[max(0, pos-150):min(len(code), pos+300)])

# find svg paths
for m in re.finditer(r'<path|\.path|path\b', code):
    pos = m.start()
    print("--- PATH SNIPPET ---")
    print(code[max(0, pos-100):min(len(code), pos+200)])
    break
