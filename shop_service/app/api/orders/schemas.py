from datetime import datetime

from pydantic import BaseModel, ConfigDict

from shop_service.app.api.products.schemas import ProductBase
from shop_service.app.models.order import OrderStatus


class OrderBase(BaseModel):
    status: OrderStatus
    amount: float
    created_at: datetime
    promocode: str | None = None


class OrderSchema(OrderBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    products_details: list[ProductBase]


