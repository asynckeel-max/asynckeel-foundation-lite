from fastapi import FastAPI
from app.core.settings import settings
from app.api.v1.router import router as api_router
from app.api.v1.auth import router as auth_router

app = FastAPI(title="AsyncKeel Foundation Lite")

app.include_router(auth_router, prefix="/api/v1/auth")
app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/info")
async def info():
    return {
        "app": settings.APP_NAME,
        "env": settings.ENV,
    }
