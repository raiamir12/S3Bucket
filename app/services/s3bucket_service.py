# import boto3
# import pandas

# def s3_bucket():
# # Creating the low level functional client
#     client = boto3.client(
#     's3',
#     aws_access_key_id = 'AKIA46SFIWN5AMWMDQVB',
#     aws_secret_access_key = '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',
#     region_name = 'ap-south-1'
#     )

#     # Creating the high level object oriented interface
#     resource = boto3.resource(
#     's3',
#     aws_access_key_id = 'AKIA46SFIWN5AMWMDQVB',
#     aws_secret_access_key = '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',
#     region_name = 'ap-south-1'
#     )

#     # Fetch the list of existing buckets
#     clientResponse = client.list_buckets()

#     # Print the bucket names one by one
#     print('Printing bucket names...')
#     for bucket in clientResponse['Buckets']:
#      print(f'Bucket Name: {bucket["Name"]}')

#     # Creating a bucket in AWS S3
#     location = {'LocationConstraint': 'ap-south-1'}
#     client.create_bucket(
#     Bucket='sql-server-shack-demo-3',
#     CreateBucketConfiguration=location
#     )


#     # Create the S3 object
#     obj = client.get_object(
#     Bucket = 'sql-server-shack-demo-1',
#     Key = 'sql-shack-demo.csv'
#     )

#     # Read data from the S3 object
#     data = pandas.read_csv(obj['Body'])

#     # Print the data frame
#     print('Printing the data frame...')
#     print(data)


# s3=s3_bucket()    



# def S3_BUCKET():


#     s3 = boto3.resource("s3")

#     # Print out bucket names
#     for bucket in s3.buckets.all():
#      print(bucket.name)


#    # Create an S3 access object
# #    s3 = boto3.client("s3")


#     s3.download_file(
#     Bucket="sample-bucket-1801", 
#     Key="train.csv", 
#     Filename="data/downloaded_from_s3.csv"
#     )

#     s3.upload_file(
#     Filename="data/downloaded_from_s3.csv",
#     Bucket="sample-bucket-1801",
#     Key="new_file.csv",
#     )


# S3_bUCKET=S3_BUCKET()




from typing import Any, Dict, List, Optional, Union
from fastapi import Depends
from sqlalchemy.orm import Session
from app.crud.s3bucket_crud import file_crud
from app.schemas.s3bucket_shemas import FilesCreate, FilesUpdate, File
import traceback

class FileService():
    
    def create(self, obj_in: FilesCreate, db: Session) -> File:
        try:
            file = file_crud.create(db, obj_in=obj_in)
            return file.to_schema(File)
        except Exception as e:
            return e
    
    def update(self, id:int, bank_in: FilesUpdate,db: Session) -> Optional[File]:
        try:
            file = file_crud.get(db=db, id=id)
            if file:
                file_updated = file_crud.update(db=db, db_obj=file, obj_in=bank_in)
                return file_updated.to_schema(File)
        except Exception as e:
            return e
    
    def remove(self, id: int, db: Session):
        try:
            file_crud.remove(db, id=id)
        except Exception as e:
            return e
    
    def get(self, id: int, db: Session) -> Optional[File]:
        try:
            return file_crud.get(db, id)
        except Exception as e:
            return e
    
    def list(self, skip: int, limit: int, db: Session ) -> List[File]:
        try:
            return file_crud.get_multi(db, skip=skip, limit = limit)
        except Exception as e:
            return e
    
    def list_by_company(self, company_id: int, status:int, db: Session) -> List[File]:
        try:
            filter_spec = [{'field': 'company_id', 'op': '==', 'value': company_id}]
            if status != None:
                filter_spec.append({'field': 'status', 'op': '==', 'value': status})
            file = file_crud.list_by_filter(db,filter_spec)
            return file
        except Exception as e:
            traceback.print_exc()
            raise e
    
file_service = FileService() 