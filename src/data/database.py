from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

from decouple import config

DB_USERNAME = config("POSTGRES_USER")
DB_PASSWORD = config("POSTGRES_PASSWORD")

#DB_SERVER = config("POSTGRES_SERVER")
DB_SERVER = 'prj-network_from_compose'
DB_PORT = config("POSTGRES_PORT")
DB_DATABASE = config("POSTGRES_DB")

DB_URL = config("RDS_URL")

#SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_DATABASE}"
SQLALCHEMY_DATABASE_URL = DB_URL

#engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
