from pydantic import BaseModel


class InventoryCreatePayload(BaseModel):
    product_id: str
    stock: int
    unit_cost: float


class InventoryUpdatePayload(BaseModel):
    stock: int = None
    unit_cost: float = None
