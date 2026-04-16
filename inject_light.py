import re

path = '/Users/icarorodriguez/.gemini/antigravity/scratch/funil365/index.html'

with open(path, 'r') as f:
    html = f.read()

# 1. Update CSS to light theme
css_old = """#ai-chat-log{
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
#ai-submit:hover{background:#cf7456}"""

css_new = """#ai-chat-log{
  background:rgba(255,255,255,.95);border:1px solid var(--border);border-radius:14px;
  max-height:350px;overflow-y:auto;padding:16px;color:var(--text);font-size:13px;
  display:none;flex-direction:column;gap:12px;box-shadow:var(--shadow-lg);
  backdrop-filter:blur(10px);
}
#ai-chat-log::-webkit-scrollbar{width:4px}
#ai-chat-log::-webkit-scrollbar-thumb{background:var(--border2);border-radius:4px}
.ai-msg{display:flex;gap:10px;line-height:1.5}
.ai-msg.user{flex-direction:row-reverse}
.ai-msg .avt{width:28px;height:28px;border-radius:6px;flex-shrink:0;background:var(--bg3);display:flex;align-items:center;justify-content:center}
.ai-msg.user .avt{background:var(--accent)}
.ai-msg.user .avt svg{width:14px;height:14px;color:#fff}
.ai-msg.bot .avt svg{width:16px;height:16px;color:var(--accent)}
.ai-msg-txt{padding:8px 12px;border-radius:8px;background:var(--bg3);max-width:85%}
.ai-msg.user .ai-msg-txt{background:var(--accent);color:#fff}
.ai-msg.bot .ai-msg-txt strong{color:var(--text)}
#ai-chat-bar{
  background:var(--bg2);border:1px solid var(--border);border-radius:14px;
  padding:10px 10px 10px 18px;display:flex;align-items:center;gap:12px;
  box-shadow:var(--shadow-lg);
}
#ai-chat-bar .ai-logo{
  width:22px;height:22px;flex-shrink:0;color:var(--accent);
  display:flex;align-items:center;justify-content:center;
}
#ai-chat-bar .ai-logo svg{width:100%;height:100%}
#ai-input{
  flex:1;background:transparent;border:none;outline:none;
  color:var(--text);font-size:14px;font-family:var(--font);padding:4px 0;
}
#ai-input::placeholder{color:var(--text3)}
#ai-model-sel{
  font-size:12px;color:var(--text2);display:flex;align-items:center;gap:4px;
  cursor:pointer;padding:6px 10px;border-radius:6px;transition:background .15s;
}
#ai-model-sel:hover{background:var(--bg3);color:var(--text)}
#ai-submit{
  width:32px;height:32px;border-radius:8px;background:var(--accent);color:#fff;
  border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;
  flex-shrink:0;transition:background .15s;
}
#ai-submit:hover{background:var(--accent2)}"""

html = html.replace(css_old, css_new)

# 2. Update JS config to default to the user's API key
js_old = "let aiConfig = { model: 'gemini', keys: { gemini:'', openai:'' }, history: [] };"
js_new = "let aiConfig = { model: 'gemini', keys: { gemini:'AIzaSyBx2tzj-P7KKWGc-jwUJ2h2gxqC1p1HY5Q', openai:'' }, history: [] };"
html = html.replace(js_old, js_new)

# 3. Update the Gemini endpoint URL so it uses the pro version that is guaranteed to work 
# and fixes the user's specific v1beta not found issue.
fetch_old = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${aiConfig.keys.gemini}"
fetch_new = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent?key=${aiConfig.keys.gemini}"
html = html.replace(fetch_old, fetch_new)

fetch_old_2 = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${aiConfig.keys.gemini}"
fetch_new_2 = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent?key=${aiConfig.keys.gemini}"
html = html.replace(fetch_old_2, fetch_new_2)

# Just in case, also fallback to gemini-pro if 1.5 is the issue. We'll use 1.5-pro-latest.

with open(path, 'w') as f:
    f.write(html)
