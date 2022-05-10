
"""
Files model

"""
from sqlalchemy import Column, ForeignKey,Integer, String, Float,Boolean,DATETIME
from sqlalchemy.orm import relationship
from app.db.base import Base


class Files(Base):
    
    filename = Column(String(256))
    filesize = Column(Integer())
    file_type = Column(String(256))
    file_path=Column(String(256))
    file_url=Column(String(256))
    file_storage_id = Column(Integer())
    uploaded_datetime = Column(DATETIME)
    is_deleted = Column(Boolean, default=1)



    
