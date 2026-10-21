with open('khaled_extracted_skills_ui.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('flex items-center gap-4')
if idx != -1:
    print(text[idx : idx + 1500])
