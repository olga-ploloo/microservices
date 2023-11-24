from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    price: float
    description: str
    stock_quantity: bool


class ProductCreate(ProductBase):
    pass


class ProductSchema(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class ProductUpdate(ProductBase):
    name: str | None = None
    price: float | None = None
    description: str | None = None
    stock_quantity: bool | None = None
