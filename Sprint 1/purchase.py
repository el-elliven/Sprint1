import csv
import os


class Purchase:
    def __init__(self, customer_id=None, product_id=None, amount_bought=None):
        self.customer_id = customer_id
        self.product_id = product_id
        self.amount_bought = amount_bought

    def __str__(self):
        sell = f'{self.customer_id}, {self.product_id}, {self.amount_bought}'
        return sell


purchases_made = []
space_small = """
              """
space_big = """

            """
with open('products.csv', 'r+') as csv_file:
    file_product = csv.reader(csv_file)
    data_product = list(file_product)
with open('customers.csv', 'r+') as csv_file:
    file_customer = csv.reader(csv_file)
    data_customer = list(file_customer)
with open("products.csv", "a+", newline="") as fp:
    writer_product = csv.writer(fp, dialect='excel')


# still trying to fix issues with customer not being present.
def check_customer():
    customer_id_from_user = str(input("Enter customer id to purchase: "))
    with open('customers.csv', 'r') as csv_file:
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


def purchase_item():
    items = []
    all_total = []
    all_quantity = []
    customer_exists = False
    product_exists = False
    total_purchase = 0
    continue_purchase = True

    with open('customers.csv', 'r+') as csv_file:
        file_customer = csv.reader(csv_file)
        data_customer = list(file_customer)

    with open('products.csv', 'r+') as csv_file:
        file_product = csv.reader(csv_file)
        data_product = list(file_product)

    customer_id_from_user = input("Enter customer id to purchase:")

    for line in data_customer:
        if customer_id_from_user == line[0]:
            print(f"Customer name is: {line[1]}")
            customer_id = line[0]
            customer_name = line[1]
            continue_purchase = True

    while continue_purchase:
        product_id = input("Enter product id to purchase: ")
        for i in data_product:
            if product_id == i[0]:
                product_exists = True
                print(i)
                product_id = i[0]
                product_name = i[1]
                product_quantity = i[2]
                product_price = i[3]

        while True:
            purchase_quantity = int(input("Enter the quantity you would like to purchase for the product: "))
            total = float(product_price) * int(purchase_quantity)
            all_total.append(total)
            all_quantity.append(purchase_quantity)
            items.append(product_name)
            if purchase_quantity > int(product_quantity):
                print(f'\nProducts ordered is more than stock\nProducts available: {product_quantity}\n')
            else:
                option = input("Enter Y to add item to purchase N to cash out: ").upper()
                if option == "Y":
                    continue_purchase
                    break
                elif option == "N":
                    continue_purchase = False
                    while True:
                        amount_tendered = int(input("Enter amount given: \n"))
                        if amount_tendered < sum(all_total):
                            print("Please enter an amount greater or equal to the total.")
                        else:
                            receipt = f'''
                            Customer Name: {customer_name}
                            Products: {items}
                            Total: {all_total}
                            '''
                            print(receipt)
                            print(f'Your total is: {sum(all_total)}')
                            change = amount_tendered - sum(all_total)
                            print(f'Change: {change}')
                        break

            break
    with open("purchase.csv", "a+", newline="") as fp:
        orderdetails = [customer_id, product_id, sum(all_total)]
        print(orderdetails)
        wr = csv.writer(fp, dialect='excel')
        wr.writerow(orderdetails)