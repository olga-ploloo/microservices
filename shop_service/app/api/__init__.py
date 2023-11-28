from fastapi import APIRouter
from .products.view import router as product_router
from .orders.view import router as order_router

router = APIRouter()
router.include_router(router=product_router,
                      prefix='/products')
router.include_router(router=order_router,
                      prefix='/orders')