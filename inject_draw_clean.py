path = '/Users/icarorodriguez/.gemini/antigravity/scratch/funil365/index.html'

with open(path, 'r') as f:
    html = f.read()

# ── 1. Remove old cvg-draw referências no HTML
html = html.replace('<svg id="cvg"></svg><svg id="cvg-draw"></svg>', '<svg id="cvg"></svg>')

# ── 2. Add a clean HTML5 canvas OUTSIDE the transformed #canvas div, but inside canvas-wrap
old_wrap = '<div id="canvas-wrap" ondragover="event.preventDefault()" ondrop="dropBlock(event)" onclick="canvasClick(event)" oncontextmenu="canvasCtx(event)">'
new_wrap = '<div id="canvas-wrap" ondragover="event.preventDefault()" ondrop="dropBlock(event)" onclick="canvasClick(event)" oncontextmenu="canvasCtx(event)">\n  <canvas id="draw-canvas" style="position:absolute;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:800;"></canvas>'
html = html.replace(old_wrap, new_wrap)

# ── 3. Remove old draw engine entirely and replace with clean canvas-based one
old_engine_start = '// ══════════════════════════════════════════\n// DRAW ENGINE\n// ══════════════════════════════════════════'
old_engine_end = "// Hook into renderCanvas\nconst _origRenderCanvas = renderCanvas;\nrenderCanvas = function() { _origRenderCanvas(); redrawnPaths(); };\n\n// Ctrl+Z undo\ndocument.addEventListener('keydown', e => {\n  if((e.ctrlKey || e.metaKey) && e.key === 'z' && drawState.active !== 'cursor') {\n    e.preventDefault();\n    undoDraw();\n  }\n});\n// ══════════════════════════════════════════"

new_engine = """// ══════════════════════════════════════════
// DRAW ENGINE (HTML5 Canvas — clean)
// ══════════════════════════════════════════
let drawState = { active: 'cursor', color: '#ef4444', size: 4 };
let _drawing = false;
let _drawCanvas = null;
let _ctx = null;

function _initDrawCanvas() {
  _drawCanvas = document.getElementById('draw-canvas');
  if(!_drawCanvas) return;
  // Resize to match canvas-wrap
  const wrap = document.getElementById('canvas-wrap');
  _drawCanvas.width = wrap.clientWidth || 1600;
  _drawCanvas.height = wrap.clientHeight || 900;
  _ctx = _drawCanvas.getContext('2d');
}

function setTool(tool) {
  drawState.active = tool;
  document.querySelectorAll('.draw-btn').forEach(e => e.classList.remove('active'));
  const btn = document.getElementById('tool-'+tool);
  if(btn) btn.classList.add('active');
  const cw = document.getElementById('canvas-wrap');
  if(tool === 'cursor') {
    cw.style.cursor = 'default';
    if(_drawCanvas) _drawCanvas.style.pointerEvents = 'none';
  } else if(tool === 'eraser') {
    cw.style.cursor = 'cell';
    if(_drawCanvas) _drawCanvas.style.pointerEvents = 'auto';
  } else {
    cw.style.cursor = 'crosshair';
    if(_drawCanvas) _drawCanvas.style.pointerEvents = 'auto';
  }
}

function setColor(el, code) {
  drawState.color = code;
  document.querySelectorAll('.draw-color').forEach(e => e.classList.remove('active'));
  el.classList.add('active');
  if(drawState.active === 'cursor') setTool('brush');
}

function setSz(el, sz) {
  drawState.size = sz;
  document.querySelectorAll('.draw-sz').forEach(e => e.classList.remove('active'));
  if(el) el.classList.add('active');
}

function setSzDot(el, sz) {
  drawState.size = sz;
  document.querySelectorAll('.draw-sz-dot').forEach(e => e.classList.remove('active'));
  if(el) el.classList.add('active');
}

function undoDraw() {
  const f = af();
  if(f && f.drawPaths && f.drawPaths.length > 0) {
    f.drawPaths.pop();
    _redrawAllPaths();
    save();
  }
}

function _redrawAllPaths() {
  if(!_ctx || !_drawCanvas) return;
  _ctx.clearRect(0, 0, _drawCanvas.width, _drawCanvas.height);
  const f = af();
  if(!f || !f.drawPaths) return;
  f.drawPaths.forEach(p => _renderStoredPath(p));
}

function _renderStoredPath(p) {
  if(!_ctx || !p.pts || p.pts.length < 2) return;
  _ctx.save();
  _ctx.beginPath();
  _ctx.strokeStyle = p.c;
  _ctx.lineWidth = p.w;
  _ctx.lineCap = 'round';
  _ctx.lineJoin = 'round';
  if(p.marker) _ctx.globalAlpha = 0.4;
  _ctx.moveTo(p.pts[0].x, p.pts[0].y);
  for(let i = 1; i < p.pts.length; i++) _ctx.lineTo(p.pts[i].x, p.pts[i].y);
  _ctx.stroke();
  _ctx.restore();
}

// ─── Event Listeners on draw-canvas ────────────────────────────────
let _currentPath = null;

function _getCanvasXY(e) {
  if(!_drawCanvas) return {x:0,y:0};
  const r = _drawCanvas.getBoundingClientRect();
  // Scale from CSS size to canvas pixel size
  const scaleX = _drawCanvas.width / r.width;
  const scaleY = _drawCanvas.height / r.height;
  return {
    x: (e.clientX - r.left) * scaleX,
    y: (e.clientY - r.top) * scaleY
  };
}

window.addEventListener('DOMContentLoaded', () => {
  _initDrawCanvas();
  window.addEventListener('resize', _initDrawCanvas);

  const dc = document.getElementById('draw-canvas');
  if(!dc) return;

  dc.addEventListener('mousedown', e => {
    if(drawState.active === 'cursor') return;
    if(e.button !== 0) return;
    _drawing = true;
    const pt = _getCanvasXY(e);
    const isMarker = drawState.active === 'marker';
    const sz = isMarker ? drawState.size * 4 : drawState.size;
    _currentPath = { c: drawState.color, w: sz, marker: isMarker, pts: [pt] };
    _ctx.save();
    _ctx.beginPath();
    _ctx.strokeStyle = _currentPath.c;
    _ctx.lineWidth = sz;
    _ctx.lineCap = 'round';
    _ctx.lineJoin = 'round';
    if(isMarker) _ctx.globalAlpha = 0.4;
    _ctx.moveTo(pt.x, pt.y);
    e.preventDefault();
    e.stopPropagation();
  });

  dc.addEventListener('mousemove', e => {
    if(!_drawing || !_currentPath) return;
    const pt = _getCanvasXY(e);
    _currentPath.pts.push(pt);
    _ctx.lineTo(pt.x, pt.y);
    _ctx.stroke();
    // Keep path open for next segment
    _ctx.beginPath();
    _ctx.moveTo(pt.x, pt.y);
  });

  dc.addEventListener('mouseup', e => {
    if(!_drawing) return;
    _drawing = false;
    if(_currentPath && _currentPath.pts.length > 1) {
      const f = af();
      if(f) {
        if(!f.drawPaths) f.drawPaths = [];
        f.drawPaths.push(_currentPath);
        save();
      }
    }
    _ctx.restore();
    _currentPath = null;
    // Redraw cleanly
    _redrawAllPaths();
  });
});

// Ctrl+Z
document.addEventListener('keydown', e => {
  if((e.ctrlKey || e.metaKey) && e.key === 'z' && drawState.active !== 'cursor') {
    e.preventDefault();
    undoDraw();
  }
});
// ══════════════════════════════════════════"""

# Find and replace the old engine block
import re
# Find from start of engine to end marker
pattern = re.compile(
    r'// ══+\n// DRAW ENGINE.*?// ══+',
    re.DOTALL
)
html = pattern.sub(new_engine, html, count=1)

# ── 4. Remove stale cvg-draw references in JS
html = html.replace("document.getElementById('cvg-draw')", "document.getElementById('draw-canvas')")
html = html.replace("const _origRenderCanvas = renderCanvas;\nrenderCanvas = function() { _origRenderCanvas(); redrawnPaths(); };", "")

with open(path, 'w') as f:
    f.write(html)

print("Done!")
