from services.base_service import BaseService
from models.sales_model import SalesModel


class SalesService(BaseService):
    def __init__(self):
        super().__init__(SalesModel)
