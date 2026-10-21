import os
import base64
from playwright.sync_api import sync_playwright

html_path = r"C:\Users\mikaa\Documents\antigravity\tm-site-lancamento\banner_facebook_tm_v2.html"
output_png = r"C:\Users\mikaa\Documents\antigravity\tm-site-lancamento\banner_facebook_tm_v2.png"
logo_file = r"C:\Users\mikaa\Documents\antigravity\tm-site-lancamento\logo_banner.png"

with open(logo_file, "rb") as f:
    b64_logo = base64.b64encode(f.read()).decode("utf-8")

html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400;1,6..72,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  
  body {{
    width: 1640px;
    height: 924px;
    background-color: #07090E;
    overflow: hidden;
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #F8FAFC;
    position: relative;
    display: flex;
    align-items: center;
  }}

  /* Ruído/Textura de design editorial refinado */
  .noise-overlay {{
    position: absolute;
    inset: 0;
    opacity: 0.025;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
    pointer-events: none;
    z-index: 4;
  }}

  /* Luzes ambientes sutis (gradientes orgânicos de design suíço/moderno) */
  .ambient-glow-1 {{
    position: absolute;
    width: 900px;
    height: 900px;
    right: 50px;
    top: 50%;
    transform: translateY(-50%);
    background: radial-gradient(circle, rgba(217, 101, 38, 0.16) 0%, rgba(217, 101, 38, 0.03) 50%, transparent 75%);
    pointer-events: none;
    z-index: 1;
  }}

  .ambient-glow-2 {{
    position: absolute;
    width: 600px;
    height: 600px;
    left: -100px;
    bottom: -150px;
    background: radial-gradient(circle, rgba(30, 41, 59, 0.4) 0%, transparent 70%);
    pointer-events: none;
    z-index: 1;
  }}

  /* Linhas arquitetônicas sutis */
  .grid-lines {{
    position: absolute;
    inset: 0;
    pointer-events: none;
    z-index: 2;
  }}
  .grid-line-h {{
    position: absolute;
    left: 0; right: 0;
    height: 1px;
    background: rgba(255, 255, 255, 0.04);
  }}
  .grid-line-v {{
    position: absolute;
    top: 0; bottom: 0;
    width: 1px;
    background: rgba(255, 255, 255, 0.04);
  }}

  /* MARCA D'ÁGUA GIGANTE DA LOGO INTEGRADA AO FUNDO */
  .bg-watermark-logo {{
    position: absolute;
    right: -60px;
    top: 50%;
    transform: translateY(-50%);
    width: 860px;
    height: 860px;
    opacity: 0.11;
    filter: grayscale(20%) contrast(110%);
    z-index: 3;
    pointer-events: none;
    mask-image: radial-gradient(circle at 60% 50%, black 30%, transparent 75%);
    -webkit-mask-image: radial-gradient(circle at 60% 50%, black 30%, transparent 75%);
  }}

  /* Marca d'água secundária com blend suave */
  .bg-watermark-ring {{
    position: absolute;
    right: 180px;
    top: 50%;
    transform: translateY(-50%);
    width: 520px;
    height: 520px;
    border: 1px solid rgba(217, 101, 38, 0.12);
    border-radius: 50%;
    z-index: 2;
    pointer-events: none;
  }}
  .bg-watermark-ring-outer {{
    position: absolute;
    right: 90px;
    top: 50%;
    transform: translateY(-50%);
    width: 700px;
    height: 700px;
    border: 1px dashed rgba(255, 255, 255, 0.04);
    border-radius: 50%;
    z-index: 2;
    pointer-events: none;
  }}

  /* Conteúdo Editorial Principal */
  .content {{
    position: relative;
    z-index: 10;
    padding-left: 130px;
    max-width: 1050px;
  }}

  .kicker {{
    display: inline-flex;
    align-items: center;
    gap: 14px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #D96526;
    margin-bottom: 28px;
  }}

  .kicker::before {{
    content: '';
    display: inline-block;
    width: 28px;
    height: 1px;
    background: #D96526;
  }}

  .headline {{
    font-family: 'Newsreader', Georgia, serif;
    font-size: 68px;
    font-weight: 500;
    line-height: 1.14;
    color: #FFFFFF;
    letter-spacing: -1px;
    margin-bottom: 24px;
  }}

  .headline em {{
    font-style: italic;
    font-weight: 400;
    color: #E2E8F0;
    text-decoration: underline;
    text-decoration-color: rgba(217, 101, 38, 0.6);
    text-underline-offset: 8px;
    text-decoration-thickness: 2px;
  }}

  .description {{
    font-size: 20px;
    line-height: 1.6;
    color: #94A3B8;
    max-width: 760px;
    font-weight: 400;
    margin-bottom: 40px;
  }}

  .signature-bar {{
    display: flex;
    align-items: center;
    gap: 32px;
    padding-top: 24px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    max-width: 720px;
  }}

  .spec-item {{
    display: flex;
    flex-direction: column;
    gap: 4px;
  }}

  .spec-label {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #64748B;
  }}

  .spec-val {{
    font-size: 15px;
    font-weight: 500;
    color: #E2E8F0;
  }}

  .spec-divider {{
    width: 1px;
    height: 28px;
    background: rgba(255, 255, 255, 0.08);
  }}

  /* Detalhe de canto / marcação editorial */
  .edition-tag {{
    position: absolute;
    top: 48px;
    right: 64px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    letter-spacing: 2px;
    color: rgba(255, 255, 255, 0.28);
    text-transform: uppercase;
    z-index: 10;
  }}

  .safe-mark {{
    position: absolute;
    bottom: 36px;
    right: 64px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 1px;
    color: rgba(217, 101, 38, 0.5);
    z-index: 10;
  }}
</style>
</head>
<body>
  <div class="noise-overlay"></div>
  <div class="ambient-glow-1"></div>
  <div class="ambient-glow-2"></div>

  <!-- Linhas arquiteturais -->
  <div class="grid-lines">
    <div class="grid-line-h" style="top: 140px;"></div>
    <div class="grid-line-h" style="bottom: 120px;"></div>
    <div class="grid-line-v" style="left: 130px;"></div>
    <div class="grid-line-v" style="right: 580px;"></div>
  </div>

  <!-- Anéis e logo fusionados organicamente como background design -->
  <div class="bg-watermark-ring-outer"></div>
  <div class="bg-watermark-ring"></div>
  <img class="bg-watermark-logo" src="data:image/png;base64,{b64_logo}" alt="TM Background">

  <!-- Marcador de Edição Superior Direito -->
  <div class="edition-tag">TM Sempre Tecnologia &bull; 2026</div>

  <!-- Conteúdo Tipográfico Editorial -->
  <div class="content">
    <div class="kicker">Infraestrutura Digital &bull; Sistemas &bull; IA</div>
    
    <h1 class="headline">
      Sistemas Sob Medida &amp;<br>
      <em>Engenharia Digital de Alta Performance</em>
    </h1>

    <p class="description">
      Desenvolvimento de plataformas proprietárias, integrações inteligentes com inteligência artificial e ecossistemas digitais construídos para escala, solidez e autoridade corporativa.
    </p>

    <div class="signature-bar">
      <div class="spec-item">
        <span class="spec-label">Núcleo</span>
        <span class="spec-val">Software Sob Medida</span>
      </div>
      <div class="spec-divider"></div>
      <div class="spec-item">
        <span class="spec-label">Operação</span>
        <span class="spec-val">Automação &amp; IA Aplicada</span>
      </div>
      <div class="spec-divider"></div>
      <div class="spec-item">
        <span class="spec-label">Objetivo</span>
        <span class="spec-val">Escala &amp; Previsibilidade</span>
      </div>
    </div>
  </div>

  <div class="safe-mark">TM STUDIO ARCHITECTURE &bull; COV-1640x924</div>
</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Renderizando Banner v2...")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1640, "height": 924})
    file_url = "file:///" + html_path.replace(os.sep, "/")
    page.goto(file_url, wait_until="networkidle")
    page.wait_for_timeout(2500)
    page.screenshot(path=output_png)
    browser.close()

print("Banner v2 gerado com sucesso!")
