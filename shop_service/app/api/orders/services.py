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
            .options(selectinload(Order.products), )
            .order_by(Order.id))
    orders = await session.scalars(stmt)

    return list(orders)

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
