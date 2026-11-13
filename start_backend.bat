@echo off
title JARVIS Backend Server
cd /d "%~dp0"
echo Starting JARVIS Backend Server...
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000
pause
