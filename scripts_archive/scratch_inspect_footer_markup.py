with open('upolitico-clone/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

idx = text.find('class="footer')
if idx != -1:
    print("--- FOOTER MARKUP ---")
    print(text[idx-100:idx+2500])
