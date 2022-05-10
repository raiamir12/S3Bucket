from fastapi import FastAPI
from app.api.v1.endpoints import s3bucket
def create_app():

    app = FastAPI(
        title="FastAPI",
        description="FastAPI",
        version="1.0",
        docs_url="/")
    
    app.include_router(
        s3bucket.router,
        prefix="/s3bucket",
        tags=["Bucket"]
    )  

    

    return app  