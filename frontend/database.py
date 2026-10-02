from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "mysql+pymysql://root:123456@localhost:3306/fast_api"              # DB connection
engine = create_engine(db_url)                                              # Creating engine
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)      # Creating sessionfactory
