with open('upolitico-clone/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

pixel_idx = text.find('Calibra')
print(f"Pixel match at index: {pixel_idx}")
if pixel_idx != -1:
    print(text[pixel_idx-300:pixel_idx+400].encode('ascii', errors='replace').decode('ascii'))
