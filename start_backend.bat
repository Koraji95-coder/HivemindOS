@echo off
echo 🚀 Starting HivemindOS backend...
uvicorn backend.fastapi_main:app --reload
pause
