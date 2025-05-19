# logs_router.py 📄
# Handles receiving frontend session logs (prompt/response)

from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/save")
async def save_log(request: Request):
    data = await request.json()
    print("🧠 Log Received:", data)  # This could be saved to file/db instead
    return {"status": "ok"}
