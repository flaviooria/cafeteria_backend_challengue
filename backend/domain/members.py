from sqlmodel import SQLModel


class MemberBase(SQLModel):
    points: int
    has_discount: bool = True
