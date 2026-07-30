# =============================================================
# PROJECT : STORE MANAGEMENT SYSTEM
# Uses pickle files as simple storage ("database") for customers,
# products, and orders.
#
# Entities:
#   customer (cid, cname, cadd, cmob)
#   product  (pid, pname, price, pdesc)
#   orders   (oid, cid, pid, qty)
#
# Menu options:
#   1. Add customer
#   2. View all customers
#   3. Delete a customer
#   4. Add product
#   5. View all products
#   6. Update a product's price
#   7. Place an order
#   8. View all orders
#   9. View orders by customer ID
#   0. Exit
# =============================================================

import pickle


# ---------------- CUSTOMER FUNCTIONS ----------------

def add_customer():
    cus_id = input("enter customer ID: ")
    cus_name = input("enter Customer name: ")
    cus_add = input("enter Customer address: ")
    cus_mob = input("enter Customer mobile: ")

    data = {cus_id: [cus_name, cus_add, cus_mob]}
    with open('database.bin', 'ab+') as file:
        pickle.dump(data, file)

    print("\n\t data added successfully!\n")
    input("\nPress Enter to return to the main menu...")


def view_customer():
    print("\n\t\t Customer Details\n")
    with open("database.bin", "rb") as file:
        while True:
            try:
                record = pickle.load(file)
                print(record)
            except EOFError:
                break
    input("\nPress Enter to return to the main menu...")


def delete_customer():
    cid = input("Enter Customer ID To Delete: ")
    all_customers = {}

    # Step 1: read every record from the file into one dictionary
    with open("database.bin", "rb") as file:
        while True:
            try:
                data = pickle.load(file)
                all_customers.update(data)
            except EOFError:
                break

    # Step 2: remove the requested customer, if they exist
    if cid in all_customers:
        all_customers.pop(cid)
        print("\n\t Customer Deleted Successfully!")
    else:
        print("\n\t Customer Not Found!")

    # Step 3: overwrite the file with the updated dictionary
    with open("database.bin", "wb") as file:
        pickle.dump(all_customers, file)

    input("\nPress Enter to return to the main menu...")


# ---------------- PRODUCT FUNCTIONS ----------------

def add_product():
    with open('product.bin', 'ab') as file:
        pid = input("enter product id: ")
        pname = input("enter product name: ")
        price = float(input("enter product price: "))
        pdesc = input("enter product description: ")
        data = {pid: [pname, price, pdesc]}
        pickle.dump(data, file)

    print("\n\t data added successfully!\n")
    input("\nPress Enter to return to the main menu...")


def view_product():
    print("\n\t\t Product Details\n")
    with open("product.bin", "rb") as file:
        while True:
            try:
                record = pickle.load(file)
                print(record)
            except EOFError:
                break
    input("\nPress Enter to return to the main menu...")


def update_product_price():
    pid = input("enter product id to update: ")
    data = {}

    # read every product record into one dictionary
    with open('product.bin', 'rb') as file:
        while True:
            try:
                record = pickle.load(file)
                data.update(record)
            except EOFError:
                break

    if pid in data:
        print("product found: ", data[pid])
        new_price = float(input("enter new price: "))
        data[pid][1] = new_price

        # overwrite the file with the updated dictionary
        with open('product.bin', 'wb') as file:
            pickle.dump(data, file)
        print("price updated successfully!")
    else:
        print("product not found!")

    input("\nPress Enter to return to the main menu...")


# ---------------- ORDER FUNCTIONS ----------------

def place_order():
    oid = input("enter order id: ")
    cid = input("enter customer id: ")
    pid = input("enter product id to order: ")

    # check the product exists before placing the order
    products = {}
    with open('product.bin', 'rb') as product_file:
        while True:
            try:
                products.update(pickle.load(product_file))
            except EOFError:
                break

    if pid in products:
        print("product found: ", products[pid])
        qty = int(input("enter quantity to order: "))
        with open('orders.bin', 'ab') as order_file:
            pickle.dump({oid: [cid, pid, qty]}, order_file)
        print("order placed successfully!")
    else:
        print("product not found!")

    input("\nPress Enter to return to the main menu...")


def view_order():
    with open('orders.bin', 'rb') as file:
        while True:
            try:
                record = pickle.load(file)
                print(record)
            except EOFError:
                break
    input("\nPress Enter to return to the main menu...")


def order_by_cid():
    cid = input("enter customer id to view orders: ")
    found = False

    with open('orders.bin', 'rb') as file:
        while True:
            try:
                record = pickle.load(file)
                # each record looks like {oid: [cid, pid, qty]}
                order_details = list(record.values())[0]
                if order_details[0] == cid:
                    print(record)
                    found = True
            except EOFError:
                break

    if not found:
        print("no orders found for this customer!")

    input("\nPress Enter to return to the main menu...")


# ---------------- MAIN DASHBOARD ----------------

def main():
    while True:
        print("\t\t Welcome to Store Management System")
        print("""
        1. Add customer
        2. View all customers
        3. Delete a customer
        4. Add product
        5. View all products
        6. Update a product price
        7. Place an order
        8. View all orders
        9. View orders by customer ID
        0. Exit
        """)
        choice = int(input("\t\t Choose an option to continue: "))

        if choice == 0:
            print("\t\t Thank you!")
            break
        elif choice == 1:
            add_customer()
        elif choice == 2:
            view_customer()
        elif choice == 3:
            delete_customer()
        elif choice == 4:
            add_product()
        elif choice == 5:
            view_product()
        elif choice == 6:
            update_product_price()
        elif choice == 7:
            place_order()
        elif choice == 8:
            view_order()
        elif choice == 9:
            order_by_cid()
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
