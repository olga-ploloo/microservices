from os import getenv

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseModel):
    # DB_HOST: str
    # DB_PORT: int
    # DB_USER: str
    # DB_PASSWORD: str
    # DB_NAME: str
    url: str = 'postgresql+asyncpg://postgres:postgres@localhost/order_service'
    echo: bool = True

    # @property
    # def url(self):
    #     return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    #
    # model_config = SettingsConfigDict(env_file=".env")

class Settings(BaseSettings):
    api_prefix: str = '/api'
    db: DBSettings = DBSettings()


settings = Settings()
