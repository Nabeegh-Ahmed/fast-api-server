from services.base_service import BaseService
from models.inventory_model import InventoryModel


class InventoryService(BaseService):
    def __init__(self):
        super().__init__(InventoryModel)
