with open('upolitico-clone/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

print("Between Footer 1 and Footer 2:")
print(text[52300:55000])
