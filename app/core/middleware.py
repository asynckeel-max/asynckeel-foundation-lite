import time
from fastapi import Request


async def log_requests(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    print(
        f"{request.method} {request.url.path} "
        f"status={response.status_code} "
        f"time={process_time:.4f}s"
    )

    return response