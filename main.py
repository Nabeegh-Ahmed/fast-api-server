from services.product_service import ProductService
from config.db import Database

from models.product_model import ProductModel

db = Database()

# # Create a new product
# new_product = ProductModel(name="My Product")
# db_session = Database.get_session()
# db_session.add(new_product)
# db_session.commit()

# # Get all products
# products = db_session.query(ProductModel).all()
# print([product.name for product in products])

# # Get a product by id
# product = db_session.query(ProductModel).get(1)
# db_session.close()


product_service = ProductService()
product_service.create(name="My Product")
products = product_service.get_all()
print([product.name for product in products])
