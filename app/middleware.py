# Author: Nguyễn Công Hùng - 2A202601071
# Role: Backend (Checkpoint 1 - Correlation ID Middleware & Request Contextvars Binding)

from __future__ import annotations

import time
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from structlog.contextvars import bind_contextvars, clear_contextvars


class CorrelationIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        clear_contextvars()
        incoming_id = request.headers.get("x-request-id", "").strip()
        correlation_id = (
            incoming_id
            if len(incoming_id) == 12 and incoming_id.startswith("req-")
            and all(char in "0123456789abcdefABCDEF" for char in incoming_id[4:])
            else f"req-{uuid.uuid4().hex[:8]}"
        )
        bind_contextvars(correlation_id=correlation_id)
        request.state.correlation_id = correlation_id
        start = time.perf_counter()
        try:
            response = await call_next(request)
            response.headers["x-request-id"] = correlation_id
            response.headers["x-response-time-ms"] = str(
                round((time.perf_counter() - start) * 1000, 2)
            )
            return response
        finally:
            clear_contextvars()
