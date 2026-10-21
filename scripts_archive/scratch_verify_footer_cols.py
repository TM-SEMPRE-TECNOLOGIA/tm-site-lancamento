with open('upolitico-clone/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

print("Has Campanhas & Soluções:", "Campanhas & Soluções" in text or "Campanhas & Solu" in text)
idx = text.find('class="footer style-2"')
if idx != -1:
    print(text[idx:idx+1500])
