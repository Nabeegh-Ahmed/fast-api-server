from config.db import Database
from fastapi import FastAPI

from routers.product_router import ProductRouter
from routers.inventory_router import InventoryRouter
from routers.sales_router import SalesRouter

db = Database()
db.init_connection()

app = FastAPI()
app.include_router(ProductRouter, prefix="/api")
app.include_router(InventoryRouter, prefix="/api")
app.include_router(SalesRouter, prefix="/api")
