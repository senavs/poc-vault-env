from fastapi import APIRouter

from api.modules.env import get_envs

router = APIRouter(prefix='/env', tags=['Environments'])


@router.get('/', summary='Get all set envs', status_code=200)
def _root():
    return get_envs()
