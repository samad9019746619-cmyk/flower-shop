@echo off
title JARVIS Launcher
echo ==========================================
echo Starting JARVIS AI System...
echo ==========================================

echo Starting Backend Server...
start cmd /k "python -m backend.main"

echo Starting Frontend HUD...
cd frontend
start cmd /k "npm run dev"

echo ==========================================
echo JARVIS is initializing...
echo ==========================================
pause
