from pydantic import BaseModel


class SalesCreatePayload(BaseModel):
    product_id: str
    quantity: int
    unit_cost: float
    sale_price: float
    customer_name: str


class SalesUpdatePayload(BaseModel):
    quantity: int = None
    unit_cost: float = None
    sale_price: float = None
    customer_name: str = None
