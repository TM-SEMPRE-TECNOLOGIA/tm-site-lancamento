with open('upolitico-clone-backup-old/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

idx = text.find('role="banner" class="navbar')
if idx != -1:
    print(text[idx-50:idx+1200])
