from fastapi import FastAPI
from app.core.settings import settings

app = FastAPI(title="AsyncKeel Foundation Lite")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/info")
async def info():
    return {
        "app": settings.APP_NAME,
        "env": settings.ENV,
    }
