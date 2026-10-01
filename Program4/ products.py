import json

FILE = "products.json"

def load_products():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_products(products):
    with open(FILE, "w") as f:
        json.dump(products, f, indent=4)

def add_product(products):
    product = {
        "id": input("Enter Product ID: "),
        "name": input("Enter Product Name: "),
        "price": input("Enter Price: "),
        "quantity": input("Enter Quantity: ")
    }

    products.append(product)
    save_products(products)
    print("Product added!")

def search_product(products):
    product_id = input("Enter Product ID: ")

    for product in products:
        if product["id"] == product_id:
            print(product)
            return

    print("Product not found.")

def delete_product(products):
    product_id = input("Enter Product ID: ")

    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            save_products(products)
            print("Product deleted!")
            return

    print("Product not found.")

products = load_products()

while True:
    print("\n--- Product Management ---")
    print("1. Add Product")
    print("2. Search Product")
    print("3. Delete Product")
    print("4. Display Products")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_product(products)
    elif choice == "2":
        search_product(products)
    elif choice == "3":
        delete_product(products)
    elif choice == "4":
        for product in products:
            print(product)
    elif choice == "5":
        break
    else:
        print("Invalid choice")