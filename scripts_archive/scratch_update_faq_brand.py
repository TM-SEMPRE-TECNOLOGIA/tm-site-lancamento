import re

html_path = r'c:\Users\mikaa\Documents\antigravity\tm-site-lancamento\upolitico-clone\index.html'
with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Replace FAQ mentions of Upolítico with Candidato PRO
text = re.sub(r'Upol[^\s]*tico tem CNPJ', 'O Candidato PRO tem CNPJ', text)
text = re.sub(r'Sim, o Upol[^\s]*tico faz parte', 'Sim, o Candidato PRO faz parte', text)
text = re.sub(r'servi[^\s]*o de cria[^\s]*o da Upol[^\s]*tico', 'serviço de criação do Candidato PRO', text)
text = re.sub(r'A Ag[^\s]*ncia Upol[^\s]*tico oferece', 'A agência Candidato PRO oferece', text)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated FAQ brand mentions to Candidato PRO!")
