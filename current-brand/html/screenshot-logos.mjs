import puppeteer from 'puppeteer-core';
import { fileURLToPath } from 'url';
import path from 'path';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const logoPath = path.join(__dirname, 'logo.html');
const outputDir = path.join(__dirname, '..', 'logo-pngs');

const browser = await puppeteer.launch({
  executablePath: '/root/.cache/ms-playwright/chromium-1194/chrome-linux/chrome',
  args: ['--no-sandbox', '--disable-setuid-sandbox'],
  headless: true,
});

const page = await browser.newPage();
await page.setViewport({ width: 1600, height: 1200, deviceScaleFactor: 3 });
await page.goto(`file://${logoPath}`, { waitUntil: 'networkidle0' });

// Make output dir
const fs = await import('fs');
fs.mkdirSync(outputDir, { recursive: true });

// 1. Full logo on dark background (primary)
const darkPrimary = await page.$('.logo-stage-dark .mark-monogram.size-lg');
await darkPrimary.screenshot({ path: path.join(outputDir, 'logo-dark-primary.png'), omitBackground: true });
console.log('Saved: logo-dark-primary.png');

// 2. Full logo on light/white background
const stages = await page.$$('.logo-stage-light .mark-monogram.size-lg');
if (stages.length > 0) {
  await stages[0].screenshot({ path: path.join(outputDir, 'logo-light.png'), omitBackground: true });
  console.log('Saved: logo-light.png');
}

// 3. Full logo on cream background
const creamStage = await page.$('.logo-stage-cream .mark-monogram.size-lg');
await creamStage.screenshot({ path: path.join(outputDir, 'logo-cream.png'), omitBackground: true });
console.log('Saved: logo-cream.png');

// 4. Icon only - large - dark bg
const iconDarkLg = await page.$('.logo-stage-dark .icon-only-lg .mark-monogram-icon');
await iconDarkLg.screenshot({ path: path.join(outputDir, 'icon-dark-large.png'), omitBackground: true });
console.log('Saved: icon-dark-large.png');

// 5. Icon only - large - light bg
const iconLightLg = await page.$('.logo-stage-light .icon-only-lg .mark-monogram-icon');
await iconLightLg.screenshot({ path: path.join(outputDir, 'icon-light-large.png'), omitBackground: true });
console.log('Saved: icon-light-large.png');

// 6. Full stage screenshots (with background) for context
const allStages = await page.$$('.logo-stage');
const stageNames = ['stage-dark-primary', 'stage-light', 'stage-cream', 'stage-sizes', 'stage-icons-dark', 'stage-icons-light'];
for (let i = 0; i < allStages.length; i++) {
  await allStages[i].screenshot({ path: path.join(outputDir, `${stageNames[i]}.png`) });
  console.log(`Saved: ${stageNames[i]}.png`);
}

await browser.close();
console.log(`\nAll PNGs saved to: ${outputDir}`);
