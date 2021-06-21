import os

from pydantic import BaseSettings, Field

from api.services.vault import VaultKVService

vault_kv = VaultKVService(os.environ.get('VAULT_HOST'), os.environ.get('VAULT_TOKEN'), 'ECS', 'LNO')


class DeploymentSettings(BaseSettings):
    """Environments variables from pydantic.BaseSettings"""

    # env variable               vault secret name
    ECS_HOST: str = vault_kv.get('HOST') or Field()  # required
    ECS_PORT: int = vault_kv.get_pydantic('PORT')  # required
    ECS_DEBUG: bool = vault_kv.get_pydantic('DEBUG', False)  # secret as default value
    ECS_RELOAD: bool = vault_kv.get_pydantic('RELOAD', False)  # secret as default value
    ECS_LOG_LEVEL: str = vault_kv.get_pydantic('LOG_LEVEL', 'info')  # secret as default value


class ServicesURLSettings:
    """Environments variables from os.environ"""

    #                                 env variable                   vault secret name
    SERVICE_01: str = os.environ.get('SERVICE_01_URL', vault_kv.get('local_SERVICE_01_URL'))  # secret as default value
    SERVICE_02: str = os.environ.get('SERVICE_02_URL', vault_kv.get('hml_SERVICE_01_URL', 'http://localhost:1234/'))  # secret as default value with default
    SERVICE_03: str = os.environ.get('SERVICE_03_URL')  # None as default value


deploy = DeploymentSettings()
services = ServicesURLSettings()
