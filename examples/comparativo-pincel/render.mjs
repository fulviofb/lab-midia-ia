// Uso: node render.mjs <pagina.html> <saida.mp4>
// Renderiza 5 s a 30 fps quadro a quadro e codifica direto (JPEG q92 -> ffmpeg).
import { chromium } from 'playwright';
import { spawn } from 'node:child_process';
import { pathToFileURL } from 'node:url';
import path from 'node:path';

const [page_, out] = process.argv.slice(2);
const FPS = 30, DUR = 5, N = FPS * DUR;

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

const tmp = out.replace(/\.mp4$/, '.tmp.mp4');
const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
  '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', tmp], { stdio: ['pipe', 'inherit', 'inherit'] });

const canvas = await page.$('canvas');
const times = [];
for (let i = 0; i < N; i++) {
  const t0 = performance.now();
  await page.evaluate(t => window.renderAt(t), i / FPS);
  times.push(performance.now() - t0);
  const buf = await canvas.screenshot({ type: 'jpeg', quality: 92 });
  if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
}
ff.stdin.end();
const code = await new Promise(r => ff.on('close', r));
await browser.close();

const avg = times.reduce((a, b) => a + b, 0) / times.length;
const max = Math.max(...times);
console.log(JSON.stringify({ page: page_, ffmpeg: code, ms_por_quadro_medio: +avg.toFixed(1), ms_max: +max.toFixed(1), erros: errors.slice(0, 5) }));
if (code === 0) { const fs = await import('node:fs'); fs.renameSync(tmp, out); }
