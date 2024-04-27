import os
from typing import Literal

from pydantic import PostgresDsn, computed_field
from pydantic_core import MultiHostHost, MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_ignore_empty=True, env_file_encoding='utf-8', extra='ignore')

    POSTGRES_DBNAME: str
    POSTGRES_HOST: str
    POSTGRES_USERNAME: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: int = 5432

    # version api
    API_VERSION: str = 'api/v1'

    DOMAIN: str = 'localhost'
    ENVIRONMENT: Literal["local", "staging", "production"] = "local"
    APP_NAME: str

    @computed_field
    @property
    def server_host(self) -> str:
        if self.ENVIRONMENT == 'local':
            return f"http://{self.DOMAIN}"

        return f"https://{self.DOMAIN}"

    @computed_field
    @property
    def database_uri(self) -> PostgresDsn:
        multihost: MultiHostHost = MultiHostHost(
            username=self.POSTGRES_USERNAME, password=self.POSTGRES_PASSWORD, host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT)

        return MultiHostUrl.build(scheme='postgresql+psycopg2', **multihost)


env_file = ".env" if os.environ.get("ENVIRONMENT") == "local" else ".env.prod"
settings = Settings(_env_file=env_file)
