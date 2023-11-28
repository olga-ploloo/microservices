from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING

from sqlalchemy import func
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from .base import Base

if TYPE_CHECKING:
    from .order_product_association import OrderProductAssociation


class OrderStatus(str, Enum):
    PENDING = 'pending'
    PROCESSING = 'processing'
    SHIPPED = 'shipped'
    DELIVERED = 'delivered'


class Order(Base):
    """Order model."""

    status: Mapped[OrderStatus] = mapped_column(default=OrderStatus.PENDING)
    amount: Mapped[float] = mapped_column(default=0, server_default="0")
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(),
                                                 default=datetime.now)
    promocode: Mapped[str | None]

    products_details: Mapped[list["OrderProductAssociation"]] = relationship(back_populates="order")

    # products: Mapped[list['Product']] = relationship(secondary='order_product_association')