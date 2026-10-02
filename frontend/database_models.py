
# Importing necessary modules from SQLAlchemy

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):

    __tablename__ = "product"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(225))
    price = Column(Float)
    quantity = Column(Integer)



