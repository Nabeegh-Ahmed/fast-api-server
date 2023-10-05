import os
from dotenv import load_dotenv
from services.sales_service import SalesService
from services.inventory_service import InventoryService
from services.product_service import ProductService
from config.db import Database


load_dotenv()
db = Database()
db.init_connection(str(os.getenv("DB_USER")), str(os.getenv("DB_HOST")),
                   str(os.getenv("DB_NAME")), str(os.getenv("DB_PASSWORD")))

product_service = ProductService()
inventory_service = InventoryService()
sales_service = SalesService()


def populate_db(n=10):
    for i in range(n):
        product = product_service.create(
            name="Test Product " + str(i), price=100, image="", description="")
        inventory_service.create(
            product_id=product.id, stock=100, unit_cost=10)
        sales_service.create(product_id=product.id,
                             quantity=1, unit_cost=10, sale_price=10, customer_name="Test Customer")


populate_db()
