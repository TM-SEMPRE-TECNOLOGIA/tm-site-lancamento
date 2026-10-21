with open('upolitico-clone/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'class="button' in line or "class='button" in line or 'button w-button' in line:
        print(f"Line {i+1}: {line.strip()}")
