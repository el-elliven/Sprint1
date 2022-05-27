import os
import csv

# class Purchase


purchases_made = []

space_small = """
              """

space_big = """
            
            """

with open('products.csv','r+') as csv_file:
    file_product = csv.reader(csv_file)
    data_product = list(file_product)

with open('customers.csv','r+') as csv_file:
    file_customer = csv.reader(csv_file)
    data_customer = list(file_customer)

with open("products.csv", "a+", newline="") as fp:
    writer_product = csv.writer(fp, dialect='excel')


# still trying to fix issues with customer not being present. 
def check_customer():
    customer_id_from_user = str(input("Enter customer id to purchase: "))
    with open('customers.csv','r') as csv_file:
        file_customer = csv.reader(csv_file)
        data_customer = list(file_customer)
        idx_data_customer = [item[0] for item in data_customer]
        print(idx_data_customer)
        for i in range(len(data_customer)):
            if customer_id_from_user in idx_data_customer:
                print()
                return print("customer found.")
            else:
                print("Customer not found.enter a valid customer Id")
                return check_customer()

# check_customer()


def purchase_item():
    customer_exists = False
    product_exists= False
    # total_purchase = 0

    customer_id_from_user = str(input("Enter customer id to purchase: "))

    for customer in range(len(data_customer)):
        if customer_id_from_user in data_customer[customer][0]:
            customer_exists = True
            print("Customer name is: ", data_customer[customer][1])
            

    print(space_small)
    product_id_from_user = input("Enter product id to purchase: ")
    # check if id in product exists
    for product in range(len(data_product)):
        if product_id_from_user == data_product[product][0]:
            product_exists = True
            print(space_small)
            print(f"The product is:  {data_product[product][1]} \nThere are {data_product[product][2]} in the store.")

    if customer_exists and product_exists:
        print(space_small)
        purchase_item_quantity = int(input("Enter the quantity you would like to purchase for the product: "))
        space_small
        for i in range(len(data_product)):
            if product_id_from_user in data_product[i][0]:
                name = data_product[i][1]
                quantity = int(data_product[i][2])
                price = float(data_product[i][3])
                if purchase_item_quantity > quantity:
                    print(name + " can't be sold because the quantity in stock is lower than ordered "+str(quantity)+'\nPlace another quantity for the order.')
                    purchase_item()
                else:
                      cost = purchase_item_quantity * price

                      purchases_made.append([product_id_from_user, name, purchase_item_quantity, cost])
                      print(f'Your purchase: {purchases_made}')

                      another_purchase = input("""
                      1. Check out with sale.
                      2. Make another purchase.

                      Your selection:  """)

                      if another_purchase == "1":
                          checking_out()
                      elif another_purchase == "2":
                        purchase_item()



def update_stock():

    for purchase in purchases_made:
        product_ID = purchase[0]
        cost_amount = purchase[2]

        file = open('products.csv', 'r')
        temp = open('temp_file.csv', 'w')

        s = ' '

        while(s):
            s = file.readline()
            L = s.split(',')
            if len(s)>0:
                if (L[0]) == product_ID:
                    product_name = L[1]
                    product_quantity = int(L[2])
                    product_price = L[3]
                    new_prod_quantity = product_quantity - cost_amount
                    temp.write(str(product_ID)+','+product_name+','+str(new_prod_quantity)+','+str(product_price))
                else:
                    temp.write(s)
        temp.close()
        file.close()
        os.remove('products.csv')
        os.rename('temp_file.csv','products.csv')
        print("Inventory updated.")
        print("Stock remaining: "+str(new_prod_quantity))
        break



def checking_out():
    total_spent = 0
    # print(space)
    for purchase in range(len(purchases_made)):
        total_spent += purchases_made[purchase][3]
    print(space_big)
    print(f'You have spent {total_spent}')
    print(space_small)
    

    customer_pay = float(input("Amount of cash given:"))
    if customer_pay < total_spent:
            print(f"""You have entered insufficient funds.
                        Total amount due is {total_spent}""")
            
            customer_pay_2 = input("""
                                    1. enter another cash amount.
                                    2. Exit
                                    
                                    Select an option: """)
            
            if customer_pay_2 == "1":
                checking_out()
            else:
                print(space_big)
                print("Exiting")
        
    else:
            balance = customer_pay - total_spent
            # print(space)
            print("Your purchase receipt is as follows:")
            print(f"""
                Total Spent: {total_spent}
                Paid: {customer_pay}
                Balance: {balance}
                """)
            # print(space)
            update_stock()



            # updated stock




# purchase_item()