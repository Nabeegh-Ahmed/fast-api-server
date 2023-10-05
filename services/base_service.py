import datetime
from typing import TypeVar
from models.base_model import BaseModel
from config.db import Database
from sqlalchemy.orm import joinedload


M = TypeVar("M", BaseModel, object)


class BaseService:
    def __init__(self, model: M):
        self.model = model

    def get_all(self, limit: int = 10, offset: int = 0, populate_attributes: list = []):
        query = Database.get_session().query(self.model)
        for attr in populate_attributes:
            query = query.options(joinedload(getattr(self.model, attr)))
        return query.limit(limit).offset(offset).all()

    def get_by_id(self, id, populate_attributes: list = []):
        query = Database.get_session().query(self.model)
        for attr in populate_attributes:
            query = query.options(joinedload(getattr(self.model, attr)))
        return query.get(id)

    def create(self, **kwargs):
        entity = self.model(**kwargs)
        Database.get_session().add(entity)
        Database.get_session().commit()
        return entity

    def update(self, entity: M):
        # Database.get_session().add(entity)
        entity.updated_at = datetime.datetime.utcnow()
        Database.get_session().commit()
        return entity

    def delete(self, id: str):
        entity = self.get_by_id(id)
        entity.is_deleted = True
        self.update(entity)

    def get_by_property(self, property, value):
        attribute = getattr(self.model, property)
        return Database.get_session().query(self.model).filter(attribute == value).first()
