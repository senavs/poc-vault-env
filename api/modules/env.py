from api import settings


def get_envs() -> dict:
    envs = {
        **settings.deploy.dict(),
        'SERVICE_01': settings.services.SERVICE_01,
        'SERVICE_02': settings.services.SERVICE_02,
        'SERVICE_03': settings.services.SERVICE_03,
    }
    return envs
