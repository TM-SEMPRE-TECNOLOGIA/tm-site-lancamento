html_path = r'c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\upolitico-clone\index.html'
with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Position right before the first redundant footer at 53453
# Find the exact snippet:
split_str = '<div class="footer style-2">'
split_idx = text.find(split_str)
print("Cutting everything from first footer at:", split_idx)

clean_base = text[:split_idx].rstrip()

new_ending = """
<div class="section image">
  <div class="container w-container">
    <div class="algin-center">
      <h1 style="line-height: 38px; font-size: 31px;" class="banner-title">Solicite um orçamento <strong>sem compromisso.</strong> Trabalhamos dentro de prazos definidos, sem complicações e surpresas desagradáveis.</h1>
      <div class="top-margin"><a href="orcamento.html" class="button btn-yellow w-button">Orçamento Online</a></div>
    </div>
  </div>
  <div class="top-margin medium w-hidden-medium w-hidden-small w-hidden-tiny"></div>
</div>

<div class="footer style-2">
  <div class="container w-container">
    <div>
      <div class="w-row">
        <div class="w-col w-col-4 w-col-stack">
          <div class="footer-column">
            <a href="index.html" class="link-block w-inline-block" style="display:block; margin-bottom:18px;">
              <img src="imagens/candidato-pro-logo.png" alt="Candidato PRO" style="max-height:48px; width:auto; display:block;">
            </a>
            <div class="top-margin">
              <div style="color:#475569; font-size:14px; line-height:22px; margin-bottom:16px;">
                Atendimento por telefone das <strong>09:00 às 18:00 para serviços personalizados</strong>.<br /><br />
                Se desejar um orçamento personalizado para sua campanha, entre em contato com nossa equipe.
              </div>
              <div class="top-margin small">
                <div style="display:flex; gap:12px; align-items:center;">
                  <a href="https://api.whatsapp.com/send?phone=5562996046458&text=Ol%C3%A1!%20Gostaria%20de%20um%20or%C3%A7amento%20para%20o%20Candidato%20PRO." target="_blank" class="social-icon w-inline-block"><img src="https://www.ulogo.com.br/imagens/whatsappt2.png" width="30" height="30" alt="WhatsApp"/></a>
                  <a href="https://www.instagram.com/upolitico.com.br/" target="_blank" class="social-icon w-inline-block"><img src="imagens/instagram.svg" width="28" height="28" alt="Instagram"/></a>
                </div>
              </div>
            </div>
          </div>
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
      </div>
    </div>
  </div>
</div>

<div class="algin-center copyrights">
  <div class="container w-container">
    <p class="paragraph-small copyright">Copyright © 2026 | Candidato PRO - Marketing Político Digital & Kit Eleitoral - Todos os direitos reservados.</p>
  </div>
</div>

<script src="js/script.js" type="text/javascript"></script>
<!--[if lte IE 9]><script src="//cdnjs.cloudflare.com/ajax/libs/placeholders/3.0.2/placeholders.min.js"></script><![endif]-->
<script src="js/easyWizard.js"></script>
<script> $(document).on("ready", function(){  $("#Wizard").wizard({    onfinish:function(){  }});}); </script>

</body>
</html>
"""

final_html = clean_base + '\n\n' + new_ending

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Saved clean index.html with exactly 1 CTA, 1 Footer, and 1 Copyright bar!")
