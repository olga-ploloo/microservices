from os import getenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_prifix: str = '/api'
    db_url: str = 'postgresql+asyncpg://postgres:postgres@localhost/order_service'
    db_echo: bool = True


settings = Settings()
