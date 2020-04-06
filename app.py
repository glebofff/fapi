from core.app import app as coreapp
from core.response import CustomJsonResponse
from api import account

# for uvicorn
app = coreapp

app.include_router(account.router, prefix='/account', default_response_class=CustomJsonResponse)
