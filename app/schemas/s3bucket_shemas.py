from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class FilesBase(BaseModel):

    filename: Optional[str]=None
    filesize: Optional[int]=None
    file_type: Optional[str]=None
    file_path:Optional[str]=None
    file_url:Optional[str]=None
    file_storage_id: Optional[str]=None
    uploaded_datetime: Optional[datetime]
    is_deleted: Optional[bool] = False


class FilesCreate(FilesBase):

    filename: str
    filesize: int
    file_type: str
    file_storage_id: str
    uploaded_datetime: datetime
    is_deleted: bool = False

# Properties to receive via API on update


class FilesUpdate(FilesBase):
    pass


class File(FilesBase):
    # id: int
    pass

    class Config:
        orm_mode = True
