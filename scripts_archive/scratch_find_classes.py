with open(r'C:\Users\mikaa\Downloads\www.khaledoghli.com\_next\static\chunks\04nwbzv778w-3.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.findall(r'(\.[a-zA-Z0-9_-]*(?:energy|chakra|rage|laser)[a-zA-Z0-9_-]*\s*\{[^}]*\})', text)
print(f"Found {len(m)} relevant classes:")
for c in m:
    print("---")
    print(c)
