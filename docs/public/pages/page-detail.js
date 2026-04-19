// Page Detail — Preview/Source Code Toggle + Copy
// Shared by all page detail pages in the gallery

// Inject styles once
(function() {
  var style = document.createElement('style');
  style.textContent = [
    '#code-panel{position:relative}',
    '#code-panel pre{position:relative;padding-top:36px}',
    '.copy-btn{position:absolute;top:12px;right:12px;z-index:5;padding:4px 12px;border:1px solid rgba(255,255,255,.1);border-radius:6px;background:rgba(255,255,255,.06);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);color:rgba(255,255,255,.45);font-size:12px;cursor:pointer;transition:all .2s;font-family:inherit;line-height:1.5}',
    '.copy-btn:hover{background:rgba(255,255,255,.1);color:rgba(255,255,255,.8);border-color:rgba(255,255,255,.2)}',
    '.copy-btn.copied{background:rgba(34,197,94,.12);border-color:rgba(34,197,94,.3);color:#22c55e}',
    '.copy-btn.error{background:rgba(239,68,68,.12);border-color:rgba(239,68,68,.3);color:#ef4444}'
  ].join('\n');
  document.head.appendChild(style);
})();

function showPreview() {
  var preview = document.getElementById('preview-panel');
  var code = document.getElementById('code-panel');
  if (preview) preview.style.display = 'block';
  if (code) code.style.display = 'none';
  document.querySelectorAll('.action-btn').forEach(function(b, i) {
    b.classList.toggle('active', i === 0);
  });
}

function showCode() {
  var preview = document.getElementById('preview-panel');
  var code = document.getElementById('code-panel');
  if (preview) preview.style.display = 'none';
  if (code) code.style.display = 'block';
  document.querySelectorAll('.action-btn').forEach(function(b, i) {
    b.classList.toggle('active', i === 1);
  });

  var iframe = document.querySelector('#preview-panel iframe');
  var sourcePath = iframe ? iframe.getAttribute('src') : null;
  if (!sourcePath) return;

  var codeContent = document.getElementById('code-content');
  if (!codeContent) return;

  codeContent.textContent = '加载中...';
  fetch(sourcePath)
    .then(function(r) { return r.text(); })
    .then(function(t) { codeContent.textContent = t; })
    .catch(function(e) { codeContent.textContent = '加载失败: ' + e.message; });
}

function copySourceCode() {
  var codeContent = document.getElementById('code-content');
  var btn = document.getElementById('copy-btn');
  if (!codeContent || !btn) return;

  var text = codeContent.textContent;
  if (!text || text === '加载中...') return;

  // Strategy 1: navigator.clipboard API
  try {
    if (navigator.clipboard && typeof navigator.clipboard.writeText === 'function') {
      navigator.clipboard.writeText(text).then(function() {
        showCopied(btn);
      }).catch(function() {
        fallbackCopy(text, btn);
      });
      return;
    }
  } catch(e) {}

  // Strategy 2: execCommand
  fallbackCopy(text, btn);
}

function fallbackCopy(text, btn) {
  var textarea = document.createElement('textarea');
  textarea.value = text;
  textarea.setAttribute('readonly', '');
  textarea.style.cssText = 'position:fixed;left:-9999px;top:-9999px;opacity:0';
  document.body.appendChild(textarea);

  textarea.contentEditable = true;
  textarea.readOnly = true;
  var range = document.createRange();
  range.selectNode(textarea);
  var sel = window.getSelection();
  sel.removeAllRanges();
  sel.addRange(range);
  textarea.setSelectionRange(0, Math.min(text.length, 50000));

  var ok = false;
  try { ok = document.execCommand('copy'); } catch(e) {}
  document.body.removeChild(textarea);

  if (ok) {
    showCopied(btn);
  } else {
    // Fallback: select code content, user presses Ctrl+C
    btn.innerHTML = '⚠️ 请按 Ctrl+C';
    btn.classList.add('error');
    var codeEl = document.getElementById('code-content');
    if (codeEl) {
      var r = document.createRange();
      r.selectNodeContents(codeEl);
      var s = window.getSelection();
      s.removeAllRanges();
      s.addRange(r);
    }
    setTimeout(function() {
      btn.innerHTML = '📋 复制源码';
      btn.classList.remove('error');
      window.getSelection().removeAllRanges();
    }, 3000);
  }
}

function showCopied(btn) {
  btn.innerHTML = '✅ 已复制';
  btn.classList.add('copied');
  setTimeout(function() {
    btn.innerHTML = '📋 复制源码';
    btn.classList.remove('copied');
  }, 2000);
}
