"""

My first approach is to build an items inventory. 
the items inventory would have the following:
The items, the prices, the amount that is available. 

"""


items_list = ['milk', 'bread', 'Tea leaves']

stock = {
    "milk": 100,
    "bread": 100,
    "Tea leaves": 200
}

prices = {
    "milk": 60,
    "bread": 50,
    "Tea leaves": 25
}


def compute_bill(food):
    total = 0

    for number in food:
        if (stock[number]>0):
            total += prices[number]
            stock[number] -= 1
    
    return print(total, stock)
    

# compute_bill(items_list)


def items():
    store = {}
    prices = {}
    print("Enter the items that you want in your store: ")
    for i in range(1):
        item_name = input("Enter item name: ")
        item_amount = input("Enter item amount: ")
        item_price = input("Enter item price: ")
        store[item_name] = item_amount, item_amount
        return store
        # prices[item_name.title()] = item_price

    print(store)
    user_items_from_input = [x for x in items_list]
    print(f'The items you have entered are: {user_items_from_input}')
    print('Items Amount')
    for item_name, item_amount in store.items():
        print('{} {}'.format(item_name, item_amount))
    return store


