with open('upolitico-clone-backup-old/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

faq_idx = text.find('Perguntas frequentes')
print("FAQ pos in backup:", faq_idx)
if faq_idx != -1:
    section_start = text.rfind('<div id="Scroll" class="section', 0, faq_idx)
    section_end = text.find('<div class="algin-center copyrights">', faq_idx)
    print("section_start:", section_start, "section_end:", section_end)
    print(text[section_start:section_start+400])
