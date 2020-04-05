from core.app import app as coreapp
from core.common import CustomResponse
from api import account

# for uvicorn
app = coreapp

app.include_router(account.router, prefix='/account', default_response_class=CustomResponse)
