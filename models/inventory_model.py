from sqlalchemy import Column, ForeignKey, Integer, Float
from sqlalchemy.orm import Mapped, relationship
from models.base_model import BaseModel


class InventoryModel(BaseModel):
    __tablename__ = 'inventory'
    product_id = Column(ForeignKey("products.id"))
    stock: Mapped[int] = Column('stock', Integer, nullable=False)
    unit_cost = Column('unit_cost', Float, nullable=False)

    product = relationship(
        'ProductModel', back_populates='inventory')
