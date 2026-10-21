with open('upolitico-clone/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# find where the original kits start (Básico, Intermediário, Avançado, Completo)
idx = text.find('preco1')
if idx == -1:
    idx = text.find('Básico')
if idx == -1:
    idx = text.find('199')

print("Index of kit básico:", idx)
if idx != -1:
    print(text[idx-200:idx+1500])
