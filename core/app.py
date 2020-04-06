from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from .middleware import RequestScopeMiddleware

from .orm import engine

app = FastAPI()


app.add_middleware(
    DBSessionMiddleware,
    custom_engine=engine
)

app.add_middleware(
    RequestScopeMiddleware
)