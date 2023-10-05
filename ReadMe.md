# Shopping Server

This server uses FastAPI and SqlAlchemy to implement a very basic CRUD API for a shopping store.

# How to Setup

1. Clone this repo
2. Make sure docker is installed and running
3. Run `docker-compose up -d`. This will initialize the database
4. Run `pip3 install -r requirements.txt` to install the dependencies
5. (Optional) You can run the seed script with `python3 seed_db.py`
6. Run `uvicorn main:app --reload` to start

# Dependencies

- Uvicorn - Works as the WSGI (Web Server Gateway Interface)
- FastApi - Serves as the REST API client
- SqlAlchemy - An ORM that helps working with relational databases easier and reduces dependency on one single database
- PyTest - To run tests

# API Routes

| Model     | GET                                                                                    | POST                                                                                                                                                  | PUT                   | DELETE                      | /{id}                        |
| --------- | -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | --------------------------- | ---------------------------- |
| Product   | <div>Returns all Products</div><div>Pass limit and offset as query params</div>        | <div>Creates a new Product</div><div>Body: `{name: string, price: float, description: string, image: string}`</div>                                   | Updates the Product   | Soft Deletes the Product    | Returns product by Id        |
| Inventory | <div>Returns all Inventory Items</div><div>Pass limit and offset as query params</div> | <div>Creates a new Inventory Item</div><div>Body: `{stock: int, unit_cost: float, product_id: string}`</div>                                          | Updates the Inventory | Soft Deletes the Inventory  | Returns Inventory item by Id |
| Sales     | <div>Returns all Sales Items</div><div>Pass limit and offset as query params</div>     | <div>Creates a new Sales Item</div><div>Body: `{product_id: string, quantity: int, unit_cost: float, sale_price: float, customer_name: string}`</div> | Updates the Sales     | Soft Deletes the Sales Item | Returns Sales Item by Id     |
| revenue   | Returns the all time calculated revenue                                                | -                                                                                                                                                     | -                     | -                           | -                            |
