from config.db import connectDB

from models.product_model import ProductModel

# Create a new product
new_product = ProductModel(name="My Product")
db_session = connectDB()
db_session.add(new_product)
db_session.commit()

# Get all products
products = db_session.query(ProductModel).all()
print([product.name for product in products])

# Get a product by id
product = db_session.query(ProductModel).get(1)
