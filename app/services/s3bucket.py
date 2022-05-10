import boto3
import pandas



def S3_BUCKET():


    s3 = boto3.resource("s3")

    # Print out bucket names
    for bucket in s3.buckets.all():
     print(bucket.name)


   # Create an S3 access object
#    s3 = boto3.client("s3")


    s3.download_file(
    Bucket="sample-bucket-1801", 
    Key="train.csv", 
    Filename="data/downloaded_from_s3.csv"
    )

    s3.upload_file(
    Filename="data/downloaded_from_s3.csv",
    Bucket="sample-bucket-1801",
    Key="new_file.csv",
    )






def s3_bucket():
# Creating the low level functional client
    client = boto3.client(
    's3',
    aws_access_key_id = 'AKIA2B73GPJ2WA4HTJWC',
    aws_secret_access_key = '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',
    region_name = 'us-east-2'
    )

    # Creating the high level object oriented interface
    resource = boto3.resource(
    's3',
    aws_access_key_id = 'AKIA46SFIWN5AMWMDQVB',
    aws_secret_access_key = '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',
    region_name = 'ap-south-1'
    )

    # Fetch the list of existing buckets
    clientResponse = client.list_buckets()

    # Print the bucket names one by one
    print('Printing bucket names...')
    for bucket in clientResponse['Buckets']:
     print(f'Bucket Name: {bucket["Name"]}')

    # # Creating a bucket in AWS S3
    # location = {'LocationConstraint': 'ap-south-1'}
    # client.create_bucket(
    # Bucket='testbucket5353',
    # CreateBucketConfiguration=location
    # )


    # # Create the S3 object
    # obj = client.get_object(
    # Bucket = 'testbucket5353',
    # Key = 'sql-shack-demo.csv'
    # )

    # # Read data from the S3 object
    # data = pandas.read_csv(obj['Body'])

    # # Print the data frame
    # print('Printing the data frame...')
    # print(data)

obj_bucket=s3_bucket()
  
