with open('upolitico-clone/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

f1 = 53453
f2 = 58926
print("Between f1 and f2:")
print(text[f1:f1+300])
print("...")
print(text[f2-300:f2])
