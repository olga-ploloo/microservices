from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import services
from .schemas import OrderSchema, OrderCreate, NewOrderSchema
from shop_service.app.database.database import db_helper
from ..products.dependencies import get_product_by_id
from ...models import Product

router = APIRouter(tags=['Orders'])


@router.get('/', response_model=list[OrderSchema])
async def get_orders_with_products(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await services.get_orders_with_products(session=session)


# @router.get('/{product_id}/', response_model=ProductSchema)
# async def get_product(product: Product = Depends(get_product_by_id)):
#     return product
#
#
@router.post('/{product_id}{count}', response_model=OrderSchema, status_code=status.HTTP_201_CREATED)
async def create_order(product: Product = Depends(get_product_by_id),
                       count: int,
                         session: AsyncSession = Depends(db_helper.session_dependency)):
    return await services.create_order(session=session,
                                     product=product)

@router.post('/add_product', response_model=OrderSchema, status_code=status.HTTP_201_CREATED)
async def add_product(new_order: OrderCreate,
                         session: AsyncSession = Depends(db_helper.session_dependency)):
    return await services.create_order(session=session,
                                     new_order=new_order)
#
#
# @router.patch('/{product_id}/')
# async def update_product(product_update: ProductUpdate,
#                          product: Product = Depends(get_product_by_id),
#                          session: AsyncSession = Depends(db_helper.session_dependency)):
#     # here session will be the same as in get_product_by_id, because fastapi cache it
#     return await endpoints.update_product(session=session,
#                                      product=product,
#                                      product_update=product_update)
#
#
# @router.delete('/{product_id}/', status_code=status.HTTP_204_NO_CONTENT)
# async def delete_product(product: Product = Depends(get_product_by_id),
#                          session: AsyncSession = Depends(db_helper.session_dependency)) -> None:
#     return await endpoints.delete_product(session=session,
#                                      product=product)
