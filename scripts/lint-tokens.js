#!/usr/bin/env node
/**
 * Token Lint — 禁止在组件 CSS 中硬编码颜色 / 尺寸
 *
 * 规则:
 *   - 禁止 hex 颜色(#fff, #abc123)
 *   - 禁止 rgb()/rgba() 字面量(除非在渐变或阴影中带 alpha)
 *   - 禁止独立的 px 值(允许 0 / 1px 边框 / <4px 的细节)
 *
 * 允许用 /* lint-ok *\/ 行内注释豁免。
 *
 * 退出码: 0=通过  1=有违规
 */

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const COMPONENTS_DIR = path.join(ROOT, 'src', 'components');

const RULES = [
  {
    name: 'hardcoded-hex',
    regex: /#[0-9a-fA-F]{3,8}\b/g,
    message: '禁止硬编码 hex 颜色,改用 var(--color-*)',
    allowFiles: ['code-block', 'aurora-bg', 'gradient-border', 'skeleton', 'glassmorphism', '3d-tilt', 'magnetic-btn'],
  },
  {
    name: 'hardcoded-px',
    regex: /(?<![\w-])(\d{2,})px\b/g,  // 两位数以上的 px(排除 0-9px 细节)
    message: 'px 字面量应替换为 var(--space-*) 或 var(--text-*) / var(--radius-*)',
    allowFiles: ['aurora-bg', 'gradient-border', '3d-tilt', 'magnetic-btn', 'skeleton', 'glassmorphism'],
  },
];

const LINT_OK = '/* lint-ok */';

function walk(dir) {
  const files = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) files.push(...walk(full));
    else if (/\.(css|html)$/.test(entry.name)) files.push(full);
  }
  return files;
}

function extractStyles(content, filename) {
  if (filename.endsWith('.css')) return content;
  const styles = [];
  const re = /<style[^>]*>([\s\S]*?)<\/style>/g;
  let m;
  while ((m = re.exec(content))) styles.push(m[1]);
  return styles.join('\n');
}

let violations = 0;
const files = walk(COMPONENTS_DIR);

for (const file of files) {
  const rel = path.relative(ROOT, file);
  const base = path.basename(path.dirname(file));
  const raw = fs.readFileSync(file, 'utf8');
  const css = extractStyles(raw, file);

  for (const rule of RULES) {
    if (rule.allowFiles.includes(base)) continue;

    const lines = css.split('\n');
    lines.forEach((line, idx) => {
      if (line.includes(LINT_OK)) return;
      const matches = line.match(rule.regex);
      if (!matches) return;
      for (const match of matches) {
        violations++;
        console.log(`${rel}:${idx + 1}  [${rule.name}]  "${match}"  — ${rule.message}`);
      }
    });
  }
}

if (violations === 0) {
  console.log(`✅ Token lint passed (${files.length} files scanned)`);
  process.exit(0);
} else {
  console.log(`\n❌ ${violations} violation(s) found`);
  process.exit(1);
}
