# POC Vault Environment
Proof of concept to use Vault by Hashicorp as local environment variables.

## Setup
Start vault container.

```shell
docker-compose up vault
```

After start, open `localhost:8200` and configure vault keys. 
Do not forget to download root and unseal keys.

Then, you can access the main page with root token.
Create a `KV` secret engine as with version `V2` and path as `ECS`.
Also create a folder `LNO` and import [secrets.json](./vault/secrets.json). 

Now you can start up the application. 
Open [docker-compose.yml](./docker-compose.yml) and change the `VAULT_TOKEN` environment variable with downloaded root key. 
The app url is `localhost:8080`
```shell
docker-compose up app
```

**NOTE:** If vault container has been stopped, start it up again and **unseal** vault with unseal download key.

## Usage
Now you can set/change `key-value` keys in vault and use them in app as realtime environment variables.