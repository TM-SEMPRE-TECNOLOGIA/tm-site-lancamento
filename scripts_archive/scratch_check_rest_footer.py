with open('upolitico-clone/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

idx = text.find('Planos & Apoio')
print(text[idx:idx+2000])
