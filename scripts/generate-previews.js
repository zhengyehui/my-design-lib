#!/usr/bin/env node
/**
 * My Design Lib — Preview Generator
 *
 * 用 Playwright 对每个组件 × 每个 variant × [light/dark] 截图,
 * 输出到 docs/public/preview/<name>-<variant>-<theme>.webp
 *
 * 用法:
 *   npm run previews              # 生成所有组件
 *   npm run previews -- button    # 只生成 button
 *   npm run previews -- --clean   # 先清空 preview 目录
 *
 * 依赖: playwright (devDep)
 */

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const COMPONENTS_DIR = path.join(ROOT, 'src', 'components');
const TOKENS_CSS = path.join(ROOT, 'src', 'tokens', 'tokens.css');
const MANIFEST_PATH = path.join(ROOT, 'ai-manifest.json');
const OUT_DIR = path.join(ROOT, 'docs', 'public', 'preview');

const VIEWPORT = { width: 960, height: 600 };

function loadManifest() {
  return JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf8'));
}

function readTokens() {
  return fs.readFileSync(TOKENS_CSS, 'utf8');
}

function readComponent(name) {
  const file = path.join(COMPONENTS_DIR, name, `${name}.html`);
  if (!fs.existsSync(file)) return null;
  return fs.readFileSync(file, 'utf8');
}

function extractVariant(content, variant) {
  const startMarker = `<!-- variant: ${variant} -->`;
  const endMarker = '<!-- /variant -->';
  const start = content.indexOf(startMarker);
  if (start === -1) return null;
  const end = content.indexOf(endMarker, start);
  if (end === -1) return null;
  return content.slice(start, end + endMarker.length);
}

function buildPage(componentHtml, tokensCss, theme) {
  return `<!DOCTYPE html>
<html lang="en" data-theme="${theme}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>${tokensCss}</style>
<style>
  body {
    margin: 0;
    padding: 40px;
    background: var(--color-bg);
    color: var(--color-text);
    font-family: var(--font-sans);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .preview-host { max-width: 800px; width: 100%; }
</style>
</head>
<body>
<div class="preview-host">
${componentHtml}
</div>
</body>
</html>`;
}

async function main() {
  const args = process.argv.slice(2);
  const filterName = args.find((a) => !a.startsWith('--'));
  const shouldClean = args.includes('--clean');

  if (shouldClean && fs.existsSync(OUT_DIR)) {
    fs.rmSync(OUT_DIR, { recursive: true, force: true });
  }
  fs.mkdirSync(OUT_DIR, { recursive: true });

  let playwright;
  try {
    playwright = require('playwright');
  } catch (err) {
    console.error('❌ playwright 未安装。先运行: npm i -D playwright && npx playwright install chromium');
    process.exit(1);
  }

  const manifest = loadManifest();
  const tokens = readTokens();
  const components = manifest.components.filter((c) => !filterName || c.name === filterName);

  const browser = await playwright.chromium.launch();
  const context = await browser.newContext({ viewport: VIEWPORT, deviceScaleFactor: 2 });
  const page = await context.newPage();

  let generated = 0;
  let skipped = 0;

  for (const comp of components) {
    const source = readComponent(comp.name);
    if (!source) {
      console.warn(`⚠️  ${comp.name}: HTML 文件缺失,跳过`);
      skipped++;
      continue;
    }

    const variants = comp.variants && comp.variants.length ? comp.variants : ['default'];

    for (const variant of variants) {
      let block = extractVariant(source, variant);
      if (!block) block = source; // 没有 variant 标记就用整个文件

      for (const theme of ['light', 'dark']) {
        const html = buildPage(block, tokens, theme);
        const filename = `${comp.name}-${variant}-${theme}.webp`;
        const outPath = path.join(OUT_DIR, filename);
        await page.setContent(html, { waitUntil: 'networkidle' });
        await page.screenshot({ path: outPath, type: 'webp', quality: 85, fullPage: false });
        generated++;
        if (generated % 10 === 0) {
          process.stdout.write(`  · generated ${generated}...\n`);
        }
      }
    }
  }

  await browser.close();
  console.log(`\n✅ 生成完成: ${generated} 张,跳过 ${skipped}`);
  console.log(`   输出目录: ${path.relative(ROOT, OUT_DIR)}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
