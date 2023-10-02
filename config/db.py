from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base_model import BaseModel
from models.product_model import ProductModel


def connectDB():
    engine = create_engine("mysql+mysqlconnector://root:%s@localhost/forsit" %
                           quote_plus("mauFJcuf5dhRMQrjj"), echo=True)
    BaseModel.metadata.create_all(engine)

    ProductModel.metadata.create_all(engine)

    session_maker = sessionmaker(bind=engine)
    return session_maker()
