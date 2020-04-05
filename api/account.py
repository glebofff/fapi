from fastapi import APIRouter
from core.common import BaseModel

router = APIRouter()


class AccountResponseModel(BaseModel):
    pass


@router.get('/')
async def get_account():
    return {
    }


@router.post('/')
def create_account():
    return {
    }

