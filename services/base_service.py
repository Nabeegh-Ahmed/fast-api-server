from typing import TypeVar
from models.base_model import BaseModel
from config.db import Database

M = TypeVar("M", BaseModel, object)


class BaseService:
    def __init__(self, model: M):
        self.model = model

    def get_all(self, limit: int = 10, offset: int = 0):
        return Database.get_session().query(self.model).limit(limit).offset(offset).all()

    def get_by_id(self, id):
        return Database.get_session().query(self.model).get(id)

    def create(self, *args, **kwargs):
        entity = self.model(*args, **kwargs)
        Database.get_session().add(entity)
        Database.get_session().commit()

    def update(self, entity: M):  # TODO
        Database.get_session().add(entity)
        Database.get_session().commit()

    def delete(self, id: str):
        entity = self.get_by_id(id)
        entity.is_deleted = True
        self.update(entity)
