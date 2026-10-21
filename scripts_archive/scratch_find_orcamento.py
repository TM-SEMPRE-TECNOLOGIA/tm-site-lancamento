with open('upolitico-clone/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'orcamento.html' in line:
        print(f"Line {i+1}: {line.strip()}")
        # print context
        for j in range(max(0, i-3), min(len(lines), i+4)):
            print(f"  {j+1}: {lines[j]}", end='')
        print("---")
