> 🇧🇷 [Ler em Português](README.pt-br.md)

# Hello, I'm Christian! 👋

### Software Engineer | Fullstack & Data Science

I am a Software Engineer focused on **solving real-world problems** through high-performance code. My approach combines the analytical mindset of **Data Science** with the build capacity of **Software Engineering**.

Currently seeking my next challenge as a **Fullstack/Backend Developer** to build efficient and impactful tools.

---

### 🚀 Case Study: Solaris

> **Strategic MVP** deployed in production at **Gran** (EdTech), automating the Audiovisual Quality Assurance sector.

I architected and developed a **"Single Pane of Glass"** platform that centralizes the technical validation workflow for media assets. The system replaced a fragmented workflow dependent on local players and manual spreadsheets with a unified, high-performance web hub.

#### 🛠️ Engineering & Architecture
The project utilizes a hybrid architecture focused on rendering performance, data integrity, and secure streaming:

* **🔬 Core DSP (Client-Side):**
    * **Video:** Implemented real-time pixel data processing using the **Canvas API** optimized with `willReadFrequently: true` to generate 60fps Oscilloscopes (RGB Parade, Waveform) and Vectorscopes directly in the browser.
    * **Audio:** Engineered progressive `AudioBuffer` decoding using the **Web Audio API** and `requestAnimationFrame` to render Spectrograms without blocking the main thread.
    * **Hybrid Caching:** Built a distributed persistence strategy for heavy analysis data (Waveforms), utilizing **LocalStorage** (L1) and **Firebase** (L2) to prevent redundant processing of assets.

* **🌐 Middleware & Streaming (Vercel Serverless):**
    * **Streaming Proxy:** Developed a custom **Node.js** proxy to handle **Byte-Range Requests** (`HTTP 206`), enabling instant seeking for private video assets hosted on Google Drive and YouTube while bypassing strict CORS policies.
    * **API Gateway:** Abstracted the Google Sheets API interaction via a serverless layer with server-side caching (TTL) to reduce latency and API quota consumption.

* **⚡ Concurrency & State (Firebase):**
    * **Optimistic Locking:** Implemented a real-time locking mechanism via **Firebase Realtime Database** to prevent race conditions and data overrides when multiple analysts edit the same Work Order simultaneously.
    * **Presence:** Real-time user monitoring and active cursor tracking.

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

### 📫 Contact

* [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/christianmaciel/)
* 📧 **Email:** christian@chr-z.dev
