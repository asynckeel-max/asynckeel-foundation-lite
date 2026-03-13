from fastapi import FastAPI
from app.core.settings import settings
from app.api.v1.router import router as api_router
from app.api.v1 import organizations
from app.api.v1.auth import router as auth_router
from app.core.middleware import log_requests

app = FastAPI(title="AsyncKeel Foundation Lite")

app.middleware("http")(log_requests)

# Core API router
app.include_router(api_router, prefix="/api/v1")

# Auth
app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"])

# Organizations
app.include_router(
    organizations.router,
    prefix="/api/v1/orgs",
    tags=["organizations"]
)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/info")
async def info():
    return {
        "app": settings.APP_NAME,
        "env": settings.ENV,
    }