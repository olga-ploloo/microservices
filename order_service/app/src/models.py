import dataclasses
import uuid
from datetime import datetime
from enum import Enum
from sqlalchemy import Column, Integer, ForeignKey, String, Float



from sqlalchemy import Uuid
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from order_service.app.src.database import Base


class OrderStatus(Enum):
    PENDING = 'pending'
    PROCESSING = 'processing'
    SHIPPED = 'shipped'
    DELIVERED = 'delivered'


class Product(Base):
    """Product model."""
    __tablename__ = 'product'

    id: Mapped[uuid] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    description: Mapped[str]
    stock_quantity: Mapped[bool] = mapped_column(default=False)


class Order(Base):
    """Order model."""
    __tablename__ = 'order'

    id: Mapped[uuid] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[uuid] = mapped_column(nullable=False)
    status: Mapped[OrderStatus] = mapped_column(default=OrderStatus.PENDING)
    amount: Mapped[float]
    created_at: Mapped[datetime]

    order_items: Mapped[list['OrderItems']] = relationship(back_populates='order')


class OrderItems(Base):
    """OrderItems model."""
    __tablename__ = 'order_items'

    id: Mapped[uuid] = mapped_column(primary_key=True, index=True)
    order_id: Mapped[uuid] = mapped_column(ForeignKey('order.id'))
    product_id: Mapped[uuid] = mapped_column(ForeignKey('product.id'))
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    product: Mapped['Product'] = relationship(back_populates='order_items')
    order: Mapped['Order'] = relationship(back_populates='order_items')
