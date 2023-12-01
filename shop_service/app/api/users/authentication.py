from typing import Annotated

from fastapi import HTTPException, status, Depends, security
from fastapi.security import HTTPBasicCredentials
from sqlalchemy.ext.asyncio import AsyncSession

from shop_service.app.api.users.crud import get_user_by_email
from shop_service.app.api.users.utils import PasswordManager
from shop_service.app.database.database import db_helper

security = HTTPBasic()
async def authenticate_user(session: AsyncSession = Depends(db_helper.session_dependency),
                        credentials: Annotated[HTTPBasicCredentials, Depends(security)]):

    user = await get_user_by_email()
    if user.is_active == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User is not active.')
    if not user:
        return False

    if not PasswordManager().verify( user.hashed_password):
        return False
    return user


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=['HS256'])
        user = models.User.filter(models.User.id == payload.get('id')).first()
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid email or password'
        )

    return user