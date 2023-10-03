from services.base_service import BaseService
from models.product_model import ProductModel


class ProductService(BaseService):
    def __init__(self):
        super().__init__(ProductModel)
