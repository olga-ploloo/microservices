from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import ProductCreate, ProductUpdate
from order_service.app.database import Product


async def get_products(session: AsyncSession) -> list[Product]:
    stmt = select(Product).order_by(Product.id)
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    print(products)
    return list(products)

async def get_product(session: AsyncSession,
                      product_id: int) -> Product | None:
    return await session.get(Product, product_id)


async def create_product(session: AsyncSession,
                         new_product: ProductCreate) -> Product:
    product = Product(**new_product.model_dump())
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product

async def update_product(session: AsyncSession,
                         product: Product,
                         product_update: ProductUpdate) -> Product:
    for name, value in product_update.model_dump(exclude_unset=True).items():
        setattr(product, name, value)
    await session.commit()
    return product

async def delete_product(session: AsyncSession,
                         product: Product) -> None:
    await session.delete(product)
    await session.commit()
