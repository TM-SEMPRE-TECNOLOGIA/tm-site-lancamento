import re

html_path = r'c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\upolitico-clone\index.html'
with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Let's find the end of the FAQ accordion
# The last question in FAQ is:
last_q = 'Voc poder contratar nosso servio e efetuar seu pagamento atravs de Boleto'
idx_last_q = text.find('Mercado Pago e PayPal')
print("idx_last_q:", idx_last_q)

# Find the closing divs of the FAQ section after idx_last_q:
# It closes with </div > \n </div> \n </div> \n </div> \n </div> \n </div>
# And then starts the CTA: <div class="section image">

cta_pattern = '<div class="section image">\n  <div class="container w-container">\n    <div class="algin-center">\n      <h1 style="line-height: 38px; font-size: 31px;" class="banner-title">Solicite um or'
idx_new_cta = text.find('line-height: 38px; font-size: 31px;')
if idx_new_cta != -1:
    idx_new_cta_start = text.rfind('<div class="section image">', 0, idx_new_cta)
    print("idx_new_cta_start:", idx_new_cta_start)
    
    # We want to remove the old CTA and old footer between the FAQ end and idx_new_cta_start
    # Let's find where the old CTA started:
    idx_old_cta_start = text.find('<div class="section image">', idx_last_q)
    print("idx_old_cta_start:", idx_old_cta_start)
    
    # Text to remove is from idx_old_cta_start to idx_new_cta_start
    text_cleaned = text[:idx_old_cta_start] + text[idx_new_cta_start:]
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(text_cleaned)
    print("Cleaned duplicate CTA and footer!")
