from fastapi import APIRouter
from services.inventory_service import InventoryService
from schemas.inventory import InventoryCreatePayload, InventoryUpdatePayload

InventoryRouter = APIRouter(
    prefix="/inventory",
    tags=["inventory"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

service = InventoryService()


@InventoryRouter.get("/")
async def read_inventory(limit: int = 10, offset: int = 0):
    return {"inventory": service.get_all(limit, offset, ["product"])}


@InventoryRouter.post("/")
async def create_inventory_item(inventory_data: InventoryCreatePayload):
    inventory_item = service.create(**inventory_data.model_dump())
    return {"inventory": inventory_item.to_dict()}


@InventoryRouter.get("/{id}")
async def get_inventory_item(id: str):
    inventory_item = service.get_by_id(id, ["product"])
    return {"inventory": inventory_item.to_dict()}


@InventoryRouter.put("/{id}")
async def update_inventory_item(id: str, inventory_data: InventoryUpdatePayload):
    inventory_item = service.get_by_id(id)
    inventory_item.stock = inventory_data.stock or inventory_item.stock
    inventory_item.unit_cost = inventory_data.unit_cost or inventory_item.unit_cost
    inventory_item = service.update(inventory_item)
    return {"inventory": inventory_item.to_dict()}


@InventoryRouter.delete("/{id}")
async def delete_inventory_item(id: str):
    service.delete(id)
    return {"message": "Inventory item deleted successfully"}
