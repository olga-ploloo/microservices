import asyncio
import typer
import uvicorn
from fastapi import FastAPI

from src.database import init_db, engine, Base


async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        print('Init db done')
        yield

app = FastAPI(lifespan=lifespan)
if __name__ == '__main__':
    uvicorn.run("main:app", port=1111, host='127.0.0.1')