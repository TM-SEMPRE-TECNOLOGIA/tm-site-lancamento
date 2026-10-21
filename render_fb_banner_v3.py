import os
from playwright.sync_api import sync_playwright

html_path = r"C:\Users\mikaa\Documents\antigravity\tm-site-lancamento\banner_facebook_tm_v3.html"
output_png = r"C:\Users\mikaa\Documents\antigravity\tm-site-lancamento\banner_facebook_tm_v3.png"

# Canvas oficial Facebook: 1640 x 924 (proporção 16:9 ideal)
# Safe zone mobile: faixa central horizontal de 640px e topo seguro livre de avatar.
html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,500;1,6..72,500&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  
  body {
    width: 1640px;
    height: 924px;
    background: #080B11;
    overflow: hidden;
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #F8FAFC;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  /* Ruído analógico sutil de estúdio */
  .noise-layer {
    position: absolute;
    inset: 0;
    opacity: 0.03;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
    pointer-events: none;
    z-index: 5;
  }

  /* Gradiente e Glows Arquitetônicos */
  .glow-center {
    position: absolute;
    width: 900px;
    height: 500px;
    left: 50%;
    top: 55%;
    transform: translate(-50%, -50%);
    background: radial-gradient(ellipse, rgba(217, 101, 38, 0.18) 0%, rgba(217, 101, 38, 0.04) 50%, transparent 75%);
    filter: blur(50px);
    z-index: 1;
  }

  .glow-blue-subtle {
    position: absolute;
    width: 1200px;
    height: 350px;
    left: 50%;
    bottom: -100px;
    transform: translateX(-50%);
    background: radial-gradient(ellipse, rgba(14, 165, 233, 0.08) 0%, transparent 70%);
    filter: blur(70px);
    z-index: 1;
  }

  /* Linhas e Grids Milimétricos (Engenharia de Software) */
  .grid-bg {
    position: absolute;
    inset: 0;
    background-image: 
      linear-gradient(to right, rgba(255,255,255,0.025) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255,255,255,0.025) 1px, transparent 1px);
    background-size: 70px 70px;
    background-position: center center;
    z-index: 2;
  }

  /* Feixe de Luz Superior Laranja TM */
  .top-edge-beam {
    position: absolute;
    top: 0;
    left: 15%;
    right: 15%;
    height: 2px;
    background: linear-gradient(90deg, transparent, rgba(217, 101, 38, 0.8), transparent);
    box-shadow: 0 0 20px rgba(217, 101, 38, 0.6);
    z-index: 10;
  }

  /* Anéis Concéntricos de Alinhamento - Atrás do Avatar */
  .orbit-ring {
    position: absolute;
    left: 50%;
    bottom: 80px;
    transform: translateX(-50%);
    border-radius: 50%;
    pointer-events: none;
    z-index: 2;
  }
  .orbit-1 {
    width: 580px;
    height: 580px;
    border: 1px dashed rgba(217, 101, 38, 0.2);
  }
  .orbit-2 {
    width: 760px;
    height: 760px;
    border: 1px solid rgba(255, 255, 255, 0.035);
  }
  .orbit-3 {
    width: 980px;
    height: 980px;
    border: 1px dashed rgba(255, 255, 255, 0.02);
  }

  /* FAiXA SUPERIOR SEGURA (Visível perfeitamente no Mobile e Desktop) */
  .top-safe-bar {
    position: relative;
    z-index: 10;
    width: 100%;
    padding: 70px 100px 0 100px;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
  }

  .brand-mono-kicker {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    letter-spacing: 3.5px;
    text-transform: uppercase;
    color: #D96526;
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .brand-mono-kicker::before {
    content: '';
    display: inline-block;
    width: 7px;
    height: 7px;
    background: #D96526;
    border-radius: 50%;
    box-shadow: 0 0 10px #D96526;
  }

  .meta-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 2px;
    color: rgba(255, 255, 255, 0.35);
    text-transform: uppercase;
  }

  /* CENTRO TOP: Statement de Autoridade (Fica ACIMA do avatar no Mobile!) */
  .statement-wrapper {
    position: relative;
    z-index: 10;
    text-align: center;
    padding: 0 80px;
    margin-top: 40px;
  }

  .statement-h1 {
    font-family: 'Newsreader', Georgia, serif;
    font-size: 58px;
    font-weight: 500;
    line-height: 1.18;
    color: #FFFFFF;
    letter-spacing: -0.5px;
  }
  .statement-h1 em {
    font-style: italic;
    color: #F97316;
  }

  .statement-sub {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: #94A3B8;
    margin-top: 14px;
  }

  /* LATERAL ESQUERDA & DIREITA (Visíveis no Desktop, fora do corte Mobile) */
  .desktop-wing-left {
    position: absolute;
    left: 90px;
    bottom: 90px;
    z-index: 10;
    display: flex;
    flex-direction: column;
    gap: 6px;
  }
  .desktop-wing-right {
    position: absolute;
    right: 90px;
    bottom: 90px;
    z-index: 10;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 6px;
  }

  .wing-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 2px;
    color: #64748B;
    text-transform: uppercase;
  }
  .wing-val {
    font-size: 14px;
    font-weight: 600;
    color: #CBD5E1;
  }

  /* Centro inferior preservado para o avatar do Facebook */
  .avatar-clearance {
    position: relative;
    z-index: 10;
    width: 100%;
    height: 140px;
  }
</style>
</head>
<body>
  <div class="top-edge-beam"></div>
  <div class="noise-layer"></div>
  <div class="grid-bg"></div>
  <div class="glow-center"></div>
  <div class="glow-blue-subtle"></div>

  <!-- Anéis de Alinhamento Radial que moldam o Avatar central -->
  <div class="orbit-ring orbit-1"></div>
  <div class="orbit-ring orbit-2"></div>
  <div class="orbit-ring orbit-3"></div>

  <!-- Barra Superior Segura -->
  <div class="top-safe-bar">
    <div class="brand-mono-kicker">TM SEMPRE TECNOLOGIA</div>
    <div class="meta-tag">ESTRUTURA DIGITAL &bull; 2026</div>
  </div>

  <!-- Statement Centralizado de Alto Nível (Acima do Avatar) -->
  <div class="statement-wrapper">
    <h1 class="statement-h1">
      Engenharia Digital &amp; <em>Sistemas Sob Medida</em>
    </h1>
    <p class="statement-sub">
      Software Proprietário &bull; Automações com IA &bull; Alta Performance
    </p>
  </div>

  <!-- Detalhes Arquiteturais para Desktop nas extremidades -->
  <div class="desktop-wing-left">
    <span class="wing-label">// NÚCLEO</span>
    <span class="wing-val">Arquitetura de Escala</span>
  </div>

  <div class="desktop-wing-right">
    <span class="wing-label">// STATUS</span>
    <span class="wing-val" style="color: #4ADE80;">&bull; Operação Ativa</span>
  </div>

  <!-- Espaço inferior onde o avatar redondo pousa organicamente -->
  <div class="avatar-clearance"></div>
</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Renderizando Banner v3 Mobile-First...")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1640, "height": 924})
    file_url = "file:///" + html_path.replace(os.sep, "/")
    page.goto(file_url, wait_until="networkidle")
    page.wait_for_timeout(2500)
    page.screenshot(path=output_png)
    browser.close()

print("Banner v3 gerado com sucesso!")
