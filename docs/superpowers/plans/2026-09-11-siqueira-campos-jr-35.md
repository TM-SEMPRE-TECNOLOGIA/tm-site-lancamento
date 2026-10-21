# Siqueira Campos Jr 35 (Democrata) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Clonar e refatorar completamente o portal de campanha (`site-siqueira-campos-jr-35`) e o dashboard analítico (`dashboard-siqueira-35`) para o candidato a Governador do Tocantins Siqueira Campos Jr (Democrata 35) e vice Capitão Osmar, com nova paleta de cores (Azul Marinho e Verde), logos oficiais transparentes, nova seção de notícias (1 destaque grande + 5 menores) e os 16 programas do Plano de Governo 2027–2030 ("O Sonho Não Acabou").

**Architecture:** Estrutura bifurcada independente: `site-siqueira-campos-jr-35` (HTML5/CSS3/JS modular sem dependências externas pesadas) rodando na porta 3006, e `dashboard-siqueira-35` (Next.js 15, Tailwind, Lucide, Recharts) rodando na porta 3005 com strictPort, sem interferir no projeto do Adir Gentil.

**Tech Stack:** HTML5, CSS3 Custom Properties, Vanilla JS, Next.js 15, React 19, TypeScript, Tailwind CSS, Lucide React, Python (para processamento de imagens e assets).

**Spec:** `docs/superpowers/specs/2026-09-11-siqueira-campos-jr-35-design.md`

## Global Constraints
- Cores Primárias: Azul Marinho Nobre `#103D80` / `#0A2540`, Verde Esmeralda `#3FA464` / `#2E9A52`, Branco `#FFFFFF`.
- Candidato: Siqueira Campos Jr (Governador) | Capitão Osmar (Vice-Governador).
- Número: 35 | Partido: DEMOCRATA | Estado: Tocantins (139 municípios).
- Mote Oficial: "O SONHO NÃO ACABOU" | "16 PROGRAMAS • 139 MUNICÍPIOS • UM SÓ TOCANTINS".
- Portas: Dashboard na porta 3005 | Portal na porta 3006.

---

### Task 1: Preparação de Assets Visuais e Tratamento de Imagens
**Files:**
- Create: `site-siqueira-campos-jr-35/assets/logo/democrata-35-logo.png`
- Create: `site-siqueira-campos-jr-35/assets/candidato/siqueira-campos-jr.png`
- Create: `site-siqueira-campos-jr-35/assets/candidato/capitao-osmar.png`
- Create: `dashboard-siqueira-35/public/democrata-35-logo.png`
- Create: `dashboard-siqueira-35/public/siqueira-campos-jr.png`

- [ ] **Step 1: Processar e recortar logomarca transparente em alta resolução**
  Copiar `media_1789094051270.png` para assets e garantir fundo alfa perfeito e nitidez.
- [ ] **Step 2: Processar foto oficial do candidato Siqueira Campos Jr**
  Otimizar `media_1789094174098.png`, ajustar contraste/iluminação e criar versão para avatar/hero.
- [ ] **Step 3: Criar favicon e badges do Democrata 35**
  Gerar favicons 16x16, 32x32, 192x192 nas cores azul e verde.

---

### Task 2: Clonagem e Refatoração de Cores e Identidade do Portal de Campanha (`site-siqueira-campos-jr-35`)
**Files:**
- Create/Clone: pasta `site-siqueira-campos-jr-35` a partir de `site-deputado-template`
- Modify: `site-siqueira-campos-jr-35/css/styles.css`
- Modify: `site-siqueira-campos-jr-35/css/revision.css`
- Modify: `site-siqueira-campos-jr-35/css/news.css`
- Modify: `site-siqueira-campos-jr-35/index.html`
- Modify: `site-siqueira-campos-jr-35/noticias.html`
- Modify: `site-siqueira-campos-jr-35/plano-de-governo.html`
- Modify: `site-siqueira-campos-jr-35/trajetoria.html`

- [ ] **Step 1: Clonar arquivos base sem histórico git antigo**
- [ ] **Step 2: Refatorar variáveis CSS globais de cores**
  Substituir `--blue-pl: #005baa` por `--blue-democrata: #103D80`, `#0A2540`; substituir amarelos por branco/verde; definir `--green-democrata: #3FA464`.
- [ ] **Step 3: Atualizar Header, Navbar, Rodapé e Metadados**
  Ajustar textos de Adir Gentil 2211 para Siqueira Campos Jr 35, Governador TO, Capitão Osmar.

---

### Task 3: Implementação da Nova Seção de Notícias (1 Super Destaque + Grade de 5 Matérias)
**Files:**
- Modify: `site-siqueira-campos-jr-35/index.html` (Seção `#noticias`)
- Modify: `site-siqueira-campos-jr-35/noticias.html`
- Modify: `site-siqueira-campos-jr-35/css/news.css`

- [ ] **Step 1: Estruturar o Super Destaque Heroico**
  Anúncio oficial da chapa Siqueira Campos Jr & Capitão Osmar pelo Democrata 35.
- [ ] **Step 2: Construir a grade editorial de 5 notícias**
  1. Segurança e Valorização Policial (Capitão Osmar)
  2. Agro: 100 Mil Famílias Produtivas e Fortes
  3. Tocantins Modal & Eixos Estratégicos (Ferrovia, Hidrovia e Rodovias)
  4. Saúde Perto de Casa (Fim do sofrimento na ambulância e hospitais regionais)
  5. Tocantins Vale da Tecnologia e Interiorização da UNITINS
- [ ] **Step 3: Validar responsividade mobile e desktop**

---

### Task 4: Integração dos 16 Programas do Plano de Governo 2027–2030
**Files:**
- Modify: `site-siqueira-campos-jr-35/plano-de-governo.html`
- Modify: `site-siqueira-campos-jr-35/index.html` (Seção `#propostas`)

- [ ] **Step 1: Inserir a íntegra dos 16 programas oficiais extraídos do documento do candidato**
  "O Sonho Não Acabou", detalhando metas e o que se busca alcançar em cada um dos 16 eixos.
- [ ] **Step 2: Atualizar os cards interativos de propostas na Home**
- [ ] **Step 3: Ajustar o simulador de urna para o número 35 e foto de Siqueira Campos Jr**

---

### Task 5: Clonagem e Customização do Dashboard Analítico (`dashboard-siqueira-35`)
**Files:**
- Create/Clone: pasta `dashboard-siqueira-35` a partir de `dashboard-adir-2211`
- Modify: `dashboard-siqueira-35/package.json`
- Modify: `dashboard-siqueira-35/app/layout.tsx`
- Modify: `dashboard-siqueira-35/app/globals.css`
- Modify: `dashboard-siqueira-35/components/Navbar.tsx`
- Modify: `dashboard-siqueira-35/components/tabs/OverviewTab.tsx`
- Modify: `dashboard-siqueira-35/components/tabs/RoiFinanceTab.tsx`

- [ ] **Step 1: Clonar projeto e atualizar dependências/configuração de porta (3005)**
- [ ] **Step 2: Refatorar paleta Tailwind e variáveis CSS para Democrata 35**
- [ ] **Step 3: Atualizar dados eleitorais: Governador TO 35, teto TSE R$ 6.226.082,16, métricas dos 139 municípios**
- [ ] **Step 4: Atualizar mapa e feeds de eventos ao vivo para o contexto de Siqueira Campos Jr**

---

### Task 6: Verificação, Build e Testes em Tempo Real
**Files:**
- Test: Verificação de carregamento HTTP do portal na porta 3006
- Test: Build Next.js do dashboard na porta 3005
- Test: Inspeção visual de contraste e ausência de resquícios do candidato anterior

- [ ] **Step 1: Iniciar servidor do portal e inspecionar DOM/CSS**
- [ ] **Step 2: Testar build e rodar dev server do dashboard**
- [ ] **Step 3: Documentar walkthrough e entregar links ao usuário**
