import os
from PIL import Image

src_path = r'C:\Users\mikaa\.gemini\antigravity-ide\brain\2a8cfc55-89d0-42be-b82a-a300aaa882d2\hero_brasil_landmarks_1789095413463.jpg'
dest_dir = r'c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\upolitico-clone\imagens'

img = Image.open(src_path)
print("Original size:", img.size)

# Target crisp panoramic hero dimension: 2400 x 1340
target_size = (2400, int(2400 * img.height / img.width))
img_resized = img.resize(target_size, Image.Resampling.LANCZOS)
print("Resized to:", img_resized.size)

# Save to destination files
png_path = os.path.join(dest_dir, 'hero-brasil-pontos.png')
jpg_path = os.path.join(dest_dir, 'hero-brasil-pontos.jpg')
banner_path = os.path.join(dest_dir, 'banner-1.png')

img_resized.save(png_path, format='PNG', optimize=True)
img_resized.save(jpg_path, format='JPEG', quality=95, optimize=True)
img_resized.save(banner_path, format='PNG', optimize=True)

print("Saved successfully:")
print(" -", png_path, f"({os.path.getsize(png_path)} bytes)")
print(" -", jpg_path, f"({os.path.getsize(jpg_path)} bytes)")
print(" -", banner_path, f"({os.path.getsize(banner_path)} bytes)")
