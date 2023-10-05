from pydantic import BaseModel


class ProductCreatePayload(BaseModel):
    name: str
    price: float
    image: str
    description: str


class ProductUpdatePayload(BaseModel):
    name: str = None
    price: float = None
    image: str = None
    description: str = None
