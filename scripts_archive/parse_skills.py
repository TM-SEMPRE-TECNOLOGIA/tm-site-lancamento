with open(r'C:\Users\mikaa\.gemini\antigravity-ide\brain\5bb536be-2de3-482a-a11e-071f2fa46483\.system_generated\steps\122\content.md', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

start = text.find('skills\\":[')
end = text.find('],\\"navigation\\":', start)

raw_json = '{"skills":' + text[start+9:end+1].replace('\\"', '"') + '}'
with open('skills_khaled.json', 'w', encoding='utf-8') as out:
    out.write(raw_json)

import json
data = json.loads(raw_json)
print("Successfully parsed", len(data['skills']), "skills!")
for s in data['skills']:
    print(f"- {s['name']} (Category: {s['category']}, Color: {s['color']}, Pos: {s['position']}, Label: {s['label']})")
