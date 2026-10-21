with open('upolitico-clone/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Let's inspect the two footer blocks
p1_start = text.rfind('<div class="section image">', 0, 52370)
print("p1_start (first CTA):", p1_start)

p2_start = text.rfind('<div class="section image">', 0, 61998)
print("p2_start (second CTA):", p2_start)

# What is right after Footer 1?
# Let's check text around 52370 to 56300
idx_f1_end = text.find('<div id="Scroll" class="section', 52370)
print("Footer 1 ends at (starts FAQ 2):", idx_f1_end)
print(text[idx_f1_end-100:idx_f1_end+200])

idx_f2_end = text.find('<div class="algin-center copyrights">', 61998)
print("Footer 2 ends at (starts copyright):", idx_f2_end)
print(text[idx_f2_end-100:idx_f2_end+200])
