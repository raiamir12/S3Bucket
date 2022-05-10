"""
FastAPI server configuration
"""

# pylint: disable=too-few-public-methods

from pathlib import Path


from urllib.parse import quote_plus  
from decouple import RepositoryEnv, Config
from pydantic import BaseModel

DEV_ENV = ".dev.env"
STG_ENV = ".stg.env"
PROD_ENV = ".env"

def __get_config() -> Config:
    if Path(DEV_ENV).exists():
        print("Loading .dev.env........")
        return Config(RepositoryEnv(".dev.env"))
    elif Path(STG_ENV).exists():
        print("Loading .stg.env........")
        return Config(RepositoryEnv(".stg.env"))
    elif Path(PROD_ENV).exists():
        print("Loading .env........")
        return Config(RepositoryEnv(".env"))
    

config = __get_config()

class Settings(BaseModel):
    """Server config settings"""
    # PROJECT_NAME = config("PROJECT_NAME")

    postgres_username = config("POSTGRES_USERNAME")
    postgres_password = quote_plus(config("POSTGRES_PASSWORD"))
    postgres_server = config("POSTGRES_SERVER")
    postgres_port = config("POSTGRES_PORT")
    postgres_db = config("POSTGRES_DB")
    POSTGRES_URI = f"postgresql://{postgres_username}:{postgres_password}@{postgres_server}:{postgres_port}/{postgres_db}"
    
settings = Settings()    