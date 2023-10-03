from config.db import Database
from fastapi import FastAPI

from routers.product_router import ProductRouter

db = Database()
app = FastAPI()
app.include_router(ProductRouter, prefix="/api")
