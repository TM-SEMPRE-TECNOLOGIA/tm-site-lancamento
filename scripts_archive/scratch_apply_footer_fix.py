import re

# 1. Update css/estilo.css with global footer styles
css_path = r'c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\upolitico-clone\css\estilo.css'
with open(css_path, 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

footer_fix_css = """
/* =========================================================
   GLOBAL FOOTER FIX (FLEXIBLE HEIGHT, CRISP LOGO, GOLD ACCENTS)
   ========================================================= */
.footer, .footer.style-2 {
  position: relative !important;
  height: auto !important;
  min-height: auto !important;
  padding-top: 55px !important;
  padding-bottom: 50px !important;
  display: block !important;
  background-color: #ffffff !important;
  border-top: 2px solid #e9eff6 !important;
  overflow: visible !important;
}

.footer-column {
  margin-right: 20px !important;
}

.footer-column a.link-block {
  display: inline-block !important;
  margin-bottom: 16px !important;
  padding: 0 !important;
  overflow: visible !important;
}

.footer-column a.link-block img {
  max-height: 48px !important;
  width: auto !important;
  display: block !important;
  object-fit: contain !important;
}

.footer-title {
  height: auto !important;
  margin-bottom: 14px !important;
  display: block !important;
}

.footer-sub-title {
  color: #102234 !important;
  font-size: 16px !important;
  font-weight: 700 !important;
  line-height: 1.3 !important;
  letter-spacing: -0.2px !important;
  border-bottom: 2px solid #FFBE00 !important;
  display: inline-block !important;
  padding-bottom: 4px !important;
  margin: 0 !important;
}

.footer-block {
  display: block !important;
  margin-bottom: 8px !important;
  color: #475569 !important;
  font-size: 14px !important;
  font-weight: 500 !important;
  text-decoration: none !important;
  transition: color 0.2s ease, transform 0.2s ease !important;
}

.footer-block:hover {
  color: #FFBE00 !important;
  transform: translateX(3px) !important;
  text-decoration: none !important;
}

.algin-center.copyrights {
  background-color: #0c1420 !important;
  color: #94a3b8 !important;
  padding: 20px 0 !important;
  border-top: 1px solid rgba(255, 255, 255, 0.08) !important;
}

.algin-center.copyrights p.copyright {
  color: #94a3b8 !important;
  font-size: 13.5px !important;
  margin: 0 !important;
}
"""

if 'GLOBAL FOOTER FIX' not in css:
    css = css + '\n' + footer_fix_css
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print("Appended footer fix to estilo.css!")
else:
    print("Footer fix already in estilo.css")

# 2. Update index.html footer markup and CTA button
html_path = r'c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\upolitico-clone\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add to <style> block in index.html for immediate precedence
if '/* =========================================================\n   GLOBAL FOOTER FIX' not in html:
    html = html.replace('</style>', footer_fix_css + '\n</style>', 1)
    print("Injected footer fix into index.html <style>!")

# Fix the CTA button above footer: change to btn-yellow
old_cta = '<div class="top-margin"><a href="orcamento.html" class="button w-button">Or'
new_cta = '<div class="top-margin"><a href="orcamento.html" class="button btn-yellow w-button">Or'
if old_cta in html:
    html = html.replace(old_cta, new_cta)
    print("Updated footer CTA button to btn-yellow!")

# Fix the logo tag in footer to ensure no clipping
old_footer_logo = '<a href="index.html" class="link-block w-inline-block"><img style="width:150px" src="imagens/candidato-pro-logo.png" style="max-height:48px;width:auto;"></a>'
new_footer_logo = '<a href="index.html" class="link-block w-inline-block" style="display:block; margin-bottom:18px;"><img src="imagens/candidato-pro-logo.png" alt="Candidato PRO" style="max-height:48px; width:auto; display:block;"></a>'
if old_footer_logo in html:
    html = html.replace(old_footer_logo, new_footer_logo)
    print("Fixed footer logo markup!")

# Balance the columns in footer:
# Col 1: w-col-4
# Col 2: w-col-3 (Soluções & Campanhas)
# Col 3: w-col-2 (Serviços & Apoio)
# Col 4: w-col-3 (Institucional & Pagamentos)

old_cols = """          <div class="w-col w-col-2 w-col-stack">
            <div class="footer-title">
              <h5 class="footer-sub-title">Acessos</h5>
            </div>
            <div class="top-margin">
              <a href="../" class="footer-block w-inline-block"><div>Incio</div></a>
              <a href="comofunciona.html" class="footer-block w-inline-block"><div>Como Funciona</div> </a>
              <a href="campanhas.html" class="footer-block w-inline-block"><div>Campanhas</div> </a>
              <a href="trafego-pago.html" class="footer-block w-inline-block"><div>Trfego Pago</div> </a>
<a href="modelos-landing-page.html" class="footer-block w-inline-block"><div>Modelos de Sites</div> </a>
<a href="automacao-whatsapp.html" class="footer-block w-inline-block"><div>Automao WhatsApp</div> </a>
<a href="precos.html" class="footer-block w-inline-block"><div>Preos & Kits</div> </a>
              <a href="servicos.html" class="footer-block w-inline-block"><div>Servios</div> </a>
              <a href="duvidas.html" class="footer-block w-inline-block"><div>Dvidas</div> </a>
              
              </div>
          </div>
          <div class="w-col w-col-2 w-col-stack">
            <div>
              <div class="footer-title">
                <h5 class="footer-sub-title">Informaes</h5>
              </div>
              <div class="top-margin">
              <a href="quemsomos.html" class="footer-block w-inline-block"><div>Quem Somos</div> </a>
              <a href="termos.html" class="footer-block w-inline-block"><div>Termos e Condies</div> </a>
              <a href="privacidade.html" class="footer-block w-inline-block"><div>Poltica de Privacidade</div> </a>
              <a href="contato.html" class="footer-block w-inline-block"><div>Contato</div> </a>
              </div>
            </div>
          </div>
          <div class="w-col w-col-4 w-col-stack">"""

new_cols = """          <div class="w-col w-col-3 w-col-stack">
            <div class="footer-title">
              <h5 class="footer-sub-title">Campanhas & Soluções</h5>
            </div>
            <div class="top-margin">
              <a href="index.html" class="footer-block w-inline-block"><div>Início</div></a>
              <a href="comofunciona.html" class="footer-block w-inline-block"><div>Como Funciona</div></a>
              <a href="campanhas.html" class="footer-block w-inline-block"><div>Campanhas Realizadas</div></a>
              <a href="trafego-pago.html" class="footer-block w-inline-block"><div>Tráfego Pago & Meta Ads</div></a>
              <a href="modelos-landing-page.html" class="footer-block w-inline-block"><div>Modelos de Sites</div></a>
              <a href="automacao-whatsapp.html" class="footer-block w-inline-block"><div>Automação WhatsApp</div></a>
            </div>
          </div>
          <div class="w-col w-col-2 w-col-stack">
            <div>
              <div class="footer-title">
                <h5 class="footer-sub-title">Planos & Apoio</h5>
              </div>
              <div class="top-margin">
                <a href="precos.html" class="footer-block w-inline-block"><div>Preços & Kits</div></a>
                <a href="servicos.html" class="footer-block w-inline-block"><div>Todos os Serviços</div></a>
                <a href="duvidas.html" class="footer-block w-inline-block"><div>Dúvidas Frequentes</div></a>
                <a href="orcamento.html" class="footer-block w-inline-block"><div>Orçamento Online</div></a>
                <a href="contato.html" class="footer-block w-inline-block"><div>Fale Conosco</div></a>
              </div>
            </div>
          </div>
          <div class="w-col w-col-3 w-col-stack">
            <div>
              <div class="footer-title">
                <h5 class="footer-sub-title">Institucional & Segurança</h5>
              </div>
              <div class="top-margin">
                <a href="quemsomos.html" class="footer-block w-inline-block"><div>Quem Somos</div></a>
                <a href="termos.html" class="footer-block w-inline-block"><div>Termos e Condições</div></a>
                <a href="privacidade.html" class="footer-block w-inline-block"><div>Política de Privacidade</div></a>
              </div>
              <div class="top-margin" style="margin-top:16px;">
                <img src="imagens/boleto_.png" style="max-width:100%; height:auto;" alt="Formas de Pagamento">
              </div>
            </div>
          </div>"""

# Check and replace columns
if old_cols in html:
    # Also need to handle the following div
    html = html.replace(old_cols, new_cols)
    # And clean up the old 4th col
    html = re.sub(
        r'<div class="w-col w-col-4 w-col-stack">\s*<div>\s*<div class="footer-title">\s*<h5 class="footer-sub-title">Pagamentos</h5>\s*</div>\s*<img src="imagens/boleto_\.png"><br><br><img src="imagens/blindado\.png">\s*</div>\s*</div>',
        '',
        html
    )
    print("Balanced footer columns cleanly!")

# Update the copyright line
html = re.sub(
    r'<p class="paragraph-small copyright">Copyright.*?</p>',
    '<p class="paragraph-small copyright">Copyright © 2026 | Candidato PRO - Marketing Político Digital & Kit Eleitoral - Todos os direitos reservados.</p>',
    html
)
print("Updated copyright text!")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved updated index.html with perfect footer successfully!")
