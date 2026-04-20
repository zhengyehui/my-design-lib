#!/usr/bin/env node
/**
 * Size Report — 组件 CSS 体积预算
 *
 * 预算: 每组件 embedded CSS ≤ 3KB gzipped / ≤ 10KB raw
 * 超出的组件会被打印,返回退出码 1
 */

const fs = require('fs');
const path = require('path');
const zlib = require('zlib');

const ROOT = path.resolve(__dirname, '..');
const COMPONENTS_DIR = path.join(ROOT, 'src', 'components');
const BUDGET_GZIP = 3 * 1024;
const BUDGET_RAW = 10 * 1024;

function extractCss(content) {
  const parts = [];
  const re = /<style[^>]*>([\s\S]*?)<\/style>/g;
  let m;
  while ((m = re.exec(content))) parts.push(m[1]);
  return parts.join('\n');
}

const rows = [];
const components = fs.readdirSync(COMPONENTS_DIR).filter((n) => {
  const stat = fs.statSync(path.join(COMPONENTS_DIR, n));
  return stat.isDirectory();
});

for (const name of components) {
  const htmlPath = path.join(COMPONENTS_DIR, name, `${name}.html`);
  const cssPath = path.join(COMPONENTS_DIR, name, `${name}.css`);
  let css = '';
  if (fs.existsSync(htmlPath)) css = extractCss(fs.readFileSync(htmlPath, 'utf8'));
  else if (fs.existsSync(cssPath)) css = fs.readFileSync(cssPath, 'utf8');
  else continue;

  const raw = Buffer.byteLength(css, 'utf8');
  const gz = zlib.gzipSync(css).length;
  rows.push({ name, raw, gz, overBudget: gz > BUDGET_GZIP || raw > BUDGET_RAW });
}

rows.sort((a, b) => b.gz - a.gz);

const fmt = (n) => `${(n / 1024).toFixed(1)}KB`;
console.log('Component        RAW        GZIP       Status');
console.log('─'.repeat(56));
for (const r of rows) {
  const status = r.overBudget ? '❌ OVER' : '✅';
  console.log(`${r.name.padEnd(16)} ${fmt(r.raw).padEnd(10)} ${fmt(r.gz).padEnd(10)} ${status}`);
}

const over = rows.filter((r) => r.overBudget);
console.log(`\nBudget: ≤${BUDGET_GZIP / 1024}KB gzip / ≤${BUDGET_RAW / 1024}KB raw per component`);
console.log(`Total: ${rows.length} components, ${over.length} over budget`);
process.exit(over.length > 0 ? 1 : 0);
