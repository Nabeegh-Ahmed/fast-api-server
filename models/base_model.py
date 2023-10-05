import datetime
import uuid
from sqlalchemy import DateTime, Column, String, Boolean
from sqlalchemy.orm import declarative_base, Mapped


class BaseModel(declarative_base()):
    __abstract__ = True
    id = Column('id', String(36), default=str(uuid.uuid1()), primary_key=True)
    created_at = Column(
        'created_at',
        DateTime(timezone=True),
        default=datetime.datetime.utcnow,
        nullable=False
    )
    updated_at: Mapped[DateTime] = Column(
        'updated_at',
        DateTime(timezone=True),
        default=datetime.datetime.utcnow,
        nullable=False
    )
    is_deleted: Mapped[bool] = Column(
        'is_deleted',
        Boolean,
        default=False,
        nullable=False
    )

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
