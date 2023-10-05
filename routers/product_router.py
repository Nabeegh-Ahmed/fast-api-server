from fastapi import APIRouter
from services.product_service import ProductService
from schemas.products import ProductCreatePayload, ProductUpdatePayload

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


@ProductRouter.post("/")
async def create_product(product_data: ProductCreatePayload):
    product = service.create(**product_data.model_dump())
    return {"product": product.to_dict()}


@ProductRouter.get("/{id}")
async def get_product_item(id: str):
    product_item = service.get_by_id(id)
    return {"product": product_item.to_dict()}


@ProductRouter.put("/{id}")
async def update_product_item(id: str, product_data: ProductUpdatePayload):
    product_item = service.get_by_id(id)
    product_item.name = product_data.name or product_item.name
    product_item.price = product_data.price or product_item.price
    product_item.image = product_data.image or product_item.image
    product_item.description = product_data.description or product_item.description

    product_item = service.update(product_item)
    return {"product": product_item.to_dict()}


@ProductRouter.delete("/{id}")
async def delete_product_item(id: str):
    service.delete(id)
    return {"message": "Product item deleted successfully"}
