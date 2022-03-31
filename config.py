import os
from starlette.config import Config

config = Config(".env")


SECRET_KEY = config("EE_SECRET_KEY", cast=str, default="2b2d197649061838c0c381612cb117d5f562ff181f2ed68c7847471af22f83ce")
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"


"""Postgres connection data"""
'''DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_NAME = os.environ["DB_NAME"]'''