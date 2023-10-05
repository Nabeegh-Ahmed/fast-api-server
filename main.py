from dotenv import load_dotenv
import os
from config.db import Database
from fastapi import FastAPI

from routers.product_router import ProductRouter
from routers.inventory_router import InventoryRouter
from routers.sales_router import SalesRouter
from routers.revenue_router import RevenueRouter
load_dotenv()
db = Database()
db.init_connection(os.getenv("DB_USER"), os.getenv("DB_HOST"),
                   os.getenv("DB_NAME"), os.getenv("DB_PASSWORD"))

app = FastAPI()
app.include_router(ProductRouter, prefix="/api")
app.include_router(InventoryRouter, prefix="/api")
app.include_router(SalesRouter, prefix="/api")
app.include_router(RevenueRouter, prefix="/api")
