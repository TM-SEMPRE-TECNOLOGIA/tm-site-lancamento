import re
import os

html_path = r"C:\Users\mikaa\Downloads\www.khaledoghli.com\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

print("HTML size:", len(html))

# Find all image paths
imgs = re.findall(r'src=["\']([^"\']+\.(?:webp|png|jpg|svg))["\']', html)
print("Images found in index.html:")
for img in set(imgs):
    print(" ", img)

# Find chakra mentions
chakras = re.findall(r'chakra[^\s"\'<>]*', html, re.IGNORECASE)
print("Chakra matches:", set(chakras))

# Find section with skills
matches = re.findall(r'<section[^>]*id=["\'][^"\']*skill[^"\']*["\'][^>]*>.*?</section>', html, re.DOTALL | re.IGNORECASE)
if matches:
    print("Found skills section in HTML! Length:", len(matches[0]))
    with open("downloaded_skills_section.html", "w", encoding="utf-8") as out:
        out.write(matches[0])
    print("Wrote to downloaded_skills_section.html")
else:
    print("Could not find <section id='*skill*'> directly, searching general:")
    # look for classes or ids containing skill
    all_skills = re.findall(r'id=["\']([^"\']*skill[^"\']*)["\']', html, re.IGNORECASE)
    print("IDs with skill:", all_skills)
