# -*- coding: utf-8 -*-
import re

NEW_PRICING_BLOCK = '''    <div class="w-row" style="margin-bottom: 50px;">
      <!-- Pacote 1: Entrada Digital -->
      <div class="w-col w-col-4">
        <div class="item">
          <div class="w-col w-col-12 w-col-stack">
            <div class="price-wrapper">
              <div class="top-price preco5">
                <h4 class="price-title">Entrada Digital</h4>
              </div>
              <div class="price-middle">
                <div class="price-square">
                  <p class="price"><span style="font-size:23px;">R$</span> 10.000<span style="font-size:23px;">,00</span></p>
                  <p class="from-text">Landing Page + 15 Dias de Tráfego</p>
                </div>
              </div>
              <div class="price-end">
                <p><img src="imagens/check.svg"> <strong>Landing Page Oficial</strong> de Alta Conversão</p>
                <p><img src="imagens/check.svg"> <strong>15 Dias de Acompanhamento</strong> de Tráfego</p>
                <p><img src="imagens/check.svg"> Gestão de Anúncios <strong>Meta Ads</strong> (Insta/Face)</p>
                <p><img src="imagens/check.svg"> Criação de Criativos de Conversão (Feed/Stories)</p>
                <p><img src="imagens/check.svg"> Calibração do <strong>Pixel Meta</strong> & Tags</p>
                <p><img src="imagens/check.svg"> Identidade Visual Digital Básica</p>
                <p class="center" style="margin-top:20px;"><img src="imagens/boleto1.png"></p>
                <div style="font-size: 12px; line-height: 16px !important; margin-top:16px;">Ao contratar você está concordando com os <a href="termos.html">Termos de Serviços</a>.</div>
                <div class="top-margin2">
                  <a target="_blank" href="https://api.whatsapp.com/send?phone=5562996046458&text=Ol%C3%A1!%20Gostaria%20de%20contratar%20o%20Pacote%20Entrada%20Digital%20(R$%2010.000)." class="button w-button" style="width:100%;">Contratar Entrada</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Pacote 2: Ecossistema Máster (Destaque) -->
      <div class="w-col w-col-4">
        <div class="item">
          <div class="w-col w-col-12 w-col-stack">
            <div class="price-wrapper" style="border: 2px solid #FFBE00; transform: scale(1.03); box-shadow: 0 16px 32px rgba(0, 61, 150, 0.15);">
              <div class="top-price preco2" style="position:relative;">
                <span style="position:absolute; top:-12px; right:15px; background:#FFBE00; color:#102234; font-size:10px; font-weight:900; padding:3px 12px; border-radius:12px; text-transform:uppercase; box-shadow: 0 2px 6px rgba(0,0,0,0.15);">Mais Escolhido</span>
                <h4 class="price-title">Ecossistema Máster</h4>
              </div>
              <div class="price-middle" style="background:#f8fbff;">
                <div class="price-square">
                  <p class="price" style="color:#003d96;"><span style="font-size:23px;">R$</span> 14.000<span style="font-size:23px;">,00</span></p>
                  <p class="from-text" style="color:#003d96; font-weight:700;">Completo com WhatsApp & Automação</p>
                </div>
              </div>
              <div class="price-end">
                <p><img src="imagens/check.svg"> <strong>TUDO do Pacote Entrada Digital</strong></p>
                <p><img src="imagens/check.svg"> <strong>Automação de WhatsApp</strong> (Estilo LideraAI)</p>
                <p><img src="imagens/check.svg"> Gestão de <strong>Grupos & Canais VIP</strong></p>
                <p><img src="imagens/check.svg"> <strong>Redirecionador Dinâmico</strong> de Grupos</p>
                <p><img src="imagens/check.svg"> <strong>E-mail Marketing Próprio</strong> (SPF/DKIM)</p>
                <p><img src="imagens/check.svg"> Segmentação de Lideranças por Bairro</p>
                <p><img src="imagens/check.svg"> Disparo Estratégico Dia D</p>
                <p><img src="imagens/check.svg"> Relatórios Executivos & Suporte VIP</p>
                <p class="center" style="margin-top:20px;"><img src="imagens/boleto1.png"></p>
                <div style="font-size: 12px; line-height: 16px !important; margin-top:16px;">Ao contratar você está concordando com os <a href="termos.html">Termos de Serviços</a>.</div>
                <div class="top-margin2">
                  <a target="_blank" href="https://api.whatsapp.com/send?phone=5562996046458&text=Ol%C3%A1!%20Quero%20contratar%20o%20Ecossistema%20M%C3%A1ster%20de%20Campanha%20(R$%2014.000)." class="button btn-yellow w-button" style="width:100%; font-weight:700;">Contratar Ecossistema</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Pacote 3: Add-on Google Ads + SEO -->
      <div class="w-col w-col-4">
        <div class="item">
          <div class="w-col w-col-12 w-col-stack">
            <div class="price-wrapper">
              <div class="top-price preco3">
                <h4 class="price-title">Add-on Especialista</h4>
              </div>
              <div class="price-middle">
                <div class="price-square">
                  <p class="price"><span style="font-size:20px;">+ R$</span> 3.800<span style="font-size:20px;">,00</span></p>
                  <p class="from-text">Google Ads + SEO Ranking</p>
                </div>
              </div>
              <div class="price-end">
                <p><img src="imagens/check.svg"> Anúncios na <strong>Rede de Pesquisa Google</strong></p>
                <p><img src="imagens/check.svg"> Anúncios em Vídeo no <strong>YouTube Ads</strong></p>
                <p><img src="imagens/check.svg"> <strong>Blindagem do Nome</strong> no Google</p>
                <p><img src="imagens/check.svg"> <strong>SEO Político</strong> (1ª Página das Buscas)</p>
                <p><img src="imagens/check.svg"> Palavras-Chave de Intenção Eleitoral</p>
                <p><img src="imagens/check.svg"> Otimização Google Tag Manager</p>
                <p style="font-size:12px; color:#64748b; margin-top:14px; line-height:18px;">* Pode ser contratado junto à Entrada ou ao Ecossistema Máster.</p>
                <p class="center" style="margin-top:15px;"><img src="imagens/boleto1.png"></p>
                <div style="font-size: 12px; line-height: 16px !important; margin-top:16px;">Ao contratar você está concordando com os <a href="termos.html">Termos de Serviços</a>.</div>
                <div class="top-margin2">
                  <a target="_blank" href="https://api.whatsapp.com/send?phone=5562996046458&text=Ol%C3%A1!%20Gostaria%20de%20adicionar%20o%20m%C3%B3dulo%20Google%20Ads%20e%20SEO%20(+R$%203.800)." class="button w-button" style="width:100%;">Adicionar Google Ads</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>'''

files_to_update = [
    'c:/Users/mikaa/Documents/antigravity/tm-site-lancamento/upolitico-clone/index.html',
    'c:/Users/mikaa/Documents/antigravity/tm-site-lancamento/upolitico-clone/precos.html'
]

pattern = re.compile(r'<div class="w-row" style="margin-bottom: 50px;">.*?<!-- Pacote 1: Entrada Digital -->.*?<!-- Pacote 3: Add-on Google Ads \+ SEO -->.*?</div>\s*</div>\s*</div>\s*</div>\s*</div>', re.DOTALL)

for fpath in files_to_update:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = pattern.search(content)
    if match:
        new_content = content[:match.start()] + NEW_PRICING_BLOCK + content[match.end():]
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully updated {fpath}")
    else:
        print(f"Pattern not found in {fpath}, checking manual replace")
