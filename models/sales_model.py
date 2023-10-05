from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from models.base_model import BaseModel


class SalesModel(BaseModel):
    __tablename__ = 'sales'
    product_id = Column(ForeignKey("products.id"))
    quantity: Mapped[int] = Column('quantity', Integer, nullable=False)
    unit_cost = Column('unit_cost', Float, nullable=False)
    total_cost = Column('total_cost', Float, nullable=False)
    customer_name = Column('customer_name', String(32), nullable=False)

    product = relationship(
        'ProductModel', back_populates='sales')
