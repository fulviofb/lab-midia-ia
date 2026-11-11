// Uso: node still.mjs <pagina.html> <prefixo> t1 t2 ...
// Salva PNGs nos tempos pedidos e confere se o mesmo t gera o mesmo quadro.
import { chromium } from 'playwright';
import { pathToFileURL } from 'node:url';
import path from 'node:path';
import { createHash } from 'node:crypto';

const [page_, prefix, ...ts] = process.argv.slice(2);
const browser = await chromium.launch({
  // CHROME_PATH: Chrome do sistema (opcional). ANGLE: swiftshader (nuvem/Linux sem GPU) ou d3d11 (Windows).
  executablePath: process.env.CHROME_PATH || undefined,
  args: [`--use-angle=${process.env.ANGLE || 'swiftshader'}`, '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--allow-file-access-from-files'],
});
const page = await browser.newPage({ viewport: { width: 960, height: 540 } });
const errors = [];
page.on('pageerror', e => errors.push(String(e)));
page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
await page.goto(pathToFileURL(path.resolve(page_)).href);
await page.waitForFunction(() => typeof window.renderAt === 'function');
const canvas = await page.$('canvas');
const h = b => createHash('md5').update(b).digest('hex').slice(0, 8);
for (const t of ts.map(Number)) {
  await page.evaluate(t => window.renderAt(t), t);
  const a = await canvas.screenshot({ path: `${prefix}-${t}.png` });
  await page.evaluate(t => window.renderAt(1.0), 0);
  await page.evaluate(t => window.renderAt(t), t);
  const b = await canvas.screenshot();
  console.log(`t=${t} hash1=${h(a)} hash2=${h(b)} igual=${h(a) === h(b)}`);
}
console.log('erros:', errors.slice(0, 5));
await browser.close();
