# class OrderItems(Base):
#     """OrderItems model."""
#     __tablename__ = 'order_item'
#
#     # id: Mapped[uuid] = mapped_column(primary_key=True, index=True)
#     order_id: Mapped[int] = mapped_column(ForeignKey('order.id'))
#     product_id: Mapped[int] = mapped_column(ForeignKey('product.id'))
#     quantity: Mapped[int] = mapped_column(Integer, nullable=False)
#
#     product: Mapped['Product'] = relationship(back_populates='order_items')
#     order: Mapped['Order'] = relationship(back_populates='order_items')
