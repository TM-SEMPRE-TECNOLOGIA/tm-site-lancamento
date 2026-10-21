
global.document = {
    getElementById: (id) => ({
        getContext: () => ({
            clearRect(){}, save(){}, restore(){}, translate(){}, scale(){},
            createRadialGradient(){ return { addColorStop(){} }; },
            beginPath(){}, arc(){}, fill(){}, stroke(){}, setLineDash(){}, fillText(){}, strokeText(){}
        }),
        addEventListener(){},
        classList: { add(){}, remove(){}, toggle(){} },
        style: {}
    })
};
global.window = { innerWidth: 1920, innerHeight: 1080, addEventListener(){} };
global.requestAnimationFrame = (fn) => {};


    const canvas = document.getElementById('galaxyCanvas');
    const ctx = canvas.getContext('2d');

    let width = window.innerWidth;
    let height = window.innerHeight;
    canvas.width = width;
    canvas.height = height;

    function resize() {
      width = window.innerWidth;
      height = window.innerHeight;
      canvas.width = width;
      canvas.height = height;
    }
    window.addEventListener('resize', resize);

    // Camera / Pan / Zoom
    let panX = width / 2;
    let panY = height / 2;
    let zoom = 1;
    let isDragging = false;
    let startX = 0, startY = 0;

    let showOrbits = true;
    let showLinks = true;

    // Blueprint Data Nodes (The Planetary Galaxy)
    const nodes = [
      // Core Supernova
      {
        id: 'core',
        label: 'Núcleo TM: Estúdio VIP',
        category: 'CENTRO DA GALÁXIA',
        price: 'Meta: R$ 2.250/mês Recorrente',
        desc: 'O coração da operação. Transforma profissionais de beleza autônomas em assinantes mensais de infraestrutura e presença digital de elite.',
        function: 'Gera previsibilidade de caixa (MRR) de R$ 2.250/mês com 20 clientes ativos pagando R$ 112,50/mês. Cobre aluguel e custos fixos automaticamente.',
        rules: '• Nenhum suporte fora do horário comercial.<br>• Todas as atualizações são solicitadas via formulário padronizado.<br>• Limite estrito de 2 atualizações mensais por cliente.',
        x: 0,
        y: 0,
        radius: 38,
        color: '#D96526',
        glowColor: 'rgba(217, 101, 38, 0.6)',
        orbit: 0
      },

      // Orbit 1: Atração & Tráfego (Meta Ads)
      {
        id: 'ad_hook',
        label: 'Meta Ads: Anúncios PAS',
        category: 'ATRAÇÃO & TRÁFEGO PAGO',
        price: 'R$ 25/dia (R$ 150 Total)',
        desc: 'Criativos em vídeo e imagem focados na dor latente da profissional de estética que vive mandando preços desorganizados no WhatsApp.',
        function: 'Gerar de 30 a 70 cliques altamente qualificados por dia para a Landing Page de Vendas (CPC entre R$ 0,40 e R$ 0,70).',
        rules: '• Criativo 1: Choque de Preço ("Menos que uma manutenção de fibra").<br>• Criativo 2: Dor do WhatsApp ("Cansada de responder 40x 'qual o valor' e a cliente sumir?").<br>• Criativo 3: Demonstração da tela do celular rolando o site elegante.',
        x: -240,
        y: -100,
        radius: 20,
        color: '#EC4899',
        glowColor: 'rgba(236, 72, 153, 0.5)',
        orbit: 250
      },
      {
        id: 'ad_target',
        label: 'Segmentação Especializada',
        category: 'ATRAÇÃO & TRÁFEGO PAGO',
        price: 'Público Alvo Aberto Qualificado',
        desc: 'Mulheres de 22 a 45 anos interessadas em Lash Lifting, Unhas de Gel, Micropigmentação e administradoras de páginas comerciais.',
        function: 'Filtrar amadores e atrair profissionais que já atendem no dia a dia e têm receita ativa para contratar.',
        rules: '• Excluir termos como "curso gratuito", "renda extra", "vagas de emprego".<br>• Segmentar por raio regional ou capitais de alta densidade.',
        x: -260,
        y: 80,
        radius: 17,
        color: '#F472B6',
        glowColor: 'rgba(244, 114, 182, 0.4)',
        orbit: 250
      },

      // Orbit 2: Landing Page de Vendas (Front-end Tripwire)
      {
        id: 'lp_entry',
        label: 'Plano Essencial Vitrine',
        category: 'FRONT-END (O PÃO QUENTE)',
        price: 'R$ 19,90 (Taxa Simbólica)',
        desc: 'Layout clean e elegante para celular. Apresentação do espaço, fotos dos procedimentos, mapa e botão direto pro WhatsApp.',
        function: 'Quebra total de atrito de compra. Abaixo de R$ 20 o cartão passa por impulso puro sem pensar.',
        rules: '• Não existe reunião de alinhamento.<br>• A cliente escolhe a paleta (Nude Chic, Rosé Gold ou Dark Glamour) e preenche o formulário.',
        x: -70,
        y: -230,
        radius: 22,
        color: '#38BDF8',
        glowColor: 'rgba(56, 189, 248, 0.5)',
        orbit: 250
      },
      {
        id: 'lp_pro',
        label: 'Plano Pro: Catálogo Completo',
        category: 'FRONT-END (O PÃO QUENTE)',
        price: 'R$ 37,00',
        desc: 'Tabela interativa de procedimentos (alongamento, manutenção, spa dos pés, sobrancelhas), bio profissional e depoimentos.',
        function: 'Atende quem já tem cardápio volumoso e quer passar imagem de clínica conceituada.',
        rules: '• A cliente envia até 8 fotos dos melhores procedimentos.<br>• Estrutura 100% responsiva para iPhone e Android.',
        x: 100,
        y: -220,
        radius: 19,
        color: '#60A5FA',
        glowColor: 'rgba(96, 165, 250, 0.4)',
        orbit: 250
      },

      // Orbit 3: O Checkout & Order Bumps (O Lucro Limpo)
      {
        id: 'bump_domain',
        label: 'Bump 1: Domínio & SSL 1 Ano',
        category: 'ORDER BUMP 1 (BACKEND OBRIGATÓRIO)',
        price: '+ R$ 120,00 no Checkout',
        desc: 'Registro oficial do endereço .com.br (ex: www.jessicalash.com.br) + servidores em nuvem ultrarrápidos + certificado SSL blindado.',
        function: 'Gera a maior margem líquida da ativação imediata (R$ 80 de lucro limpo com custo de R$ 40 no Registro.br).',
        rules: '• O cliente marca a caixinha com 1 clique no mesmo checkout.<br>• Apresentado como ativação técnica essencial para o site funcionar.',
        x: 240,
        y: -90,
        radius: 24,
        color: '#10B981',
        glowColor: 'rgba(16, 185, 129, 0.6)',
        orbit: 260
      },
      {
        id: 'bump_express',
        label: 'Bump 2: Fila Full Express 48h',
        category: 'ORDER BUMP 2 (VELOCIDADE VALORIZADA)',
        price: '+ R$ 57,00 no Checkout',
        desc: 'A cliente fura a fila padrão de 15 dias e recebe seu ecossistema 100% no ar e homologado em até 48 horas úteis.',
        function: 'Margem 100% líquida. Custa zero de insumo e aproveita a urgência de quem está perdendo agendamentos no fim de semana.',
        rules: '• Prioridade imediata no dashboard de produção.<br>• Entrega garantida em até 48 horas após preenchimento do formulário.',
        x: 260,
        y: 60,
        radius: 20,
        color: '#34D399',
        glowColor: 'rgba(52, 211, 153, 0.5)',
        orbit: 260
      },
      {
        id: 'bump_mrr',
        label: 'Bump 3: Estúdio Blindado (Mensal / Anual)',
        category: 'ORDER BUMP 3 (RECORRÊNCIA / CAIXA IMEDIATO)',
        price: 'R$ 112,50/mês OU R$ 997/ano (12x R$ 99)',
        desc: 'Hospedagem turbo contínua + até 2 rodadas mensais de atualização rápida de fotos e preços + suporte prioritário WhatsApp. Opção de pagamento anual com 2 meses grátis.',
        function: 'Constrói a esteira de R$ 2.250,00/mês previsível (mensal) OU injeta R$ 997,00 à vista por cliente no plano anual (com 3 anuais = ~R$ 3.000 no bolso hoje).',
        rules: '• Mensal: R$ 112,50/mês recorrente.<br>• Anual VIP: De R$ 1.350 por R$ 997 à vista (ou 12x de R$ 99,70).<br>• Zero risco de cancelamento no anual e caixa imediato na sua conta.',
        x: 180,
        y: 200,
        radius: 26,
        color: '#F59E0B',
        glowColor: 'rgba(245, 158, 11, 0.6)',
        orbit: 270
      },

      // Orbit 4: Upsell Pós-Compra (Estilo Laschuk)
      {
        id: 'upsell_call',
        label: 'Call VIP Co-criação 1-a-1',
        category: 'UPSELL ONE-CLICK (ESTILO LASCHUK)',
        price: 'R$ 197,00 na Página de Obrigado',
        desc: '1 hora ao vivo no Google Meet com o Thiago personalizando a página, ajustando a copy e ensinando a usar o link nos stories.',
        function: 'Gera R$ 200 de lucro imediato por hora técnica sem custo de aquisição adicional.',
        rules: '• Disparado instantaneamente após a aprovação da compra.<br>• Horários pré-travados na agenda via Calendly/Google Calendar.',
        x: 20,
        y: 260,
        radius: 22,
        color: '#A855F7',
        glowColor: 'rgba(168, 85, 247, 0.6)',
        orbit: 280
      },

      // Orbit 5: Fábrica & Entrega Zero-Touch
      {
        id: 'briefing_tally',
        label: 'Briefing Inteligente Tally.so',
        category: 'OPERAÇÃO INDUSTRIAL ZERO-TOUCH',
        price: 'Zero Custo de Atendimento',
        desc: 'Formulário automatizado em 4 perguntas objetivas: Nome do Estúdio, Serviços & Preços, WhatsApp de Agendamento e Fotos.',
        function: 'Elimina conversas longas no WhatsApp. A cliente só recebe o link pronto para aprovar.',
        rules: '• 1 único envio permitido.<br>• Respostas sincronizadas diretamente no modelo React/Vite.',
        x: -160,
        y: 210,
        radius: 18,
        color: '#06B6D4',
        glowColor: 'rgba(6, 182, 212, 0.4)',
        orbit: 260
      },
      {
        id: 'lock_hourly',
        label: 'Trava de Suporte Técnico',
        category: 'REGULAMENTO OPERACIONAL',
        price: 'R$ 69,00/hora de Alteração',
        desc: 'Taxa fixa para qualquer alteração estética extra solicitada após a entrega do site aprovado.',
        function: 'Blinda o seu tempo e educa o cliente a valorizar o trabalho profissional.',
        rules: '• Cobrança antecipada via PIX para qualquer modificação avulsa fora do escopo homologado.',
        x: -250,
        y: 190,
        radius: 17,
        color: '#E11D48',
        glowColor: 'rgba(225, 29, 72, 0.4)',
        orbit: 280
      },

      // Orbit 6: Backend High Ticket (A Ponte dos R$ 2.500)
      {
        id: 'high_ticket',
        label: 'Ponte High Ticket (Clínicas VIP)',
        category: 'BACKEND CORPORATIVO',
        price: 'R$ 2.500 a R$ 5.000',
        desc: 'Chamada sutil e elegante no rodapé da página para clínicas médicas, estética avançada e centros de harmonização facial.',
        function: 'Filtra os clientes que já faturam alto e precisam de ecossistemas digitais complexos.',
        rules: '• Atendimento consultivo por agendamento executivo.<br>• Proposta Comercial Executiva TM com 50% de entrada.',
        x: -290,
        y: -190,
        radius: 20,
        color: '#FBBF24',
        glowColor: 'rgba(251, 191, 36, 0.5)',
        orbit: 310
      }
    ];

    // Constellation Connections
    const connections = [
      { from: 'ad_target', to: 'ad_hook' },
      { from: 'ad_hook', to: 'lp_entry' },
      { from: 'ad_hook', to: 'lp_pro' },
      { from: 'lp_entry', to: 'bump_domain' },
      { from: 'lp_pro', to: 'bump_domain' },
      { from: 'bump_domain', to: 'bump_express' },
      { from: 'bump_domain', to: 'bump_mrr' },
      { from: 'bump_mrr', to: 'core' },
      { from: 'bump_express', to: 'upsell_call' },
      { from: 'upsell_call', to: 'briefing_tally' },
      { from: 'briefing_tally', to: 'core' },
      { from: 'briefing_tally', to: 'lock_hourly' },
      { from: 'lp_entry', to: 'high_ticket' },
      { from: 'high_ticket', to: 'core' }
    ];

    // Background Stars Particle System
    const stars = [];
    for (let i = 0; i < 280; i++) {
      stars.push({
        x: (Math.random() - 0.5) * 2200,
        y: (Math.random() - 0.5) * 2200,
        size: Math.random() * 1.5 + 0.5,
        alpha: Math.random() * 0.8 + 0.2
      });
    }

    // Interaction State
    let hoveredNode = null;
    let selectedNode = null;

    canvas.addEventListener('mousedown', (e) => {
      isDragging = true;
      startX = e.clientX - panX;
      startY = e.clientY - panY;
    });

    window.addEventListener('mousemove', (e) => {
      if (isDragging) {
        panX = e.clientX - startX;
        panY = e.clientY - startY;
      }

      // Check hover
      const mouseWorldX = (e.clientX - panX) / zoom;
      const mouseWorldY = (e.clientY - panY) / zoom;

      hoveredNode = null;
      for (const node of nodes) {
        const dist = Math.hypot(node.x - mouseWorldX, node.y - mouseWorldY);
        if (dist <= node.radius + 8) {
          hoveredNode = node;
          break;
        }
      }
      canvas.style.cursor = hoveredNode ? 'pointer' : (isDragging ? 'grabbing' : 'grab');
    });

    window.addEventListener('mouseup', () => {
      isDragging = false;
    });

    // Zoom
    canvas.addEventListener('wheel', (e) => {
      e.preventDefault();
      const zoomFactor = e.deltaY < 0 ? 1.08 : 0.92;
      const newZoom = Math.min(Math.max(zoom * zoomFactor, 0.4), 2.2);

      panX = e.clientX - (e.clientX - panX) * (newZoom / zoom);
      panY = e.clientY - (e.clientY - panY) * (newZoom / zoom);
      zoom = newZoom;
    }, { passive: false });

    // Click
    canvas.addEventListener('click', (e) => {
      const mouseWorldX = (e.clientX - panX) / zoom;
      const mouseWorldY = (e.clientY - panY) / zoom;

      for (const node of nodes) {
        const dist = Math.hypot(node.x - mouseWorldX, node.y - mouseWorldY);
        if (dist <= node.radius + 8) {
          openDrawer(node);
          return;
        }
      }
    });

    // Drawer
    const drawer = document.getElementById('nodeDrawer');
    const drawerClose = document.getElementById('drawerClose');

    function openDrawer(node) {
      selectedNode = node;
      document.getElementById('drawerCategory').textContent = node.category;
      document.getElementById('drawerTitle').textContent = node.label;
      document.getElementById('drawerPrice').textContent = node.price;
      document.getElementById('drawerDesc').textContent = node.desc;
      document.getElementById('drawerFunction').innerHTML = node.function;
      document.getElementById('drawerRules').innerHTML = node.rules;
      drawer.classList.add('open');
    }

    drawerClose.addEventListener('click', () => {
      drawer.classList.remove('open');
      selectedNode = null;
    });

    document.getElementById('btn-reset-view').addEventListener('click', () => {
      panX = width / 2;
      panY = height / 2;
      zoom = 1;
    });

    const btnOrbits = document.getElementById('btn-toggle-orbits');
    btnOrbits.addEventListener('click', () => {
      showOrbits = !showOrbits;
      btnOrbits.classList.toggle('active', showOrbits);
    });

    const btnLinks = document.getElementById('btn-toggle-links');
    btnLinks.addEventListener('click', () => {
      showLinks = !showLinks;
      btnLinks.classList.toggle('active', showLinks);
    });

    // Render Loop
    let time = 0;
    function render() {
      time += 0.015;
      ctx.clearRect(0, 0, width, height);

      ctx.save();
      ctx.translate(panX, panY);
      ctx.scale(zoom, zoom);

      // 1. Nebula Center Glow
      const grad = ctx.createRadialGradient(0, 0, 30, 0, 0, 480);
      grad.addColorStop(0, 'rgba(217, 101, 38, 0.12)');
      grad.addColorStop(0.35, 'rgba(56, 189, 248, 0.05)');
      grad.addColorStop(1, 'rgba(5, 7, 13, 0)');
      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.arc(0, 0, 480, 0, Math.PI * 2);
      ctx.fill();

      // 2. Stars
      stars.forEach(s => {
        const pulse = Math.sin(time * 2.5 + s.x) * 0.25 + 0.75;
        ctx.fillStyle = `rgba(255, 255, 255, ${s.alpha * pulse})`;
        ctx.beginPath();
        ctx.arc(s.x, s.y, s.size, 0, Math.PI * 2);
        ctx.fill();
      });

      // 3. Orbits
      if (showOrbits) {
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
        ctx.lineWidth = 1;
        [250, 260, 280, 310].forEach(r => {
          ctx.beginPath();
          ctx.arc(0, 0, r, 0, Math.PI * 2);
          ctx.stroke();
        });
      }

      // 4. Connections (Constellations)
      if (showLinks) {
        connections.forEach(conn => {
          const fromNode = nodes.find(n => n.id === conn.from);
          const toNode = nodes.find(n => n.id === conn.to);
          if (!fromNode || !toNode) return;

          const isHighlight = (hoveredNode && (hoveredNode.id === fromNode.id || hoveredNode.id === toNode.id)) ||
                              (selectedNode && (selectedNode.id === fromNode.id || selectedNode.id === toNode.id));

          ctx.strokeStyle = isHighlight ? 'rgba(56, 189, 248, 0.85)' : 'rgba(255, 255, 255, 0.14)';
          ctx.lineWidth = isHighlight ? 2.5 : 1;
          ctx.setLineDash(isHighlight ? [] : [4, 4]);

          ctx.beginPath();
          ctx.moveTo(fromNode.x, fromNode.y);
          ctx.lineTo(toNode.x, toNode.y);
          ctx.stroke();
          ctx.setLineDash([]);

          // Animated flow particle
          const flowT = (time * 0.35 + (Math.abs(fromNode.x) * 0.01)) % 1;
          const px = fromNode.x + (toNode.x - fromNode.x) * flowT;
          const py = fromNode.y + (toNode.y - fromNode.y) * flowT;

          ctx.fillStyle = isHighlight ? '#38BDF8' : 'rgba(255, 255, 255, 0.6)';
          ctx.beginPath();
          ctx.arc(px, py, isHighlight ? 3.5 : 2, 0, Math.PI * 2);
          ctx.fill();
        });
      }

      // 5. Draw Planetary Nodes
      nodes.forEach(node => {
        const isHovered = hoveredNode && hoveredNode.id === node.id;
        const isSelected = selectedNode && selectedNode.id === node.id;

        ctx.save();
        const pulse = Math.sin(time * 2 + node.x) * 0.15 + 0.85;
        const glowRadius = (node.radius + (isHovered || isSelected ? 18 : 10)) * pulse;
        const glowGrad = ctx.createRadialGradient(node.x, node.y, node.radius * 0.4, node.x, node.y, glowRadius);
        glowGrad.addColorStop(0, node.glowColor);
        glowGrad.addColorStop(1, 'rgba(0,0,0,0)');
        ctx.fillStyle = glowGrad;
        ctx.beginPath();
        ctx.arc(node.x, node.y, glowRadius, 0, Math.PI * 2);
        ctx.fill();

        // Solid Body
        ctx.fillStyle = node.color;
        ctx.beginPath();
        ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
        ctx.fill();

        // Border ring
        ctx.strokeStyle = isSelected ? '#FFFFFF' : (isHovered ? '#38BDF8' : 'rgba(255, 255, 255, 0.35)');
        ctx.lineWidth = isSelected || isHovered ? 2.5 : 1.5;
        ctx.stroke();

        // Center Dot
        ctx.fillStyle = '#FFFFFF';
        ctx.beginPath();
        ctx.arc(node.x, node.y, 3, 0, Math.PI * 2);
        ctx.fill();

        // Label
        ctx.font = `${isHovered || isSelected ? 'bold 12px' : '600 11px'} 'Plus Jakarta Sans', sans-serif`;
        ctx.fillStyle = isHovered || isSelected ? '#FFFFFF' : '#CBD5E1';
        ctx.textAlign = 'center';
        ctx.fillText(node.label, node.x, node.y + node.radius + 18);

        // Price badge
        ctx.font = "500 10px 'JetBrains Mono', monospace";
        ctx.fillStyle = node.id === 'core' ? '#D96526' : (node.id === 'bump_mrr' ? '#F59E0B' : '#10B981');
        const shortPrice = node.price.split(' ')[0] + (node.price.includes('/mês') ? '/mês' : '');
        ctx.fillText(shortPrice, node.x, node.y + node.radius + 32);

        ctx.restore();
      });

      ctx.restore();
      requestAnimationFrame(render);
    }

    render();
  