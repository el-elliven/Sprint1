from customer import all_customers, delete_customer, add_customer, update_customer
from products import all_products, add_product, delete_product, update_product

from purchase import *


def menu():
    while True:
        print("""

        ***** WELCOME WELCOME *****
        
        CUSTOMER
        1. Add a customer.
        2. Delete a customer. 
        3. View customers.
        4. Update a customer's records.

        PRODUCTS
        5. Insert a product.
        6. View all the products. 
        7. Delete a product in products. 
        8. Modify/update a product. 
        
        MAKE A PURCHASE
        9. Make a purchase.
        
        EXIT
        0. Exit the program.   
        """)
        ans = input("Enter your selection: ")
        if ans == '1':
            print("You have selected Add a customer.")
            add_customer()
        elif ans == '2':
            print("You have selected delete a customer.")
            delete_customer()
        elif ans == '3':
            print("You have selected view customers")
            all_customers()
        elif ans == '4':
            print("You have selected Update customer's record")
            update_customer()
        elif ans == '5':
            print("You have selected Insert a product into the record")
            add_product()
        elif ans == '6':
            print("You have selected View all product records")
            all_products()
        elif ans == '7':
            print("You have selected delete a product from the record")
            delete_product()
        elif ans == '8':
            print("You have selected update/modify a product from the record")
            update_product()
        elif ans == '9':
            print("You have selected make a purchase")
            purchase_item()
        elif ans == '0':
            print("Thank you for shopping with us!!!.")
            break
        else:
            print("Please enter a valid selection")
            continue

if __name__ == "__main__":
    menu()
