with open('upolitico-clone/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(340, 355):
    print(f"{i+1}: {lines[i]}", end='')
