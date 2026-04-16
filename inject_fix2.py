import re

path = '/Users/icarorodriguez/.gemini/antigravity/scratch/funil365/index.html'

with open(path, 'r') as f:
    html = f.read()

# ── 1. Fix: position ai-chat-wrap as fixed (not absolute) so it floats properly over everything
old_css = """#ai-chat-wrap{
  position:absolute;bottom:12px;left:50%;transform:translateX(-50%);
  width:600px;max-width:90%;z-index:900;display:flex;flex-direction:column;gap:8px;
  align-items:center;
}"""
new_css = """#ai-chat-wrap{
  position:fixed;bottom:14px;left:50%;transform:translateX(-50%);
  width:620px;max-width:92vw;z-index:1000;display:flex;flex-direction:column;gap:8px;
  align-items:center; pointer-events:auto;
}
#ai-chat-wrap * { pointer-events:auto; }"""
html = html.replace(old_css, new_css)

# ── 2. Fix draw engine: guard against buttons getting snagged by drawWrap mousedown
old_draw_guard = """  if(drawState.active === 'cursor') return;
  if(drawState.active === 'eraser') return;
  if(e.button !== 0) return;
  // Don't draw if clicking on a node
  if(e.target.closest('.node')) return;"""
new_draw_guard = """  if(drawState.active === 'cursor') return;
  if(drawState.active === 'eraser') return;
  if(e.button !== 0) return;
  // Don't draw if clicking UI elements
  if(e.target.closest('.node')) return;
  if(e.target.closest('#ai-chat-wrap')) return;
  if(e.target.closest('#draw-toolbar')) return;
  if(e.target.closest('#ctx')) return;"""
html = html.replace(old_draw_guard, new_draw_guard)

# ── 3. Fix draw-toolbar CSS: use fixed positioning too so it doesn't move with canvas
old_toolbar_css = """#draw-toolbar {
  background:var(--bg2); border:1px solid var(--border);
  border-radius:12px; padding:6px 10px; display:flex; flex-direction:row; align-items:center; gap:2px;
  box-shadow:var(--shadow-lg); width:auto;
}"""
new_toolbar_css = """#draw-toolbar {
  background:var(--bg2); border:1px solid var(--border);
  border-radius:12px; padding:6px 12px; display:flex; flex-direction:row; align-items:center; gap:2px;
  box-shadow:var(--shadow-lg); width:auto; flex-shrink:0;
}"""
html = html.replace(old_toolbar_css, new_toolbar_css)

# ── 4. Also move cvg-draw outside of canvas (so zoom doesn't affect tool overlay)
# cvg-draw should be fixed/absolute over canvas-wrap, not inside the transformed canvas div
old_cvg_pos = "#cvg-draw { position:absolute; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:500; }"
new_cvg_pos = "#cvg-draw { position:absolute; top:0; left:0; width:100%; height:100%; pointer-events:auto; z-index:500; }"
html = html.replace(old_cvg_pos, new_cvg_pos)

# ── 5. Add Claude as AI option in modal select
old_select = """      <select id="api-select" style="width:100%;padding:8px;border-radius:6px;border:1px solid var(--border);background:var(--bg3);font-family:var(--font);color:var(--text)">
        <option value="gemini">Google Gemini (gemini-1.5-flash)</option>
        <option value="openai">OpenAI (gpt-4o-mini)</option>
      </select>"""
new_select = """      <select id="api-select" style="width:100%;padding:8px;border-radius:6px;border:1px solid var(--border);background:var(--bg3);font-family:var(--font);color:var(--text)">
        <option value="gemini">Google Gemini (gemini-2.0-flash)</option>
        <option value="openai">OpenAI (gpt-4o-mini)</option>
        <option value="claude">Anthropic Claude (claude-3-5-haiku)</option>
      </select>"""
html = html.replace(old_select, new_select)

# ── 6. Add Claude handling in sendAIChat
old_end_model = """    } else {
      // Gemini
      const messages = aiConfig.history.map(m => ({
        role: m.role === 'user' ? 'user' : 'model',
        parts: [{text: m.content}]
      }));
      const res = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${aiConfig.keys.gemini}`, {"""
new_end_model = """    } else if(aiConfig.model === 'claude') {
      const claudeMsgs = aiConfig.history.map(m => ({
        role: m.role === 'user' ? 'user' : 'assistant',
        content: m.content
      }));
      const res = await fetch('https://corsproxy.io/?https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-api-key': aiConfig.keys.claude,
          'anthropic-version': '2023-06-01'
        },
        body: JSON.stringify({
          model: 'claude-haiku-4-5',
          max_tokens: 1024,
          system: sysMsg,
          messages: claudeMsgs
        })
      });
      const data = await res.json();
      if(data.error) throw new Error(data.error.message || JSON.stringify(data.error));
      responseText = data.content[0].text;
    } else {
      // Gemini
      const messages = aiConfig.history.map(m => ({
        role: m.role === 'user' ? 'user' : 'model',
        parts: [{text: m.content}]
      }));
      const res = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${aiConfig.keys.gemini}`, {"""
html = html.replace(old_end_model, new_end_model)

# ── 7. Fix aiConfig to include claude key
old_aiconfig = "let aiConfig = { model: 'gemini', keys: { gemini:'AIzaSyBx2tzj-P7KKWGc-jwUJ2h2gxqC1p1HY5Q', openai:'' }, history: [] };"
new_aiconfig = "let aiConfig = { model: 'gemini', keys: { gemini:'AIzaSyBx2tzj-P7KKWGc-jwUJ2h2gxqC1p1HY5Q', openai:'', claude:'' }, history: [] };"
html = html.replace(old_aiconfig, new_aiconfig)

# ── 8. Fix: update label when model changes in modal
old_save_cfg = """function saveAPIConfig() {
  aiConfig.model = document.getElementById('api-select').value;
  aiConfig.keys[aiConfig.model] = document.getElementById('api-key-input').value.trim();
  try { localStorage.setItem('fn365ai', JSON.stringify(aiConfig)); } catch(e){}
  document.getElementById('api-modal-overlay').style.display='none';
  toast('Configuração salva');
}"""
new_save_cfg = """function saveAPIConfig() {
  aiConfig.model = document.getElementById('api-select').value;
  aiConfig.keys[aiConfig.model] = document.getElementById('api-key-input').value.trim();
  try { localStorage.setItem('fn365ai', JSON.stringify(aiConfig)); } catch(e){}
  document.getElementById('api-modal-overlay').style.display='none';
  const labels = { gemini:'Gemini', openai:'GPT-4o', claude:'Claude' };
  const lbl = document.getElementById('ai-model-label');
  if(lbl) lbl.textContent = labels[aiConfig.model] || aiConfig.model;
  toast('Configuração salva');
}"""
html = html.replace(old_save_cfg, new_save_cfg)

with open(path, 'w') as f:
    f.write(html)

print("Done!")
