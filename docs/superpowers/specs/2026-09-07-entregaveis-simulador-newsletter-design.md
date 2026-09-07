# Especificação Arquitetural: Entregáveis, Simulador de Investimento, Playbook e Newsletter

> **Status do Projeto**: Planejamento e Especificação Pré-Implementação  
> **Diretriz Ativa**: NÃO CODAR AGORA (Fase de Validação de Escopo e Design)  
> **Data**: 07 de Setembro de 2026  
> **Branch**: `feature/galaxia-stacks-secao2`

---

## 1. Auditoria Técnica do Repositório & Resumo de Estado

### 1.1 O que já está 100% Construído e Comitado
- **Commit `464dfb3` (Atual)**:
  1. **Hero Cinemático**:
     - Canvas 2D frame scrubbing em alta resolução.
     - Web Audio API espacial com switch tátil de áudio (On/Off).
     - Tipografia editorial suíça, contrastes OLED dark, assinatura e marquee de disponibilidade.
  2. **Seção 01 — Portfólio / Showcase Interativo**:
     - Carrossel 3D cilíndrico WebGL (engenharia inspirada em Jesper Landberg).
     - Scroll pinning suave via GSAP ScrollTrigger (`#portfolio-pin-wrapper`).
     - Integração de projetos reais (Dashboard Eleitoral Adir Gentil 2211, Central TM, Caderno de Leads CRM).
  3. **Seção 02 — Engenharia & Stacks (Cyber-Chakra)**:
     - Engenharia reversa fiel do site de Khaled com manequim celeste *headless* (sem rosto humano, silhueta anatômica cibernética pura com fundo alfa 100% transparente).
     - 7 chakras com coordenadas anatômicas reais conectando lasers SVG com animação de fluxo de dados (`laserStream`).
     - 7 cards HUD laterais compactos sem qualquer sobreposição vertical (zero overlap) com expansão interativa em clique para revelar domínios, ferramentas, provas em produção e links de repositório no GitHub.

### 1.2 O que está Não-Comitado (Working Tree)
- O código-fonte de produção (`index.html`) está **100% limpo e sincronizado com o git**.
- Apenas arquivos utilitários de scratch (`scratch_*.py`), dumps de engenharia reversa para consulta (`C:\Users\mikaa\Downloads\www.khaledoghli.com`), capturas de tela e assets de simulação permanecem no diretório local como arquivos não rastreados, garantindo segurança total do código existente.

---

## 2. Auditoria Técnica e Comercial: O que o site tem de mais vs. O que faltava

| Aspecto | Diagnóstico | Veredito |
| :--- | :--- | :--- |
| **Impacto Visual & Credibilidade Técnica** | O site está no escalão internacional (padrão Awwwards / Site do Ano). Passa autoridade de arquiteto de software de elite. | **Excelente (Tem de sobra)** |
| **Fluidez de Transição & Performance** | A transição lateral do carrossel 3D para o boneco celeste está contínua e a 60 FPS com GSAP. | **Excelente** |
| **Clareza de Serviços ("O que eu posso comprar?")** | **Faltava**: O cliente via a tecnologia (Next.js, Python, Three.js), mas não tinha um menu claro de soluções prontas para contratar. | **Crítico — Resolvido nesta especificação** |
| **Preços & Transparência Comercial** | **Faltava**: O visitante não sabia se um projeto custa R$ 2 mil ou R$ 50 mil. Sentia-se receoso de entrar em contato sem baliza de preço. | **Crítico — Resolvido nesta especificação** |
| **Regra de Adesão / Pagamento** | **Faltava**: Deixar explícita a condição de 50% de entrada na contratação + 50% na entrega. | **Crítico — Resolvido nesta especificação** |
| **Captação Recorrente de Leads** | **Faltava**: Um ponto de contato rápido (Newsletter) para quem ainda não vai comprar um software hoje, mas quer acompanhar os lançamentos. | **Crítico — Resolvido nesta especificação** |

---

## 3. Arquitetura da Nova Seção: Entregáveis & Simulador de Investimento

A seção será posicionada após o Cyber-Chakra, funcionando como a ponte de conversão entre a **capacidade técnica demonstrada** e a **contratação prática**.

### 3.1 O Simulador Interativo de Orçamento (Console HUD)
Interface tátil inspirada no design system industrial (Linear / Stripe / Vercel), sem elementos genéricos:

1. **Seletor de Arquétipo Base (Tipo de Projeto)**:
   - **Landing Page Imersiva / Lançamento**: Foco em conversão de alto impacto visual, SEO técnico e performance móvel.
   - **Dashboard & Plataforma Web Sob Medida**: Aplicações corporativas, área de membros, bancos de dados, mapas vetoriais ou CRM.
   - **Ecossistema Inteligente com IA & Automação**: Agentes autônomos, pipelines ETL em Python e integrações de processos complexos.

2. **Módulos / Add-ons Selecionáveis**:
   - `[+ Módulo 3D WebGL / Shader Cinemático]`
   - `[+ Painel Administrativo / CMS Customizado]`
   - `[+ Agente Autônomo de Atendimento / WhatsApp]`
   - `[+ Pipeline ETL de Dados / Relatórios Automáticos]`
   - `[+ Sprint Expresso (Entrega Acelerada em 10-15 dias)]`

3. **Painel de Resultados em Tempo Real (Live HUD)**:
   - **Investimento Estimado**: Faixa dinâmica (ex: `R$ 4.500 — R$ 6.200`).
   - **Condição Comercial Obrigatória**:
     - **Adesão Inicial (50%)**: `R$ 2.250 — R$ 3.100` (no início do desenvolvimento).
     - **Saldo Final (50%)**: `R$ 2.250 — R$ 3.100` (na homologação e entrega do deploy).
   - **Prazo Estimado**: Dinâmico em semanas (ex: `2 a 3 semanas`).
   - **Disclaimer Técnico Visível**: *"Valores representam uma estimativa preliminar baseada nos módulos selecionados. O valor final é homologado após briefing técnico."*

---

## 4. O Playbook Integrado: O Método de Execução em 4 Passos

Para não poluir o site com páginas longas ou confusas, o **Playbook** é inserido diretamente adjacente ou logo abaixo do Simulador, como a **Garantia de Processo**:

```
[ PASSO 01: BRIEFING & ARQUITETURA ]
Diagnóstico técnico profundo, levantamento de requisitos, wireframe e definição dos contratos de API.

[ PASSO 02: PROTOTIPAGEM & TOKENS DE DESIGN ]
Criação do Design System no Figma, paleta HSL e validação da identidade visual antes de codar.

[ PASSO 03: ENGENHARIA & DESENVOLVIMENTO ]
Construção modular em sprints, código TypeScript estrito, testes automatizados e relatórios semanais.

[ PASSO 04: TESTE DE CARGA & LANÇAMENTO ]
Homologação em ambiente de staging, otimização Lighthouse 100, deploy em produção e pagamento final.
```

---

## 5. Fluxo de Conversão Duplo (WhatsApp + Resend Webhook)

Ao clicar no botão de ação principal do simulador: **`[ INICIAR PROJETO COM ESTA ESTIMATIVA ]`**:
1. **WhatsApp Imediato (Zero Atrito)**:
   - Abre o WhatsApp de Thiago com a mensagem pré-formatada:
     ```text
     Olá Thiago! Fiz uma estimativa no seu site:
     - Projeto: Dashboard & Plataforma Web
     - Módulos: Painel Administrativo + Pipeline Python
     - Faixa Estimada: R$ 8.000 a R$ 11.500
     - Adesão (50%): R$ 4.000 a R$ 5.750
     - Prazo: ~3 a 4 semanas
     Gostaria de agendar o alinhamento técnico.
     ```
2. **Disparo Automático via Resend**:
   - Um formulário integrado / endpoint envia um e-mail de notificação com o lead para `thiago@sempretecnologia.com.br` com todos os parâmetros da simulação gravados.

---

## 6. Seção de Newsletter: "Radar TM // Engenharia & Inteligência"

Localizada antes do rodapé final:
- **Proposta de Valor**: *"Receba ensaios técnicos, bastidores de lançamentos e novidades sobre IA agêntica e arquitetura web moderna."*
- **Layout**: Bloco minimalista OLED dark, input com foco neon, validação instantânea e integração com a lista do Resend / Audience API.

---

## 7. Próximos Passos (Aguardando Aprovação)

Nenhuma linha de código será alterada até que o documento acima seja revisado e aprovado. Após a sua aprovação, o desenvolvimento seguirá o plano de implementação progressivo.
