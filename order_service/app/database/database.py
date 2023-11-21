import asyncio
import uuid
from asyncio import current_task
from collections.abc import AsyncGenerator

from sqlalchemy import create_engine, exc
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine, async_sessionmaker, \
    async_scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, declared_attr
import os

# DATABASE_URL = "sqlite+aiosqlite:///./order_service.sqlite3"
DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/order_service"


#
# engine = create_async_engine(DATABASE_URL,
#                              echo=True)

# SessionLocal = async_sessionmaker(engine)

class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(url=url,
                                          echo=echo)
        self.session_factory = async_sessionmaker(bind=self.engine,
                                                  autoflush=False,
                                                  autocommit=False,
                                                  expire_on_commit=False)

    def get_scope_session(self):
        session = async_scoped_session(session_factory=self.session_factory,
                                       scopefunc=current_task)
        return session

    async def session_dependency(self):
        async with self.session_factory() as session:
            yield session
            await session.close()



db_helper = DatabaseHelper(url=DATABASE_URL, echo=True)

