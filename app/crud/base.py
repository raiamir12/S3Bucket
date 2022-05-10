from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy_filters import apply_filters

from app.db.base import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()
    
    def get_multi(self, db: Session, skip: int = 0, limit: int = 100) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()
    '''
        Return filtered resultset based on condition.
        :param query: takes session
        :param filter_spec: Its a list, ie: [(field,op,value)], can also pass a model for joints(optional)
        operator list:
            ==, eq
            !=, ne
            >, gt
            <, lt
            >=, ge
            <=, le
            like
            in
            not_in
        :return: resultset
        Example : filter_spec = [
                                    {'model': 'Foo', 'field': 'name', 'op': '==', 'value': 'name_1'},
                                    {'model': 'Bar', 'field': 'count', 'op': '>=', 'value': 5},
                                ]
    '''
    def query_by_filter(self, db: Session, filter_spec: Any) -> Optional[List[ModelType]]:
        query = db.query(self.model)
        filtered_query = apply_filters(query, filter_spec)
        return filtered_query.all()

    def create_all(self, db: Session, obj_in: List[CreateSchemaType]):
        for obj in obj_in:
            obj_data = jsonable_encoder(obj)
            db_obj = self.model(**obj_data)  # type: ignore
            db.add(db_obj)
        db.commit()
    
    def create(self, db: Session, obj_in: CreateSchemaType,**kwargs) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        for key, value in kwargs.items():
            if hasattr(db_obj,key):
                setattr(db_obj, key, value)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def create_bulk(self,db: Session, obj_in: List[UpdateSchemaType]) -> ModelType:
        model_dict = []
        for obj in obj_in:
            model_dict.append(obj.dict())
        db.bulk_insert_mappings(self.model, model_dict)
        db.commit()
        return obj_in


    def update(self,db: Session, db_obj: ModelType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def update_bulk(self,db: Session, obj_in: List[UpdateSchemaType]) -> ModelType:
        model_dict = []
        for obj in obj_in:
            model_dict.append(obj.dict())
        db.bulk_update_mappings(self.model, model_dict)
        db.commit()
        return obj_in

    def remove(self, db: Session, id: int) -> ModelType:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj