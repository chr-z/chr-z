<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7C3AED,50:A855F7,100:F97316&height=180&section=header&text=Christian%20Eliel&fontSize=42&fontColor=ffffff&desc=Software%20Engineer%20%C2%B7%20Fullstack%20%2B%20Data%20Science&descSize=16&descColor=e8eaf0&animation=fadeIn" width="100%" />

[![Solaris v2](https://img.shields.io/badge/SOLARIS-v2_shipped-F97316?style=for-the-badge)](https://github.com/chr-z/solaris-av-engine)
[![10 SaaS no ar](https://img.shields.io/badge/portfolio-10_SaaS_live-7C3AED?style=for-the-badge)](#-portfolio--saas-fleet)
[![CI](https://img.shields.io/badge/CI-green_on_all_repos-34D399?style=for-the-badge&logo=githubactions)](https://github.com/chr-z?tab=repositories&q=&type=source)

🇧🇷 [Ler em Português](README.pt-br.md)

</div>

# Hello, I'm Christian!

### Software Engineer | Fullstack & Data Science | Polyglot-stack builder

I solve real-world problems with high-performance code — from broadcast-grade
media DSP running at 60fps in the browser to zero-dependency PWA products that
work offline on a $50 phone. I ship, measure, and iterate.

**Currently:** building a 12-product SaaS fleet (each in a different language/stack),
plus a TypeScript+React AV analysis engine serving production traffic.

---

## 🚀 Flagship: Solaris — AV Analysis Engine

> **Production-proven** — deployed at **Gran** (EdTech), automating Audiovisual QA
> for pipelines delivering thousands of hours of content per month.

A "Single Pane of Glass" platform centralizing technical validation of media assets.
v2 shipped in Aug/2026: i18n (EN/PT-BR), installable offline-first PWA, WCAG-oriented
a11y, QC report export, A/B comparative mode, Pro licensing.

| Layer | Engineering |
|---|---|
| 🔬 **Client-side DSP** | Real-time RGB Parade / Waveform / Vectorscope via Canvas (`willReadFrequently`), FFT spectrograms via Web Audio API + `requestAnimationFrame`, 60fps without WebGL |
| 🌐 **Middleware & Streaming** | Node.js serverless proxy handling HTTP 206 byte-range seeking over Google Drive & YouTube sources; Sheets API gateway with TTL caching |
| ⚡ **Concurrency & State** | Firebase RTDB optimistic locking + presence for multi-analyst queues; hybrid L1/L2 waveform caching |
| ✅ **Quality** | Vitest (129 tests), ESLint ratchet CI, secret-scan, code-split bundles |

→ [Live demo](https://solaris-av-engine.vercel.app) · [Repository](https://github.com/chr-z/solaris-av-engine)

---

## 💼 Portfolio — SaaS Fleet

Ten production apps. Every single one: mobile-first, offline-capable PWA,
i18n EN/PT-BR, tested, CI-deployed to GitHub Pages — and **each in a different
language/stack**, because range is the point.

_Sixteen products shipped and counting — see the fleet below._

| Product | What it does | Stack |
|---|---|---|
| [Propostly](https://chr-z.github.io/propostaja/) | Client-ready proposals in minutes | JavaScript (vanilla) |
| [PriceCraft](https://chr-z.github.io/pricecraft/) | Cost-plus & value-based pricing for makers | Rust → WASM |
| [ContractKit](https://chr-z.github.io/contractkit/) | Freelancer contracts & receipts | ClojureScript |
| [LinkForge](https://chr-z.github.io/linkforge/) | Seller bio-link + WhatsApp CTA + catalog | SolidJS |
| [MenuPulse](https://chr-z.github.io/menupulse/) | QR digital menu that sells more | Gleam/Lustre |
| [ResumeForge](https://chr-z.github.io/resumeforge/) | ATS-friendly resume builder | Python (Pyodide/WASM) |
| [DebtFree](https://chr-z.github.io/debtfree/) | Snowball debt payoff planner | Svelte 5 (runes) |
| [RaffleMint](https://chr-z.github.io/rafflemint/) | Transparent verifiable giveaways | Elm |
| [Tably](https://chr-z.github.io/tably/) | Offline sales ledger for stalls & salons | TypeScript (no framework) |
| [SheetBound](https://chr-z.github.io/sheetbound/) | Printable TTRPG character sheets | Go (TinyGo → WASM) |
| [UnitForge](https://chr-z.github.io/unitforge/) | Offline unit converter — pure C engine compiled to WebAssembly | C → WASM (zig cc) |
| [ZigZip](https://chr-z.github.io/zigzip/) | Offline image squeezer — downscale, grayscale & quantize | Zig → WebAssembly (`zig build-exe`) |
| [NimNote](https://chr-z.github.io/nimnote/) | Instant-search local notes — search engine written in Nim, compiled to JS | Nim → JavaScript (`nim js`) |
| [PrologPricing](https://chr-z.github.io/prologpricing/) | Declarative pricing & discount rules engine — the .pl IS the engine | Prolog (Trealla → WASM) |
| [LuaLoop](https://chr-z.github.io/lualoop/) | Pomodoro whose rules are live-editable Lua scripts — real Lua 5.3 VM on WASM | Lua 5.3 → WASM (Fengari) |
| [LambdaHabits](https://chr-z.github.io/lambdahabits/) | Habit tracker — engine written in PureScript, compiled to plain JS | PureScript → JavaScript |
| [LedgerLoom](https://chr-z.github.io/ledgerloom/) | Freelancer ledger — accounting core is real PHP 8.4 running in-browser | PHP 8.4 → WASM (php-wasm) |
| [MainframeMint](https://chr-z.github.io/mainframemint/) | Mainframe money math — compound, amortization & savings computed by a real GnuCOBOL engine | COBOL (GnuCOBOL 3.1.2) |
| [OCamlCalc](https://chr-z.github.io/ocamlcalc/) | Exact financial calculator - loans, savings & compound interest by an OCaml engine compiled to JS, zero floats | OCaml -> JavaScript (js_of_ocaml) |

Also open-sourced: [Rubethyst Snap](https://github.com/chr-z/rubethyst-snap) —
yt-dlp/ffmpeg download engine as a library + FastAPI + Celery stack with SSE progress,
signed delivery URLs and abuse controls.

---

## 🛠️ Tech Stack

**Core**
![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![NodeJS](https://img.shields.io/badge/node.js-%2343853D.svg?style=for-the-badge&logo=node.js&logoColor=white)
![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)

**Polyglot portfolio**
![Rust](https://img.shields.io/badge/rust-%23000000.svg?style=for-the-badge&logo=rust&logoColor=white)
![Go](https://img.shields.io/badge/go-%2300ADD8.svg?style=for-the-badge&logo=go&logoColor=white)
![Svelte](https://img.shields.io/badge/svelte-%23f1413d.svg?style=for-the-badge&logo=svelte&logoColor=white)
![Elm](https://img.shields.io/badge/elm-%231291DB.svg?style=for-the-badge&logo=elm&logoColor=white)
![Clojure](https://img.shields.io/badge/clojurescript-%235881C4.svg?style=for-the-badge&logo=clojure&logoColor=white)
![Solid](https://img.shields.io/badge/solidjs-2c4f7c?style=for-the-badge&logo=solid&logoColor=blue)
![Lua](https://img.shields.io/badge/lua-%232C2D72.svg?style=for-the-badge&logo=lua&logoColor=white)

**Infra & Data**
![Firebase](https://img.shields.io/badge/Firebase-039BE5?style=for-the-badge&logo=Firebase&logoColor=white)
![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)
![Vercel](https://img.shields.io/badge/vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)

---

## 📫 Contact

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/christianmaciel/)
📧 **christian@chr-z.dev**

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:F97316,50:A855F7,100:7C3AED&height=100&section=footer" width="100%" />
