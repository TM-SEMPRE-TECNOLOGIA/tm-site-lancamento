import urllib.request
import re
import os
from PIL import Image, ImageDraw

os.makedirs('assets/logos', exist_ok=True)

# 1. Fetch Hermes 3 official banner or icon from NousResearch repo
hermes_url = None
try:
    req = urllib.request.Request('https://raw.githubusercontent.com/NousResearch/Hermes-3/main/README.md', headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=8) as resp:
        content = resp.read().decode('utf-8', errors='ignore')
        matches = re.findall(r'https://[^\s\)\"\']+\.(?:png|jpg|webp)', content)
        print("Hermes repo images:", matches)
        if matches:
            hermes_url = matches[0]
except Exception as e:
    print("Hermes error:", e)

# Let's also check NousResearch avatar on GitHub
nous_avatar_url = 'https://avatars.githubusercontent.com/u/84102146?v=4' # NousResearch org avatar on github
print("Nous avatar URL:", nous_avatar_url)
