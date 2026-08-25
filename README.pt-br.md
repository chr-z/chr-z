<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7C3AED,50:A855F7,100:F97316&height=180&section=header&text=Christian%20Eliel&fontSize=42&fontColor=ffffff&desc=Software%20Engineer%20%C2%B7%20Fullstack%20%26%20Data%20Science&descSize=16&descColor=e8eaf0&animation=fadeIn" width="100%" />

[![Solaris v2](https://img.shields.io/badge/SOLARIS-v2_no_ar-F97316?style=for-the-badge)](https://github.com/chr-z/solaris-av-engine)
[![10 SaaS no ar](https://img.shields.io/badge/portf%C3%B3lio-10_SaaS_live-7C3AED?style=for-the-badge)](#-portf%C3%B3lio--frota-saas)
[![CI](https://img.shields.io/badge/CI-verde_todos_repos-34D399?style=for-the-badge&logo=githubactions)](https://github.com/chr-z?tab=repositories&q=&type=source)

🇺🇸 [Read in English](README.md)

</div>

# Olá, eu sou o Christian!

### Software Engineer | Fullstack & Data Science | construtor poliglota

Eu resolvo problemas reais com código de alta performance — de DSP de mídia
broadcast-grade rodando a 60fps no navegador a produtos PWA sem dependências
que funcionam offline num celular simples. Eu entrego, meço e itero.

**Agora:** construindo uma frota de 12 produtos SaaS (cada um numa
linguagem/stack diferente) e um motor de análise AV em TypeScript+React
servindo tráfego de produção.

---

## 🚀 Projeto principal: Solaris — AV Analysis Engine

> **Comprovado em produção** — implantado na **Gran** (EdTech), automatizando o QA
> audiovisual de pipelines que entregam milhares de horas de conteúdo por mês.

Plataforma "Single Pane of Glass" que centraliza a validação técnica de mídias.
A v2 saiu em ago/2026: i18n (EN/PT-BR), PWA offline instalável, acessibilidade,
exportação de relatório QC, modo comparativo A/B e licenciamento Pro.

| Camada | Engenharia |
|---|---|
| 🔬 **DSP client-side** | RGB Parade / Waveform / Vectorscope em tempo real via Canvas (`willReadFrequently`), espectrogramas FFT via Web Audio API + `requestAnimationFrame`, 60fps sem WebGL |
| 🌐 **Middleware & Streaming** | Proxy serverless Node.js com seek por byte-range (HTTP 206) sobre fontes Google Drive & YouTube; gateway da Sheets API com cache TTL |
| ⚡ **Concorrência & Estado** | Optimistic locking + presença via Firebase RTDB para filas multi-analista; cache híbrido L1/L2 de waveforms |
| ✅ **Qualidade** | Vitest (129 testes), CI com lint ratchet, secret-scan, code splitting |

→ [Demo ao vivo](https://solaris-av-engine.vercel.app) · [Repositório](https://github.com/chr-z/solaris-av-engine)

---

## 💼 Portfólio — Frota SaaS

Dez apps em produção. Todos: mobile-first, PWA offline, i18n EN/PT-BR,
testados, CI → GitHub Pages — e **cada um numa linguagem/stack diferente**,
porque range técnico é o ponto.

| Produto | O que faz | Stack |
|---|---|---|
| [Propostly](https://chr-z.github.io/propostaja/) | Propostas prontas pro cliente em minutos | JavaScript (vanilla) |
| [PriceCraft](https://chr-z.github.io/pricecraft/) | Precificação custo+ e valor p/ makers | Rust → WASM |
| [ContractKit](https://chr-z.github.io/contractkit/) | Contratos e recibos p/ freelancers | ClojureScript |
| [LinkForge](https://chr-z.github.io/linkforge/) | Bio-link vendedor + WhatsApp + catálogo | SolidJS |
| [MenuPulse](https://chr-z.github.io/menupulse/) | Menu digital QR que vende mais | Gleam/Lustre |
| [ResumeForge](https://chr-z.github.io/resumeforge/) | Currículo ATS-friendly | Python (Pyodide/WASM) |
| [DebtFree](https://chr-z.github.io/debtfree/) | Plano snowball p/ sair das dívidas | Svelte 5 (runes) |
| [RaffleMint](https://chr-z.github.io/rafflemint/) | Sorteios transparentes e verificáveis | Elm |
| [Tably](https://chr-z.github.io/tably/) | Caixa offline p/ barraca e salão | TypeScript (sem framework) |
| [SheetBound](https://chr-z.github.io/sheetbound/) | Fichas de RPG imprimíveis | Go (TinyGo → WASM) |
| [UnitForge](https://chr-z.github.io/unitforge/) | Conversor de unidades offline — motor em C puro compilado para WebAssembly | C → WASM (zig cc) |
| [ZigZip](https://chr-z.github.io/zigzip/) | Espremedor de imagens offline — reduz, cinza e quantiza cores | Zig → WebAssembly (`zig build-exe`) |
| [NimNote](https://chr-z.github.io/nimnote/) | Notas locais com busca instantânea — motor de busca escrito em Nim, compilado pra JS | Nim → JavaScript (`nim js`) |
| [PrologPricing](https://chr-z.github.io/prologpricing/) | Motor declarativo de regras de preço e desconto — o .pl É o motor | Prolog (Trealla → WASM) |

Também open-source: [Rubethyst Snap](https://github.com/chr-z/rubethyst-snap) —
motor de download yt-dlp/ffmpeg como biblioteca + FastAPI + Celery, progresso SSE,
entrega com URL assinada e controles anti-abuso.

---

## 🛠️ Tech Stack

**Core**
![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![NodeJS](https://img.shields.io/badge/node.js-%2343853D.svg?style=for-the-badge&logo=node.js&logoColor=white)
![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)

**Portfólio poliglota**
![Rust](https://img.shields.io/badge/rust-%23000000.svg?style=for-the-badge&logo=rust&logoColor=white)
![Go](https://img.shields.io/badge/go-%2300ADD8.svg?style=for-the-badge&logo=go&logoColor=white)
![Svelte](https://img.shields.io/badge/svelte-%23f1413d.svg?style=for-the-badge&logo=svelte&logoColor=white)
![Elm](https://img.shields.io/badge/elm-%231291DB.svg?style=for-the-badge&logo=elm&logoColor=white)
![Clojure](https://img.shields.io/badge/clojurescript-%235881C4.svg?style=for-the-badge&logo=clojure&logoColor=white)
![Solid](https://img.shields.io/badge/solidjs-2c4f7c?style=for-the-badge&logo=solid&logoColor=blue)

**Infra & Dados**
![Firebase](https://img.shields.io/badge/Firebase-039BE5?style=for-the-badge&logo=Firebase&logoColor=white)
![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)
![Vercel](https://img.shields.io/badge/vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)

---

## 📫 Contato

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/christianmaciel/)
📧 **christian@chr-z.dev**

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:F97316,50:A855F7,100:7C3AED&height=100&section=footer" width="100%" />
