import os
import re

DASH_DIR = 'dashboard-siqueira-35'

# 1. Update package.json
pkg_file = os.path.join(DASH_DIR, 'package.json')
with open(pkg_file, 'r', encoding='utf-8') as f:
    pkg = f.read()

pkg = pkg.replace('"name": "dashboard-adir-2211"', '"name": "dashboard-siqueira-35"')
pkg = pkg.replace('"dev": "next dev"', '"dev": "next dev -p 3005"')
with open(pkg_file, 'w', encoding='utf-8') as f:
    f.write(pkg)
print("Updated package.json")

# 2. Update globals.css
css_file = os.path.join(DASH_DIR, 'app', 'globals.css')
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

css_replacements = [
    ('#005CAA', '#103D80'),
    ('#005caa', '#103d80'),
    ('#004B8C', '#0A2540'),
    ('#00407A', '#07172C'),
    ('#004480', '#0A2540'),
    ('#FFCB05', '#3FA464'),
    ('#ffcb05', '#3fa464'),
    ('#008744', '#3FA464'),
    ('rgba(0, 92, 170,', 'rgba(16, 61, 128,'),
]

for old, new in css_replacements:
    css = css.replace(old, new)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated globals.css")

# 3. Update app/layout.tsx
layout_file = os.path.join(DASH_DIR, 'app', 'layout.tsx')
with open(layout_file, 'r', encoding='utf-8') as f:
    lay = f.read()

lay = lay.replace(
    "title: 'Adir Gentil 2211 • Dashboard de Analytics & Inteligência de Campanha'",
    "title: 'Siqueira Campos Jr 35 • Dashboard de Analytics & Inteligência de Campanha'"
)
lay = lay.replace(
    "description: 'Painel executivo de analytics, tráfego pago, SEO/GEO e mobilização política no Tocantins para o Deputado Adir Gentil 2211.'",
    "description: 'Painel executivo de analytics, tráfego pago, SEO/GEO e mobilização eleitoral no Tocantins para Siqueira Campos Jr 35 (Democrata).'"
)
with open(layout_file, 'w', encoding='utf-8') as f:
    f.write(lay)
print("Updated app/layout.tsx")

# 4. Global string replacements across tsx and ts files
ts_replacements = [
    ('Adir Gentil 2211', 'Siqueira Campos Jr 35'),
    ('ADIR GENTIL 2211', 'SIQUEIRA CAMPOS JR 35'),
    ('Adir Gentil', 'Siqueira Campos Jr'),
    ('ADIR GENTIL', 'SIQUEIRA CAMPOS JR'),
    ('adir gentil', 'siqueira campos jr'),
    ('Adir', 'Siqueira Campos Jr'),
    ('Deputado Federal', 'Governador do Tocantins'),
    ('DEPUTADO FEDERAL', 'GOVERNADOR DO TOCANTINS'),
    ('Deputado Adir Gentil 2211', 'Siqueira Campos Jr 35'),
    ('2211', '35'),
    ('PL (Partido Liberal)', 'Democrata (35)'),
    ('Partido Liberal', 'Democrata'),
    ('PARTIDO LIBERAL', 'DEMOCRATA'),
    ('/logo-adir-gentil-2211.png', '/democrata-35-logo.png'),
    ('/logo-adir-gentil-35.png', '/democrata-35-logo.png'),
    ('adirgentil2211.vercel.app', 'localhost:3006'),
    ('adirgentil35.vercel.app', 'localhost:3006'),
    ('#FFCB05', '#3FA464'),
    ('#ffcb05', '#3fa464'),
    ('#005CAA', '#103D80'),
    ('#005caa', '#103d80'),
    ('#005baa', '#103d80'),
    ('#005BAA', '#103d80'),
    ('oadirgentil', 'siqueiracamposjr_'),
    ('tocomadir', 'tocomsiqueira')
]

for root, dirs, files in os.walk(DASH_DIR):
    for f in files:
        if f.endswith(('.tsx', '.ts', '.js', '.json', '.html')):
            fpath = os.path.join(root, f)
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
            
            orig = content
            for old, new in ts_replacements:
                content = content.replace(old, new)
            
            if content != orig:
                with open(fpath, 'w', encoding='utf-8') as fp:
                    fp.write(content)
                print(f"Refactored: {fpath}")

print("Dashboard refactoring completed successfully!")
