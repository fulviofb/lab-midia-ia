// Mostra qual renderizador o WebGL2 do Chrome está usando (GPU real ou SwiftShader).
import { chromium } from 'playwright';
const b = await chromium.launch({ executablePath: process.env.CHROME_PATH || undefined,
  args: [`--use-angle=${process.env.ANGLE || 'swiftshader'}`, '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
const p = await b.newPage();
const r = await p.evaluate(() => { const gl = document.createElement('canvas').getContext('webgl2'); if (!gl) return 'sem WebGL2';
  const e = gl.getExtension('WEBGL_debug_renderer_info'); return e ? gl.getParameter(e.UNMASKED_RENDERER_WEBGL) : gl.getParameter(gl.RENDERER); });
console.log(`ANGLE=${process.env.ANGLE} -> ${r}`);
await b.close();
