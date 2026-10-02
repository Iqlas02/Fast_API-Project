# FastAPI Product Management Project

## Screenshots

![React Products Page](Screenshots/Frontend-Dashboard.png)

![FastAPI Swagger UI](Screenshots/Swagger-UI.png)

## Overview

This project is a full-stack web application built using **FastAPI**, **React**, **SQLAlchemy**, and **MySQL**.

The application provides a REST API for managing products and a React-based frontend for displaying and interacting with the product data.

The project was developed as a practical exercise to understand how a modern backend API connects with a frontend application and a relational database.

### Application Flow

```text
React Frontend
      ↓
   HTTP / Axios
      ↓
FastAPI Backend
      ↓
   SQLAlchemy
      ↓
    MySQL
```


## Technologies Used

| Technology | Purpose                                      |
| ---------- | -------------------------------------------- |
| Python     | Backend programming language                 |
| FastAPI    | Building the REST API                        |
| Uvicorn    | Running the FastAPI application server       |
| Pydantic   | Request and response data validation         |
| SQLAlchemy | ORM for database interaction                 |
| PyMySQL    | Connecting Python/SQLAlchemy to MySQL        |
| MySQL      | Relational database                          |
| React      | Frontend user interface                      |
| HTML / CSS | Frontend structure and styling               |
| Git        | Version control                              |
| GitHub     | Source code repository                       |

## Project Structure

```text
Fast API/
│
├── frontend/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── database_models.py
│   │
│   ├── package.json
│   ├── package-lock.json
│   │
│   ├── public/
│   │   ├── index.html
│   │   └── manifest.json
│   │
│   └── src/
│       ├── App.js
│       ├── App.css
│       ├── TaglineSection.js
│       ├── TaglineSection.css
│       ├── index.js
│       └── index.css
│
├── Screenshots/
│   ├── Frontend-Dashboard.png
│   └── Swagger-UI.png
│
├── .gitignore
├── README.md
├── requirements.txt
└── package-lock.json
```

### Backend Files

| File                 | Purpose                                                       |
| -------------------- | ------------------------------------------------------------- |
| `main.py`            | Creates the FastAPI application and defines API endpoints     |
| `models.py`          | Defines the Pydantic `Product` model used for validation      |
| `database.py`        | Configures the SQLAlchemy database engine and session factory |
| `database_models.py` | Defines the SQLAlchemy database model and `product` table     |

### Frontend

The React frontend is located inside the `frontend/` directory.

It communicates with the FastAPI backend through HTTP requests and displays the product information returned by the API.





## API Endpoints

The FastAPI backend provides CRUD operations for managing products.

**Base URL:**

```text
http://127.0.0.1:8000
```

### 1. Get All Products

```http
GET /products
```

Returns all products stored in the MySQL database.

Example:

```text
GET http://127.0.0.1:8000/products
```

---

### 2. Get Product by ID

```http
GET /product/{id}
```

Returns a specific product using its ID.

Example:

```text
GET http://127.0.0.1:8000/product/2
```

The `{id}` value is a path parameter.

---

### 3. Create a Product

```http
POST /products
```

Creates a new product in the database.

Example request body:

```json
{
  "id": 10,
  "name": "Keyboard",
  "description": "Mechanical keyboard",
  "price": 2500,
  "quantity": 20
}
```

The request data is validated using the Pydantic `Product` model before being stored in MySQL.

---

### 4. Update a Product

```http
PUT /products/{id}
```

Updates an existing product using its ID.

Example:

```text
PUT http://127.0.0.1:8000/products/2
```

Example request body:

```json
{
  "id": 2,
  "name": "MacBook",
  "description": "Updated product description",
  "price": 189000,
  "quantity": 10
}
```

---

### 5. Delete a Product

```http
DELETE /products/{id}
```

Deletes a product from the database using its ID.

Example:

```text
DELETE http://127.0.0.1:8000/products/2
```

---

## CRUD Operations

The API follows the basic CRUD pattern:

| Operation | HTTP Method | Endpoint         | Purpose           |
| --------- | ----------- | ---------------- | ----------------- |
| Create    | POST        | `/products`      | Add a new product |
| Read      | GET         | `/products`      | Get all products  |
| Read      | GET         | `/product/{id}`  | Get one product   |
| Update    | PUT         | `/products/{id}` | Update a product  |
| Delete    | DELETE      | `/products/{id}` | Delete a product  |

## Interactive API Documentation

FastAPI automatically provides interactive API documentation through Swagger UI.

When the backend is running, open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI can be used to test the available API endpoints directly from the browser.



## Database

This project uses **MySQL** as the relational database.

**SQLAlchemy** is used as the ORM (Object Relational Mapper) between the FastAPI application and MySQL.

The database interaction follows this flow:

```text
FastAPI
   ↓
SQLAlchemy
   ↓
PyMySQL
   ↓
MySQL
   ↓
Product Table
```

### Database Configuration

The database connection is configured in:

```text
frontend/database.py
```

SQLAlchemy creates a database engine using the MySQL connection URL.

The application then uses a SQLAlchemy session to perform database operations such as:

* Reading products
* Adding products
* Updating products
* Deleting products

### Database Model

The SQLAlchemy database model is defined in:

```text
frontend/database_models.py
```

The `Product` model represents the `product` table in MySQL.

The table contains the following columns:

| Column        | Type    | Description                               |
| ------------- | ------- | ----------------------------------------- |
| `id`          | Integer | Primary key and unique product identifier |
| `name`        | String  | Product name                              |
| `description` | String  | Product description                       |
| `price`       | Float   | Product price                             |
| `quantity`    | Integer | Available product quantity                |

### Pydantic Model vs SQLAlchemy Model

The project uses two `Product` models for different purposes.

| Model                | File                 | Purpose                       |
| -------------------- | -------------------- | ----------------------------- |
| Pydantic `Product`   | `models.py`          | Validates API request data    |
| SQLAlchemy `Product` | `database_models.py` | Represents the database table |

The conversion between them is performed using:

```python
database_models.Product(
    **product.model_dump()
)
```

Conceptually:

```text
Client JSON
     ↓
Pydantic Product
     ↓
Validation
     ↓
product.model_dump()
     ↓
Python Dictionary
     ↓
SQLAlchemy Product
     ↓
MySQL
```

### Database Session

The FastAPI application creates database sessions through the `get_db()` dependency.

```python
def get_db():
    db = session()

    try:
        yield db

    finally:
        db.close()
```

The session is provided to API endpoints using FastAPI's dependency injection:

```python
db: Session = Depends(get_db)
```

After the API operation is completed, the database session is closed.

This helps prevent database connections from remaining open unnecessarily.

> **Note:** The current learning project contains local database configuration. In a production application, database credentials should be stored in environment variables rather than committed directly to source code.


## Installation & Setup

### 1. Clone the Repository

Clone the GitHub repository:

```bash
git clone https://github.com/Iqlas02/Fast_API-Project.git
```

Move into the project directory:

```bash
cd Fast_API-Project
```

### 2. Create a Python Virtual Environment

Create a virtual environment:

```bash
python3 -m venv myenv
```

Activate it on macOS/Linux:

```bash
source myenv/bin/activate
```

After activation, the terminal should show something similar to:

```text
(myenv)
```

### 3. Install Python Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

The main backend dependencies include:

* FastAPI
* Uvicorn
* Pydantic
* SQLAlchemy
* PyMySQL
* python-dotenv

### 4. Configure MySQL

Make sure a MySQL Server is installed and running.

Create a database named:

```text
fast_api
```

The application uses MySQL through SQLAlchemy and PyMySQL.

> **Important:** Database credentials should be configured locally and should not be committed to GitHub.

### 5. Configure the Database Connection

The database connection is configured in:

```text
frontend/database.py
```

For a local setup, use your own MySQL username, password, host, port, and database name.

Do not use another developer's database credentials.

### 6. Start the FastAPI Backend

From the project root directory, run:

```bash
uvicorn frontend.main:app --reload
```

The FastAPI backend will be available at:

```text
http://127.0.0.1:8000
```

FastAPI's interactive Swagger documentation is available at:

```text
http://127.0.0.1:8000/docs
```

### 7. Start the React Frontend

Open another terminal window.

Navigate to the React application:

```bash
cd frontend
```

Install the frontend dependencies:

```bash
npm install
```

Start the React development server:

```bash
npm start
```

The React frontend will normally be available at:

```text
http://localhost:3000
```

### 8. Application Architecture

Once both servers are running, the application works approximately as follows:

```text
                  Browser
                     │
                     ▼
          React Frontend
        http://localhost:3000
                     │
                     │ HTTP / Axios
                     ▼
           FastAPI Backend
        http://127.0.0.1:8000
                     │
                     ▼
                SQLAlchemy
                     │
                     ▼
                  MySQL
                     │
                     ▼
               Product Table
```

### 9. Stopping the Servers

To stop a running development server, press:

```text
Ctrl + C
```

This stops the local server process.

The server can be started again using the corresponding command.

## Development Notes

This project was created as a learning/practice project to understand:

* FastAPI application structure
* REST API development
* CRUD operations
* Pydantic data validation
* FastAPI dependency injection
* SQLAlchemy ORM
* MySQL database connectivity
* React frontend integration
* Axios HTTP requests
* CORS configuration
* Git and GitHub workflow



