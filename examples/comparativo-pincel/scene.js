// Cena comum aos dois motores: 960x540, 5 s a 30 fps.
// Mesma geometria e mesma linha do tempo; cada motor só decide como pintar.
const SW = 960, SH = 540, FPS = 30, DUR = 5;
const COL = { paper: '#f1e9da', ink: '#2b2520', sun: '#e08a3c', hill: '#7a9a5a', leaf: '#4f7a3a', shade: '#3d5a2c' };

// linha do horizonte (morro)
const HILL = [[0, 400], [160, 372], [330, 350], [500, 362], [680, 390], [840, 380], [960, 395]];
// polígono do morro (para preencher/hachurar)
const HILL_POLY = [...HILL, [960, 540], [0, 540]];
// tronco e galhos
const TRUNK = [[300, 362], [304, 300], [298, 240], [306, 190]];
const BRANCHES = [
  [[302, 260], [260, 225], [228, 214]],
  [[303, 230], [345, 196], [380, 188]],
  [[305, 200], [292, 165], [300, 140]],
];
// copa (centro, raio)
const CROWN = [305, 180, 70];
// sol (centro, raio)
const SUN = [720, 130, 58];

// linha do tempo: [início, fim] em segundos
const T = {
  hill: [0.0, 1.0], trunk: [0.6, 1.6], branches: [1.2, 2.2],
  sun: [2.0, 3.2], crown: [2.6, 3.8], shade: [3.2, 4.2],
};
const prog = (t, k) => Math.max(0, Math.min(1, (t - T[k][0]) / (T[k][1] - T[k][0])));
const ease = p => p < .5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2;

// recorta uma polilinha até a fração p do comprimento
function partial(pts, p) {
  if (p >= 1) return pts.map(q => q.slice());
  const L = []; let tot = 0;
  for (let i = 1; i < pts.length; i++) { const d = Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]); L.push(d); tot += d; }
  let want = tot * p; const out = [pts[0].slice()];
  for (let i = 1; i < pts.length; i++) {
    if (want >= L[i - 1]) { out.push(pts[i].slice()); want -= L[i - 1]; continue; }
    const f = want / L[i - 1];
    out.push([pts[i - 1][0] + (pts[i][0] - pts[i - 1][0]) * f, pts[i - 1][1] + (pts[i][1] - pts[i - 1][1]) * f]);
    break;
  }
  return out;
}
