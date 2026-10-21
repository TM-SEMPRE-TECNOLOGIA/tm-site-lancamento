with open('upolitico-clone/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(300, 360):
    print(f"{i+1}: {lines[i]}", end='')
