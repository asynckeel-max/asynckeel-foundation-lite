from fastapi import FastAPI

app = FastAPI(title="AsyncKeel Foundation Lite")

@app.get("/health")
async def health_check():
    return {"status": "ok"}
