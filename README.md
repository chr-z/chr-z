# Olá, sou o Christian! 👋

### Engenheiro de Software | Fullstack & Data Science

Sou um Engenheiro de Software focado em **resolver problemas reais** através de código de alta performance. Minha abordagem combina a visão analítica de **Ciência de Dados** com a capacidade de construção de **Engenharia de Software**.

Atualmente, busco desafios como **Desenvolvedor Fullstack/Backend** para criar ferramentas que geram eficiência e impacto.

---

### 🚀 Case de Sucesso: Solaris

> **MVP em Produção** implementado na operação do setor de Análise de Qualidade Audiovisual da EdTech **Gran Concursos**.

Desenvolvi uma plataforma de **Análise Audiovisual** que centraliza o fluxo de trabalho de transmissão e validação técnica de qualidade.

* **O Problema:** Workflow fragmentado, dependência de players locais e falta de instrumentação técnica padronizada.
* **A Solução:** Um Hub web-based que integra gestão de tarefas (W.O.), streaming seguro e instrumentação técnica (DSP) em tempo real.

#### 🛠️ Arquitetura & Engenharia
O projeto utiliza uma arquitetura híbrida focada em performance de renderização e integridade de dados:

* **🔬 Core DSP (Client-Side):**
    * **Vídeo:** Processamento de pixel data via **Canvas API** otimizado com `willReadFrequently: true` para gerar Osciloscópios (RGB/Waveform) e Vetorscópios a 15fps sem drop de frames.
    * **Áudio:** Decodificação progressiva de `AudioBuffer` utilizando **Web Audio API** e `requestAnimationFrame` para evitar bloqueio da Main Thread durante a geração de espectrogramas.
    * **Cache Híbrido:** Sistema de persistência de análise (Waveform Data) distribuído entre **LocalStorage** (L1) e **Firebase** (L2) para evitar reprocessamento de assets pesados.

* **🌐 Middleware & Streaming (Vercel Serverless):**
    * **Streaming Proxy:** Implementação manual de **Byte-Range Requests** (`HTTP 206 Partial Content`) em Node.js para permitir *seeking* eficiente em vídeos privados do Google Drive e YouTube, contornando restrições rígidas de CORS.
    * **API Gateway:** Camada de abstração para a Google Sheets API com cache *server-side* (TTL) para reduzir latência e consumo de quota.

* **⚡ Concorrência & Estado (Firebase):**
    * **Lock Otimista:** Sistema de travamento de registros em tempo real via **Realtime Database** para impedir que múltiplos analistas editem a mesma Ordem de Serviço simultaneamente.
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
