with open('upolitico-clone/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

idx = text.find('Entrada Digital')
print("Index in index.html:", idx)
if idx != -1:
    print(text[idx-150:idx+1200])
