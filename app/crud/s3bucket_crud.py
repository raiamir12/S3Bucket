
from typing import Any, Dict, List, Optional, Union
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.s3bucket import Files
from app.schemas.s3bucket_shemas import FilesCreate,FilesUpdate

class CRUDBank(CRUDBase[Files, FilesCreate, FilesUpdate]):
    
    def create(self, db: Session, obj_in: FilesCreate) -> Files:
        return super().create(db, obj_in=obj_in)
    
    def update(self, db: Session, db_obj: Files, obj_in: Union[FilesUpdate, Dict[str, Any]]) -> Files:
        return super().update(db, db_obj=db_obj, obj_in = obj_in)
    
    def remove(self, db: Session, id: int) -> Files:
        return super().remove(db, id=id)
    
    def get(self, db: Session, id: Any) -> Optional[Files]:
        return super().get(db, id)
    
    def get_multi(self, db: Session, skip: int = 0, limit: int = 100) -> List[Files]:
        return super().get_multi(db, skip=skip, limit = limit)
    
    def get_by_filter(self, db: Session, filter_spec: Any) -> Optional[Files]:
        file = super().query_by_filter(db,filter_spec)
        if file:
            return file[0]
    
    def list_by_filter(self, db: Session, filter_spec: Any) -> List[Files]:
        file = super().query_by_filter(db,filter_spec)
        return file
    
file_crud = CRUDBank(Files) 