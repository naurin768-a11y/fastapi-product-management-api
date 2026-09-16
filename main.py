# pip install fastapi uvicorn

from fastapi import FastAPI

app = FastAPI()

products = ["Milk", "Eggs", "Bread", "Butter", "Cheese"]
prices = [2.5, 3.0, 1.5, 4.0, 5.0]
stock = [10, 20, 15, 8, 5]


# GET - Display all products

@app.get("/products")
def display_products():

    result = []

    for i in range(len(products)):
        result.append({
            "product": products[i],
            "price": prices[i],
            "stock": stock[i]
        })

    return result


# GET - Search product

@app.get("/products/{product_name}")
def search_product(product_name):

    if product_name in products:

        index = products.index(product_name)

        return {
            "product": products[index],
            "price": prices[index],
            "stock": stock[index]
        }

    return {"message": "Product not found!"}


# PUT - Update price

@app.put("/products/{product_name}/price")
def update_price(product_name: str, new_price: float):

    if product_name in products:

        index = products.index(product_name)

        prices[index] = new_price

        return {
            "message": "Price updated successfully",
            "product": product_name,
            "new_price": new_price
        }

    return {"message": "Product not found!"}


# PUT - Update stock

@app.put("/products/{product_name}/stock")
def update_stock(product_name: str, quantity: int):

    if product_name in products:

        index = products.index(product_name)

        stock[index] += quantity

        return {
            "message": "Stock updated successfully",
            "product": product_name,
            "stock": stock[index]
        }

    return {"message": "Product not found!"}


# DELETE - Delete product

@app.delete("/products/{product_name}")
def delete_product(product_name: str):

    if product_name in products:

        index = products.index(product_name)

        # Using pop()
        products.pop(index)
        prices.pop(index)
        stock.pop(index)

        return {
            "message": f"{product_name} deleted successfully!"
        }

    return {"message": "Product not found!"}

@app.post("/products/{product_name}/price/stocks")
def post_product(product_name: str,price:int,stocks:int):

    if product_name not in products:


        # Using pop()
        products.append(product_name)
        prices.append(price)
        stock.append(stocks)

        return {
            "product": products[-1],
            "price": prices[-1],
            "stock": stock[-1]
        }

    return {"message": "Product also there in list and found!"}