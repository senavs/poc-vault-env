import uvicorn

from api import settings

uvicorn.run(
    'api:app',
    host=settings.deploy.ECS_HOST,
    port=settings.deploy.ECS_PORT,
    debug=settings.deploy.ECS_DEBUG,
    reload=settings.deploy.ECS_RELOAD,
    log_level=settings.deploy.ECS_LOG_LEVEL
)
