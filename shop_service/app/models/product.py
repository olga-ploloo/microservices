from typing import TYPE_CHECKING

from sqlalchemy import String

from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from .base import Base

if TYPE_CHECKING:
    from .order_product_association import OrderProductAssociation


class Product(Base):
    """Product model."""

    name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    price: Mapped[float] = mapped_column(nullable=False)
    description: Mapped[str]
    stock_quantity: Mapped[bool] = mapped_column(default=False)
    orders_details: Mapped[list["OrderProductAssociation"]] = relationship(back_populates="product")

    # orders: Mapped[list['Order']] = relationship(secondary='order_product_association',
    #                                              back_populates='products')
