from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .dependencies import get_product_by_id
from .schemas import ProductCreate, ProductSchema, ProductUpdate
from order_service.app.database.database import db_helper
from order_service.app.models import Product

router = APIRouter(tags=['Products'])


@router.get('/', response_model=list[ProductSchema])
async def get_products(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_products(session=session)


@router.get('/{product_id}/', response_model=ProductSchema)
async def get_product(product: Product = Depends(get_product_by_id)):
    return product


@router.post('/', response_model=ProductSchema, status_code=status.HTTP_201_CREATED)
async def create_product(new_product: ProductCreate,
                         session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.create_product(session=session,
                                     new_product=new_product)


@router.patch('/{product_id}/')
async def update_product(product_update: ProductUpdate,
                         product: Product = Depends(get_product_by_id),
                         session: AsyncSession = Depends(db_helper.session_dependency)):
    # here session will be the same as in get_product_by_id, because fastapi cache it
    return await crud.update_product(session=session,
                                     product=product,
                                     product_update=product_update)


@router.delete('/{product_id}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product: Product = Depends(get_product_by_id),
                         session: AsyncSession = Depends(db_helper.session_dependency)) -> None:
    return await crud.delete_product(session=session,
                                     product=product)
