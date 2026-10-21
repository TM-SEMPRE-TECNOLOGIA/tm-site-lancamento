with open('upolitico-clone/css/estilo.css', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for j in range(2668, min(len(lines), 2730)):
    print(f"{j+1}: {lines[j]}", end='')
