from contextlib import asynccontextmanager

from database.base import Base
from database.database import db_helper
import uvicorn
from fastapi import FastAPI
from api import router as api_router
from order_service.app.core.config import settings


#

@asynccontextmanager
async def lifespan(app: FastAPI):
    # executed before the application starts up.
    async with db_helper.engine.begin() as conn:
        #         # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        print('Init db done')
    yield
    # executed after the application finishes handling requests


app = FastAPI(lifespan=lifespan)
app.include_router(router=api_router, prefix=settings.api_prifix)



if __name__ == '__main__':
    uvicorn.run("main:app", port=1111, host='127.0.0.1')