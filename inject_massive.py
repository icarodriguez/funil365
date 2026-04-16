import re

path = '/Users/icarorodriguez/.gemini/antigravity/scratch/funil365/index.html'

with open(path, 'r') as f:
    html = f.read()

# 1. Update SVGs
icons_inject = """
    group:`<svg ${s}><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>`,
    monitor:`<svg ${s}><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>`,
    smartphone:`<svg ${s}><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>`,
    split:`<svg ${s}><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>`,
    webinar:`<svg ${s}><circle cx="12" cy="12" r="10"/><circle cx="12" cy="10" r="3"/><path d="M7 20.662V19a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v1.662"/></svg>`,
    camera:`<svg ${s}><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>`,
    download:`<svg ${s}><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>`,
    clock:`<svg ${s}><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>`,
    file_check:`<svg ${s}><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><polyline points="9 15 11 17 16 12"/></svg>`,
    target:`<svg ${s}><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>`,
    volume:`<svg ${s}><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg>`,
"""
html = html.replace("const paths={", "const paths={\n" + icons_inject)

# 2. Add New Blocks
blocks_new = """
  // ELEMENTOS GERAIS
  comunidade:{cat:'Páginas',label:'Comunidade',sub:'Grupo/comunidade',shape:'page',color:'#ec4899',bg:'#fdf2f8',icon:'group',conv:100},
  membros:{cat:'Páginas',label:'Área de Membros',sub:'Plataforma de curso',shape:'page',color:'#e11d48',bg:'#ffe4e6',icon:'monitor',conv:100},
  app:{cat:'Páginas',label:'App',sub:'Aplicativo mobile',shape:'page',color:'#0ea5e9',bg:'#f0f9ff',icon:'smartphone',conv:100},

  // PAGINAS ESPECÍFICAS
  pag_captura:{cat:'Páginas',label:'Página de Captura',sub:'Captura de leads',shape:'page',color:'#3b82f6',bg:'#eff6ff',icon:'page',conv:40},
  pag_obrigado:{cat:'Páginas',label:'Página de Obrigado',sub:'Confirmação',shape:'page',color:'#22c55e',bg:'#f0fdf4',icon:'file_check',conv:100},
  pag_obrigado_count:{cat:'Páginas',label:'Obrigado + Countdown',sub:'Contagem para Whats',shape:'page',color:'#16a34a',bg:'#dcfce7',icon:'clock',conv:100},
  pag_obrigado_vid:{cat:'Páginas',label:'Obrigado + Vídeo',sub:'Confirmação com vídeo',shape:'page',color:'#15803d',bg:'#dcfce7',icon:'file_check',conv:100},
  pag_download:{cat:'Páginas',label:'Página de Download',sub:'Entrega de material',shape:'page',color:'#10b981',bg:'#ecfdf5',icon:'download',conv:100},
  live:{cat:'Páginas',label:'Live AO VIVO',sub:'YouTube/Streaming',shape:'page',color:'#ef4444',bg:'#fef2f2',icon:'camera',conv:20},
  reuniao:{cat:'Páginas',label:'Reunião Online',sub:'Zoom / Meet',shape:'page',color:'#3b82f6',bg:'#eff6ff',icon:'camera',conv:20},
  pag_webinar:{cat:'Páginas',label:'Página de Webinar',sub:'Transmissão',shape:'page',color:'#a855f7',bg:'#faf5ff',icon:'webinar',conv:20},

  // LOGICA E AÇÕES
  condicional:{cat:'Ação',label:'Se/ou',sub:'Condicional',shape:'icon',color:'#f97316',bg:'#fff7ed',icon:'split',conv:50},
  acao_lead:{cat:'Ação',label:'Lead',sub:'Ação de lead',shape:'icon',color:'#ea580c',bg:'#ffedd5',icon:'form',conv:100},
  acao_compra:{cat:'Ação',label:'Compra',sub:'Ação de compra',shape:'icon',color:'#22c55e',bg:'#f0fdf4',icon:'cart',conv:100},
  trafego:{cat:'Ação',label:'Tráfego Pago',sub:'Anúncios pagos',shape:'icon',color:'#10b981',bg:'#ecfdf5',icon:'target',conv:100},
  remarketing:{cat:'Ação',label:'Remarketing',sub:'Ação de remarketing',shape:'icon',color:'#3b82f6',bg:'#eff6ff',icon:'target',conv:100},
  audiencia:{cat:'Ação',label:'Audiência',sub:'Engajamento',shape:'icon',color:'#14b8a6',bg:'#f0fdfa',icon:'volume',conv:100},
"""
html = html.replace("const BLOCKS = {", "const BLOCKS = {\n" + blocks_new)

# 3. Add to MTpls array (Massive templates)
mtpls = """
  {id:'web_mentoria',title:'Webinário + Mentoria',bdg:'27 elementos',nodes:[
    {k:'pag_captura',x:100,y:200,c:30},{k:'pag_webinar',x:350,y:200,c:40},{k:'pag_vendas',x:600,y:200,c:15},{k:'acao_compra',x:850,y:200,c:100}
  ],conns:[[0,1],[1,2],[2,3]]},
  {id:'story365',title:'STORY365 - Sequência',bdg:'20 elementos',nodes:[
    {k:'instagram',x:100,y:100,c:50},{k:'pag_vendas',x:350,y:100,c:20},{k:'carrinho',x:600,y:100,c:40}
  ],conns:[[0,1],[1,2]]},
  {id:'captacao',title:'Captação de Leads',bdg:'10 elementos',nodes:[
    {k:'facebook',x:100,y:100,c:100},{k:'pag_captura',x:350,y:100,c:45},{k:'pag_obrigado',x:600,y:100,c:100}
  ],conns:[[0,1],[1,2]]},
  {id:'anuncio_direto',title:'Anúncio',bdg:'10 elementos',nodes:[
    {k:'criativo_img',x:100,y:100,c:100},{k:'pag_vendas',x:350,y:100,c:15}
  ],conns:[[0,1]]},
  {id:'dm_insta',title:'DM Instagram',bdg:'13 elementos',nodes:[
    {k:'instagram',x:100,y:100,c:100},{k:'manychat',x:300,y:100,c:80},{k:'pag_vendas',x:500,y:100,c:20}
  ],conns:[[0,1],[1,2]]},
  {id:'whats11',title:'Whatsapp 1:1',bdg:'14 elementos',nodes:[
    {k:'instagram',x:100,y:100,c:100},{k:'whatsapp',x:300,y:100,c:50},{k:'pag_vendas',x:550,y:100,c:30}
  ],conns:[[0,1],[1,2]]},
  {id:'lancamento_ld1',title:'Lançamento de 1 dia - LD1™',bdg:'22 elementos',nodes:[
    {k:'facebook',x:100,y:100,c:100},{k:'pag_captura',x:300,y:100,c:50},{k:'whatsapp',x:550,y:100,c:100},{k:'live',x:800,y:100,c:30},{k:'pag_vendas',x:1050,y:100,c:15}
  ],conns:[[0,1],[1,2],[2,3],[3,4]]},
  {id:'grupo_vip',title:'Grupo VIP (Whatsapp)',bdg:'20 elementos',nodes:[
    {k:'facebook',x:100,y:100,c:100},{k:'pag_captura',x:300,y:100,c:60},{k:'whatsapp',x:550,y:100,c:100},{k:'comunidade',x:800,y:100,c:90}
  ],conns:[[0,1],[1,2],[2,3]]},
"""
# Replace MTpls inside buildMTpls
html = re.sub(
    r"const MTpls\s*=\s*\[(.*?)\];",
    "const MTpls = [" + r"\1" + mtpls + "];",
    html, flags=re.DOTALL
)

# 4. Canvas Drawing Engine (CSS + Toolbar HTML + Logic)
draw_css = """
/* ── FLUTUANTES DRAW ── */
#draw-toolbar {
  position:absolute; top:80px; right:20px; z-index:900; background:var(--bg2); border:1px solid var(--border);
  border-radius:12px; padding:10px; display:flex; flex-direction:column; gap:10px; box-shadow:var(--shadow-lg);
}
.draw-btn {
  width:36px; height:36px; border-radius:8px; border:1px solid transparent; background:var(--bg3);
  display:flex; align-items:center; justify-content:center; cursor:pointer; color:var(--text);
}
.draw-btn.active { background:var(--accent-bg); color:var(--accent); border-color:var(--accent); }
.draw-btn svg { width:18px; height:18px; }
.draw-color { width:24px; height:24px; border-radius:50%; cursor:pointer; margin:2px auto; border:2px solid transparent;}
.draw-color.active { border-color:var(--text); box-shadow:0 0 0 1px #fff inset;}
.draw-sz { width:28px; height:24px; font-size:10px; background:var(--bg3); border-radius:4px; margin:2px auto; display:flex; align-items:center; justify-content:center; cursor:pointer;}
.draw-sz.active { background:var(--accent); color:#fff; }
#cvg-draw { position:absolute; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:500; }
"""
html = html.replace("</style>", draw_css + "</style>")

draw_html = """
<div id="draw-toolbar">
  <div class="draw-btn active" id="tool-cursor" onclick="setTool('cursor')" title="Menu Padrão">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3l7.07 16.97 2.51-7.39 7.39-2.51L3 3z"/></svg>
  </div>
  <div class="draw-btn" id="tool-brush" onclick="setTool('brush')" title="Pincel">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 19l7-7 3 3-7 7-3-3z"/><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/><path d="M2 2l7.586 7.586"/></svg>
  </div>
  <div class="draw-btn" id="tool-eraser" onclick="setTool('eraser')" title="Borracha">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 20H7L3 16C2 15 2 13.5 3 12.5L13.5 2C14.5 1 16 1 17 2L22 7C23 8 23 9.5 22 10.5L12 20.5L20 20Z"/></svg>
  </div>
  <div style="height:1px;background:var(--border);margin:4px 0"></div>
  <div class="draw-color active" style="background:#ef4444" onclick="setColor(this, '#ef4444')"></div>
  <div class="draw-color" style="background:#f97316" onclick="setColor(this, '#f97316')"></div>
  <div class="draw-color" style="background:#3b82f6" onclick="setColor(this, '#3b82f6')"></div>
  <div class="draw-color" style="background:#22c55e" onclick="setColor(this, '#22c55e')"></div>
  <div class="draw-color" style="background:#1e293b" onclick="setColor(this, '#1e293b')"></div>
  <div style="height:1px;background:var(--border);margin:4px 0"></div>
  <div class="draw-sz active" onclick="setSz(this, 3)">3px</div>
  <div class="draw-sz" onclick="setSz(this, 6)">6px</div>
  <div class="draw-sz" onclick="setSz(this, 12)">12px</div>
  <div style="height:1px;background:var(--border);margin:4px 0"></div>
  <div class="draw-btn" id="tool-undo" onclick="undoDraw()" title="Desfazer traço">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 7v6h6"/><path d="M21 17a9 9 0 00-9-9 9 9 0 00-6 2.3L3 13"/></svg>
  </div>
</div>
"""
html = html.replace('<div id="ai-chat-wrap">', draw_html + '\n<div id="ai-chat-wrap">')

# Modify Draw layer into canvas
html = html.replace('<svg id="cvg"></svg>', '<svg id="cvg"></svg><svg id="cvg-draw"></svg>')

draw_logic = """
// ══════════════════════════════════════════
// DRAW ENGINE
// ══════════════════════════════════════════
let drawState = { active: 'cursor', color: '#ef4444', size: 3, isDrawing: false, paths: [] };
let currentPathData = '';
let currentPathEl = null;

function setTool(tool) {
  drawState.active = tool;
  document.querySelectorAll('.draw-btn').forEach(e => e.classList.remove('active'));
  document.getElementById('tool-'+tool).classList.add('active');
  const cw = document.getElementById('canvas-wrap');
  if(tool === 'brush') { cw.style.cursor = 'crosshair'; document.getElementById('cvg-draw').style.pointerEvents = 'all'; }
  else if(tool === 'eraser') { cw.style.cursor = 'help'; document.getElementById('cvg-draw').style.pointerEvents = 'all'; }
  else { cw.style.cursor = ''; document.getElementById('cvg-draw').style.pointerEvents = 'none'; }
}

function setColor(el, code) {
  drawState.color = code;
  document.querySelectorAll('.draw-color').forEach(e => e.classList.remove('active'));
  el.classList.add('active');
  setTool('brush');
}

function setSz(el, sz) {
  drawState.size = sz;
  document.querySelectorAll('.draw-sz').forEach(e => e.classList.remove('active'));
  el.classList.add('active');
  setTool('brush');
}

function undoDraw() {
  const svg = document.getElementById('cvg-draw');
  if(svg.lastChild) {
     svg.removeChild(svg.lastChild);
     const f = af();
     if(f && f.drawPaths) { f.drawPaths.pop(); save(); }
  }
}

function redrawnPaths() {
  const f = af();
  const svg = document.getElementById('cvg-draw');
  svg.innerHTML = '';
  if(!f || !f.drawPaths) return;
  f.drawPaths.forEach(pData => {
    const p = document.createElementNS('http://www.w3.org/2000/svg','path');
    p.setAttribute('d', pData.d);
    p.setAttribute('stroke', pData.c);
    p.setAttribute('stroke-width', pData.w);
    p.setAttribute('fill', 'none');
    p.setAttribute('stroke-linecap', 'round');
    p.setAttribute('stroke-linejoin', 'round');
    svg.appendChild(p);
  });
}

document.getElementById('cvg-draw').addEventListener('mousedown', e => {
  if(drawState.active === 'brush') {
    if(e.button !== 0) return;
    drawState.isDrawing = true;
    currentPathEl = document.createElementNS('http://www.w3.org/2000/svg','path');
    currentPathEl.setAttribute('stroke', drawState.color);
    currentPathEl.setAttribute('stroke-width', drawState.size * (1/UI.scale)); // brush scale compensation
    currentPathEl.setAttribute('fill', 'none');
    currentPathEl.setAttribute('stroke-linecap', 'round');
    currentPathEl.setAttribute('stroke-linejoin', 'round');
    
    const r = document.getElementById('canvas-wrap').getBoundingClientRect();
    const rx = (e.clientX - r.left - UI.panX) / UI.scale;
    const ry = (e.clientY - r.top - UI.panY) / UI.scale;
    currentPathData = `M${rx},${ry}`;
    currentPathEl.setAttribute('d', currentPathData);
    document.getElementById('cvg-draw').appendChild(currentPathEl);
  }
});

window.addEventListener('mousemove', e => {
  if(drawState.isDrawing && drawState.active === 'brush') {
    const r = document.getElementById('canvas-wrap').getBoundingClientRect();
    const rx = (e.clientX - r.left - UI.panX) / UI.scale;
    const ry = (e.clientY - r.top - UI.panY) / UI.scale;
    currentPathData += ` L${rx},${ry}`;
    currentPathEl.setAttribute('d', currentPathData);
  }
});

window.addEventListener('mouseup', e => {
  if(drawState.isDrawing && drawState.active === 'brush') {
    drawState.isDrawing = false;
    const f = af();
    if(f) {
      if(!f.drawPaths) f.drawPaths = [];
      f.drawPaths.push({d: currentPathData, c: drawState.color, w: drawState.size * (1/UI.scale)});
      save();
    }
    currentPathEl = null;
  }
});

document.getElementById('cvg-draw').addEventListener('click', e => {
  if(drawState.active === 'eraser') {
    const trg = e.target;
    if(trg.tagName.toLowerCase() === 'path') {
      const idx = Array.from(trg.parentNode.children).indexOf(trg);
      const f = af();
      if(f && f.drawPaths) { f.drawPaths.splice(idx, 1); save(); }
      trg.remove();
    }
  }
});

// hook into load/render
const oldRenderCanvas = renderCanvas;
renderCanvas = function() {
  oldRenderCanvas();
  redrawnPaths();
}
// ══════════════════════════════════════════
"""
html = html.replace('// ══════════════════════════════════════════\n// CANVAS TRANSFORM (Pan/Zoom)', draw_logic + '\n// ══════════════════════════════════════════\n// CANVAS TRANSFORM (Pan/Zoom)')

# Let's fix Pan behaviour so it doesn't pan when drawing.
pan_old = """  if(e.button === 0 || e.button === 1) { 
    UI.isPan = true;"""
pan_new = """  if((e.button === 0 && drawState.active === 'cursor') || e.button === 1) { 
    UI.isPan = true;"""
html = html.replace(pan_old, pan_new)


with open(path, 'w') as f:
    f.write(html)
