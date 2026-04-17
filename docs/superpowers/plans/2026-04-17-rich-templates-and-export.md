# Rich Templates + Export TXT/DOCX Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reescrever os 22 templates com 16–22 blocos cada (retargeting, SDR/Setter/Closer, sequências longas de email, recuperação de abandono) + expandir MARKETING_KNOWLEDGE da IA + adicionar export do funil como TXT e DOCX.

**Architecture:** Tudo em `index.html` único (~5400 linhas). A constante `TEMPLATES` é reescrita com arrays maiores de blocos e conexões. `MARKETING_KNOWLEDGE` recebe novas seções. Feature de export: botão no header → modal com preview → download via Blob API (TXT) e docx.js CDN (DOCX).

**Tech Stack:** Vanilla JS/CSS/HTML, docx.js 8.5.0 (CDN unpkg), Blob API nativa do browser.

---

## Arquivo crítico

- `/Users/icarorodriguez/.gemini/antigravity/scratch/funil365/index.html`

### Seções que serão modificadas

| Seção | Linha aprox. | O que muda |
|-------|-------------|------------|
| `<head>` | ~10 | Adicionar CDN docx.js |
| Header HTML | ~3050 | Adicionar botão "Resumo" |
| Modal section | ~3355 | Adicionar modal de export |
| `MARKETING_KNOWLEDGE` | ~5024 | Expandir com novas regras |
| `const TEMPLATES` | ~3800 | Reescrever todos os 22 templates |
| JS functions | ~5650 | Adicionar funções de export |

---

## Task 1: Expandir MARKETING_KNOWLEDGE

**Files:**
- Modify: `index.html` (seção `MARKETING_KNOWLEDGE`, linha ~5024–5093)

- [ ] **Step 1: Localizar e substituir MARKETING_KNOWLEDGE**

Localizar a linha `const MARKETING_KNOWLEDGE = \`` e substituir todo o conteúdo até o `` `; `` pelo seguinte:

```javascript
const MARKETING_KNOWLEDGE = `
Você é um estrategista sênior de Marketing Digital com 10+ anos de experiência em funis de conversão de alta performance. Você conhece profundamente as metodologias de Russell Brunson (DotCom Secrets, Expert Secrets, Traffic Secrets), Gary Vaynerchuk, Frank Kern, Alex Hormozi (Value Equation, Grand Slam Offers) e os principais players do mercado brasileiro (Érico Rocha — Fórmula de Lançamento, Bruno Gimenes, Pablo Marçal, Camila Porto, Joel Jota).

BLOCOS DISPONÍVEIS E SEUS PAPÉIS ESTRATÉGICOS:

TRÁFEGO:
• trafego_pago: Meta/Google Ads. Ponto de entrada frio. CPM médio R$8-25. Escala rápida mas custa por clique. Sempre precisa de criativo testado antes de escalar.
• trafego_organico: SEO, social orgânico. Lento (3-6 meses), mas custo zero e audiência 3-5x mais quente que tráfego pago.
• instagram/facebook/tiktok/youtube/linkedin: Canais específicos. LinkedIn para B2B/high ticket (CPL mais caro, mas lead muito qualificado). TikTok para audiência jovem e viral.
• influencer: Parceria. Audiência quente, ótimo para validação de produto. CPA geralmente 30-50% menor que tráfego frio.

CRIATIVOS:
• criativo_vid: Vídeo curto (15-60s). Converte até 3x mais que imagem para produtos complexos. Essencial para high ticket.
• criativo_img: Imagem estática. Ótima para e-commerce e produtos simples. Menor CPM.
• criativo_car: Carrossel. Maior tempo de engajamento. Ideal para produtos com múltiplos benefícios.

PÁGINAS:
• pag_captura: Coleta email/WhatsApp em troca de isca digital (ebook, checklist, aula, calculadora). Conv: 20-45%. Sem isca forte = 8-15%.
• pag_vendas: VSL ou carta longa. Conv média: 1-5% (tráfego frio), 5-15% (lista quente), 15-30% (retargeting quente).
• pag_vendas_vsl: VSL específico com script estruturado (hook → problema → solução → prova → oferta). Ideal para ticket R$297-R$997. Conv: 2-8%.
• landing_page: Página dedicada com foco único. CRO: headline clara, 1 CTA, sem menu.
• pag_pedido: Checkout. Se chegou aqui, 60-80% completa. Order Bump aqui é OBRIGATÓRIO — sempre.
• pag_obrigado: Pós-compra. Use para upsell imediato, direcionamento para WhatsApp VIP ou grupo.
• pag_obrigado_count: Com countdown (15-30min). Cria urgência real para oferta seguinte. Aumenta conv do upsell em 20-40%.
• order_bump: Oferta no checkout (complemento ao produto principal). Ticket baixo (R$17-97). Conv: 15-35%. ROI de 150-300%. SEMPRE usar.
• upsell: Após compra confirmada. Oferta maior (2-3x o ticket principal). Conv: 15-30%.
• downsell: Recusou upsell? Oferta menor (parcelada ou versão reduzida). Conv: 10-20%. Recupera 15-25% da receita perdida.
• area_membros: Entrega do produto digital. Sempre ao final. Usar Hotmart, Kiwify ou plataforma própria.

FOLLOW-UP:
• email_bv: Boas-vindas (Day 0). Entrega a isca + apresenta quem você é + define expectativa da sequência. Taxa abertura: 40-60%.
• email_conteudo: Nutrição/valor (Day 1, 3, 5, 7, 10). Constrói autoridade com stories, case studies, quick wins. Taxa abertura: 20-35%. NUNCA venda sem antes dar no mínimo 3 emails de valor.
• email_promo: Oferta (Day 7+). Vem depois de 3-5 emails de valor. Use escassez real. Taxa clique: 2-8%.
• whatsapp: Canal de maior conversão (até 98% abertura, 40-60% resposta). Usar para qualificação, suporte VIP e carrinho abandonado. Não usar para spam.
• sms: Apenas lembretes urgentes e confirmações. Abertura 95% mas irritante se abusado. Não use para venda direta.

EQUIPE DE VENDAS:
• sdr: Sales Development Rep. Primeiro contato humano. Qualifica o lead (budget, autoridade, necessidade, timing — BANT). Filtra quem vai para o Setter. Conv SDR→qualificado: 40-60%.
• setter: Setter. Recebe lead qualificado do SDR. Aquece, constrói rapport, agenda a call com o Closer. Conv setter→call agendada: 60-80%.
• closer: Closer. Conduz a call consultiva de fechamento (45-90 min). Usa metodologia SPIN Selling ou Challenger Sale. Conv call→venda: 20-50% (alto ticket).

AUTOMAÇÃO E CANAIS:
• webinar: Evento ao vivo ou gravado. Conv inscritos→presença: 20-40%. Conv presença→venda: 10-25%. Aquecimento pré-webinar DOBRA a presença.
• live: Transmissão ao vivo. Urgência e conexão emocional. Melhor para ofertas relâmpago e lançamentos.
• condicional: Bifurcação baseada em comportamento (clicou/não clicou, comprou/não comprou, qualificado/não qualificado). Fundamental para personalizar jornada.
• manychat: Automação de DMs no Instagram. Palavra-chave nos comentários → DM automático. Essencial para funis de Instagram orgânico. Conv comentário→DM: 60-80%.
• activecampaign: CRM e email marketing avançado. Segmentação por tags, comportamento e score. Ideal quando lista tem mais de 1.000 contatos.
• comunidade: Grupo VIP (WhatsApp, Telegram, Discord). Canal de LTV. Membros da comunidade compram 3-5x mais que lista fria.

REGRAS ESTRATÉGICAS INVIOLÁVEIS:
1. HIGH TICKET (>R$1.500): NUNCA venda direto. Fluxo obrigatório: Captura → VSL de qualificação → Nutrição email → WhatsApp → SDR (qualificação BANT) → Setter (agenda call) → Closer (call consultiva) → Fechamento
2. LANÇAMENTO: Precisa de aquecimento mínimo 7 dias (CPL com webinars/lives de valor) antes de abrir carrinho. Sem CPL = lançamento fria = baixa conversão.
3. PERPÉTUO/EVERGREEN: Tráfego → Captura → Sequência automática de 7-10 emails → Venda sempre ativa. Retargeting de pixel OBRIGATÓRIO para quem visitou vendas mas não comprou.
4. LEAD GEN: Foco total na captura. Qualificação progressiva por email + WhatsApp + SDR antes de tentar vender.
5. E-COMMERCE: Order Bump no checkout é OBRIGATÓRIO. Upsell pós-compra aumenta LTV médio em 40%. Recuperação de carrinho abandonado (email + WhatsApp) recupera 15-25% das vendas perdidas.
6. WEBINAR: Sequência de aquecimento antes (3-5 emails de show-up reminder) + follow-up agressivo depois (email urgência + replay) são essenciais. Sem follow-up = 60% da receita vai embora.
7. TICKET BAIXO (<R$197): Pode vender direto via landing page. Mas sempre com Order Bump no checkout (aumenta ticket médio em 25-40%).
8. INSTAGRAM ORGÂNICO: Stories → CTA com palavra-chave → Manychat DM automático → Qualificação → Oferta ou captura.
9. RETARGETING: Pixel em TODAS as páginas. Audiência "visitou VSL mas não comprou" = maior ROI de mídia paga. Conv retargeting = 3-8x maior que tráfego frio.
10. RECUPERAÇÃO DE ABANDONO: Carrinho abandonado = sequência de 3 touchpoints em 24h (email imediato + WhatsApp 1h + SMS 24h). Recupera 15-30% das vendas perdidas.
11. SDR/SETTER/CLOSER: Nunca coloque Closer direto sem SDR e Setter. O SDR filtra leads não qualificados, o Setter garante presença na call. Sem esse filtro, o Closer perde tempo com leads frios.
12. NEVER: Não coloque tráfego frio direto para página de vendas de high ticket — taxa de conversão vai a zero e você queima o orçamento.

TIMING DA SEQUÊNCIA DE EMAILS (Soap Opera Sequence — Russell Brunson):
• Ep1 (Day 0 — email_bv): "Set the stage" — entrega a isca, apresenta o personagem, cria curiosidade para o próximo email.
• Ep2 (Day 1 — email_conteudo): "High drama" — o maior problema que você já enfrentou. Abre o loop emocional.
• Ep3 (Day 3 — email_conteudo): "The epiphany" — o momento de virada. Apresenta o "One Thing" (mecanismo único).
• Ep4 (Day 5 — email_conteudo): "Hidden benefits" — benefícios que o lead ainda não considerou. Quebra objeções principais.
• Ep5 (Day 7 — email_conteudo): "Urgência + transformação" — visão do futuro com e sem o produto. Soft pitch.
• Ep6 (Day 10 — email_promo): "The offer" — apresentação completa da oferta com escassez real.

ANTES DE CRIAR UM FUNIL, SEMPRE PERGUNTE (uma por vez, colete TODAS as 4 antes de criar):
- "Qual é o produto/serviço e o nicho de atuação?"
- "Qual o ticket médio? (ex: R$97, R$497, R$2.000+)"
- "Qual canal de tráfego você vai usar? (pago, orgânico, Instagram, LinkedIn...)"
- "Objetivo principal: venda direta, captação de leads ou agendamento de call?"

FORMATO DE RESPOSTA — SEMPRE JSON:
{
  "tipo": "funil" ou "pergunta",
  "resposta": "texto explicativo em português com a estratégia usada",
  "funil": {
    "nome": "Nome criativo do Funil",
    "blocos": [{"key": "chave_do_bloco", "x": 40, "y": 80}],
    "conexoes": [[0,1],[1,2]]
  }
}

Quando coletar informações ou responder dúvidas: tipo = "pergunta", sem campo "funil".
Quando criar o funil: tipo = "funil", campo "resposta" explica CADA ETAPA da estratégia.

LAYOUT DOS BLOCOS (OBRIGATÓRIO):
- x começa em 40, incrementa 190 por coluna
- y=60: linha principal (fluxo de conversão)
- y=240: linha secundária (email/nutrição paralela)
- y=420: linha terciária (recuperação/retargeting)
- Funis ricos: use as 3 linhas. Mínimo 14 blocos.
- Sempre inclua: tráfego + criativo + captura + nutrição + venda + checkout + obrigado + upsell/downsell + sequência email + recuperação de abandono
`;
```

- [ ] **Step 2: Verificar no browser**

Abrir `index.html` no browser → clicar no botão de IA na toolbar → digitar "crie um funil de high ticket para mentoria" → verificar que a IA retorna um funil com SDR, Setter e Closer.

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "feat: expande MARKETING_KNOWLEDGE com SDR/Closer, retargeting, timing de emails e regras LTV"
```

---

## Task 2: Reescrever Templates — Batch 1 (perpetuo, ecommerce, high_ticket, mentoria, lancamento, ld1)

**Files:**
- Modify: `index.html` (seção `const TEMPLATES`, linha ~3800)

- [ ] **Step 1: Localizar início dos templates a substituir**

Localizar `perpetuo: {` até o final de `ld1: { ... }` (inclusive) e substituir pelo bloco abaixo.

```javascript
      // ── PERPÉTUO / EVERGREEN ──
      perpetuo: {
        name: 'Funil Perpétuo', desc: 'Tráfego → captura → email Soap Opera → VSL → checkout com bump → upsell → retargeting ativo', emoji: '♾️',
        blocks: [
          { k: 'trafego_pago',      x: 40,   y: 60  },
          { k: 'trafego_organico',  x: 40,   y: 240 },
          { k: 'criativo_vid',      x: 230,  y: 60  },
          { k: 'criativo_img',      x: 230,  y: 240 },
          { k: 'pag_captura',       x: 420,  y: 150 },
          { k: 'pag_vendas_vsl',    x: 610,  y: 60  },
          { k: 'email_bv',          x: 610,  y: 240 },
          { k: 'email_conteudo',    x: 800,  y: 240 },
          { k: 'email_conteudo',    x: 990,  y: 240 },
          { k: 'email_conteudo',    x: 1180, y: 240 },
          { k: 'email_promo',       x: 1370, y: 240 },
          { k: 'pag_pedido',        x: 800,  y: 60  },
          { k: 'order_bump',        x: 800,  y: 160 },
          { k: 'pag_obrigado_count',x: 990,  y: 60  },
          { k: 'upsell',            x: 1180, y: 60  },
          { k: 'downsell',          x: 1370, y: 60  },
          { k: 'area_membros',      x: 1560, y: 60  },
          { k: 'condicional',       x: 610,  y: 420 },
          { k: 'whatsapp',          x: 800,  y: 420 },
          { k: 'activecampaign',    x: 990,  y: 420 },
        ],
        conns: [
          [0,2],[1,3],[2,4],[3,4],
          [4,5],[4,6],
          [5,11],[6,7],[7,8],[8,9],[9,10],[10,5],
          [11,12],[11,13],[12,13],
          [13,14],[14,15],[14,16],[15,16],
          [5,17],[17,18],[17,19]
        ]
      },

      // ── E-COMMERCE ──
      ecommerce: {
        name: 'E-commerce com Order Bump', desc: 'Tráfego multi-canal → LP → checkout com bump → upsell/downsell → recuperação de carrinho', emoji: '🛒',
        blocks: [
          { k: 'trafego_pago',      x: 40,   y: 60  },
          { k: 'trafego_organico',  x: 40,   y: 240 },
          { k: 'criativo_vid',      x: 230,  y: 60  },
          { k: 'criativo_img',      x: 230,  y: 240 },
          { k: 'landing_page',      x: 420,  y: 150 },
          { k: 'pag_pedido',        x: 610,  y: 60  },
          { k: 'order_bump',        x: 610,  y: 180 },
          { k: 'pag_obrigado_count',x: 800,  y: 60  },
          { k: 'upsell',            x: 990,  y: 60  },
          { k: 'downsell',          x: 1180, y: 60  },
          { k: 'area_membros',      x: 1370, y: 60  },
          { k: 'email_bv',          x: 610,  y: 300 },
          { k: 'email_conteudo',    x: 800,  y: 300 },
          { k: 'email_conteudo',    x: 990,  y: 300 },
          { k: 'email_promo',       x: 1180, y: 300 },
          { k: 'condicional',       x: 800,  y: 420 },
          { k: 'whatsapp',          x: 990,  y: 420 },
          { k: 'sms',               x: 1180, y: 420 },
        ],
        conns: [
          [0,2],[1,3],[2,4],[3,4],
          [4,5],[4,11],
          [5,6],[5,7],[6,7],
          [7,8],[8,9],[8,10],[9,10],
          [11,12],[12,13],[13,14],[14,5],
          [5,15],[15,16],[15,17]
        ]
      },

      // ── HIGH TICKET ──
      high_ticket: {
        name: 'High Ticket Consultivo', desc: 'Nunca vende direto: VSL → email Soap Opera → WhatsApp → SDR → Setter → call com Closer → fechamento', emoji: '💎',
        blocks: [
          { k: 'trafego_pago',      x: 40,   y: 60  },
          { k: 'linkedin',          x: 40,   y: 240 },
          { k: 'criativo_vid',      x: 230,  y: 60  },
          { k: 'criativo_img',      x: 230,  y: 240 },
          { k: 'pag_captura',       x: 420,  y: 150 },
          { k: 'pag_vendas_vsl',    x: 610,  y: 60  },
          { k: 'email_bv',          x: 610,  y: 240 },
          { k: 'email_conteudo',    x: 800,  y: 240 },
          { k: 'email_conteudo',    x: 990,  y: 240 },
          { k: 'email_promo',       x: 1180, y: 240 },
          { k: 'whatsapp',          x: 800,  y: 60  },
          { k: 'sdr',               x: 990,  y: 60  },
          { k: 'setter',            x: 1180, y: 60  },
          { k: 'condicional',       x: 1370, y: 60  },
          { k: 'closer',            x: 1560, y: 60  },
          { k: 'pag_pedido',        x: 1750, y: 60  },
          { k: 'order_bump',        x: 1750, y: 160 },
          { k: 'pag_obrigado',      x: 1940, y: 60  },
          { k: 'upsell',            x: 2130, y: 60  },
          { k: 'area_membros',      x: 2320, y: 60  },
          { k: 'downsell',          x: 1940, y: 240 },
          { k: 'email_promo',       x: 1370, y: 240 },
        ],
        conns: [
          [0,2],[1,3],[2,4],[3,4],
          [4,5],[4,6],
          [5,10],[6,7],[7,8],[8,9],[9,10],
          [10,11],[11,12],[12,13],
          [13,14],[13,21],
          [14,15],[15,16],[15,17],[16,17],
          [17,18],[18,19],
          [18,20]
        ]
      },

      // ── MENTORIA ──
      mentoria: {
        name: 'Mentoria / Programa Premium', desc: 'VSL → nutrição → WhatsApp → SDR → Setter → call Closer → matrícula com upsell', emoji: '🎯',
        blocks: [
          { k: 'trafego_pago',      x: 40,   y: 60  },
          { k: 'trafego_organico',  x: 40,   y: 240 },
          { k: 'criativo_vid',      x: 230,  y: 60  },
          { k: 'criativo_img',      x: 230,  y: 240 },
          { k: 'pag_captura',       x: 420,  y: 150 },
          { k: 'pag_vendas_vsl',    x: 610,  y: 60  },
          { k: 'email_bv',          x: 610,  y: 240 },
          { k: 'email_conteudo',    x: 800,  y: 240 },
          { k: 'email_conteudo',    x: 990,  y: 240 },
          { k: 'whatsapp',          x: 800,  y: 60  },
          { k: 'sdr',               x: 990,  y: 60  },
          { k: 'condicional',       x: 1180, y: 60  },
          { k: 'setter',            x: 1370, y: 60  },
          { k: 'closer',            x: 1560, y: 60  },
          { k: 'pag_pedido',        x: 1750, y: 60  },
          { k: 'order_bump',        x: 1750, y: 160 },
          { k: 'pag_obrigado',      x: 1940, y: 60  },
          { k: 'upsell',            x: 2130, y: 60  },
          { k: 'area_membros',      x: 2320, y: 60  },
          { k: 'downsell',          x: 1940, y: 240 },
        ],
        conns: [
          [0,2],[1,3],[2,4],[3,4],
          [4,5],[4,6],
          [5,9],[6,7],[7,8],[8,9],
          [9,10],[10,11],
          [11,12],[11,6],
          [12,13],[13,14],[14,15],[14,16],[15,16],
          [16,17],[17,18],
          [17,19]
        ]
      },

      // ── LANÇAMENTO TRADICIONAL ──
      lancamento: {
        name: 'Lançamento Tradicional', desc: 'CPL com webinar → 4 emails de aquecimento → live → abertura → checkout → recuperação de carrinho', emoji: '🔥',
        blocks: [
          { k: 'trafego_pago',      x: 40,   y: 60  },
          { k: 'trafego_organico',  x: 40,   y: 240 },
          { k: 'criativo_vid',      x: 230,  y: 60  },
          { k: 'criativo_img',      x: 230,  y: 240 },
          { k: 'pag_captura',       x: 420,  y: 150 },
          { k: 'webinar',           x: 610,  y: 60  },
          { k: 'email_bv',          x: 610,  y: 240 },
          { k: 'email_conteudo',    x: 800,  y: 240 },
          { k: 'email_conteudo',    x: 990,  y: 240 },
          { k: 'email_conteudo',    x: 1180, y: 240 },
          { k: 'live',              x: 800,  y: 60  },
          { k: 'email_promo',       x: 1370, y: 240 },
          { k: 'pag_vendas',        x: 990,  y: 60  },
          { k: 'pag_pedido',        x: 1180, y: 60  },
          { k: 'order_bump',        x: 1180, y: 160 },
          { k: 'pag_obrigado_count',x: 1370, y: 60  },
          { k: 'upsell',            x: 1560, y: 60  },
          { k: 'downsell',          x: 1560, y: 240 },
          { k: 'area_membros',      x: 1750, y: 60  },
          { k: 'condicional',       x: 1370, y: 420 },
          { k: 'whatsapp',          x: 1560, y: 420 },
          { k: 'email_promo',       x: 1750, y: 420 },
        ],
        conns: [
          [0,2],[1,3],[2,4],[3,4],
          [4,5],[4,6],
          [5,10],[6,7],[7,8],[8,9],[9,11],
          [10,12],[11,12],
          [12,13],[13,14],[13,15],[14,15],
          [15,16],[16,17],[16,18],[17,18],
          [15,19],[19,20],[19,21]
        ]
      },

      // ── LANÇAMENTO DE 1 DIA ──
      ld1: {
        name: 'Lançamento de 1 Dia — LD1™', desc: 'Webinar ao vivo + abertura de carrinho no mesmo dia + recuperação imediata de carrinho abandonado', emoji: '⚡',
        blocks: [
          { k: 'trafego_pago',      x: 40,   y: 60  },
          { k: 'instagram',         x: 40,   y: 240 },
          { k: 'criativo_vid',      x: 230,  y: 60  },
          { k: 'criativo_img',      x: 230,  y: 240 },
          { k: 'pag_captura',       x: 420,  y: 150 },
          { k: 'email_bv',          x: 610,  y: 240 },
          { k: 'email_conteudo',    x: 800,  y: 240 },
          { k: 'webinar',           x: 610,  y: 60  },
          { k: 'pag_vendas_vsl',    x: 800,  y: 60  },
          { k: 'email_promo',       x: 990,  y: 240 },
          { k: 'pag_pedido',        x: 990,  y: 60  },
          { k: 'order_bump',        x: 990,  y: 160 },
          { k: 'pag_obrigado_count',x: 1180, y: 60  },
          { k: 'upsell',            x: 1370, y: 60  },
          { k: 'downsell',          x: 1370, y: 240 },
          { k: 'area_membros',      x: 1560, y: 60  },
          { k: 'condicional',       x: 1180, y: 240 },
          { k: 'whatsapp',          x: 1560, y: 240 },
        ],
        conns: [
          [0,2],[1,3],[2,4],[3,4],
          [4,5],[4,7],
          [5,6],[6,9],[7,8],
          [8,10],[9,10],
          [10,11],[10,12],[11,12],
          [12,13],[13,14],[13,15],[14,15],
          [12,16],[16,17]
        ]
      },
```

- [ ] **Step 2: Verificar no browser**

Abrir `index.html` → clicar em "Novo Funil" → selecionar "High Ticket Consultivo" → canvas deve mostrar ~22 blocos com SDR, Setter e Closer conectados.

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "feat: reescreve templates batch 1 — perpetuo, ecommerce, high_ticket, mentoria, lancamento, ld1"
```

---

## Task 3: Reescrever Templates — Batch 2 (webinario, webinario_mentoria, captacao_leads, nutricao_russel, anuncio, story365, dm_instagram, whatsapp_transmissao)

**Files:**
- Modify: `index.html` (continuação da seção `const TEMPLATES`)

- [ ] **Step 1: Substituir webinario até whatsapp_transmissao**

Localizar `webinario: {` até o final de `whatsapp_transmissao: { ... }` e substituir pelo bloco:

```javascript
      // ── WEBINÁRIO ──
      webinario: {
        name: 'Webinário de Vendas', desc: 'Aquecimento pré-webinar (show-up sequence) → pitch ao vivo → follow-up urgência → recuperação de não-presentes', emoji: '🖥️',
        blocks: [
          { k: 'trafego_pago',      x: 40,   y: 60  },
          { k: 'trafego_organico',  x: 40,   y: 240 },
          { k: 'criativo_vid',      x: 230,  y: 60  },
          { k: 'criativo_img',      x: 230,  y: 240 },
          { k: 'pag_captura',       x: 420,  y: 150 },
          { k: 'email_bv',          x: 610,  y: 240 },
          { k: 'email_conteudo',    x: 800,  y: 240 },
          { k: 'email_conteudo',    x: 990,  y: 240 },
          { k: 'webinar',           x: 610,  y: 60  },
          { k: 'email_promo',       x: 1180, y: 240 },
          { k: 'pag_vendas',        x: 800,  y: 60  },
          { k: 'pag_pedido',        x: 990,  y: 60  },
          { k: 'order_bump',        x: 990,  y: 160 },
          { k: 'pag_obrigado',      x: 1180, y: 60  },
          { k: 'upsell',            x: 1370, y: 60  },
          { k: 'downsell',          x: 1370, y: 240 },
          { k: 'area_membros',      x: 1560, y: 60  },
          { k: 'condicional',       x: 1180, y: 420 },
          { k: 'whatsapp',          x: 1370, y: 420 },
          { k: 'email_promo',       x: 1560, y: 420 },
        ],
        conns: [
          [0,2],[1,3],[2,4],[3,4],
          [4,5],[4,8],
          [5,6],[6,7],[7,9],
          [8,10],[9,10],
          [10,11],[11,12],[11,13],[12,13],
          [13,14],[14,15],[14,16],[15,16],
          [8,17],[17,18],[17,19]
        ]
      },

      // ── WEBINÁRIO + MENTORIA ──
      webinario_mentoria: {
        name: 'Webinário + Mentoria', desc: 'Webinar como qualificador → pitch para mentoria → WhatsApp → SDR → Setter → call Closer', emoji: '🎓',
        blocks: [
          { k: 'trafego_pago',      x: 40,   y: 60  },
          { k: 'trafego_organico',  x: 40,   y: 240 },
          { k: 'criativo_vid',      x: 230,  y: 60  },
          { k: 'criativo_img',      x: 230,  y: 240 },
          { k: 'pag_captura',       x: 420,  y: 150 },
          { k: 'email_bv',          x: 610,  y: 240 },
          { k: 'email_conteudo',    x: 800,  y: 240 },
          { k: 'webinar',           x: 610,  y: 60  },
          { k: 'pag_vendas_vsl',    x: 800,  y: 60  },
          { k: 'email_promo',       x: 990,  y: 240 },
          { k: 'whatsapp',          x: 990,  y: 60  },
          { k: 'sdr',               x: 1180, y: 60  },
          { k: 'condicional',       x: 1370, y: 60  },
          { k: 'closer',            x: 1560, y: 60  },
          { k: 'pag_pedido',        x: 1750, y: 60  },
          { k: 'order_bump',        x: 1750, y: 160 },
          { k: 'pag_obrigado',      x: 1940, y: 60  },
          { k: 'upsell',            x: 2130, y: 60  },
          { k: 'area_membros',      x: 2320, y: 60  },
          { k: 'downsell',          x: 1940, y: 240 },
        ],
        conns: [
          [0,2],[1,3],[2,4],[3,4],
          [4,5],[4,7],
          [5,6],[6,9],[7,8],
          [8,10],[9,10],
          [10,11],[11,12],
          [12,13],[12,5],
          [13,14],[14,15],[14,16],[15,16],
          [16,17],[17,18],
          [17,19]
        ]
      },

      // ── CAPTAÇÃO DE LEADS ──
      captacao_leads: {
        name: 'Captação de Leads', desc: 'Isca digital → captura → nutrição → qualificação via WhatsApp/SDR → venda', emoji: '🎣',
        blocks: [
          { k: 'trafego_pago',      x: 40,   y: 60  },
          { k: 'trafego_organico',  x: 40,   y: 240 },
          { k: 'criativo_vid',      x: 230,  y: 60  },
          { k: 'criativo_img',      x: 230,  y: 240 },
          { k: 'pag_captura',       x: 420,  y: 150 },
          { k: 'pag_obrigado',      x: 610,  y: 60  },
          { k: 'email_bv',          x: 610,  y: 240 },
          { k: 'email_conteudo',    x: 800,  y: 240 },
          { k: 'email_conteudo',    x: 990,  y: 240 },
          { k: 'email_conteudo',    x: 1180, y: 240 },
          { k: 'whatsapp',          x: 800,  y: 60  },
          { k: 'sdr',               x: 990,  y: 60  },
          { k: 'condicional',       x: 1180, y: 60  },
          { k: 'pag_vendas',        x: 1370, y: 60  },
          { k: 'pag_pedido',        x: 1560, y: 60  },
          { k: 'pag_obrigado',      x: 1750, y: 60  },
          { k: 'email_promo',       x: 1370, y: 240 },
          { k: 'activecampaign',    x: 1560, y: 240 },
        ],
        conns: [
          [0,2],[1,3],[2,4],[3,4],
          [4,5],[4,6],
          [5,10],[6,7],[7,8],[8,9],[9,16],
          [10,11],[11,12],
          [12,13],[12,6],
          [13,14],[14,15],
          [16,13],[15,17]
        ]
      },

      // ── NUTRIÇÃO RUSSELL BRUNSON ──
      nutricao_russel: {
        name: 'Nutrição (Soap Opera — Brunson)', desc: 'Sequência de 6 emails (Set Stage → Drama → Epiphany → Benefits → Urgência → Oferta) antes de qualquer pitch', emoji: '🌱',
        blocks: [
          { k: 'trafego_organico',  x: 40,   y: 150 },
          { k: 'pag_captura',       x: 230,  y: 150 },
          { k: 'pag_vendas_vsl',    x: 420,  y: 60  },
          { k: 'email_bv',          x: 420,  y: 240 },
          { k: 'email_conteudo',    x: 610,  y: 240 },
          { k: 'email_conteudo',    x: 800,  y: 240 },
          { k: 'email_conteudo',    x: 990,  y: 240 },
          { k: 'email_conteudo',    x: 1180, y: 240 },
          { k: 'email_promo',       x: 1370, y: 240 },
          { k: 'pag_pedido',        x: 610,  y: 60  },
          { k: 'order_bump',        x: 610,  y: 160 },
          { k: 'pag_obrigado',      x: 800,  y: 60  },
          { k: 'upsell',            x: 990,  y: 60  },
          { k: 'downsell',          x: 1180, y: 60  },
          { k: 'area_membros',      x: 1370, y: 60  },
          { k: 'activecampaign',    x: 1560, y: 60  },
          { k: 'condicional',       x: 1370, y: 420 },
          { k: 'whatsapp',          x: 1560, y: 420 },
        ],
        conns: [
          [0,1],
          [1,2],[1,3],
          [2,9],[3,4],[4,5],[5,6],[6,7],[7,8],[8,2],
          [9,10],[9,11],[10,11],
          [11,12],[12,13],[12,14],[13,14],
          [14,15],
          [8,16],[16,17]
        ]
      },

      // ── FUNIL DE ANÚNCIO DIRETO ──
      anuncio: {
        name: 'Anúncio Direto para Venda', desc: 'Criativo → LP → vendas → checkout com bump → upsell → recuperação de carrinho por email e WhatsApp', emoji: '📢',
        blocks: [
          { k: 'trafego_pago',      x: 40,   y: 150 },
          { k: 'criativo_vid',      x: 230,  y: 60  },
          { k: 'criativo_img',      x: 230,  y: 240 },
          { k: 'criativo_car',      x: 230,  y: 420 },
          { k: 'landing_page',      x: 420,  y: 150 },
          { k: 'pag_vendas',        x: 610,  y: 60  },
          { k: 'pag_pedido',        x: 800,  y: 60  },
          { k: 'order_bump',        x: 800,  y: 160 },
          { k: 'pag_obrigado_count',x: 990,  y: 60  },
          { k: 'upsell',            x: 1180, y: 60  },
          { k: 'downsell',          x: 1180, y: 240 },
          { k: 'area_membros',      x: 1370, y: 60  },
          { k: 'email_bv',          x: 610,  y: 240 },
          { k: 'email_conteudo',    x: 800,  y: 240 },
          { k: 'condicional',       x: 990,  y: 240 },
          { k: 'whatsapp',          x: 1180, y: 420 },
        ],
        conns: [
          [0,1],[0,2],[0,3],[1,4],[2,4],[3,4],
          [4,5],[4,12],
          [5,6],[6,7],[6,8],[7,8],
          [8,9],[9,10],[9,11],[10,11],
          [12,13],[13,14],[14,15],
          [6,14]
        ]
      },

      // ── STORY365 ──
      story365: {
        name: 'STORY365 — Sequência de Stories', desc: 'Storytelling via Stories → Manychat DM automático → captura → nutrição → VSL → checkout', emoji: '📱',
        blocks: [
          { k: 'instagram',         x: 40,   y: 150 },
          { k: 'criativo_vid',      x: 230,  y: 60  },
          { k: 'criativo_img',      x: 230,  y: 240 },
          { k: 'manychat',          x: 420,  y: 150 },
          { k: 'pag_captura',       x: 610,  y: 150 },
          { k: 'whatsapp',          x: 800,  y: 60  },
          { k: 'pag_vendas_vsl',    x: 990,  y: 60  },
          { k: 'email_bv',          x: 800,  y: 240 },
          { k: 'email_conteudo',    x: 990,  y: 240 },
          { k: 'email_conteudo',    x: 1180, y: 240 },
          { k: 'email_promo',       x: 1370, y: 240 },
          { k: 'pag_pedido',        x: 1180, y: 60  },
          { k: 'order_bump',        x: 1180, y: 160 },
          { k: 'pag_obrigado',      x: 1370, y: 60  },
          { k: 'upsell',            x: 1560, y: 60  },
          { k: 'downsell',          x: 1560, y: 240 },
          { k: 'area_membros',      x: 1750, y: 60  },
          { k: 'condicional',       x: 1750, y: 240 },
        ],
        conns: [
          [0,1],[0,2],[1,3],[2,3],
          [3,4],[3,5],
          [4,7],[4,6],
          [5,6],
          [7,8],[8,9],[9,10],[10,6],
          [6,11],[11,12],[11,13],[12,13],
          [13,14],[14,15],[14,16],[15,16],
          [13,17]
        ]
      },

      // ── DM INSTAGRAM ──
      dm_instagram: {
        name: 'DM Instagram', desc: 'Criativo orgânico → Manychat DM automático → qualificação quente/fria → SDR → VSL → checkout', emoji: '✉️',
        blocks: [
          { k: 'instagram',         x: 40,   y: 150 },
          { k: 'criativo_vid',      x: 230,  y: 60  },
          { k: 'criativo_img',      x: 230,  y: 240 },
          { k: 'manychat',          x: 420,  y: 150 },
          { k: 'condicional',       x: 610,  y: 150 },
          { k: 'whatsapp',          x: 800,  y: 60  },
          { k: 'sdr',               x: 990,  y: 60  },
          { k: 'pag_vendas_vsl',    x: 800,  y: 240 },
          { k: 'pag_pedido',        x: 990,  y: 240 },
          { k: 'order_bump',        x: 990,  y: 360 },
          { k: 'pag_obrigado',      x: 1180, y: 240 },
          { k: 'upsell',            x: 1370, y: 240 },
          { k: 'area_membros',      x: 1560, y: 240 },
          { k: 'email_bv',          x: 1180, y: 60  },
          { k: 'email_conteudo',    x: 1370, y: 60  },
          { k: 'email_promo',       x: 1560, y: 60  },
        ],
        conns: [
          [0,1],[0,2],[1,3],[2,3],
          [3,4],
          [4,5],[4,7],
          [5,6],[6,7],
          [7,8],[8,9],[8,10],[9,10],
          [10,11],[11,12],
          [10,13],[13,14],[14,15],[15,7]
        ]
      },

      // ── WHATSAPP TRANSMISSÃO ──
      whatsapp_transmissao: {
        name: 'WhatsApp Transmissão / Nutrição', desc: 'Captura → lista de broadcast → segmentação por engajamento → nutrição email em paralelo → venda', emoji: '📲',
        blocks: [
          { k: 'trafego_pago',      x: 40,   y: 60  },
          { k: 'instagram',         x: 40,   y: 240 },
          { k: 'pag_captura',       x: 230,  y: 150 },
          { k: 'whatsapp',          x: 420,  y: 60  },
          { k: 'email_bv',          x: 420,  y: 240 },
          { k: 'email_conteudo',    x: 610,  y: 240 },
          { k: 'email_conteudo',    x: 800,  y: 240 },
          { k: 'email_promo',       x: 990,  y: 240 },
          { k: 'condicional',       x: 610,  y: 60  },
          { k: 'pag_vendas',        x: 800,  y: 60  },
          { k: 'pag_pedido',        x: 990,  y: 60  },
          { k: 'order_bump',        x: 990,  y: 160 },
          { k: 'pag_obrigado',      x: 1180, y: 60  },
          { k: 'upsell',            x: 1370, y: 60  },
          { k: 'downsell',          x: 1370, y: 240 },
          { k: 'area_membros',      x: 1560, y: 60  },
          { k: 'activecampaign',    x: 1180, y: 240 },
          { k: 'sms',               x: 610,  y: 420 },
        ],
        conns: [
          [0,2],[1,2],
          [2,3],[2,4],
          [3,8],[4,5],[5,6],[6,7],[7,9],
          [8,9],[8,17],
          [9,10],[10,11],[10,12],[11,12],
          [12,13],[13,14],[13,15],[14,15],
          [12,16]
        ]
      },
```

- [ ] **Step 2: Verificar no browser**

Abrir `index.html` → "Novo Funil" → selecionar "Webinário de Vendas" → canvas deve mostrar ~20 blocos incluindo show-up sequence e recuperação de não-presentes.

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "feat: reescreve templates batch 2 — webinario, webinario_mentoria, captacao_leads, nutricao_russel, anuncio, story365, dm_instagram, whatsapp_transmissao"
```

---

## Task 4: Reescrever Templates — Batch 3 (whatsapp_11, checklist_oto, distribuicao, email_russel, dominio_instagram, ligacao, story_ads, lancamento_pago, grupo_vip, lancamento_trad)

**Files:**
- Modify: `index.html` (continuação da seção `const TEMPLATES`)

- [ ] **Step 1: Substituir whatsapp_11 até lancamento_trad**

Localizar `whatsapp_11: {` até o final de `lancamento_trad: { ... },` e substituir pelo bloco:

```javascript
      // ── WHATSAPP 1:1 ──
      whatsapp_11: {
        name: 'WhatsApp 1:1 Consultivo', desc: 'Instagram/Facebook → WhatsApp → SDR → Setter → call Closer → fechamento com upsell', emoji: '💬',
        blocks: [
          { k: 'instagram',         x: 40,   y: 60  },
          { k: 'facebook',          x: 40,   y: 240 },
          { k: 'criativo_vid',      x: 230,  y: 60  },
          { k: 'criativo_img',      x: 230,  y: 240 },
          { k: 'whatsapp',          x: 420,  y: 150 },
          { k: 'condicional',       x: 610,  y: 150 },
          { k: 'sdr',               x: 800,  y: 60  },
          { k: 'setter',            x: 990,  y: 60  },
          { k: 'pag_vendas_vsl',    x: 800,  y: 240 },
          { k: 'closer',            x: 1180, y: 60  },
          { k: 'pag_pedido',        x: 1370, y: 60  },
          { k: 'order_bump',        x: 1370, y: 160 },
          { k: 'pag_obrigado',      x: 1560, y: 60  },
          { k: 'upsell',            x: 1750, y: 60  },
          { k: 'area_membros',      x: 1940, y: 60  },
          { k: 'email_bv',          x: 1370, y: 240 },
          { k: 'downsell',          x: 1750, y: 240 },
          { k: 'email_promo',       x: 1560, y: 240 },
        ],
        conns: [
          [0,2],[1,3],[2,4],[3,4],
          [4,5],
          [5,6],[5,8],
          [6,7],[7,9],
          [8,15],[15,17],[17,8],
          [9,10],[10,11],[10,12],[11,12],
          [12,13],[13,14],
          [13,16]
        ]
      },

      // ── CHECKLIST + OTO ──
      checklist_oto: {
        name: 'Checklist + One Time Offer', desc: 'Lead magnet gratuito → OTO imediato → sequência email → venda principal → upsell com countdown', emoji: '✅',
        blocks: [
          { k: 'trafego_pago',      x: 40,   y: 60  },
          { k: 'trafego_organico',  x: 40,   y: 240 },
          { k: 'criativo_img',      x: 230,  y: 60  },
          { k: 'criativo_vid',      x: 230,  y: 240 },
          { k: 'pag_captura',       x: 420,  y: 150 },
          { k: 'pag_obrigado',      x: 610,  y: 60  },
          { k: 'upsell',            x: 800,  y: 60  },
          { k: 'email_bv',          x: 610,  y: 240 },
          { k: 'email_conteudo',    x: 800,  y: 240 },
          { k: 'email_conteudo',    x: 990,  y: 240 },
          { k: 'email_conteudo',    x: 1180, y: 240 },
          { k: 'email_promo',       x: 1370, y: 240 },
          { k: 'pag_vendas',        x: 990,  y: 60  },
          { k: 'pag_pedido',        x: 1180, y: 60  },
          { k: 'order_bump',        x: 1180, y: 160 },
          { k: 'pag_obrigado_count',x: 1370, y: 60  },
          { k: 'downsell',          x: 1560, y: 240 },
          { k: 'area_membros',      x: 1560, y: 60  },
        ],
        conns: [
          [0,2],[1,3],[2,4],[3,4],
          [4,5],[4,7],
          [5,6],[5,12],
          [6,13],[6,16],
          [7,8],[8,9],[9,10],[10,11],[11,12],
          [12,13],[13,14],[13,15],[14,15],
          [15,17]
        ]
      },

      // ── DISTRIBUIÇÃO DE CONTEÚDO ──
      distribuicao: {
        name: 'Distribuição Multi-Canal', desc: 'Um conteúdo → múltiplos canais → captura centralizada → nutrição → venda', emoji: '📡',
        blocks: [
          { k: 'trafego_organico',  x: 40,   y: 150 },
          { k: 'youtube',           x: 230,  y: 40  },
          { k: 'instagram',         x: 230,  y: 150 },
          { k: 'tiktok',            x: 230,  y: 260 },
          { k: 'linkedin',          x: 230,  y: 380 },
          { k: 'pag_captura',       x: 420,  y: 150 },
          { k: 'email_bv',          x: 610,  y: 240 },
          { k: 'email_conteudo',    x: 800,  y: 240 },
          { k: 'email_conteudo',    x: 990,  y: 240 },
          { k: 'email_promo',       x: 1180, y: 240 },
          { k: 'whatsapp',          x: 610,  y: 60  },
          { k: 'manychat',          x: 800,  y: 60  },
          { k: 'pag_vendas',        x: 990,  y: 60  },
          { k: 'pag_pedido',        x: 1180, y: 60  },
          { k: 'order_bump',        x: 1180, y: 160 },
          { k: 'pag_obrigado',      x: 1370, y: 60  },
          { k: 'upsell',            x: 1560, y: 60  },
          { k: 'area_membros',      x: 1750, y: 60  },
        ],
        conns: [
          [0,1],[0,2],[0,3],[0,4],
          [1,5],[2,5],[3,5],[4,5],
          [5,6],[5,10],
          [6,7],[7,8],[8,9],[9,12],
          [10,11],[11,12],
          [12,13],[13,14],[13,15],[14,15],
          [15,16],[16,17]
        ]
      },

      // ── EMAIL RUSSELL BRUNSON ──
      email_russel: {
        name: 'Sequência Email (Soap Opera)', desc: 'Sequência Brunson completa: 6 emails Soap Opera + VSL de qualificação + upsell em cadeia', emoji: '📧',
        blocks: [
          { k: 'pag_captura',       x: 40,   y: 150 },
          { k: 'pag_vendas_vsl',    x: 230,  y: 60  },
          { k: 'email_bv',          x: 230,  y: 240 },
          { k: 'email_conteudo',    x: 420,  y: 240 },
          { k: 'email_conteudo',    x: 610,  y: 240 },
          { k: 'email_conteudo',    x: 800,  y: 240 },
          { k: 'email_conteudo',    x: 990,  y: 240 },
          { k: 'email_promo',       x: 1180, y: 240 },
          { k: 'pag_vendas',        x: 610,  y: 60  },
          { k: 'pag_pedido',        x: 800,  y: 60  },
          { k: 'order_bump',        x: 800,  y: 160 },
          { k: 'pag_obrigado',      x: 990,  y: 60  },
          { k: 'upsell',            x: 1180, y: 60  },
          { k: 'downsell',          x: 1370, y: 240 },
          { k: 'area_membros',      x: 1370, y: 60  },
          { k: 'activecampaign',    x: 1560, y: 60  },
        ],
        conns: [
          [0,1],[0,2],
          [1,8],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],
          [8,9],[9,10],[9,11],[10,11],
          [11,12],[12,13],[12,14],[13,14],
          [14,15]
        ]
      },

      // ── DOMÍNIO INSTAGRAM ──
      dominio_instagram: {
        name: 'Domínio Instagram', desc: 'Estratégia de audiência orgânica → Manychat DM → captura → nutrição email + WhatsApp → venda', emoji: '👑',
        blocks: [
          { k: 'instagram',         x: 40,   y: 150 },
          { k: 'criativo_vid',      x: 230,  y: 60  },
          { k: 'criativo_img',      x: 230,  y: 240 },
          { k: 'manychat',          x: 420,  y: 150 },
          { k: 'pag_captura',       x: 610,  y: 150 },
          { k: 'email_bv',          x: 800,  y: 240 },
          { k: 'email_conteudo',    x: 990,  y: 240 },
          { k: 'email_promo',       x: 1180, y: 240 },
          { k: 'whatsapp',          x: 800,  y: 60  },
          { k: 'pag_vendas_vsl',    x: 990,  y: 60  },
          { k: 'pag_pedido',        x: 1180, y: 60  },
          { k: 'order_bump',        x: 1180, y: 160 },
          { k: 'pag_obrigado',      x: 1370, y: 60  },
          { k: 'upsell',            x: 1560, y: 60  },
          { k: 'area_membros',      x: 1750, y: 60  },
          { k: 'activecampaign',    x: 1560, y: 240 },
        ],
        conns: [
          [0,1],[0,2],[1,3],[2,3],
          [3,4],[3,8],
          [4,5],[4,9],
          [5,6],[6,7],[7,9],
          [8,9],
          [9,10],[10,11],[10,12],[11,12],
          [12,13],[13,14],
          [12,15]
        ]
      },

      // ── LIGAÇÃO / CALL BOOK ──
      ligacao: {
        name: 'Ligação / Agendamento de Call', desc: 'Captação → VSL de qualificação → WhatsApp → SDR → Setter → Closer → fechamento', emoji: '📞',
        blocks: [
          { k: 'trafego_pago',      x: 40,   y: 60  },
          { k: 'linkedin',          x: 40,   y: 240 },
          { k: 'criativo_vid',      x: 230,  y: 60  },
          { k: 'criativo_img',      x: 230,  y: 240 },
          { k: 'pag_captura',       x: 420,  y: 150 },
          { k: 'pag_vendas_vsl',    x: 610,  y: 60  },
          { k: 'email_bv',          x: 610,  y: 240 },
          { k: 'email_conteudo',    x: 800,  y: 240 },
          { k: 'email_conteudo',    x: 990,  y: 240 },
          { k: 'whatsapp',          x: 800,  y: 60  },
          { k: 'sdr',               x: 990,  y: 60  },
          { k: 'setter',            x: 1180, y: 60  },
          { k: 'condicional',       x: 1370, y: 60  },
          { k: 'closer',            x: 1560, y: 60  },
          { k: 'pag_pedido',        x: 1750, y: 60  },
          { k: 'order_bump',        x: 1750, y: 160 },
          { k: 'pag_obrigado',      x: 1940, y: 60  },
          { k: 'upsell',            x: 2130, y: 60  },
          { k: 'area_membros',      x: 2320, y: 60  },
          { k: 'downsell',          x: 1940, y: 240 },
        ],
        conns: [
          [0,2],[1,3],[2,4],[3,4],
          [4,5],[4,6],
          [5,9],[6,7],[7,8],[8,9],
          [9,10],[10,11],[11,12],
          [12,13],[12,6],
          [13,14],[14,15],[14,16],[15,16],
          [16,17],[17,18],
          [17,19]
        ]
      },

      // ── STORY ADS ──
      story_ads: {
        name: 'Story Ads', desc: 'Anúncio em stories → LP → checkout com bump → email + recuperação de carrinho por WhatsApp e SMS', emoji: '🎬',
        blocks: [
          { k: 'instagram',         x: 40,   y: 60  },
          { k: 'facebook',          x: 40,   y: 240 },
          { k: 'criativo_vid',      x: 230,  y: 60  },
          { k: 'criativo_img',      x: 230,  y: 240 },
          { k: 'landing_page',      x: 420,  y: 150 },
          { k: 'pag_pedido',        x: 610,  y: 60  },
          { k: 'order_bump',        x: 610,  y: 180 },
          { k: 'pag_obrigado_count',x: 800,  y: 60  },
          { k: 'upsell',            x: 990,  y: 60  },
          { k: 'downsell',          x: 990,  y: 240 },
          { k: 'area_membros',      x: 1180, y: 60  },
          { k: 'email_bv',          x: 800,  y: 240 },
          { k: 'email_promo',       x: 1180, y: 240 },
          { k: 'condicional',       x: 610,  y: 360 },
          { k: 'whatsapp',          x: 800,  y: 360 },
          { k: 'sms',               x: 990,  y: 360 },
        ],
        conns: [
          [0,2],[1,3],[2,4],[3,4],
          [4,5],[4,11],
          [5,6],[5,7],[6,7],
          [7,8],[8,9],[8,10],[9,10],
          [11,12],[12,8],
          [5,13],[13,14],[13,15]
        ]
      },

      // ── LANÇAMENTO PAGO ──
      lancamento_pago: {
        name: 'Lançamento via Tráfego Pago', desc: 'Escala rápida: webinar de conversão → live pré-venda → abertura → checkout → recuperação de carrinho', emoji: '🚀',
        blocks: [
          { k: 'trafego_pago',      x: 40,   y: 60  },
          { k: 'criativo_vid',      x: 230,  y: 60  },
          { k: 'criativo_img',      x: 230,  y: 240 },
          { k: 'pag_captura',       x: 420,  y: 150 },
          { k: 'email_bv',          x: 610,  y: 240 },
          { k: 'email_conteudo',    x: 800,  y: 240 },
          { k: 'email_conteudo',    x: 990,  y: 240 },
          { k: 'webinar',           x: 610,  y: 60  },
          { k: 'live',              x: 800,  y: 60  },
          { k: 'email_promo',       x: 1180, y: 240 },
          { k: 'pag_vendas',        x: 990,  y: 60  },
          { k: 'pag_pedido',        x: 1180, y: 60  },
          { k: 'order_bump',        x: 1180, y: 160 },
          { k: 'pag_obrigado_count',x: 1370, y: 60  },
          { k: 'upsell',            x: 1560, y: 60  },
          { k: 'downsell',          x: 1560, y: 240 },
          { k: 'area_membros',      x: 1750, y: 60  },
          { k: 'condicional',       x: 1370, y: 240 },
          { k: 'whatsapp',          x: 1560, y: 420 },
          { k: 'email_promo',       x: 1750, y: 420 },
        ],
        conns: [
          [0,1],[0,2],[1,3],[2,3],
          [3,4],[3,7],
          [4,5],[5,6],[6,9],
          [7,8],[8,10],[9,10],
          [10,11],[11,12],[11,13],[12,13],
          [13,14],[14,15],[14,16],[15,16],
          [13,17],[17,18],[17,19]
        ]
      },

      // ── GRUPO VIP WHATSAPP ──
      grupo_vip: {
        name: 'Grupo VIP (WhatsApp)', desc: 'Captura → WhatsApp + email em paralelo → venda → comunidade VIP → upsell de LTV → CRM de retenção', emoji: '🔐',
        blocks: [
          { k: 'trafego_pago',      x: 40,   y: 60  },
          { k: 'instagram',         x: 40,   y: 240 },
          { k: 'criativo_vid',      x: 230,  y: 60  },
          { k: 'criativo_img',      x: 230,  y: 240 },
          { k: 'pag_captura',       x: 420,  y: 150 },
          { k: 'whatsapp',          x: 610,  y: 60  },
          { k: 'email_bv',          x: 610,  y: 240 },
          { k: 'email_conteudo',    x: 800,  y: 240 },
          { k: 'email_conteudo',    x: 990,  y: 240 },
          { k: 'email_promo',       x: 1180, y: 240 },
          { k: 'pag_vendas',        x: 800,  y: 60  },
          { k: 'pag_pedido',        x: 990,  y: 60  },
          { k: 'order_bump',        x: 990,  y: 160 },
          { k: 'pag_obrigado',      x: 1180, y: 60  },
          { k: 'comunidade',        x: 1370, y: 60  },
          { k: 'upsell',            x: 1560, y: 60  },
          { k: 'area_membros',      x: 1750, y: 60  },
          { k: 'activecampaign',    x: 1370, y: 240 },
        ],
        conns: [
          [0,2],[1,3],[2,4],[3,4],
          [4,5],[4,6],
          [5,10],[6,7],[7,8],[8,9],[9,10],
          [10,11],[11,12],[11,13],[12,13],
          [13,14],[14,15],[15,16],
          [13,17]
        ]
      },

      // ── LANÇAMENTO FÓRMULA ──
      lancamento_trad: {
        name: 'Lançamento Fórmula de Lançamento', desc: 'CPL completo (4 conteúdos) + JV Webinar + live de abertura + carrinho com upsell + recuperação', emoji: '🏆',
        blocks: [
          { k: 'trafego_pago',      x: 40,   y: 60  },
          { k: 'trafego_organico',  x: 40,   y: 240 },
          { k: 'criativo_vid',      x: 230,  y: 60  },
          { k: 'criativo_img',      x: 230,  y: 240 },
          { k: 'pag_captura',       x: 420,  y: 150 },
          { k: 'email_bv',          x: 610,  y: 240 },
          { k: 'email_conteudo',    x: 800,  y: 240 },
          { k: 'email_conteudo',    x: 990,  y: 240 },
          { k: 'email_conteudo',    x: 1180, y: 240 },
          { k: 'webinar',           x: 610,  y: 60  },
          { k: 'live',              x: 800,  y: 60  },
          { k: 'email_promo',       x: 1370, y: 240 },
          { k: 'pag_vendas',        x: 990,  y: 60  },
          { k: 'pag_pedido',        x: 1180, y: 60  },
          { k: 'order_bump',        x: 1180, y: 160 },
          { k: 'pag_obrigado_count',x: 1370, y: 60  },
          { k: 'upsell',            x: 1560, y: 60  },
          { k: 'downsell',          x: 1560, y: 240 },
          { k: 'area_membros',      x: 1750, y: 60  },
          { k: 'condicional',       x: 1370, y: 420 },
          { k: 'whatsapp',          x: 1560, y: 420 },
          { k: 'email_promo',       x: 1750, y: 420 },
        ],
        conns: [
          [0,2],[1,3],[2,4],[3,4],
          [4,5],[4,9],
          [5,6],[6,7],[7,8],[8,11],
          [9,10],[10,12],[11,12],
          [12,13],[13,14],[13,15],[14,15],
          [15,16],[16,17],[16,18],[17,18],
          [15,19],[19,20],[19,21]
        ]
      },
```

- [ ] **Step 2: Verificar no browser**

Abrir `index.html` → "Novo Funil" → testar "Fórmula de Lançamento" (deve ter ~22 blocos) e "Ligação/Agendamento" (deve mostrar SDR → Setter → Closer).

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "feat: reescreve templates batch 3 — whatsapp_11, checklist_oto, distribuicao, email_russel, dominio_instagram, ligacao, story_ads, lancamento_pago, grupo_vip, lancamento_trad"
```

---

## Task 5: Export — CDN docx.js + HTML do botão e modal

**Files:**
- Modify: `index.html` — head (linha ~10), header HTML (linha ~3050), modal section (linha ~3355)

- [ ] **Step 1: Adicionar CDN docx.js no `<head>`**

Localizar a linha `</head>` e inserir antes:

```html
  <script src="https://unpkg.com/docx@8.5.0/build/index.js"></script>
```

- [ ] **Step 2: Adicionar botão "Resumo" no header**

Localizar o botão de exportar PNG no header (contém `doExport()` no onclick). Inserir logo ANTES dele:

```html
<button onclick="openSummaryModal()" id="btn-resumo" class="h-btn" title="Exportar resumo estratégico do funil" style="gap:5px">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="15" height="15"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
  Resumo
</button>
```

- [ ] **Step 3: Adicionar modal de export**

Localizar `<!-- ═══ MODALS ═══ -->` e inserir logo após:

```html
  <!-- Summary Export Modal -->
  <div id="summary-overlay" style="display:none;position:fixed;inset:0;z-index:5000;background:rgba(0,0,0,.6);backdrop-filter:blur(4px);align-items:center;justify-content:center">
    <div style="background:var(--bg2);border:1px solid var(--border);border-radius:18px;padding:28px;width:640px;max-width:94vw;max-height:85vh;display:flex;flex-direction:column;gap:16px;box-shadow:var(--shadow-lg)">
      <div style="display:flex;justify-content:space-between;align-items:center">
        <div>
          <h2 style="margin:0;font-size:16px;font-weight:700">Resumo Estratégico do Funil</h2>
          <p style="margin:4px 0 0;font-size:12px;color:var(--text3)">Passo a passo completo da estratégia, pronto para exportar</p>
        </div>
        <button onclick="closeSummaryModal()" style="background:none;border:none;cursor:pointer;color:var(--text3);font-size:18px;line-height:1;padding:4px 8px;border-radius:6px">✕</button>
      </div>
      <pre id="summary-preview" style="flex:1;overflow-y:auto;font-family:var(--mono);font-size:12px;line-height:1.7;background:var(--bg3);border:1px solid var(--border);border-radius:10px;padding:16px;color:var(--text);white-space:pre-wrap;max-height:450px;margin:0"></pre>
      <div style="display:flex;gap:8px;justify-content:flex-end;padding-top:4px;border-top:1px solid var(--border)">
        <button onclick="downloadSummaryTXT()" class="h-btn" style="gap:6px">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="14" height="14"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          Baixar .TXT
        </button>
        <button onclick="downloadSummaryDOCX()" class="h-btn" style="gap:6px;background:var(--accent);color:#fff;border-color:var(--accent)">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="14" height="14"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
          Baixar .DOCX
        </button>
      </div>
    </div>
  </div>
```

- [ ] **Step 4: Verificar no browser**

Abrir `index.html` → criar funil com template → verificar que botão "Resumo" aparece no header → clicar → modal deve abrir (preview ainda vazio, funções JS virão na Task 6).

- [ ] **Step 5: Commit**

```bash
git add index.html
git commit -m "feat: adiciona botão Resumo no header e modal de export TXT/DOCX"
```

---

## Task 6: Export — Funções JS

**Files:**
- Modify: `index.html` — seção de funções JS (inserir antes de `// BOOT`)

- [ ] **Step 1: Adicionar funções de export**

Localizar o comentário `// BOOT` e inserir o bloco abaixo imediatamente antes:

```javascript
    // ══════════════════════════════════════════
    // EXPORT — RESUMO ESTRATÉGICO
    // ══════════════════════════════════════════
    function buildFunnelOrdered() {
      const f = af();
      if (!f || f.nodes.length === 0) return null;
      const adj = {};
      f.nodes.forEach(n => { adj[n.id] = []; });
      f.connections.forEach(c => { if (adj[c.from] !== undefined) adj[c.from].push(c.to); });
      const hasIncoming = new Set();
      f.connections.forEach(c => hasIncoming.add(c.to));
      const roots = f.nodes.filter(n => !hasIncoming.has(n.id));
      const visited = new Set();
      const ordered = [];
      const queue = roots.length > 0 ? roots.map(r => r.id) : [f.nodes[0].id];
      while (queue.length > 0) {
        const id = queue.shift();
        if (visited.has(id)) continue;
        visited.add(id);
        const node = f.nodes.find(n => n.id === id);
        if (node) { ordered.push(node); (adj[id] || []).forEach(nid => { if (!visited.has(nid)) queue.push(nid); }); }
      }
      f.nodes.forEach(n => { if (!visited.has(n.id)) ordered.push(n); });
      return ordered;
    }

    function buildSummaryText(ordered) {
      const funil = STATE.funils.find(fn => fn.id === STATE.current);
      const title = funil ? funil.name : 'Funil';
      const date = new Date().toLocaleDateString('pt-BR', { day: '2-digit', month: '2-digit', year: 'numeric' });
      let txt = '';
      txt += '═'.repeat(52) + '\n';
      txt += `  FUNIL365 — RESUMO ESTRATÉGICO\n`;
      txt += '═'.repeat(52) + '\n';
      txt += `  ${title}\n`;
      txt += `  Gerado em: ${date}  |  Total de etapas: ${ordered.length}\n`;
      txt += '═'.repeat(52) + '\n\n';
      const cats = {};
      ordered.forEach((node, i) => {
        const b = BLOCKS[node.key];
        if (!b) return;
        if (!cats[b.cat]) cats[b.cat] = [];
        cats[b.cat].push({ node, b, step: i + 1 });
      });
      ordered.forEach((node, i) => {
        const b = BLOCKS[node.key];
        if (!b) return;
        txt += `ETAPA ${String(i + 1).padStart(2, '0')}  ▸  ${b.label.toUpperCase()}\n`;
        txt += `         Categoria : ${b.cat}\n`;
        txt += `         Função    : ${b.sub}\n`;
        txt += `         Conv.     : ${node.conv}%\n`;
        if (node.name && node.name !== b.label) txt += `         Nome      : ${node.name}\n`;
        if (node.url) txt += `         URL       : ${node.url}\n`;
        if (node.note) txt += `         Nota      : ${node.note}\n`;
        txt += '\n';
      });
      const f = af();
      if (f && f.connections.length > 0) {
        txt += '─'.repeat(52) + '\n';
        txt += 'FLUXO DE CONEXÕES\n';
        txt += '─'.repeat(52) + '\n';
        const nodeMap = {};
        f.nodes.forEach((n, i) => { nodeMap[n.id] = { b: BLOCKS[n.key], step: ordered.findIndex(o => o.id === n.id) + 1 }; });
        f.connections.forEach(c => {
          const from = nodeMap[c.from];
          const to = nodeMap[c.to];
          if (from && to && from.b && to.b) {
            txt += `  Etapa ${String(from.step).padStart(2,'0')} [${from.b.label}]  →  Etapa ${String(to.step).padStart(2,'0')} [${to.b.label}]\n`;
          }
        });
      }
      txt += '\n' + '─'.repeat(52) + '\n';
      txt += 'Gerado com Funil365 — funil365.app\n';
      return txt;
    }

    function openSummaryModal() {
      const ordered = buildFunnelOrdered();
      if (!ordered || ordered.length === 0) { toast('Adicione blocos ao canvas primeiro'); return; }
      const txt = buildSummaryText(ordered);
      document.getElementById('summary-preview').textContent = txt;
      const overlay = document.getElementById('summary-overlay');
      overlay.style.display = 'flex';
    }

    function closeSummaryModal() {
      document.getElementById('summary-overlay').style.display = 'none';
    }

    function downloadSummaryTXT() {
      const ordered = buildFunnelOrdered();
      if (!ordered) return;
      const txt = buildSummaryText(ordered);
      const funil = STATE.funils.find(fn => fn.id === STATE.current);
      const name = (funil?.name || 'funil').toLowerCase().replace(/\s+/g, '-');
      const blob = new Blob([txt], { type: 'text/plain;charset=utf-8' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = `resumo-${name}.txt`;
      a.click();
      URL.revokeObjectURL(a.href);
    }

    function downloadSummaryDOCX() {
      if (typeof docx === 'undefined') { toast('Biblioteca DOCX não carregou. Verifique sua conexão.'); return; }
      const ordered = buildFunnelOrdered();
      if (!ordered) return;
      const funil = STATE.funils.find(fn => fn.id === STATE.current);
      const title = funil ? funil.name : 'Funil';
      const date = new Date().toLocaleDateString('pt-BR', { day: '2-digit', month: '2-digit', year: 'numeric' });
      const { Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, BorderStyle } = docx;
      const children = [];
      children.push(new Paragraph({ text: 'FUNIL365 — RESUMO ESTRATÉGICO', heading: HeadingLevel.HEADING_1, alignment: AlignmentType.CENTER }));
      children.push(new Paragraph({ children: [new TextRun({ text: title, bold: true, size: 28 })], alignment: AlignmentType.CENTER }));
      children.push(new Paragraph({ children: [new TextRun({ text: `Gerado em: ${date}  |  Total de etapas: ${ordered.length}`, color: '666666', size: 20 })], alignment: AlignmentType.CENTER }));
      children.push(new Paragraph({ text: '' }));
      children.push(new Paragraph({ text: 'SEQUÊNCIA DO FUNIL', heading: HeadingLevel.HEADING_2 }));
      children.push(new Paragraph({ text: '' }));
      ordered.forEach((node, i) => {
        const b = BLOCKS[node.key];
        if (!b) return;
        children.push(new Paragraph({ children: [new TextRun({ text: `${String(i + 1).padStart(2, '0')}. ${b.label}`, bold: true, size: 24 }), new TextRun({ text: `  —  ${b.sub}`, size: 22, color: '444444' })] }));
        children.push(new Paragraph({ children: [new TextRun({ text: `Categoria: ${b.cat}`, size: 18, color: '888888' }), new TextRun({ text: `   |   Conversão esperada: ${node.conv}%`, size: 18, color: '888888' })] }));
        if (node.url) children.push(new Paragraph({ children: [new TextRun({ text: `URL: ${node.url}`, size: 18, color: '0ea5e9' })] }));
        if (node.note) children.push(new Paragraph({ children: [new TextRun({ text: `Nota: ${node.note}`, size: 18, italics: true, color: '555555' })] }));
        children.push(new Paragraph({ text: '' }));
      });
      const f = af();
      if (f && f.connections.length > 0) {
        children.push(new Paragraph({ text: 'FLUXO DE CONEXÕES', heading: HeadingLevel.HEADING_2 }));
        children.push(new Paragraph({ text: '' }));
        const nodeMap = {};
        f.nodes.forEach(n => { nodeMap[n.id] = { b: BLOCKS[n.key], step: ordered.findIndex(o => o.id === n.id) + 1 }; });
        f.connections.forEach(c => {
          const from = nodeMap[c.from]; const to = nodeMap[c.to];
          if (from && to && from.b && to.b) {
            children.push(new Paragraph({ children: [new TextRun({ text: `Etapa ${String(from.step).padStart(2,'0')} [${from.b.label}]`, bold: true }), new TextRun({ text: '  →  ' }), new TextRun({ text: `Etapa ${String(to.step).padStart(2,'0')} [${to.b.label}]`, bold: true })] }));
          }
        });
      }
      children.push(new Paragraph({ text: '' }));
      children.push(new Paragraph({ children: [new TextRun({ text: 'Gerado com Funil365 — funil365.app', size: 16, color: '999999', italics: true })], alignment: AlignmentType.CENTER }));
      const doc = new Document({ sections: [{ properties: {}, children }] });
      const name = title.toLowerCase().replace(/\s+/g, '-');
      Packer.toBlob(doc).then(blob => {
        const a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = `resumo-${name}.docx`;
        a.click();
        URL.revokeObjectURL(a.href);
      });
    }
```

- [ ] **Step 2: Verificar TXT no browser**

Abrir `index.html` → criar funil "High Ticket Consultivo" → clicar "Resumo" no header → modal abre com texto listando todas as etapas do funil → clicar "Baixar .TXT" → arquivo baixa com etapas numeradas, categorias e taxas de conversão.

- [ ] **Step 3: Verificar DOCX no browser**

No mesmo modal → clicar "Baixar .DOCX" → arquivo `.docx` baixa → abrir no Word/Google Docs → deve mostrar título formatado, lista de etapas em negrito com subtítulos, seção de conexões.

- [ ] **Step 4: Fechar modal com ESC**

Adicionar este event listener junto aos outros listeners de keyboard (próximo ao listener de hotkeys de desenho):

```javascript
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') {
    closeSummaryModal();
    closeGenModal();
  }
});
```

- [ ] **Step 5: Commit final**

```bash
git add index.html
git commit -m "feat: export resumo estratégico do funil em TXT e DOCX"
```

---

## Self-Review

**Spec coverage:**
- ✅ MARKETING_KNOWLEDGE expandido com SDR/Closer/Setter, retargeting, timing emails, LTV (Task 1)
- ✅ Todos 22 templates reescritos com 16–22 blocos (Tasks 2, 3, 4)
- ✅ Botão "Resumo" no header + modal com preview (Task 5)
- ✅ Download TXT funcional (Task 6)
- ✅ Download DOCX via docx.js CDN (Task 6)
- ✅ Fechar modal com ESC (Task 6)

**Placeholder scan:** Nenhum. Todo código é completo.

**Type consistency:** `buildFunnelOrdered()` retorna array de nodes, `buildSummaryText()` recebe esse array, `openSummaryModal()` chama ambas — consistente. `downloadSummaryTXT()` e `downloadSummaryDOCX()` chamam `buildFunnelOrdered()` independentemente — correto.
