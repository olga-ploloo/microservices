from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from starlette.responses import JSONResponse
from fastapi import APIRouter, Depends, status

from .cart import Cart
from decimal import Decimal

from .schemas import AddProductToCart
from ..products.dependencies import get_product_by_id
from ...database.database import db_helper

router = APIRouter(tags=['Carts'],
    prefix='/carts')


@router.post('/')
async def add_product_to_cart(add_to_cart: AddProductToCart,
                      session: AsyncSession = Depends(db_helper.session_dependency),
                      user: User = Depends(get_current_user)):
    product = await get_product_by_id(add_to_cart.product_id)
    Cart.add_to_cart(
        user_id=user.id,
        product_id=product.id,
        product_price=str(Decimal(product.price) * add_to_cart.quantity),
        product_quantity=add_to_cart.quantity,
    )
    content = {'message': 'Add to cart.'}
    return JSONResponse(status_code=status.HTTP_200_OK, content=content)


@router.get('/list', response_model=schemas.Carts)
async def carts(user: User = Depends(get_current_user)):
    total_price = 0
    items = Cart.carts(user.id)
    for item in items:
        total_price += float(item['product_price'])

    return {'total_price': total_price, 'items': items}


@router.delete('/clear')
async def clear_cart(user: User = Depends(get_current_user)):
    Cart.delete_all_carts(user.id)
    content = {'message': 'Clear carts.'}
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=content)


@router.delete('/delete-item-cart/{row_id}')
async def delete_item_cart(row_id: str, user: User = Depends(get_current_user)):
    Cart.delete_cart(user.id, row_id)
    content = {'message': 'Delete item cart.'}
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=content)
