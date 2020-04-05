import time
import typing

from pydantic import BaseModel as PyBaseModel
from fastapi.responses import JSONResponse
from starlette.background import BackgroundTask


class CustomResponse(JSONResponse):
    start_time = None
    operation_id = None

    def __init__(
            self,
            content: typing.Any = None,
            status_code: int = 200,
            headers: dict = None,
            media_type: str = None,
            background: BackgroundTask = None,
    ) -> None:
        self.body = None
        self.content = content
        self.status_code = status_code
        self.headers_ = headers
        if media_type is not None:
            self.media_type = media_type
        self.background = background
        self.raw_headers = []

    async def __call__(self, scope, *args) -> None:

        if isinstance(self.content, dict):
            self.start_time = scope.get('start_time')
            self.operation_id = scope.get('operation_id')

            if self.start_time:
                operation_time = time.time() - self.start_time
                self.content['operation_time'] = operation_time

            if self.operation_id:
                self.content['operation_id'] = self.operation_id

        self.body = self.render(self.content)
        self.init_headers()

        await super().__call__(scope, *args)

class BaseModel(PyBaseModel):
    operation_id: int = None
    operation_time: int = None

