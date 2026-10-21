with open('upolitico-clone/duvidas.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

s_start = 7224
s_end = 18077
snippet = text[s_start:s_end]
print("Snippet length:", len(snippet))
print("Start of snippet:")
print(snippet[:300])
print("\nEnd of snippet:")
print(snippet[-400:])
