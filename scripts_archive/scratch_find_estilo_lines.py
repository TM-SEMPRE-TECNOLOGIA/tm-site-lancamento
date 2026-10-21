with open('upolitico-clone/css/estilo.css', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'linear-gradient(to left, #79a0d8' in line or 'linear-gradient(to left, #ffffff' in line:
        print(f"Line {i+1}: {line.strip()}")
        for j in range(max(0, i-6), min(len(lines), i+8)):
            print(f"  {j+1}: {lines[j]}", end='')
