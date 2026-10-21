import os
from PIL import Image

src_img = r'C:\Users\mikaa\.gemini\antigravity-ide\brain\2a8cfc55-89d0-42be-b82a-a300aaa882d2\.user_uploaded\media_1789095502260.jpg'
dest_dir = r'c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\upolitico-clone\imagens'

img = Image.open(src_img)
print("Original size:", img.size)

# High-resolution resize (2048px width)
target_w = 2048
target_h = int(target_w * img.height / img.width)
resized = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
print("Resized to:", resized.size)

jpg_path = os.path.join(dest_dir, 'hero-war-room.jpg')
png_path = os.path.join(dest_dir, 'hero-war-room.png')
banner_path = os.path.join(dest_dir, 'banner-1.png')

resized.save(jpg_path, format='JPEG', quality=95, optimize=True)
resized.save(png_path, format='PNG', optimize=True)
resized.save(banner_path, format='PNG', optimize=True)

print("Saved hero images:")
print(" -", jpg_path, f"({os.path.getsize(jpg_path)} bytes)")
print(" -", png_path, f"({os.path.getsize(png_path)} bytes)")
print(" -", banner_path, f"({os.path.getsize(banner_path)} bytes)")
