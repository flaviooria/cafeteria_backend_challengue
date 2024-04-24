from datetime import datetime
from uuid import uuid4

from pydantic import UUID4, EmailStr
from sqlmodel import Field, Relationship, SQLModel

from backend.enums.user_enum import Status
from backend.models.members import Members


class UserBase(SQLModel):
    name: str
    lastname: str
    email: EmailStr = Field(unique=True, index=True)
    password: str
    birthday: datetime


class UserRegister(UserBase):
    pass


class UserSingIn(SQLModel):
    email: EmailStr
    password: str


class Users(UserBase, table=True):
    id: UUID4 = Field(uuid4(), primary_key=True)
    isAdmin: bool
    status: Status = Status.active

    member_id: UUID4 | None = Field(..., foreign_key="members.id")
    members: Members | None = Relationship(back_populates="members")
