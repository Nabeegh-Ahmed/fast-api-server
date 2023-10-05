from pydantic import BaseModel


class SalesCreatePayload(BaseModel):
    product_id: str
    quantity: int
    unit_cost: float
    total_cost: float
    customer_name: str


class SalesUpdatePayload(BaseModel):
    quantity: int = None
    unit_cost: float = None
    total_cost: float = None
    customer_name: str = None
