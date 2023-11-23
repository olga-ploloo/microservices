from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from api import router as api_router
from order_service.app.core.config import settings


#

@asynccontextmanager
async def lifespan(app: FastAPI):
    # executed before the application starts up.
    yield
    # executed after the application finishes handling requests


app = FastAPI(lifespan=lifespan)
app.include_router(router=api_router, prefix=settings.api_prefix)



if __name__ == '__main__':
    uvicorn.run("main:app", port=1111, host='127.0.0.1')