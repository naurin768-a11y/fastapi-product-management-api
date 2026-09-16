# fastapi-product-management-api
A beginner-friendly Product Management REST API built with Python and FastAPI, demonstrating CRUD operations, path parameters, and query parameters.
# FastAPI Product Management API

A beginner-friendly REST API built with **FastAPI** and **Python** to practice CRUD operations and API endpoints.

## 📌 Project Overview

This project is a simple product management API.

It stores product information such as:

* Product name
* Price
* Stock quantity

The API allows users to view, search, add, update, and delete products.

## 🛠️ Technologies Used

* Python
* FastAPI
* Uvicorn

## 📂 Project Structure

```text
FastAPI-Product-API/
│
├── main.py
└── README.md
```

## 🚀 Installation

Install the required packages:

```bash
pip install fastapi uvicorn
```

## ▶️ Run the Application

Run the FastAPI server using:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## 📖 API Documentation

FastAPI automatically provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can test all the endpoints directly from the Swagger UI.

## 🔗 API Endpoints

| Method | Endpoint                                | Description          |
| ------ | --------------------------------------- | -------------------- |
| GET    | `/products`                             | Display all products |
| GET    | `/products/{product_name}`              | Search for a product |
| POST   | `/products/{product_name}/price/stocks` | Add a new product    |
| PUT    | `/products/{product_name}/price`        | Update product price |
| PUT    | `/products/{product_name}/stock`        | Update product stock |
| DELETE | `/products/{product_name}`              | Delete a product     |

## 💡 Example

### Get all products

```http
GET /products
```

Example response:

```json
[
  {
    "product": "Milk",
    "price": 2.5,
    "stock": 10
  }
]
```

### Search for a product

```http
GET /products/Milk
```

### Update price

```http
PUT /products/Milk/price?new_price=3.5
```

### Update stock

```http
PUT /products/Milk/stock?quantity=5
```

### Delete a product

```http
DELETE /products/Milk
```

## 🎯 What I Learned

Through this project, I practiced:

* Creating a FastAPI application
* Creating API routes
* Using GET, POST, PUT, and DELETE methods
* Using path parameters
* Using query parameters
* Working with lists in Python
* Updating and deleting list elements
* Testing APIs using Swagger UI

## 📌 Future Improvements

Possible improvements for this project:

* Use a database such as SQLite or PostgreSQL
* Use Pydantic models for request validation
* Separate the project into multiple files
* Add better error handling
* Add proper HTTP status codes
* Add authentication

## 👩‍💻 Author

Built as part of my journey learning **Python, FastAPI, and backend development**.
