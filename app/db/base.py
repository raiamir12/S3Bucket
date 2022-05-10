from typing import Any
from sqlalchemy import Boolean, Column,DateTime, Integer, func
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id = Column(Integer, primary_key=True,autoincrement=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_deleted = Column(Boolean, default=False)
    __name__: str
    
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    
    def to_schema(self, schema_cls):
        return schema_cls(**self.__dict__)
    
    @classmethod
    def from_schema(cls, schema_obj):
        return cls(**schema_obj.__dict__)