from fastapi import APIRouter
from services.sales_service import SalesService
from services.inventory_service import InventoryService
from schemas.sales import SalesCreatePayload, SalesUpdatePayload

SalesRouter = APIRouter(
    prefix="/sales",
    tags=["sales"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

service = SalesService()


@SalesRouter.get("/")
async def read_sales(limit: int = 10, offset: int = 0):
    return {"sales": service.get_all(limit, offset, ["product"])}


@SalesRouter.post("/")
async def create_sales_item(sales_data: SalesCreatePayload):
    inventory_service = InventoryService()
    inventory_item = inventory_service.get_by_property(
        "product_id", sales_data.product_id)

    if inventory_item.stock < sales_data.quantity:
        return {"error": "Insufficient Quantity"}

    sales_item = service.create(**sales_data.model_dump())

    inventory_item.stock -= sales_item.quantity
    inventory_service.update(inventory_item)

    return {"sales": sales_item.to_dict()}


@SalesRouter.get("/{id}")
async def get_sales_item(id: str):
    sales_item = service.get_by_id(id, ["product"])
    return {"sales": sales_item.to_dict()}


@SalesRouter.put("/{id}")
async def update_sales_item(id: str, sales_data: SalesUpdatePayload):
    sales_item = service.get_by_id(id)
    sales_item.quantity = sales_data.quantity or sales_item.quantity
    sales_item.unit_cost = sales_data.unit_cost or sales_item.unit_cost
    sales_item.sale_price = sales_data.sale_price or sales_item.sale_price
    sales_item.customer_name = sales_data.customer_name or sales_item.customer_name
    sales_item = service.update(sales_item)
    return {"sales": sales_item.to_dict()}


@SalesRouter.delete("/{id}")
async def delete_sales_item(id: str):
    service.delete(id)
    return {"message": "Sales item deleted successfully"}
