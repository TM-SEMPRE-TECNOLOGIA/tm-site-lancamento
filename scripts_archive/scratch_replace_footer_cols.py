import re

html_path = r'c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\upolitico-clone\index.html'
with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Find the footer inner w-row
# It starts right after <div class="w-col w-col-4 w-col-stack"> (which is the logo column)
pos_logo_end = html.find('</div>\n          </div>\n          <div class="w-col w-col-2 w-col-stack">')
if pos_logo_end == -1:
    pos_logo_end = html.find('</div>          </div>          <div class="w-col w-col-2 w-col-stack">')
if pos_logo_end == -1:
    # let's search via regex
    m = re.search(r'</div>\s*</div>\s*<div class="w-col w-col-2 w-col-stack">', html)
    if m:
        pos_logo_end = m.start()

pos_row_end = html.find('</div>\n        \n      </div>\n    </div>\n  </div>')
if pos_row_end == -1:
    pos_row_end = html.find('</div>        </div>      </div>    </div>  </div>')
if pos_row_end == -1:
    m = re.search(r'</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*<div class="algin-center copyrights">', html)
    if m:
        pos_row_end = m.start()

print("pos_logo_end:", pos_logo_end)
print("pos_row_end:", pos_row_end)

if pos_logo_end != -1 and pos_row_end != -1:
    # The snippet to replace is between pos_logo_end + len('</div>\n          </div>\n') and pos_row_end
    # Let's inspect the exact substring
    old_sub = html[pos_logo_end:pos_row_end]
    print("Old substring length:", len(old_sub))
    
    new_sub = """</div>
          </div>
          <div class="w-col w-col-3 w-col-stack">
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
          </div>
        </div>"""
    
    html = html[:pos_logo_end] + new_sub + html[pos_row_end:]
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully replaced footer columns!")
