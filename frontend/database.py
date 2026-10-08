import os

from sqlalchemy import create_engine
from urllib.parse import quote_plus
from sqlalchemy.orm import sessionmaker

# Read database configuration from environment variables. 
# Defaults are useful for running the application directly on your Mac during development.

DB_HOST = os.getenv("DB_HOST", "localhost") 
DB_USER = os.getenv("DB_USER", "root") 
DB_PASSWORD = os.getenv("DB_PASSWORD", "YOUR_PASSWORD") 
DB_PORT = os.getenv("DB_PORT", "3306") 
DB_NAME = os.getenv("DB_NAME", "fast_api")


encoded_password = quote_plus(DB_PASSWORD)

db_url = (                                                                  # DB Connection URL for SQLAlchemy
    f"mysql+pymysql://{DB_USER}:{encoded_password}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
engine = create_engine(db_url)                                              # Creating engine
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)      # Creating sessionfactory
