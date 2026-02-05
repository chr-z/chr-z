> 🇺🇸 [Read in English](README.md)

# Olá, sou o Christian! 👋

### Engenheiro de Software | Fullstack & Data Science

Sou um Engenheiro de Software focado em **resolver problemas reais** através de código de alta performance. Minha abordagem combina a visão analítica de **Ciência de Dados** com a capacidade de construção de **Engenharia de Software**.

Atualmente, busco desafios como **Desenvolvedor Fullstack/Backend** para criar ferramentas que geram eficiência e impacto.

---

### 🚀 Case de Sucesso: Solaris

> **MVP Estratégico** implementado em produção na operação da EdTech **Gran**, automatizando o setor de Garantia de Qualidade Audiovisual.

Desenvolvi uma plataforma **"Single Pane of Glass"** que centraliza o fluxo de trabalho de transmissão e validação técnica. O sistema substituiu um workflow fragmentado (baseado em players locais e planilhas manuais) por um Hub web unificado de alta performance.

#### 🛠️ Arquitetura & Engenharia
O projeto utiliza uma arquitetura híbrida focada em performance de renderização, integridade de dados e streaming seguro:

* **🔬 Core DSP (Client-Side):**
    * **Vídeo:** Processamento de dados de pixel via **Canvas API** otimizado com `willReadFrequently: true` para gerar Osciloscópios (RGB Parade, Waveform) e Vetorscópios em tempo real (60fps) diretamente no navegador.
    * **Áudio:** Engenharia de decodificação progressiva de `AudioBuffer` utilizando **Web Audio API** e `requestAnimationFrame` para renderizar Espectrogramas sem bloquear a thread principal.
    * **Cache Híbrido:** Estratégia de persistência distribuída para dados pesados de análise (Waveforms), utilizando **LocalStorage** (L1) e **Firebase** (L2) para evitar o reprocessamento de assets.

* **🌐 Middleware & Streaming (Vercel Serverless):**
    * **Streaming Proxy:** Desenvolvimento de um proxy customizado em **Node.js** para gerenciar **Byte-Range Requests** (`HTTP 206`), permitindo "seeking" instantâneo em vídeos privados do Google Drive e YouTube, contornando restrições rígidas de CORS.
    * **API Gateway:** Camada de abstração para a Google Sheets API com cache *server-side* (TTL) para reduzir latência e consumo de cota.

* **⚡ Concorrência & Estado (Firebase):**
    * **Lock Otimista:** Implementação de travamento de registros em tempo real via **Firebase Realtime Database** para impedir condições de corrida e sobrescrita de dados quando múltiplos analistas editam a mesma Ordem de Serviço.
    * **Presença:** Monitoramento de usuários online e cursores ativos.

---

### 💻 Tech Stack

**Front-end & UI**
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB) ![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white) ![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white) ![Vite](https://img.shields.io/badge/vite-%23646CFF.svg?style=for-the-badge&logo=vite&logoColor=white)

**Back-end & Serverless**
![NodeJS](https://img.shields.io/badge/node.js-%2343853D.svg?style=for-the-badge&logo=node.js&logoColor=white) ![Firebase](https://img.shields.io/badge/Firebase-039BE5?style=for-the-badge&logo=Firebase&logoColor=white) ![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)

**Data & APIs**
![Google Sheets](https://img.shields.io/badge/Google%20Sheets-34A853?style=for-the-badge&logo=google-sheets&logoColor=white) ![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)

**Tools**
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) ![VS Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

---

### 📫 Contato

* [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/christianmaciel/)
* 📧 **Email:** christian@chr-z.dev
