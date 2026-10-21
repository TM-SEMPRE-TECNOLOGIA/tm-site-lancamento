with open(r'C:\Users\mikaa\.gemini\antigravity-ide\brain\5bb536be-2de3-482a-a11e-071f2fa46483\.system_generated\steps\122\content.md', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

target = '"skills":['
idx = text.find(target)
print("Skills data located at:", idx)
with open('skills_data.json', 'w', encoding='utf-8') as out:
    # grab from idx to end of array
    end = text.find('],"navigation":', idx)
    out.write('{' + text[idx:end+1] + '}')

print("Saved skills_data.json successfully!")
