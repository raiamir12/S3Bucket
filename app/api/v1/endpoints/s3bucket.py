from fastapi import APIRouter,HTTPException, UploadFile
import traceback
from typing import Any
from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.s3bucket_shemas import File as FileSchema
from app.schemas.s3bucket_shemas import FilesCreate
from app.services.s3bucket_service import file_service
from app.api import dependency
from app.services.s3bucket import obj_bucket
from app.services.filebucket import file_download,file_upload
import json
router = APIRouter()

@router.post("/upload")
def upload_file(file:UploadFile) :
    """
    Retrieve Files.
    """
    try:
        result =file_upload(file=file)
        if result is not None:
           return result
        if not result:
          print(result)  
          raise HTTPException(status_code=404, detail="User Group not found")

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Server Error")

@router.get("/dowload")
def download_file() :
    """
    Retrieve Files.
    """
    try:
        result =file_download()
        if result is not None:
           return result
        if not result:
          raise HTTPException(status_code=404, detail="User Group not found")

    except Exception as e:
        raise HTTPException(status_code=500, detail="Server Error")        

@router.get("", response_model=List[FileSchema])
def list_files(db: Session = Depends(dependency.get_db)) -> Any:
    """
    Retrieve Files.
    """
    try:
        result =obj_bucket
        if result is not None:
           return result
        if not result:
          raise HTTPException(status_code=404, detail="User Group not found")

    except Exception as e:
        raise HTTPException(status_code=500, detail="Server Error")
    

@router.get("", response_model=List[FileSchema])
def list_files(db: Session = Depends(dependency.get_db)) -> Any:
    """
    Retrieve Files.
    """
    try:
        
        file = file_service.list(db)
        return file
       
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server Error")
    


@router.post("", response_model=FileSchema)
def create_file(file_create: FilesCreate,db: Session = Depends(dependency.get_db)) -> Any:
    """
    Create new File.
    """
    try:
       
        file = file_service.create(file_create, db)
        print("***********Here****************")
       
        return file
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server Error")


@router.put("/{id}", response_model=FileSchema)
def update_file(id: int, file_create: FilesCreate, db: Session = Depends(dependency.get_db)) -> Any:
    """
    Update a File.
    """
    if file:
        file = file_service.update(id, file_create, db)
        if not file:
            raise HTTPException(status_code=404, detail="User Group not found")
        else:
            return file
    else:
        raise HTTPException(status_code=403, detail="Forbidden")
    



@router.get("/{id}", response_model=FileSchema)
def get_file(id: int, db: Session = Depends(dependency.get_db)) -> Any:
    """
    Get a File by Id.
    """
    if file:
        file = file_service.get(id, db)
        if not file:
            raise HTTPException(status_code=404, detail="User Group not found")
        else:
            return file
    else:
        raise HTTPException(status_code=403, detail="Forbidden")


@router.delete("/{id}")
def delete_file(id: int, db: Session = Depends(dependency.get_db)) -> Any:
    """
    Delete a File by Id.
    """
    if file_service:
        file_service.remove(id,db)
        return {"detail": "Success"}
    else:
        raise HTTPException(status_code=403, detail="Forbidden")
