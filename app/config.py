import os

from dotenv import load_dotenv, find_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware
from fastapi_sqlalchemy import DBSessionMiddleware

load_dotenv(find_dotenv())

# setting up db url
# DB_USERNAME = os.getenv("DB_USERNAME")
# DB_PASSWORD = os.getenv("DB_PASSWORD")
# DB_HOSTNAME = os.getenv("DB_HOSTNAME")
# DB_PORT = str(os.getenv("DB_PORT"))
# DB_NAME = os.getenv("DB_NAME")
# SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/{DB_NAME}"

# setting middlewares ['CORSMiddleware', 'DBSessionMiddleware']
middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    ),
    # Middleware(
    #     DBSessionMiddleware,
    #     db_url=SQLALCHEMY_DATABASE_URL
    # )
]
