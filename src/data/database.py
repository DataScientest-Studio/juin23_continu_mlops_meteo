from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

from decouple import config

DB_USERNAME = config("POSTGRES_USERNAME")
DB_PASSWORD = config("POSTGRES_PASSWORD")

DB_SERVER = config("POSTGRES_SERVER")
DB_PORT = config("POSTGRES_PORT")
DB_DATABASE = config("POSTGRES_DB")

#DB_URL = config("POSTGRES_URL")

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_DATABASE}"

#engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
