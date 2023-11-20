import asyncio
from collections.abc import AsyncGenerator

from sqlalchemy import create_engine, exc
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# DATABASE_URL = "postgresql://user:password@postgresserver/db"
DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/order_service"

engine = create_async_engine(DATABASE_URL,
                             echo=True)


Base = declarative_base()
print(Base)


async def init_db():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)




async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    engine = create_async_engine(DATABASE_URL)
    factory = async_sessionmaker(engine)
    async with factory() as session:
        try:
            yield session
            await session.commit()
        except exc.SQLAlchemyError as error:
            await session.rollback()
            print(error)
            raise