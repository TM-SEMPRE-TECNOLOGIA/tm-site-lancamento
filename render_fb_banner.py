import os
import base64
from playwright.sync_api import sync_playwright

html_path = r"C:\Users\mikaa\Documents\antigravity\tm-site-lancamento\banner_facebook_tm.html"
output_png = r"C:\Users\mikaa\Documents\antigravity\tm-site-lancamento\banner_facebook_tm.png"
logo_file = r"C:\Users\mikaa\Documents\antigravity\tm-site-lancamento\logo_banner.png"

with open(logo_file, "rb") as f:
    b64_logo = base64.b64encode(f.read()).decode("utf-8")

html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700;800&family=Newsreader:ital,opsz,wght@0,6..72,500;0,6..72,700;1,6..72,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    width: 1640px;
    height: 924px;
    background: #060B14;
    overflow: hidden;
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
    color: #F8FAFC;
    position: relative;
  }}
  
  /* Cyber Grid & Ambient Lighting */
  .grid-bg {{
    position: absolute;
    inset: 0;
    background-image: 
      linear-gradient(to right, rgba(255,255,255,0.035) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255,255,255,0.035) 1px, transparent 1px);
    background-size: 55px 55px;
  }}
  
  .glow-orange {{
    position: absolute;
    width: 800px;
    height: 800px;
    right: -100px;
    top: -150px;
    background: radial-gradient(circle, rgba(217, 101, 38, 0.32) 0%, rgba(217, 101, 38, 0.08) 50%, transparent 70%);
    filter: blur(60px);
  }}

  .glow-blue {{
    position: absolute;
    width: 700px;
    height: 700px;
    left: 100px;
    bottom: -180px;
    background: radial-gradient(circle, rgba(30, 58, 138, 0.35) 0%, rgba(14, 165, 233, 0.08) 50%, transparent 70%);
    filter: blur(70px);
  }}

  /* Top Accent Border Line */
  .top-accent-line {{
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #D96526 0%, #F97316 40%, #0A192F 100%);
    z-index: 20;
  }}

  /* Layout Container */
  .container {{
    position: relative;
    z-index: 10;
    width: 100%;
    height: 100%;
    padding: 80px 100px 80px 100px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}

  .left-col {{
    max-width: 960px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }}

  .kicker {{
    display: inline-flex;
    align-items: center;
    gap: 12px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 2px;
    color: #F97316;
    text-transform: uppercase;
    background: rgba(217, 101, 38, 0.12);
    border: 1px solid rgba(217, 101, 38, 0.35);
    padding: 8px 18px;
    border-radius: 4px;
    width: fit-content;
    margin-bottom: 26px;
  }}
  .kicker .dot {{
    width: 8px;
    height: 8px;
    background: #F97316;
    border-radius: 50%;
    box-shadow: 0 0 10px #F97316;
  }}

  .main-title {{
    font-family: 'Newsreader', Georgia, serif;
    font-size: 66px;
    font-weight: 600;
    line-height: 1.12;
    color: #FFFFFF;
    margin-bottom: 24px;
    letter-spacing: -0.5px;
  }}
  .main-title span {{
    font-style: italic;
    color: #F97316;
  }}

  .subtitle {{
    font-size: 21px;
    line-height: 1.5;
    color: #94A3B8;
    max-width: 840px;
    font-weight: 400;
    margin-bottom: 44px;
  }}

  .pill-row {{
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
  }}

  .pill {{
    background: rgba(15, 23, 42, 0.75);
    border: 1px solid rgba(255, 255, 255, 0.12);
    padding: 13px 22px;
    border-radius: 6px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    color: #F1F5F9;
    display: flex;
    align-items: center;
    gap: 10px;
    backdrop-filter: blur(12px);
  }}
  .pill svg {{
    width: 17px;
    height: 17px;
    fill: #F97316;
  }}

  /* Right Column (Hero Brand Card) */
  .right-col {{
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
  }}

  .brand-card {{
    background: linear-gradient(145deg, rgba(15, 23, 42, 0.9) 0%, rgba(8, 14, 26, 0.98) 100%);
    border: 1px solid rgba(217, 101, 38, 0.4);
    border-radius: 20px;
    padding: 44px 48px;
    display: flex;
    flex-direction: column;
    align-items: center;
    box-shadow: 0 30px 70px -15px rgba(0, 0, 0, 0.85), 0 0 50px rgba(217, 101, 38, 0.15);
    position: relative;
    backdrop-filter: blur(18px);
  }}

  .brand-card::before {{
    content: '';
    position: absolute;
    top: 0; left: 15%; right: 15%;
    height: 2px;
    background: linear-gradient(90deg, transparent, #F97316, transparent);
  }}

  .logo-img {{
    width: 220px;
    height: 220px;
    object-fit: contain;
    filter: drop-shadow(0 15px 30px rgba(0,0,0,0.6));
    margin-bottom: 22px;
  }}

  .brand-name {{
    font-family: 'Newsreader', Georgia, serif;
    font-size: 27px;
    font-weight: 700;
    color: #FFFFFF;
    letter-spacing: 0.5px;
    text-align: center;
  }}

  .brand-tag {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #F97316;
    margin-top: 8px;
    font-weight: 700;
  }}

  .metric-badge {{
    margin-top: 24px;
    display: flex;
    align-items: center;
    gap: 9px;
    padding: 7px 16px;
    background: rgba(34, 197, 94, 0.12);
    border: 1px solid rgba(34, 197, 94, 0.35);
    border-radius: 20px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: #4ADE80;
    letter-spacing: 1px;
  }}
  .metric-badge .dot-green {{
    width: 7px;
    height: 7px;
    background: #4ADE80;
    border-radius: 50%;
    box-shadow: 0 0 10px #4ADE80;
  }}

  .safe-code {{
    position: absolute;
    bottom: 24px;
    right: 40px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: rgba(255,255,255,0.25);
    letter-spacing: 1.5px;
  }}
</style>
</head>
<body>
  <div class="top-accent-line"></div>
  <div class="grid-bg"></div>
  <div class="glow-orange"></div>
  <div class="glow-blue"></div>

  <div class="container">
    <div class="left-col">
      <div class="kicker">
        <span class="dot"></span>
        <span>TM SEMPRE TECNOLOGIA // INFRAESTRUTURA DIGITAL</span>
      </div>
      <h1 class="main-title">
        Sistemas Sob Medida &amp;<br>
        <span>Engenharia Digital de Alta Performance</span>
      </h1>
      <p class="subtitle">
        Automações inteligentes com IA, softwares proprietários e arquiteturas de alta conversão para empresas que buscam escala e autoridade máxima.
      </p>

      <div class="pill-row">
        <div class="pill">
          <svg viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
          Sistemas &amp; Web Apps
        </div>
        <div class="pill">
          <svg viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
          Automações com IA
        </div>
        <div class="pill">
          <svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm1 15h-2v-6h2zm0-8h-2V7h2z"/></svg>
          Sites &amp; Landing Pages
        </div>
        <div class="pill">
          <svg viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4z"/></svg>
          Escala &amp; Performance
        </div>
      </div>
    </div>

    <div class="right-col">
      <div class="brand-card">
        <img class="logo-img" src="data:image/png;base64,{b64_logo}" alt="TM Logo">
        <div class="brand-name">TM Sempre Tecnologia</div>
        <div class="brand-tag">Sistemas &bull; IA &bull; Engenharia</div>
        <div class="metric-badge">
          <span class="dot-green"></span>
          <span>ESTRUTURA OPERACIONAL ATIVA</span>
        </div>
      </div>
    </div>
  </div>

  <div class="safe-code">// TM-FB-COVER &bull; 1640x924 &bull; EXECUTIVO</div>
</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML salvo com sucesso. Renderizando via Playwright...")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1640, "height": 924})
    file_url = "file:///" + html_path.replace(os.sep, "/")
    page.goto(file_url, wait_until="networkidle")
    page.wait_for_timeout(2500)
    page.screenshot(path=output_png)
    browser.close()

print("Banner gerado com sucesso em:", output_png)
