# GUIA INTERNO DE OPERAÇÃO: MÉTRICAS REAIS, TELEMETRIA & INTEGRAÇÕES
**Campanha Oficial Adir Gentil 2211 • Deputado Federal (PL Tocantins)**  
*Documento Técnico Interno de Operações e Gestão de Tráfego — TM Sempre Tecnologia*

---

## 1. Visão Geral da Arquitetura do Sistema

O ecossistema digital da campanha é composto por duas camadas integradas:

```
┌────────────────────────────────────────────────────────┐
│           SITE OFICIAL (site-deputado-template)        │
│  - Formulário de Newsletter (Home)                     │
│  - Cadastro de Voluntários & Apoiadores (Participe)    │
│  - Telemetria de Cliques (WhatsApp, Jingles, Materiais)│
└─────────────────────────┬──────────────────────────────┘
                          │ (CORS / REST Beacons)
                          ▼
┌────────────────────────────────────────────────────────┐
│           DASHBOARD DE INTELIGÊNCIA (Porta 3005)       │
│  - API /api/analytics/track (Buffer de Telemetria)     │
│  - API /api/newsletter/subscribe                       │
│  - API /api/leads (Voluntários nos 139 municípios)    │
│  - API /api/resend/stats & /api/resend/send-test       │
│  - Conectores /api/ads/meta e /api/ads/google          │
└────────────┬─────────────────────────────┬─────────────┘
             │                             │
             ▼                             ▼
┌─────────────────────────┐   ┌───────────────────────────┐
│     RESEND EMAIL CRM    │   │ CONTAS DE ANÚNCIOS REAIS  │
│  - Audiência: General   │   │  - Meta Ads Graph API     │
│  - Contatos Automatizados│  │  - Google Ads API (MCC)   │
└─────────────────────────┘   └───────────────────────────┘
```

---

## 2. Integração Resend (E-mail Marketing & CRM)

### 2.1. Credenciais Oficiais Ativas
- **Chave de API**: `re_SECRET_KEY_PLACEHOLDER`
- **Nome da Credencial no Resend**: `SITE ADIR GENTIL (disparodeemail)`
- **ID da Audiência Principal**: `aac938e8-2fcd-4306-b350-b100cda609ac` (*General*)
- **Remetente Provisório**: `onboarding@resend.dev`
- **Remetente Oficial Definitivo**: `contato@adirgentil2211.com.br` (após verificação de DNS)

### 2.2. Como Funciona a Captura Automática
1. Quando qualquer eleitor se inscreve no rodapé da Home ou no formulário de voluntariado em `participe.html`:
   - O contato é automaticamente inserido na audiência do Resend (`aac938e8-2fcd-4306-b350-b100cda609ac`).
   - O lead é salvo no banco local de contingência (`data/leads.json`).
   - Um evento em tempo real `newsletter_subscribe` ou `volunteer_signup` é enviado para o buffer da telemetria do Dashboard.
2. Na aba **E-mail CRM** do Dashboard:
   - A contagem de contatos reais da audiência é atualizada em tempo real via endpoint `/api/resend/stats`.
   - O gestor pode testar disparos imediatos para qualquer endereço de e-mail pelo testador integrado no próprio painel.

### 2.3. Passo a Passo para Ativação do Domínio `@adirgentil2211.com.br` no Resend
Para sair do modo de testes (`resend.dev`) e disparar com o domínio oficial da campanha:
1. Acesse [resend.com/domains](https://resend.com/domains).
2. Clique em **Add Domain** e digite `adirgentil2211.com.br` (região *sa-east-1* ou *us-east-1*).
3. O Resend fornecerá 3 registros DNS obrigatórios:
   - **MX**: `feedback-smtp.resend.com` (Prioridade 10).
   - **TXT (SPF)**: `v=spf1 include:resend.com ~all`.
   - **TXT / CNAME (DKIM)**: Chave criptográfica única de assinatura.
   - **TXT (DMARC)**: `_dmarc.adirgentil2211.com.br` com valor `v=DMARC1; p=none;`.
4. Insira os registros no painel DNS (Cloudflare ou Registro.br).
5. No arquivo `.env` do Dashboard, altere `RESEND_FROM_EMAIL=contato@adirgentil2211.com.br`.

---

## 3. Conexão com Contas de Anúncio Reais (Meta Ads & Google Ads)

Para que o Dashboard puxe os gastos financeiros, impressões e cliques diretamente dos servidores das plataformas de anúncio sem depender de projeções manuais, a equipe de tráfego deve fornecer os tokens de acesso correspondentes.

### 3.1. Conexão com Meta Ads (Facebook & Instagram)
O Meta exige um Token de Acesso do Sistema permanente vinculado à Conta de Anúncios da Campanha.

#### Passo a Passo:
1. Acesse o **Meta Business Suite** (business.facebook.com) onde está a conta de anúncios de Adir Gentil.
2. Vá em **Configurações do Negócio &gt; Contas &gt; Contas de Anúncios**:
   - Copie o **ID da Conta de Anúncios** (ex: `act_9876543210`).
3. Vá em **Configurações do Negócio &gt; Usuários &gt; Usuários do Sistema**:
   - Clique em **Adicionar** e nomeie como `Dashboard-Adir-Gentil`.
   - Atribua a função de *Administrador* ou *Funcionário*.
   - Em *Ativos Atribuídos*, adicione a Conta de Anúncios e marque a permissão **Gerenciar Campanhas / Ver Desempenho**.
4. Clique em **Gerar Novo Token**:
   - Selecione o aplicativo da campanha.
   - Validade do token: **Nunca expira** (Sistema permanente).
   - Marque as permissões obrigatórias:
     - `ads_read` (leitura de anúncios e gastos)
     - `read_insights` (métricas de alcance, cliques, CPC e CPA)
     - `ads_management` (opcional, se desejar pausar campanhas pelo painel)
5. No arquivo `dashboard-adir-2211/.env`, preencha:
   ```env
   META_ACCESS_TOKEN=EAAG...SEU_TOKEN_AQUI...
   META_AD_ACCOUNT_ID=act_9876543210
   META_PIXEL_ID=123456789012345
   ```
6. Pronto! A rota `/api/ads/meta` passará a puxar automaticamente o gasto diário, CPC, CPM e conversões diretas para o Dashboard.

---

### 3.2. Conexão com Google Ads (Rede de Pesquisa & YouTube)
A Google Ads API requer autenticação via OAuth 2.0 e Developer Token emitido pela Central de Contas (MCC).

#### Passo a Passo:
1. Acesse o [Google Cloud Console](https://console.cloud.google.com):
   - Crie um projeto chamado `Adir-Gentil-Campanha-2211`.
   - Em *APIs e Serviços &gt; Biblioteca*, procure por **Google Ads API** e clique em **Ativar**.
   - Em *Tela de Consentimento OAuth*, selecione tipo *Interno* ou *Externo* e configure o nome da aplicação.
   - Em *Credenciais*, crie uma **ID do cliente OAuth 2.0** (tipo Aplicação Web). Guarde o *Client ID* e o *Client Secret*.
2. Obtenha o **Developer Token**:
   - Na conta MCC (Central de Contas) da agência / gestor de tráfego, acesse *Ferramentas e Configurações &gt; Configuração &gt; Central da API do Google Ads*.
   - Copie o **Developer Token**.
3. Obtenha o **Customer ID**:
   - O número de 10 dígitos da conta de anúncios do Adir Gentil no canto superior direito (formato: `123-456-7890`).
4. Preencha no arquivo `dashboard-adir-2211/.env`:
   ```env
   GOOGLE_ADS_CUSTOMER_ID=1234567890
   GOOGLE_ADS_DEVELOPER_TOKEN=SEU_DEV_TOKEN
   GOOGLE_ADS_CLIENT_ID=SEU_CLIENT_ID.apps.googleusercontent.com
   GOOGLE_ADS_CLIENT_SECRET=SEU_CLIENT_SECRET
   GOOGLE_ADS_REFRESH_TOKEN=SEU_REFRESH_TOKEN
   ```

---

## 4. Auditoria de Telemetria e Capturas do Site

### 4.1. Como o Site Envia Eventos para o Dashboard
O script `site-deputado-template/js/analytics-client.js` captura as ações do visitante no site e as encaminha em segundo plano via `navigator.sendBeacon` ou `fetch` para:
`http://localhost:3005/api/analytics/track` (em ambiente de teste/local) ou URL de produção.

### 4.2. Catálogo de Eventos Principais Rastreados:
- `newsletter_submit`: Cadastro de e-mail no formulário da Home.
- `volunteer_signup`: Cadastro completo de voluntário na página Participe.
- `click_tocomadir-zap`: Clique para entrada no grupo VIP oficial do WhatsApp.
- `download_jingle`: Download do arquivo de áudio MP3 do jingle oficial.
- `download_material`: Download de adesivos, santinhos digitais e plano de trabalho.
- `click_doacao`: Clique para acesso à plataforma de doação eleitoral.

### 4.3. Armazenamento Local dos Cadastros
Além do espelhamento imediato no Resend, todos os dados submetidos pelo site ficam salvos em:
`dashboard-adir-2211/data/leads.json`  
Permitindo exportação em CSV para a coordenação geral de campanha a qualquer momento.

---

## 5. Resumo das Portas Locais de Operação

Em conformidade com a convenção de portas do ecossistema:
- **Dashboard Next.js**: `http://localhost:3005` (porta padrão: 3005)
- **Site de Campanha**: `http://localhost:3001` (porta padrão: 3001)

Para rodar o ambiente completo:
1. **Terminal 1 (Dashboard)**:
   ```bash
   cd dashboard-adir-2211
   npm run dev
   ```
2. **Terminal 2 (Site Oficial)**:
   ```bash
   cd site-deputado-template
   python serve.py
   ```

---
*Documento aprovado pela Coordenação Digital — TM Sempre Tecnologia • Eleições 2026*
