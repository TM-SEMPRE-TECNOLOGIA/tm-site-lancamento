import os

clone_dir = r'c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\upolitico-clone'
index_path = os.path.join(clone_dir, 'index.html')

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect where banner style-3 is defined and the hero image tag
print("banner style-3 pos:", html.find('class="banner style-3"'))
print("banner-1.png pos:", html.find('banner-1.png'))
