from services.product_service import ProductService
from services.inventory_service import InventoryService
from services.sales_service import SalesService

from dotenv import load_dotenv
import os
from config.db import Database


load_dotenv()
db = Database()
db.init_connection(os.getenv("DB_USER"), os.getenv("DB_HOST"),
                   os.getenv("DB_NAME"), os.getenv("DB_PASSWORD"))


def test_product_flow():
    service = ProductService()
    # Create
    product = service.create(
        name="Test Product", price=100, image="", description="")
    assert product.id is not None
    assert product.name == "Test Product"
    assert product.price == 100
    assert product.image == ""
    assert product.description == ""

    # Get All
    products = service.get_all()
    assert len(products) > 0

    # Get By Id
    product = service.get_by_id(product.id)
    assert product.id is not None
    assert product.name == "Test Product"
    assert product.price == 100
    assert product.image == ""
    assert product.description == ""

    # Update
    product.name = "Test Product 2"
    product.price = 200
    product.image = "test_image.png"
    product.description = "Test Description"
    product = service.update(product)
    assert product.id is not None
    assert product.name == "Test Product 2"
    assert product.price == 200
    assert product.image == "test_image.png"
    assert product.description == "Test Description"

    # Delete
    service.delete(product.id)
    product = service.get_by_id(product.id)
    assert product.is_deleted is True


def test_inventory_flow():
    product_service = ProductService()
    inventory_service = InventoryService()
    # Create
    product = product_service.create(
        name="Test Product", price=100, image="", description="")
    inventory = inventory_service.create(
        product_id=product.id, stock=100, unit_cost=10)
    assert inventory.id is not None
    assert inventory.product_id == product.id
    assert inventory.stock == 100
    assert inventory.unit_cost == 10

    # Get All
    inventories = inventory_service.get_all()
    assert len(inventories) > 0

    # Get By Id
    inventory = inventory_service.get_by_id(inventory.id)
    assert inventory.id is not None
    assert inventory.product_id == product.id
    assert inventory.stock == 100
    assert inventory.unit_cost == 10

    # Update
    inventory.stock = 200
    inventory.unit_cost = 20
    inventory = inventory_service.update(inventory)
    assert inventory.id is not None
    assert inventory.product_id == product.id
    assert inventory.stock == 200
    assert inventory.unit_cost == 20

    # Delete
    inventory_service.delete(inventory.id)
    inventory = inventory_service.get_by_id(inventory.id)
    assert inventory.is_deleted is True


def test_sales_flow():
    product_service = ProductService()
    inventory_service = InventoryService()
    sales_service = SalesService()
    # Create
    product = product_service.create(
        name="Test Product", price=100, image="", description="")
    inventory = inventory_service.create(
        product_id=product.id, stock=100, unit_cost=10)
    sale = sales_service.create(product_id=product.id,
                                quantity=1, unit_cost=10, sale_price=10, customer_name="Test Customer")
    assert sale.id is not None
    assert sale.product_id == product.id
    assert sale.quantity == 1
    assert sale.unit_cost == 10
    assert sale.sale_price == 10
    assert sale.customer_name == "Test Customer"

    # Get All
    sales = sales_service.get_all()
    assert len(sales) > 0

    # Get By Id
    sales = sales_service.get_by_id(sale.id)
    assert sales.id is not None
    assert sales.product_id == product.id
    assert sales.quantity == 1
    assert sales.unit_cost == 10
    assert sales.sale_price == 10
    assert sales.customer_name == "Test Customer"

    # Update
    sales.quantity = 2
    sales.unit_cost = 20
    sales.sale_price = 20
    sales.customer_name = "Test Customer 2"
    sales = sales_service.update(sales)
    assert sales.id is not None
    assert sales.product_id == product.id
    assert sales.quantity == 2
    assert sales.unit_cost == 20
    assert sales.sale_price == 20
    assert sales.customer_name == "Test Customer 2"

    # Delete
    sales_service.delete(sales.id)
    sales = sales_service.get_by_id(sales.id)
    assert sales.is_deleted is True
