from sqlalchemy import Column, String, Float
from sqlalchemy.orm import Mapped, relationship
from models.base_model import BaseModel


class ProductModel(BaseModel):
    __tablename__ = 'products'
    name: Mapped[str] = Column('name', String(32), nullable=False)
    price: Mapped[int] = Column('price', Float, nullable=False)
    image: Mapped[str] = Column('image', String(80), nullable=False)
    description: Mapped[str] = Column(
        'description', String(256), nullable=False)
    inventory = relationship(
        'InventoryModel', back_populates='product', uselist=False)
    sales = relationship(
        'SalesModel', back_populates='product', uselist=False)
