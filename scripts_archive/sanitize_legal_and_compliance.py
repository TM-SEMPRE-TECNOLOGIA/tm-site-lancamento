import os
import re

site_dir = r"c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\site-deputado-template"
html_files = [f for f in os.listdir(site_dir) if f.endswith('.html')]

print(f"Iniciando sanitizacao legal e de compliance em {len(html_files)} arquivos...")

# 1. Atualizacao de metadata e tags gerais em todos os HTMLs
for fname in html_files:
    fpath = os.path.join(site_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Remover vice Alfredo Gaspar das tags og:image:alt e meta
    content = content.replace("Adir Gentil, Deputado Federal 2211, vice Alfredo Gaspar", "Adir Gentil, Deputado Federal 2211 - Tocantins")
    content = content.replace("vice Alfredo Gaspar", "PL Tocantins")
    content = content.replace("Alfredo Gaspar — Partido Liberal (PL)", "PL Tocantins (2211)")
    
    # Corrigir meta descriptions de trajetoria
    content = content.replace(
        "sua experiência como deputado estadual e senador da República e sua candidatura à Presidência pelo número 2211.",
        "sua trajetória de realizações no Tocantins, sua liderança e sua candidatura a Deputado Federal pelo número 2211."
    )

    # Corrigir CNPJ generico / em homologacao
    content = content.replace("CNPJ sob o nº Em homologação eleitoral", "CNPJ sob o nº 68.492.004/0001-78")
    content = content.replace("<td>Em homologação eleitoral</td>", "<td>68.492.004/0001-78</td>")
    content = content.replace("<td>flaviobolsonaro.com.br</td>", "<td>adirgentil2211.com.br</td>")
    content = content.replace("materiais.flaviobolsonaro.com.br", "materiais.adirgentil2211.com.br")

    # Corrigir handles de redes sociais residuais
    content = content.replace("@FlavioBolsonaro", "@oadirgentil")
    content = content.replace("/flaviobolsonaro", "/oadirgentil")
    content = content.replace("flaviobolsonaro", "oadirgentil")

    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[SANITIZADO]: {fname}")

# 2. Ajustes especificos no aviso-legal.html
aviso_path = os.path.join(site_dir, "aviso-legal.html")
with open(aviso_path, 'r', encoding='utf-8') as f:
    aviso_content = f.read()

old_aviso_table = """<div class="legal-table-wrap"><table><thead><tr><th scope="col">Informação eleitoral</th><th scope="col">Dado</th></tr></thead><tbody><tr><td>Candidato</td><td>Adir Gentil</td></tr><tr><td>Cargo</td><td>Deputado Federal da República</td></tr><tr><td>Número</td><td>2211</td></tr><tr><td>Partido</td><td>Partido Liberal — PL</td></tr><tr><td>Vice</td><td>Alfredo Gaspar — Partido Liberal (PL)</td></tr><tr><td>Coligação</td><td>Não há</td></tr><tr><td>CNPJ da candidatura</td><td>Em homologação eleitoral</td></tr><tr><td>Domínio oficial</td><td>flaviobolsonaro.com.br</td></tr></tbody></table></div>"""

new_aviso_table = """<div class="legal-table-wrap"><table><thead><tr><th scope="col">Informação eleitoral</th><th scope="col">Dado</th></tr></thead><tbody><tr><td>Candidato</td><td>ADIR CARDOSO GENTIL</td></tr><tr><td>Nome de Urna</td><td>ADIR GENTIL</td></tr><tr><td>Cargo Eletivo</td><td>Deputado Federal</td></tr><tr><td>Número Oficial</td><td>2211</td></tr><tr><td>Partido Político</td><td>Partido Liberal — PL (Tocantins)</td></tr><tr><td>Circunscrição / UF</td><td>Tocantins (TO) — 139 Municípios</td></tr><tr><td>CNPJ da Campanha</td><td>68.492.004/0001-78</td></tr><tr><td>Endereço do Comitê Central</td><td>Quadra ARSO 111, Alameda 19 — Palmas/TO</td></tr><tr><td>Telefone Oficial</td><td>48 9974-0613</td></tr><tr><td>E-mail Oficial</td><td>contato@adirgentil2211.com.br</td></tr><tr><td>Domínio Oficial</td><td>adirgentil2211.com.br</td></tr></tbody></table></div>"""

if old_aviso_table in aviso_content:
    aviso_content = aviso_content.replace(old_aviso_table, new_aviso_table)
    with open(aviso_path, 'w', encoding='utf-8') as f:
        f.write(aviso_content)
    print("[OK] Tabela do aviso-legal.html substituida com dados completos.")
else:
    # Substituir via regex caso haja pequenas variacoes
    aviso_content = re.sub(
        r'<div class="legal-table-wrap"><table><thead><tr><th scope="col">Informação eleitoral</th>[\s\S]*?</table></div>',
        new_aviso_table,
        aviso_content,
        flags=re.IGNORECASE
    )
    with open(aviso_path, 'w', encoding='utf-8') as f:
        f.write(aviso_content)
    print("[OK] Tabela do aviso-legal.html atualizada via regex.")

# 3. Ajustes de termos-de-uso.html (remover mencoes ao vice)
termos_path = os.path.join(site_dir, "termos-de-uso.html")
with open(termos_path, 'r', encoding='utf-8') as f:
    termos_content = f.read()

termos_content = termos_content.replace("número, vice e eventual", "número e eventual")
termos_content = termos_content.replace("ao candidato, ao vice ou à Campanha", "ao candidato ou à Campanha")
with open(termos_path, 'w', encoding='utf-8') as f:
    f.write(termos_content)
print("[OK] termos-de-uso.html atualizado.")

# 4. Ajustes no noticias.html
noticias_path = os.path.join(site_dir, "noticias.html")
with open(noticias_path, 'r', encoding='utf-8') as f:
    noticias_content = f.read()

noticias_content = noticias_content.replace("Deputado Federal da República", "Deputado Federal")
noticias_content = noticias_content.replace("Candidato do PL à Presidência da República", "Candidato a Deputado Federal pelo PL Tocantins")
noticias_content = noticias_content.replace("Senador e candidato do PL à Presidência da República", "Adir Gentil, candidato a Deputado Federal pelo PL Tocantins")
noticias_content = noticias_content.replace("rumo ao Palácio do Planalto", "rumo à Câmara dos Deputados")
noticias_content = noticias_content.replace(
    "”Ano que vem quero voltar aqui como Deputado Federal da República e trarei junto comigo meu pai, Jair Messias Bolsonaro”,...",
    "”Como Deputado Federal pelo Tocantins, trabalharei incansavelmente por recursos para a saúde, infraestrutura e juventude dos nossos 139 municípios.”,..."
)
with open(noticias_path, 'w', encoding='utf-8') as f:
    f.write(noticias_content)
print("[OK] noticias.html atualizado com contexto 100% de Tocantins.")

# 5. Ajustes no js/analytics-client.js
analytics_path = os.path.join(site_dir, "js", "analytics-client.js")
if os.path.exists(analytics_path):
    with open(analytics_path, 'r', encoding='utf-8') as f:
        ac_content = f.read()
    ac_content = ac_content.replace("Campanha Flávio Bolsonaro Presidente 22", "Campanha Oficial Adir Gentil 2211")
    ac_content = ac_content.replace("materiais.flaviobolsonaro.com.br", "materiais.adirgentil2211.com.br")
    with open(analytics_path, 'w', encoding='utf-8') as f:
        f.write(ac_content)
    print("[OK] js/analytics-client.js limpo e atualizado.")

# 6. Atualizar institucional em participe.html
participe_path = os.path.join(site_dir, "participe.html")
with open(participe_path, 'r', encoding='utf-8') as f:
    part_content = f.read()

part_content = part_content.replace("Palmas - TO", "Quadra ARSO 111, Alameda 19 — Palmas/TO")
part_content = part_content.replace("(62) 99604-6458", "48 9974-0613")
with open(participe_path, 'w', encoding='utf-8') as f:
    f.write(part_content)
print("[OK] participe.html institucional atualizado.")

print("Sanitizacao concluida com exito!")
