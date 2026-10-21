import re

with open(r'C:\Users\mikaa\.gemini\antigravity-ide\brain\5bb536be-2de3-482a-a11e-071f2fa46483\.system_generated\steps\122\content.md', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

pos = text.find('id="skills"')
if pos == -1:
    pos = text.find('skills')

with open('skills_dom_dump.html', 'w', encoding='utf-8') as out:
    out.write(text[pos:pos+15000])

print("Wrote snippet at pos:", pos)
