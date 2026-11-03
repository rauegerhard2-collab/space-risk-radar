import assert from "node:assert/strict";
import { chromium } from "playwright";

const browser = await chromium.launch({ headless: true });
const errors = [];
try {
  const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
  page.on("pageerror", error => errors.push(error.message));
  await page.goto("http://127.0.0.1:4173/", { waitUntil: "networkidle" });

  assert.match(await page.title(), /Space Risk Radar/);
  assert.equal(await page.locator(".kpi").count(), 4, "four KPI cards should render");

  await page.locator(".kpi").first().click();
  await page.waitForSelector("#detail-dialog[open]");
  assert.match(await page.locator("#dialog-title").innerText(), /Katalogisierte Objekte/);
  await page.locator("#dialog-close").click();
  await page.waitForFunction(() => !document.querySelector("#detail-dialog").open);

  await page.locator('#chart-controls button[data-key="large"]').click();
  assert.match(await page.locator("#chart-note").innerText(), /Modellierte Population/);
  assert.ok(await page.locator("#trend-chart .chart-point").count() >= 1);

  const orbitA = page.locator('[data-orbit-layer="a"]').first();
  await page.locator('.layer-controls input[data-layer="a"]').uncheck();
  assert.equal(await orbitA.evaluate(el => getComputedStyle(el).display), "none");
  await page.locator('.layer-controls input[data-layer="a"]').check();

  await page.locator("#refresh-source-health").click();
  await page.waitForFunction(() => document.querySelectorAll("#health-grid .health-card").length === 3);
  assert.match(await page.locator("#health-grid").innerText(), /CelesTrak/);
  assert.match(await page.locator("#health-grid").innerText(), /OrbitalWiki/);

  await page.setViewportSize({ width: 390, height: 844 });
  await page.waitForTimeout(150);
  const dimensions = await page.evaluate(() => ({
    viewport: document.documentElement.clientWidth,
    content: document.documentElement.scrollWidth
  }));
  assert.ok(dimensions.content <= dimensions.viewport + 2,
    `mobile layout overflows horizontally: ${JSON.stringify(dimensions)}`);

  assert.deepEqual(errors, [], "no uncaught browser JavaScript errors");
  console.log("PASS: dashboard smoke test (desktop + mobile, interactions, source health, console)");
} finally {
  await browser.close();
}
