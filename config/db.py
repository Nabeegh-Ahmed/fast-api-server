from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base_model import BaseModel
from models.product_model import ProductModel
from models.inventory_model import InventoryModel
from models.sales_model import SalesModel


class Database:
    session_maker = None
    session = None
    engine = None

    @staticmethod
    def my_static_method(arg1, arg2):
        return arg1 + arg2

    @staticmethod
    def init_connection():
        Database.engine = create_engine("mysql+mysqlconnector://root:%s@localhost/forsit" %
                                        quote_plus("mauFJcuf5dhRMQrjj"), echo=True)
        BaseModel.metadata.create_all(Database.engine)

        ProductModel.metadata.create_all(Database.engine)
        InventoryModel.metadata.create_all(Database.engine)
        SalesModel.metadata.create_all(Database.engine)

        Database.session_maker = sessionmaker(bind=Database.engine)
        Database.session = Database.session_maker()

    @staticmethod
    def connect():
        return Database.session_maker()

    @staticmethod
    def close():
        Database.session.flush()
        Database.session.rollback()
        Database.session.close()

    @staticmethod
    def get_session():
        if Database.session is None:
            raise Exception("Database session is not initialized.")
        return Database.session
