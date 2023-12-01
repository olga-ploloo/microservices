from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr, ConfigDict


class UserBase(BaseModel):
    username: Annotated[str, MinLen(2), MaxLen(32)]
    phone: str
    email: EmailStr
    password: str


class UserCreate(UserBase):
    pass


class UserSchema(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

class UserAuth(BaseModel):
    pass