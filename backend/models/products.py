from uuid import uuid4

from pydantic import UUID4
from sqlmodel import Field, SQLModel


class ProductBase(SQLModel):
    name: str
    description: str
    price: float
    percentage_offer: float
    json_config: str
    image: str
    is_new: bool = True


class ProductCreateDto(ProductBase):
    json_config: str | None = None


class Products(ProductBase, table=True):
    id: UUID4 = Field(uuid4(), primary_key=True)
