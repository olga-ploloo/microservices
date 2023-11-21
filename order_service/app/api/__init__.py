from fastapi import APIRouter
from .products.view import router as product_router

router = APIRouter()
router.include_router(router=product_router,
                      prefix='/products')