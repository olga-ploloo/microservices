from fastapi import HTTPException
from sqlalchemy import select, Result
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from .shemas import UserCreate
from .utils import PasswordManager
from ...models import User


async def get_user_by_id(session: AsyncSession,
                         user_id: int) -> User | None:
    return await session.get(User, user_id)


async def get_user_by_email(session: AsyncSession,
                            user_email: str) -> User | None:
    return await session.get(User, user_email)


async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)


async def create_user(session: AsyncSession,
                      new_user: UserCreate) -> User:
    new_user.password = PasswordManager().hash(new_user.password)
    user = User(**new_user.model_dump())
    session.add(user)
    try:
        await session.commit()
        await session.refresh(user)
        return user
    except IntegrityError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"User with Email: {new_user.email} already exists")
