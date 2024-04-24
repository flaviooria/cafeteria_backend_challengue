from datetime import datetime
from uuid import uuid4

from models.users import Users
from pydantic import UUID4
from sqlmodel import Field, Relationship, SQLModel


class MemberBase(SQLModel):
    points: int
    has_discount: bool = True


class Members(MemberBase, table=True):
    id: UUID4 = Field(uuid4(), primary_key=True)
    created_at: datetime | None = None
    users_list: list[Users] = Relationship(back_populates="users")
