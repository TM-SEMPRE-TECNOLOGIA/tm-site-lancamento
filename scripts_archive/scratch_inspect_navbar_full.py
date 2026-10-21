with open('upolitico-clone/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

idx_start = text.find('class="navbar')
idx_end = text.find('</nav>')
print("Navbar block in upolitico-clone/index.html:")
print(text[idx_start-50:idx_end+150])
