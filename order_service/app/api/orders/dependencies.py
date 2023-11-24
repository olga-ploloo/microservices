from typing import Annotated

from fastapi import Depends, Path, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from order_service.app.api.products import crud
from order_service.app.models import Product
from order_service.app.database.database import db_helper


async def get_product_by_id(product_id: Annotated[int, Path],
                            session: AsyncSession = Depends(db_helper.session_dependency)) -> Product:
    product = await crud.get_product(session=session,
                                     product_id=product_id)
    if product is not None:
        return product

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'Product {product_id} not found')