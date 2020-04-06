import time
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from .common import request_ctx


class RequestScopeMiddleware(BaseHTTPMiddleware):
    operation_id: int = 0
    """
    Adds 'start_time' and 'operation_id' to request scope.
    """
    async def dispatch(
            self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        RequestScopeMiddleware.operation_id += 1
        request_ctx.set(request)
        request.scope['start_time'] = time.time()
        request.scope['operation_id'] = RequestScopeMiddleware.operation_id
        response = await call_next(request)
        return response
