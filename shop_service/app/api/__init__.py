from fastapi import APIRouter

from .products.routes import router as product_router
from .orders.routes import router as order_router
from .carts.routes import router as cart_router

router = APIRouter()
router.include_router(router=product_router,
                      prefix='/products')
router.include_router(router=order_router,
                      prefix='/orders')
router.include_router(router=cart_router,
                      prefix='/carts')
