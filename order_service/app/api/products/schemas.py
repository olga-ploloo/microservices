from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    price: float
    description: str
    stock_quantity: bool

class ProductCreate(BaseModel):
    pass

class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    id: int