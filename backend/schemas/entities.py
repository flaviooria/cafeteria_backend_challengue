from datetime import datetime
from typing import Literal, Annotated, Optional
from uuid import uuid4

from pydantic import ConfigDict
from sqlmodel import Field, Relationship

from backend.domain.members import MemberBase
from backend.domain.products import ProductBase
from backend.domain.users import UserBase
from backend.enums.user_enum import Status

UserStatusTypes: Literal["active", "banned", "deleted"] = "active"

UserStatus = Annotated[str, UserStatusTypes]


class Products(ProductBase, table=True):
    id: str | None = Field(default_factory=lambda: uuid4(), primary_key=True)


class Members(MemberBase, table=True):
    id: str | None = Field(default_factory=lambda: uuid4(), primary_key=True)
    created_at: datetime | None = None
    users_list: list["Users"] = Relationship(back_populates="users")


class Users(UserBase, table=True):
    model_config = ConfigDict(use_enum_values=True, arbitrary_types_allowed=True)

    id: str = Field(default_factory=lambda: uuid4(), primary_key=True)
    isAdmin: bool
    status: Optional[Status] = Field(default=Status.active)

    member_id: str | None = Field(..., foreign_key="members.id")
    members: Members | None = Relationship(back_populates="members")
