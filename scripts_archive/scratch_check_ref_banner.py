import os

for path in ['reference-site/index.html', 'modelo-politico/index.html']:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            c = f.read()
        print(f"=== {path} ===")
        idx = c.find('class="banner')
        if idx != -1:
            print(c[idx:idx+800])
        else:
            print("No class='banner' found")
