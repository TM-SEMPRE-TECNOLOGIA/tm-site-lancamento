import os
import re

site_dir = r"c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\site-deputado-template"

html_files = [f for f in os.listdir(site_dir) if f.endswith('.html')]

print(f"Encontrados {len(html_files)} arquivos HTML para auditar e atualizar.")

new_footer_copy = """<div class="footer-legal-copy">
            <strong style="display:block; margin-bottom: 6px; color: #f8fafc; font-size: 0.92rem; text-transform: uppercase;">
              Propaganda eleitoral. ELEIÇÃO 2026 ADIR CARDOSO GENTIL DEPUTADO FEDERAL — CNPJ 68.492.004/0001-78
            </strong>
            <span style="display:block; font-size: 0.82rem; color: #94a3b8; line-height: 1.6;">
              Quadra ARSO 111, Alameda 19 — Palmas/TO. © 2026 Adir Gentil 2211. Todos os direitos reservados.<br/>
              Telefone: <a href="tel:+554899740613" style="color: #ffcb05; text-decoration: none; font-weight: bold;">48 9974-0613</a> • 
              e-mail: <a href="mailto:contato@adirgentil2211.com.br" style="color: #ffcb05; text-decoration: none;">contato@adirgentil2211.com.br</a> • 
              <a href="https://divulgacandcontas.tse.jus.br/divulga/#/candidato/NORTE/TO/20322002026" target="_blank" rel="noopener noreferrer" style="color: #ffcb05; text-decoration: underline;">Prestação de Contas DivulgaCandContas (TSE)</a>
            </span>
          </div>"""

for fname in html_files:
    fpath = os.path.join(site_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Substituir numero de whatsapp em links e textos
    content = content.replace("phone=5562996046458", "phone=554899740613")
    content = content.replace("5562996046458", "554899740613")
    content = content.replace("(62) 99604-6458", "48 9974-0613")
    content = content.replace("(62)&nbsp;99604-6458", "48 9974-0613")
    content = content.replace("62 99604-6458", "48 9974-0613")

    # 2. Atualizar secao de contatos institucionais
    content = content.replace("suporte@sempretecnologia.com.br", "contato@adirgentil2211.com.br")
    content = content.replace("imprensa@adirgentil2211.com.br", "contato@adirgentil2211.com.br")

    # 3. Atualizar footer-legal-copy
    content = re.sub(
        r'<div class="footer-legal-copy">[\s\S]*?</div>',
        new_footer_copy,
        content,
        flags=re.IGNORECASE
    )

    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Atualizado: {fname}")
    else:
        print(f"[SEM ALTERACOES]: {fname}")

print("Concluida a atualizacao em todos os arquivos HTML.")
