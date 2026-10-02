
#! 1.main.py -- Fast API code tells how the data is fetched from the database and how it is displayed in the frontend
#!2.database_models.py -- SQLAlchemy code which tells how the data is stored in the database
#!3.models.py -- Pydantic code which tells how the data is stored in the frontend
#!4.database.py -- Database connection code tells how should the connection be established with the database



# Importing the required libraries for the dependencies and for the Fast API framework

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from frontend.models import Product
from frontend.database import engine, session
from frontend import database_models
from sqlalchemy.orm import Session



app = FastAPI()

# CORS configuration to allow requests from the frontend application running on localhost:3000

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
    )

database_models.Base.metadata.create_all(bind=engine)   # engine -- Used to connect SQLAlchemy to the database

@app.get("/")            # get -- to retrieve data from the server
def greet():
    return "Welcome to the new server"

products = [
    Product (id=1, name="Mobile", description="Very Usefull", price=19000, quantity=12),
    Product (id=2, name="Mac", description="Best of all",price=189000, quantity=8),
    Product (id=3, name="Lenovo", description="VeryFast",price=18000, quantity=10),
    Product (id=8, name="HP", description="Average working",price=19000, quantity=2),  
    Product (id=12, name="Asus", description="Heating issue",price=14000, quantity=4)                            
]

def get_db():
    db = session()                      # Creating a session to connect to the database
    try:
        yield db
    finally:
        db.close()


def init_db():
    db = session()
    count = db.query(database_models.Product).count

    if count == 0:
       for product in products:
           db.add(database_models.Product(** product.model_dump()))    # ** means unpacking

       db.commit()

init_db()

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products
    

# To fetch the single product individually -- http://127.0.0.1:8000/product/2 -- will fetch the order in the index two

@app.get("/product/{id}")                             # Dynamically fetching product with prod id
def get_product_by_id(id:int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product
    
    return "product not found"


# http://127.0.0.1:8000/docs -- Swagger UI build in default in Fast API & can be accessed using 'docs'
# After accessing the URL, go to post --try it out --update the data. Can verify in Products if the product has added

@app.post("/products")                                 #post -- to create new data/resources
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product
  


# http://127.0.0.1:8000/docs -- go to put
@app.put("/products/{id}")                                  # put -- to update the data
def update_product(id:int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name                                             # type: ignore
        db_product.description = product.description                               # type: ignore
        db_product.price = product.price                                           # type: ignore
        db_product.quantity = product.quantity                                     # type: ignore             
        db.commit()
        return "Product updated"
    else:
        return "No Product found"


@app.delete("/products/{id}")           # delete -- to delete the data
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    else:
        return "Product not found"



