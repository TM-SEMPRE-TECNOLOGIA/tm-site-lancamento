with open('upolitico-clone/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

idx = text.find('class="footer style-2"')
print("Footer section from style-2:")
print(text[idx:idx+2500])
