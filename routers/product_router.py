from fastapi import APIRouter, HTTPException
from services.product_service import ProductService

ProductRouter = APIRouter(
    prefix="/products",
    tags=["items"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

service = ProductService()


@ProductRouter.get("/")
async def read_products(limit: int = 10, offset: int = 0):
    return {"products": service.get_all(limit, offset)}
