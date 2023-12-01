from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from shop_service.app.api.users import crud
from shop_service.app.api.users.shemas import UserSchema, UserCreate
from shop_service.app.database.database import db_helper
from shop_service.app.models import User

router = APIRouter(tags=['Users'])


@router.post('/', response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def create_user(new_user: UserCreate,
                      session: AsyncSession = Depends(db_helper.session_dependency)) -> User:
    return await crud.create_user(session=session,
                                  new_user=new_user)
