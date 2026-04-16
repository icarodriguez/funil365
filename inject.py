import re

path = '/Users/icarorodriguez/.gemini/antigravity/scratch/funil365/index.html'

with open(path, 'r') as f:
    html = f.read()

# 1. Add CSS
css_to_add = """
/* ── AI CHAT ── */
#ai-chat-wrap{
  position:absolute;bottom:45px;left:50%;transform:translateX(-50%);
  width:600px;max-width:90%;z-index:900;display:flex;flex-direction:column;gap:8px;
}
#ai-chat-log{
  background:rgba(15,20,30,.95);border:1px solid #334155;border-radius:14px;
  max-height:350px;overflow-y:auto;padding:16px;color:#cbd5e1;font-size:13px;
  display:none;flex-direction:column;gap:12px;box-shadow:0 8px 32px rgba(0,0,0,.3);
  backdrop-filter:blur(10px);
}
#ai-chat-log::-webkit-scrollbar{width:4px}
#ai-chat-log::-webkit-scrollbar-thumb{background:#475569;border-radius:4px}
.ai-msg{display:flex;gap:10px;line-height:1.5}
.ai-msg.user{flex-direction:row-reverse}
.ai-msg .avt{width:26px;height:26px;border-radius:6px;flex-shrink:0;background:#334155;display:flex;align-items:center;justify-content:center}
.ai-msg.user .avt{background:var(--accent)}
.ai-msg.user .avt svg{width:14px;height:14px;color:#fff}
.ai-msg.bot .avt svg{width:16px;height:16px;color:#f97316}
.ai-msg-txt{padding:8px 12px;border-radius:8px;background:#1e293b;max-width:85%}
.ai-msg.user .ai-msg-txt{background:var(--accent);color:#fff}
.ai-msg.bot .ai-msg-txt strong{color:#fff}
#ai-chat-bar{
  background:#171717;border:1px solid #262626;border-radius:14px;
  padding:10px 10px 10px 18px;display:flex;align-items:center;gap:12px;
  box-shadow:0 8px 24px rgba(0,0,0,.2);
}
#ai-chat-bar .ai-logo{
  width:22px;height:22px;flex-shrink:0;color:#db8568;
  display:flex;align-items:center;justify-content:center;
}
#ai-chat-bar .ai-logo svg{width:100%;height:100%}
#ai-input{
  flex:1;background:transparent;border:none;outline:none;
  color:#f8fafc;font-size:14px;font-family:var(--font);padding:4px 0;
}
#ai-input::placeholder{color:#737373}
#ai-model-sel{
  font-size:12px;color:#a3a3a3;display:flex;align-items:center;gap:4px;
  cursor:pointer;padding:6px 10px;border-radius:6px;transition:background .15s;
}
#ai-model-sel:hover{background:#262626;color:#e5e5e5}
#ai-submit{
  width:32px;height:32px;border-radius:8px;background:#db8568;color:#fff;
  border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;
  flex-shrink:0;transition:background .15s;
}
#ai-submit:hover{background:#cf7456}
#ai-submit svg{width:16px;height:16px}
</style>
"""
html = html.replace("</style>", css_to_add)

# 2. Add HTML
html_to_add = """
<!-- AI CHAT -->
<div id="ai-chat-wrap">
  <div id="ai-chat-log"></div>
  <div id="ai-chat-bar">
    <div class="ai-logo">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>
      </svg>
    </div>
    <input type="text" id="ai-input" placeholder="Como posso ajudar você hoje?" autocomplete="off" onkeydown="if(event.key==='Enter') sendAIChat()"/>
    <div id="ai-model-sel" onclick="openAPIModal()">
      <span id="ai-model-label">Novo Chat</span>
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>
    </div>
    <button id="ai-submit" onclick="sendAIChat()">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
    </button>
  </div>
</div>

<!-- API MODAL -->
<div id="api-modal-overlay" style="position:fixed;inset:0;background:rgba(15,20,30,.5);z-index:2000;display:none;align-items:center;justify-content:center">
  <div id="api-modal-inner" style="background:var(--bg2);width:400px;border-radius:14px;padding:20px;border:1px solid var(--border);box-shadow:var(--shadow-lg)">
    <h3 style="margin-bottom:12px;font-size:15px;color:var(--text)">Configurar IA (API)</h3>
    <div style="margin-bottom:10px">
      <label style="font-size:11px;color:var(--text3);display:block;margin-bottom:4px">Modelo Ativo</label>
      <select id="api-select" style="width:100%;padding:8px;border-radius:6px;border:1px solid var(--border);background:var(--bg3);font-family:var(--font);color:var(--text)">
        <option value="gemini">Google Gemini (gemini-1.5-flash)</option>
        <option value="openai">OpenAI (gpt-4o-mini)</option>
      </select>
    </div>
    <div style="margin-bottom:14px">
      <label style="font-size:11px;color:var(--text3);display:block;margin-bottom:4px">Sua Chave da API</label>
      <input id="api-key-input" type="password" placeholder="Cole sua chave aqui..." style="width:100%;padding:8px;border-radius:6px;border:1px solid var(--border);background:var(--bg3);color:var(--text);font-family:var(--font)" />
    </div>
    <div style="display:flex;justify-content:flex-end;gap:8px">
      <button onclick="document.getElementById('api-modal-overlay').style.display='none'" class="mbtn cancel">Cancelar</button>
      <button onclick="saveAPIConfig()" class="mbtn ok" style="background:#db8568;border:none">Salvar</button>
    </div>
  </div>
</div>

<div id="toast"></div>"""
html = html.replace("<div id=\"toast\"></div>", html_to_add)

# 3. Add to BLOCKS
blocks_inject = """
  // CANAIS (REDES SOCIAIS)
  instagram:{cat:'Canais',label:'Instagram',sub:'Tráfego orgânico/pago',shape:'icon',color:'#ec4899',bg:'#fdf2f8',icon:'instagram',conv:100},
  facebook:{cat:'Canais',label:'Facebook',sub:'Anúncios FB Ads',shape:'icon',color:'#3b82f6',bg:'#eff6ff',icon:'facebook',conv:100},
  tiktok:{cat:'Canais',label:'TikTok',sub:'Vídeos curtos',shape:'icon',color:'#1e293b',bg:'#f1f5f9',icon:'tiktok',conv:100},
  youtube:{cat:'Canais',label:'YouTube',sub:'Vídeos orgânicos/Ads',shape:'icon',color:'#ef4444',bg:'#fef2f2',icon:'youtube',conv:100},
  linkedin:{cat:'Canais',label:'LinkedIn',sub:'B2B',shape:'icon',color:'#0284c7',bg:'#e0f2fe',icon:'linkedin',conv:100},

  // CRIATIVOS
  criativo_img:{cat:'Criativos',label:'Imagem Única',sub:'Anúncio estático',shape:'icon',color:'#8b5cf6',bg:'#f5f3ff',icon:'image',conv:100},
  criativo_vid:{cat:'Criativos',label:'Vídeo Curto',sub:'Reels / TikTok Ads',shape:'icon',color:'#f43f5e',bg:'#fff1f2',icon:'video_short',conv:100},
  criativo_car:{cat:'Criativos',label:'Carrossel',sub:'Múltiplas imagens',shape:'icon',color:'#10b981',bg:'#ecfdf5',icon:'carousel',conv:100},
  criativo_cp:{cat:'Criativos',label:'Copy / Artigo',sub:'Texto focado',shape:'icon',color:'#06b6d4',bg:'#ecfeff',icon:'copy',conv:100},

  // FERRAMENTAS
  activecampaign:{cat:'Ferramentas',label:'ActiveCampaign',sub:'E-mail mkt / CRM',shape:'icon',color:'#2563eb',bg:'#eff6ff',icon:'activecampaign',conv:100},
  manychat:{cat:'Ferramentas',label:'Manychat',sub:'Automação msg',shape:'icon',color:'#0ea5e9',bg:'#f0f9ff',icon:'manychat',conv:100},
  wordpress:{cat:'Ferramentas',label:'WordPress',sub:'CMS',shape:'icon',color:'#334155',bg:'#f8fafc',icon:'wp',conv:100},
  
  // CARRINHO
  carrinho:{cat:'Ação',label:'Carrinho',sub:'Adição ao carrinho',shape:'icon',color:'#f59e0b',bg:'#fffbeb',icon:'cart',conv:60},
"""
html = html.replace("const BLOCKS = {", "const BLOCKS = {\n" + blocks_inject)

# 4. Add Icons to paths in svgIcon
icons_inject = """
    instagram:`<svg ${s}><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>`,
    facebook:`<svg ${s}><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>`,
    tiktok:`<svg ${s}><path d="M9 12a4 4 0 1 0 4 4V4a5 5 0 0 0 5 5v3a3 3 0 0 1-3-3"/></svg>`,
    youtube:`<svg ${s}><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33 2.78 2.78 0 0 0 1.94 2c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.33 29 29 0 0 0-.46-5.33z"/><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"/></svg>`,
    linkedin:`<svg ${s}><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>`,
    image:`<svg ${s}><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>`,
    video_short:`<svg ${s}><rect x="4" y="2" width="16" height="20" rx="2" ry="2"/><line x1="12" y1="18" x2="12" y2="18"/><polygon points="10 8 15 12 10 16 10 8"/></svg>`,
    carousel:`<svg ${s}><rect x="2" y="4" width="20" height="16" rx="2" ry="2"/><line x1="7" y1="4" x2="7" y2="20"/><line x1="17" y1="4" x2="17" y2="20"/></svg>`,
    copy:`<svg ${s}><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>`,
    activecampaign:`<svg ${s}><circle cx="12" cy="12" r="10"/><path d="M8 12l3 3 5-5"/></svg>`,
    manychat:`<svg ${s}><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>`,
    wp:`<svg ${s}><circle cx="12" cy="12" r="10"/><path d="M5.5 5.5l3.5 11 2-6-2-6h-2zM18.5 5.5l-3.5 11-2-6 2-6h2z"/></svg>`,
"""
html = html.replace("const paths={", "const paths={\n" + icons_inject)

# 5. Add AI Logic
ai_logic = """
// ══════════════════════════════════════════
// AI CHAT INTEGRATION
// ══════════════════════════════════════════
let aiConfig = { model: 'gemini', keys: { gemini:'', openai:'' }, history: [] };

function loadAIConfig() {
  try {
    const r = localStorage.getItem('fn365ai');
    if(r) aiConfig = JSON.parse(r);
  } catch(e){}
  document.getElementById('api-select').value = aiConfig.model || 'gemini';
  if(aiConfig.keys[aiConfig.model]) document.getElementById('api-key-input').value = aiConfig.keys[aiConfig.model];
}

function openAPIModal() {
  document.getElementById('api-key-input').value = aiConfig.keys[document.getElementById('api-select').value] || '';
  document.getElementById('api-modal-overlay').style.display='flex';
}

document.getElementById('api-select').addEventListener('change', e => {
  document.getElementById('api-key-input').value = aiConfig.keys[e.target.value] || '';
});

function saveAPIConfig() {
  aiConfig.model = document.getElementById('api-select').value;
  aiConfig.keys[aiConfig.model] = document.getElementById('api-key-input').value.trim();
  try { localStorage.setItem('fn365ai', JSON.stringify(aiConfig)); } catch(e){}
  document.getElementById('api-modal-overlay').style.display='none';
  toast('Configuração salva');
}

function addAILog(text, isUser) {
  const log = document.getElementById('ai-chat-log');
  log.style.display = 'flex';
  const div = document.createElement('div');
  div.className = 'ai-msg ' + (isUser ? 'user' : 'bot');
  div.innerHTML = `<div class="avt">${isUser ? '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>' : '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>'}</div>
  <div class="ai-msg-txt">${text}</div>`;
  log.appendChild(div);
  log.scrollTop = log.scrollHeight;
  return div.querySelector('.ai-msg-txt');
}

function buildFunnelContext() {
  const f = af();
  if(!f || f.nodes.length === 0) return "O usuário está começando um funil do zero (canvas vazio).";
  let ctx = `O usuário está montando um funil com ${f.nodes.length} blocos.\\n`;
  const nodeDict = {};
  f.nodes.forEach(n => {
    nodeDict[n.id] = BLOCKS[n.key]?.label || n.key;
    ctx += `- Bloco: [${nodeDict[n.id]}] (Taxa de Conv: ${n.conv}%) \\n`;
  });
  if(f.connections.length > 0) {
    ctx += `As conexões são:\\n`;
    f.connections.forEach(c => {
      ctx += `${nodeDict[c.from]} -> ${nodeDict[c.to]}\\n`;
    });
  }
  return ctx;
}

async function sendAIChat() {
  const input = document.getElementById('ai-input');
  const text = input.value.trim();
  if(!text) return;
  input.value = '';
  
  if(!aiConfig.keys[aiConfig.model]) {
    openAPIModal();
    toast('Insira a chave da API primeiro!');
    return;
  }
  
  addAILog(text, true);
  aiConfig.history.push({role: 'user', content: text});
  
  const botTxtEl = addAILog('Pensando...', false);
  const context = buildFunnelContext();
  const sysMsg = "Você é um especialista em Marketing Digital e Funis de Venda ajudando o usuário no software Funil365. " + context + " Responda de forma concisa e útil.";
  
  try {
    let responseText = '';
    
    if(aiConfig.model === 'openai') {
      const res = await fetch('https://api.openai.com/v1/chat/completions', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${aiConfig.keys.openai}` },
        body: JSON.stringify({
          model: 'gpt-4o-mini',
          messages: [{role: 'system', content: sysMsg}, ...aiConfig.history]
        })
      });
      const data = await res.json();
      if(data.error) throw new Error(data.error.message);
      responseText = data.choices[0].message.content;
    } else {
      // Gemini
      const messages = aiConfig.history.map(m => ({
        role: m.role === 'user' ? 'user' : 'model',
        parts: [{text: m.content}]
      }));
      const res = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${aiConfig.keys.gemini}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          contents: [{role: 'user', parts:[{text: sysMsg}] }, ...messages]
        })
      });
      const data = await res.json();
      if(data.error) throw new Error(data.error.message);
      responseText = data.candidates[0].content.parts[0].text;
    }
    
    botTxtEl.innerHTML = responseText.replace(/\\n/g, '<br/>');
    aiConfig.history.push({role: 'assistant', content: responseText});
  } catch(err) {
    botTxtEl.innerText = "[Erro da API] " + err.message;
  }
  document.getElementById('ai-chat-log').scrollTop = document.getElementById('ai-chat-log').scrollHeight;
}

loadAIConfig();
// ══════════════════════════════════════════
"""
html = html.replace("// BOOT", ai_logic + "\n// BOOT")

# Final check
with open(path, 'w') as f:
    f.write(html)
