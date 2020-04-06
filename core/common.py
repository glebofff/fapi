from pydantic import BaseModel as PyBaseModel
from contextvars import ContextVar

request_ctx = ContextVar('request')


class BaseModel(PyBaseModel):
    operation_id: int = None
    operation_time: int = None

