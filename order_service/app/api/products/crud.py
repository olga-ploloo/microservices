from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import ProductCreate
from order_service.app.database import Product


async def get_products(session: AsyncSession) -> list[Product]:
    stmt = select(Product).order_by(Product.id)
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    print(products)
    return list(products)

async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(Product, product_id)


async def create_product(session: AsyncSession, product_in: ProductCreate) -> Product:
    product = Product(**product_in.model_dump())
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product

# @app.get('/product')
# async def get_product(db_session: AsyncSession, user_id: int):
#     user = (await db_session.scalars(select(UserDBModel).where(UserDBModel.id == user_id))).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user