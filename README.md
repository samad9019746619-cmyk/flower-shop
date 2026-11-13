# J.A.R.V.I.S. // Extreme Personal AI for Windows

An Iron-Man-inspired, full-stack personal AI assistant built for Windows. Features voice recognition, computer control, long-term memory, web intelligence, a plugin system, and a futuristic sci-fi React HUD wrapped in Electron.

---

## Architecture & Phases

- **Phase 1**: Backend Core (FastAPI, WebSockets, Wake Word, VAD, Whisper STT, Edge-TTS, Provider-agnostic LLM Brain).
- **Phase 2**: Computer Control (PyAutoGUI, PyWinAuto, Application Manager, Desktop Actions).
- **Phase 3**: Intelligence & Memory (SQLite + ChromaDB long-term memory, DuckDuckGo search, Plugin Loader, Scheduler).
- **Phase 4**: Sci-Fi HUD Frontend (React + Vite + Tailwind + Three.js + Electron).

---

## Setup & Running

1. **Install Python Requirements**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Configure Environment**:
   Copy `.env.example` to `.env` and add your API keys.
3. **Install Frontend Dependencies**:
   ```cd frontend && npm install```
4. **Start JARVIS**:
   Simply run `start.bat` from the root folder, or start backend (`python -m backend.main`) and frontend (`cd frontend && npm run dev`) separately.
