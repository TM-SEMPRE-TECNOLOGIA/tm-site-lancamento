import os

for path in ['upolitico-clone/referencia/index.html', 'upolitico-clone-backup-old/index.html']:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            c = f.read()
        print(f"=== {path} ===")
        idx = c.find('class="banner')
        if idx != -1:
            print(c[idx:idx+600])
