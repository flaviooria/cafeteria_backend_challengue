from sqlmodel import SQLModel


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
