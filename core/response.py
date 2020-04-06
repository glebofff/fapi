import time
from fastapi import Request
from starlette.types import Scope
import typing
from starlette.responses import JSONResponse
from .common import request_ctx


class CustomJsonResponse(JSONResponse):
    @property
    def scope(self) -> Scope:
        request = request_ctx.get()
        if not isinstance(request, Request):
            return {}

        return request.scope

    def update_content(self, content):
        scope = self.scope
        if not isinstance(content, dict) or not scope:
            return

        start_time = scope.get('start_time')
        operation_id = scope.get('operation_id')

        if start_time:
            content['operation_time'] = time.time() - start_time

        if operation_id:
            content['operation_id'] = operation_id

    def render(self, content: typing.Any) -> bytes:
        self.update_content(content)
        return super().render(content)

