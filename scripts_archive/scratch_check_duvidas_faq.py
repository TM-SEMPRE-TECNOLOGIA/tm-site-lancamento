with open('upolitico-clone/duvidas.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

faq_idx = text.find('Perguntas frequentes')
print("FAQ pos in duvidas.html:", faq_idx)
if faq_idx != -1:
    s_start = text.rfind('<div id="Scroll" class="section', 0, faq_idx)
    s_end = text.find('<div class="algin-center copyrights">', faq_idx)
    print("s_start:", s_start, "s_end:", s_end)
