from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped
from models.base_model import BaseModel


class ProductModel(BaseModel):
    __tablename__ = 'products'
    name: Mapped[str] = Column('name', String(32), nullable=False)
