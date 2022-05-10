from pprint import pprint
from urllib import response
from boto3 import Session
import boto3
import requests
from fastapi import UploadFile
import string,random
import datetime
import uuid
# session = boto3.Session(profile_name='arundhaj')

# s3_client = session.client('s3')

# s3_bucket_name = 'codepossibility-presigned'
object_name = 'TestUploadFile.txt'

ACCESS_KEY = "AKIA2B73GPJ2WA4HTJWC"
SECRET_KEY = "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"
REGION_NAME = "us-east-2"
BUCKET_NAME = "testbucket5353"
# file_name = response['fields']['key'].split("/")[-1]
key = ' '.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
key+=".txt"
# uniq_filename = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '.')+".txt"
uniq_filename = str(uuid.uuid4())+".txt"
session = Session(aws_access_key_id=ACCESS_KEY,
              aws_secret_access_key=SECRET_KEY,
              region_name=REGION_NAME)

s3_client = session.client('s3')


def create_bucket():
    response = s3_client.create_bucket(Bucket=BUCKET_NAME)
    pprint(response)


def file_upload(file:UploadFile):
    response = s3_client.generate_presigned_post(
        BUCKET_NAME,
        key,
        ExpiresIn=3600
    )
    pprint(response)
    #Upload file to S3 using presigned URL
    # files = { 'file': open(OBJECT_NAME_TO_UPLOAD, 'rb')}
    res = requests.post(response['url'], data=response['fields'], files={'file':(file.filename,file.file)})
    print(res.status_code)
    # key = os.file.endswith(".txt")
    return res 
def file_download():
    response = s3_client.generate_presigned_url(
        'get_object',
        Params={
            'Bucket': BUCKET_NAME,
            'Key': key
        },
        ExpiresIn=3600
    )

    pprint(response)
    return response


# create_bucket()
# file_upload()
# file_download()