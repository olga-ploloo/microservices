from sqlalchemy import select, Result
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from shop_service.app.api.orders.schemas import OrderCreate
from shop_service.app.models import Product, Order, OrderProductAssociation


# async def get_products(session: AsyncSession) -> list[Product]:
#     stmt = select(Product).order_by(Product.id)
#     result: Result = await session.execute(stmt)
#     products = result.scalars().all()
#     return list(products)

async def get_orders_with_products(session: AsyncSession) -> list[Order]:
    stmt = (select(Order)
            .options(selectinload(Order.products_details).joinedload(OrderProductAssociation.product))
            .order_by(Order.id))
    orders = await session.scalars(stmt)

    return list(orders)


async def create_order(session: AsyncSession,
                       product: Product) -> Order:
    order = Order()
    session.add(order)
    await session.commit()

    return order

# async def get_orders_with_products_assoc(session: AsyncSession) -> list[Order]:
#     stmt = (
#         select(Order)
#         .options(
#             selectinload(Order.products_details).joinedload(
#                 OrderProductAssociation.product
#             ),
#         )
#         .order_by(Order.id)
#     )
#     orders = await session.scalars(stmt)
#
#     return list(orders)


# async def demo_get_orders_with_products_with_assoc(session: AsyncSession):
#     orders = await get_orders_with_products_assoc(session)
#
#     for order in orders:
#         print(order.id, order.promocode, order.created_at, "products:")
#         for (
#             order_product_details
#         ) in order.products_details:  # type: OrderProductAssociation
#             print(
#                 "-",
#                 order_product_details.product.id,
#                 order_product_details.product.name,
#                 order_product_details.product.price,
#                 "qty:",
#                 order_product_details.count,
#             )


# async def create_product(session: AsyncSession,
#                          new_product: ProductCreate) -> Product:
#     product = Product(**new_product.model_dump())
#     session.add(product)
#     await session.commit()
#     await session.refresh(product)
#     return product
#
# async def update_product(session: AsyncSession,
#                          product: Product,
#                          product_update: ProductUpdate) -> Product:
#     for name, value in product_update.model_dump(exclude_unset=True).items():
#         setattr(product, name, value)
#     await session.commit()
#     return product
#
# async def delete_product(session: AsyncSession,
#                          product: Product) -> None:
#     await session.delete(product)
#     await session.commit()
