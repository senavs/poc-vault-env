from fastapi import FastAPI

__version__ = 'v1.0.0'

from api.routes import env

app = FastAPI(
    title='POC VAULT ENV',
    description='Proof of concept to use Vault by Hashicorp as local environment variables',
    version=__version__
)

app.include_router(env.router)
