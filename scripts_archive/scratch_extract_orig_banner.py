import os
import base64
from PIL import Image
import io

path = 'upolitico-clone-backup-old/index.html'
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

idx = c.find('class="banner style-3"><img src="data:image/png;base64,')
if idx == -1:
    idx = c.find('class="banner style-3"><img src=data:image/png;base64,')

if idx != -1:
    sub = c[idx:]
    start_b64 = sub.find('base64,') + 7
    end_b64 = sub.find('"', start_b64)
    if end_b64 == -1:
        end_b64 = sub.find(' ', start_b64)
    b64_str = sub[start_b64:end_b64]
    data = base64.b64decode(b64_str)
    im = Image.open(io.BytesIO(data))
    print("Original banner image size:", im.size, "Mode:", im.mode)
    out_path = 'upolitico-clone/scratch_original_banner_img.png'
    im.save(out_path)
    print("Saved to", out_path)
