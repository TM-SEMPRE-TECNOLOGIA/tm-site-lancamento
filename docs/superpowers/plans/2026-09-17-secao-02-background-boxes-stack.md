# Seção 02: Background Boxes Isometric Grid com Frameworks TM — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implementar o componente Aceternity UI `BackgroundBoxes` adaptado como a nova Seção 02 ("Engenharia & Stack // O Motor de Construção") no `index.html`, com grade isométrica em tons alaranjados/âmbar TM, células interativas com logos oficiais dos frameworks e rolagem vertical natural e responsiva.

**Architecture:** Transformar o conceito React/Framer Motion em uma arquitetura pura e ultra-otimizada de HTML5 + CSS3 + Vanilla JS (com suporte a GSAP já carregado no projeto). A grade geométrica isométrica com retículos `+` será gerada no DOM com malha controlada (~24 colunas x 16 linhas = 384 células), contendo células especiais mapeadas para os 10 frameworks principais da TM com SVGs vetoriais embutidos, iluminação em tons de fogo/âmbar/laranja via hover e pulsos orgânicos automáticos, e vinheta de máscara radial que dissolve o chão no fundo escuro `#05070b`.

**Tech Stack:** HTML5, CSS3 (Transforms 3D, CSS Variables, radial-gradient masks), Vanilla JavaScript (Event Delegation para 60 FPS, IntersectionObserver), SVGs vetoriais dos frameworks (Next.js, TypeScript, Python, FastAPI, React, Three.js, Tailwind, Agentic AI/Gemini, Docker, PostgreSQL).

**Spec:** Baseado na especificação enviada pelo usuário da biblioteca Aceternity UI (`BackgroundBoxes`), adaptando a paleta de azul/cinza para tons alaranjados TM (`#d96526`, `#f97316`, `#f59e0b`), inserindo os títulos canônicos de Engenharia e integrando logos dos frameworks com acendimento dinâmico.

---

## Global Constraints

- **Zero dependência externa nova**: Usar o que já está carregado no projeto (CSS Variables, Google Fonts Inter/Newsreader/JetBrains Mono, GSAP 3.12). Não empacotar React/Node em tempo de execução no `index.html`.
- **Performance pura (60 FPS)**: Evitar o erro original do snippet React de criar 15.000 divs (150 x 100), o que travaria o navegador. Usar uma grade perfeitamente dimensionada para cobrir a viewport com folga (~24x16 a 28x18 = ~450 células) com Event Delegation no container pai (`pointermove` / `mouseenter`).
- **Paleta Alaranjada Corporativa TM**: Bordas em `rgba(217, 101, 38, 0.22)` a `rgba(217, 101, 38, 0.45)`, cruzes `+` em `rgba(217, 101, 38, 0.35)`, e cores aleatórias de acendimento em variações de laranja elétrico, âmbar, ouro incandescente e acento ciano sutil.
- **Mobile First / Rolagem Vertical**: No mobile, a seção deve permitir a rolagem vertical 100% natural, sem pinned scrolls travados nem carrosséis horizontais.
- **Preservação de Integridade**: Manter o carrossel da Seção 01 e as demais seções intactas.

---

## File Structure

- **Modify**: `index.html` (Inserção do HTML da Seção 02 no slot `#slot-2`, regras CSS dedicadas para o grid isométrico e script do motor de caixas interativas).
- **Create**: `simulador-background-boxes-stack.html` (Sandbox isolada para validação e testes visuais prévios antes da incorporação final).
- **Update**: `specs-arquitetura-site.html` (Atualização do status da Seção 02 de "Slot Limpo" para "Componente Background Boxes Aprovado").

---

## Task 1: Construção do Protótipo Isolado (Sandbox) em `simulador-background-boxes-stack.html`

**Files:**
- Create: `C:\Users\mikaa\Documents\antigravity\tm-site-lancamento\simulador-background-boxes-stack.html`

**Interfaces:**
- Consumes: Estrutura do snippet Aceternity UI `BackgroundBoxes` + paleta TM (`#d96526`, `#f97316`, `#f59e0b`).
- Produces: Página standalone funcional com a grade isométrica, retículos `+`, máscaras de vinheta radial, títulos editoriais e células de frameworks interativas.

- [ ] **Step 1: Criar a base HTML e tokens CSS da grade isométrica alaranjada**
  - Definir container com perspectiva: `transform: translate(-35%, -45%) skewX(-48deg) skewY(14deg) scale(0.72) rotate(0deg) translateZ(0);`
  - Criar células `.box-cell` com bordas superiores e direitas em `rgba(217, 101, 38, 0.22)`.
  - Inserir cruzes vetoriais `+` SVG nas interseções pares (`top: -10px; left: -10px;`).
  - Aplicar vinheta radial com `mask-image: radial-gradient(circle at 50% 50%, rgba(0,0,0,1) 30%, rgba(0,0,0,0.5) 60%, transparent 85%);`.

- [ ] **Step 2: Incorporar as logos vetoriais (SVGs limpos) dos frameworks nas células-chave**
  - Mapear coordenadas de células no grid para 10 tecnologias fundamentais:
    1. `Next.js 15` (Logomarca N estilizada)
    2. `React 19` (Átomo reativo)
    3. `TypeScript` (Badge TS)
    4. `Python 3.12` (Cobras entrelaçadas)
    5. `FastAPI` (Raio de velocidade)
    6. `Three.js` (Triângulo 3D isométrico)
    7. `Tailwind CSS` (Ondas de estilo)
    8. `Agentic AI / Gemini` (Estrela cognitiva de 4 pontas)
    9. `Docker` (Baleia com contêineres)
    10. `PostgreSQL` (Elefante relacional)
  - Configurar estado recolhido sutil (`opacity: 0.35`) e estado iluminado com cor própria e glow ao passar o mouse.

- [ ] **Step 3: Implementar o motor de interação JavaScript com Event Delegation**
  - Criar array de cores quentes TM:
    ```javascript
    const WARM_COLORS = [
      "rgba(217, 101, 38, 0.85)",  // TM Orange
      "rgba(249, 115, 22, 0.85)",  // Orange 500
      "rgba(245, 158, 11, 0.85)",  // Amber 500
      "rgba(251, 191, 36, 0.85)",  // Yellow 400
      "rgba(234, 88, 12, 0.85)",   // Orange 600
      "rgba(239, 68, 68, 0.85)",   // Red 500
      "rgba(10, 252, 219, 0.85)"   // Cyan TM Glow Accent
    ];
    ```
  - Adicionar listener de mouse com transição de desvanecimento suave (fade out de 2 segundos).
  - Adicionar pulso de vida autônomo aleatório (a cada 600ms uma célula aleatória se acende suavemente para manter o chão vivo mesmo sem interação do usuário).

- [ ] **Step 4: Incorporar o Título e Cabeçalho Canônico da Seção de Stack**
  - Eyebrow: `// ENGENHARIA & STACK · O MOTOR DE CONSTRUÇÃO`
  - H2: `Linguagens, Frameworks & <strong>Engenharia.</strong>`
  - Subtítulo: `A arquitetura por trás de aplicações corporativas, pipelines de dados e interfaces 3D de alta performance.`
  - Centralizar sobre a vinheta no eixo Z superior (`z-index: 20; pointer-events: none;`).

- [ ] **Step 5: Validar o simulador no navegador via Chrome DevTools MCP**
  - Abrir `file:///.../simulador-background-boxes-stack.html` e tirar screenshot.
  - Verificar alinhamento da grade, tom alaranjado e comportamento do hover.

---

## Task 2: Integração e Refinamento Responsivo no `index.html`

**Files:**
- Modify: `C:\Users\mikaa\Documents\antigravity\tm-site-lancamento\index.html`

**Interfaces:**
- Consumes: Componente validado na Task 1.
- Produces: Seção 02 integrada no fluxo normal de rolagem vertical da landing page principal.

- [ ] **Step 1: Substituir o placeholder `#slot-2` pelo componente estrutural**
  - Inserir `<section id="section-stack-boxes" class="stack-boxes-section">` logo após `#portfolio-pin-wrapper`.
  - Configurar container com `position: relative; overflow: hidden; min-height: 85vh; background: #05070b;`.

- [ ] **Step 2: Adicionar os estilos CSS otimizados no `<style>` de `index.html`**
  - Inserir as regras `.stack-boxes-container`, `.box-cell`, `.box-crosshair`, `.box-framework-icon`, `.box-tooltip`.
  - Configurar media queries para mobile:
    - Em telas `< 768px`: diminuir escala e inclinação para evitar qualquer corte horizontal (`transform: translate(-25%, -35%) skewX(-32deg) skewY(10deg) scale(0.6)`).
    - Ajustar tipografia fluida com `clamp()` para o título não quebrar em telas estreitas.

- [ ] **Step 3: Injetar a lógica JS de inicialização da Seção 02**
  - Adicionar função `initStackBackgroundBoxes()` vinculada a `DOMContentLoaded`.
  - Usar `IntersectionObserver` para pausar os pulsos aleatórios quando a seção não estiver visível na tela, garantindo zero consumo de CPU/bateria em segundo plano.

- [ ] **Step 4: Validar e inspecionar a landing page principal**
  - Recarregar `index.html` no navegador local.
  - Rolar até a Seção 02 e validar transição visual entre o carrossel de portfólio 3D e o chão isométrico da stack.
  - Testar tanto em desktop (1440x900) quanto em mobile (390x844).

---

## Task 3: Atualização do Caderno de Specs e Registro de Commit

**Files:**
- Modify: `C:\Users\mikaa\Documents\antigravity\tm-site-lancamento\specs-arquitetura-site.html`

- [ ] **Step 1: Atualizar o status da Seção 02 no Caderno de Arquitetura**
  - Marcar Seção 02 como `Status: Em Produção / Background Boxes Aprovado`.
  - Atualizar o resumo descritivo no roadmap.

- [ ] **Step 2: Commit estruturado no Git**
  - Executar `git add` e commit:
    `git commit -m "feat(secao2): implementa background boxes isometrico alaranjado com frameworks TM"`
