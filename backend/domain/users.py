from datetime import datetime

from pydantic import EmailStr
from sqlmodel import Field, SQLModel
from typing_extensions import Annotated


class UserBase(SQLModel):
    name: str
    lastname: str
    email: Annotated[str, EmailStr] = Field(default=None, unique=True, index=True)
    password: str
    birthday: datetime


class UserRegister(UserBase):
    pass


class UserSingIn(SQLModel):
    email: Annotated[str, EmailStr]
    password: str
