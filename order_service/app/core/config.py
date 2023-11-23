from os import getenv

from pydantic import BaseModel
from pydantic_settings import BaseSettings


class DBSettings(BaseModel):
    url: str = 'postgresql+asyncpg://postgres:postgres@localhost/order_service'
    echo: bool = True


class Settings(BaseSettings):
    api_prefix: str = '/api'
    db: DBSettings = DBSettings()


settings = Settings()
