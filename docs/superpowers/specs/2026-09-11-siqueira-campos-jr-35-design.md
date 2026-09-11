# Especificação de Design: Plataforma de Campanha Siqueira Campos Jr 35 (Democrata) & Dashboard Eleitoral

- **Data:** 11/09/2026
- **Candidato a Governador:** José Wilson Siqueira Campos Júnior (Siqueira Campos Jr) — Nº 35
- **Candidato a Vice-Governador:** Capitão Osmar (Osmar Gomes de Lima)
- **Partido:** Democrata (35)
- **Estado:** Tocantins (139 municípios)
- **Mote Central:** "O SONHO NÃO ACABOU" | "16 PROGRAMAS • 139 MUNICÍPIOS • UM SÓ TOCANTINS"
- **Compromisso:** "O TOCANTINS EM PRIMEIRO LUGAR — Desenvolver cada região. Valorizar cada pessoa."

---

## 1. Visão Geral e Arquitetura

O projeto consiste na clonagem e remodelagem de dois sistemas complementares existentes no ecossistema de campanha:

1. **`site-siqueira-campos-jr-35` (Portal Oficial de Campanha Pública):**
   - Baseado no template institucional de alta conversão (`site-deputado-template`).
   - Refatoração total de cores para a identidade oficial Democrata 35.
   - Substituição de todas as marcas, favicons e metatags.
   - Nova seção de notícias na Home: **1 Super Destaque Heroico + Grade de 5 Matérias Reais da Candidatura**.
   - Integração completa dos **16 Programas Estruturantes do Plano de Governo 2027–2030** na página de Plano de Governo e na Home.
   - Atualização da biografia (trajetória de Siqueira Campos Jr e legado histórico do fundador do Tocantins).
   - Atualização do simulador da urna para o número **35**.

2. **`dashboard-siqueira-35` (Command Center de Marketing, Tráfego & Inteligência de Campanha):**
   - Baseado em Next.js 15 / React 19 (`dashboard-adir-2211`).
   - Refatoração cromática de Tailwind e CSS vars para o Azul Marinho Nobre (`#103D80`) e Verde Esmeralda (`#3FA464`).
   - Atualização dos dados do candidato, partido, teto de gastos oficial do TSE (R$ 6.226.082,16) e mapa dos 139 municípios do Tocantins.
   - Configuração de portas de execução dedicadas (ex: 3005 para o dashboard, 3006 para o portal) evitando qualquer conflito de portas no ambiente de desenvolvimento.

---

## 2. Identidade Visual e Sistema de Design (Democrata 35)

### 2.1 Paleta Cromática
- **Azul Primário (Navy Blue Democrata):** `#103D80`
- **Azul Escuro Profundo (Headers, Rodapés, Contrastes):** `#0A2540` / `#07172C`
- **Verde Acento (Leaf/Emerald Green Democrata):** `#3FA464`
- **Verde Hover / Ativo:** `#2E9A52`
- **Branco Puro / Superfície:** `#FFFFFF`
- **Cinza Neutro / Fundo de Seção:** `#F8FAFC`
- **Bordas / Linhas Editoriais:** `#E2E8F0` / `#CBD5E1`
- **Texto Principal:** `#0F172A` (Slate 900)
- **Texto Secundário:** `#475569` (Slate 600)

### 2.2 Tipografia e Grafismos
- Tipografia moderna sem serifa (Gotham / Inter / System Sans).
- Aplicação do logo oficial transparente `DEMOCRATA 35`.
- Aplicação do mini-badge da bandeira e ícones vetorizados estilizados nas cores verde e azul marinho.

---

## 3. Conteúdo Editorial & Notícias

### 3.1 Super Destaque Principal
- **Título:** Siqueira Campos Jr assume candidatura ao Governo do Tocantins pelo Democrata 35 com Capitão Osmar como vice
- **Lead:** Resgatando o legado histórico de criação e desenvolvimento do Tocantins sob a liderança de seu pai, Siqueira Campos Jr une experiência empresarial e a disciplina militar do Capitão Osmar para colocar o Tocantins no rumo certo.
- **Badge:** COMUNICADO OFICIAL • ELEIÇÕES 2026

### 3.2 Grade Editorial (5 Matérias Menores)
1. **Segurança Pública (Capitão Osmar):** Fortalecimento dos batalhões da PM, videomonitoramento inteligente e policiamento presente nos 139 municípios.
2. **Agro 100 Mil Famílias:** Programa quer transformar pequenos produtores em protagonistas com irrigação, armazenagem e conexão à agroindústria.
3. **Tocantins Modal & Porto Praia Norte:** Integração estratégica da Ferrovia Norte-Sul, Hidrovia Araguaia-Tocantins e malha rodoviária.
4. **Saúde Perto de Casa:** Fim do sofrimento na ambulância: plano propõe regionalização e ampliação dos hospitais de Araguaína, Gurupi e Porto Nacional.
5. **Tocantins Vale da Tecnologia & UNITINS:** Interiorização do ensino superior gratuito e estímulo a polos de inovação e inteligência artificial no Estado.

---

## 4. Estrutura do Plano de Governo 2027–2030 (16 Programas Estruturantes)

1. Tocantins Superior para Todos (UNITINS interiorizada)
2. Tocantins em Crescimento (Economia e empregos)
3. Tocantins Mineral, Industrial e Tecnológico (Verticalização da riqueza)
4. Saúde Perto de Casa (Fim do sofrimento na ambulância)
5. Educação Básica (Escola que forma para a vida)
6. Agro – 100 Mil Famílias Produtivas e Fortes
7. Turismo – Muito Além do Jalapão
8. Tocantins Modal (Ferrovia, Hidrovia e Rodovias)
9. Segurança Presente (Inteligência e combate ao crime)
10. Municipalismo (Governo nos 139 municípios)
11. Tocantins de Volta ao Mundo (Atração de investimentos)
12. Meio Ambiente, Água e Energia (Sustentabilidade e segurança hídrica)
13. Tocantins Vale da Tecnologia (Polos de inovação e IA)
14. Tocantins Transparente e Responsável (Gestão fiscal rigorosa)
15. Tocantins Justiça Acelerada (Resolução em até 6 meses)
16. Gestão, Tecnologia e Juventude (Governo digital e futuro dos jovens)

---

## 5. Plano de Portas e Servidores Locais

Conforme a regra de gerenciamento de portas:
- **`site-siqueira-campos-jr-35`:** Servidor estático na porta **3006**
- **`dashboard-siqueira-35`:** Next.js Dev Server na porta **3005** (`strictPort: true`)

---

## 6. Critérios de Sucesso e Verificação
1. Ambos os projetos criados em diretórios próprios sem afetar os do Adir Gentil.
2. Logos Democrata 35 com transparência e alta nitidez aplicados em ambos os projetos.
3. Cores 100% atualizadas (sem vestígios do azul/amarelo do PL).
4. Seção de notícias com 1 Super Destaque + 5 cards menores funcionando perfeitamente em desktop e mobile.
5. Os 16 programas estruturantes refletidos no Plano de Governo.
6. Build e preview local verificados via browser/curl sem erros no console.
