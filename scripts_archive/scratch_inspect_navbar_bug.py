with open('upolitico-clone/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# Let's inspect the navbar markup from <div data-collapse="medium" to </nav> or end of navbar
nav_idx = text.find('role="banner" class="navbar')
if nav_idx != -1:
    print("--- NAVBAR SNIPPET (from start) ---")
    print(text[nav_idx-50:nav_idx+1200])

# Also let's check where "Calibração do Pixel Meta" appears in index.html!
pixel_idx = text.find('Calibra')
if pixel_idx != -1:
    print("\n--- 'Calibração' SNIPPET ---")
    print(text[pixel_idx-200:pixel_idx+300])
