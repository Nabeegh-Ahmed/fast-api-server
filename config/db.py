from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base_model import BaseModel
from models.product_model import ProductModel


class Database:
    session_maker = None
    session = None
    engine = None

    @staticmethod
    def my_static_method(arg1, arg2):
        return arg1 + arg2

    def __init__(self):
        Database.engine = create_engine("mysql+mysqlconnector://root:%s@localhost/forsit" %
                                        quote_plus("mauFJcuf5dhRMQrjj"), echo=True)
        BaseModel.metadata.create_all(self.engine)

        ProductModel.metadata.create_all(self.engine)

        Database.session_maker = sessionmaker(bind=self.engine)
        Database.session = self.session_maker()

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
