with open('upolitico-clone/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find("var words = [")
if idx != -1:
    print(text[max(0, idx-100):min(len(text), idx+600)])
