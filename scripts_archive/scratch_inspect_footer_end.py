with open('upolitico-clone/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

idx = text.find('class="footer style-2"')
if idx != -1:
    print(text[idx-200:idx+3500])
