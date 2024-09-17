import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
#THIS FILE IS TO SET THE ORM 
# sqlalchemy is the tool in python to connect postgreSQL to python. Its an ORM tool in python.
load_dotenv()

#SQLALCHEMY_DATABASE_URL = f"postgresql://{os.environ['DATABASE_USER']}:@{os.environ['DATABASE_HOST']}/{os.environ['DATABASE_NAME']}"

user = os.environ['DATABASE_USER']
password = os.environ['DATABASE_PASSWORD']
host = os.environ['DATABASE_HOST']
port = os.environ['DATABASE_PORT']
db_name = os.environ['DATABASE_NAME']

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#Loads Environment Variables: Using load_dotenv(), it loads database credentials from a .env file.
#Constructs a Database URL: Builds the connection string using these credentials.
#Creates a Database Engine: Sets up the engine that will connect to the database.
#Sets Up a Session Factory: Defines how to create sessions to interact with the database.
#Defines a Base Class for Models: Provides a base class for creating database tables using SQLAlchemy models.