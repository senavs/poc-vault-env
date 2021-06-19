from typing import Union, Any

from hvac import Client
from pydantic import Field
from pydantic.fields import Undefined


class VaultKVService:
    _metadata = dict()
    _data = dict()

    def __init__(self, host: str = None, token: str = None, engine: str = None, folder: str = None, *, verify: bool = True):
        if all([host, token, engine, folder]):
            client: Client = Client(host, token, verify=verify)
            self._metadata = client.secrets.kv.v2.read_secret(path=folder, mount_point=engine).get('data', {})
            self._data = self._metadata.get('data', {})

    def get(self, item: str, default: Any = None) -> Union[str, Any, None]:
        return self._data.get(item, default)

    def get_pydantic(self, item: str, default: Any = Undefined) -> Union[str, Any, Field]:
        return self.get(item, Field(default))


if __name__ == '__main__':
    v = VaultKVService('http://localhost:8200', 's.56gO1gnu7bYOSBoDrWNC8qme', 'ECS', 'LNO')
    print(v.get('a'))
