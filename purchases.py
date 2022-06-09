import datetime
from customer import Customer, updateCustomerinfo
from products import Products, updateProduct
import random

order_id = random.randint(100 - 1000)
pieces_purchased = 0
TOTAL = 0
PRODUCTS = []
AMOUNT_SPENT = []

class Purchases:
    def __init__(self, order_id, product_quantity, product_price, product_name, customer_name):
        self.customer_name = customer_name
        self.product_name = product_name
        self.product_quantity = product_quantity
        self.product_price = product_price
        self.order_id = order_id
        self.date_of_purchase = datetime.date.today()
        self.time_of_purchase = datetime.time.now()
        
    def total_for_specific_product(self):
        self.total = self.pieces_purchased * self.product_price
        return self.total

    def __str__(self):
        self.order_details = f'''
                        order ID: {self.order_id}
                        customer name: {self.customer_name}
                        product name: {self.product_name}
                        amount: {self.total_apent}
        '''
        return self.order_details

def order_menu():
   print('''\n Select the order operation you would want to go through:
            1. Select for purchase operation
            2. Print receipt 
            3. Select for products inventory
            ''') 
    
    selection = int(input('Enter your option: '))
    
    while selection:
        if selection == 1:
            purchase_operation()
        elif selection == 2:
            print_receipt()
        elif selection == 3:
            order_details()
        else:
            print('\t Wrong input')
            order_menu()     
        break
pd = Purchases(int, int, float, str, str)
def purchase_operation():
    with open('customer.txt', 'r') as fc:
        cus_list = fc.readlines()
        customer_id = input('Enter customer id: ')
        
        
        for line in cus_list:
            if customer_id in line:
                cus_details = line.split('--')
                customer_id = cus_details[0]
                purch_det.customer_name = cus_details[1]
                print(f'''
                            Welcome {pd.customer_name}.\n
                ''')
    
    
    with open('products.txt', 'r') as fp:
        prod_list = fp.readlines()
        product_id = input('Enter product ID:')
        for product in prod_list:
            if product_id in product:
                prod_det = product.split('--')
                product_id = pd[0]
                pd.product_name = pd[1]
                pd.product_quantity = pd[2]
                pd.product_price = pd[3]
                print(f'''
                            You have selected {pd.product_name}\n
                    ''')
                PRODUCTS.append(pd.product_name)
        print('''
                ----Select an option----
                1. Purchase another product
                2. Sell product
        ''')
        pick = input('\t Enter your selection: ')
        while pick:
            if pick == 1:
                purchase_operation()
            elif pick ==2:
                sell_an_item
            else pick == 0:
                print('Enter zero to quit')
                quit()
            break
        
def sell_an_item():
    pd.product_price = pd[3]

    pieces_purchased = input('How many pieces do you require?: ')
    if int(pieces_purchased) > pd.product_quantity:
        print(f'''
                Purchases is more than the stock. 
                Products available : {pd.product_quantity}
        ''')
        input('Enter new amount or buy something else')
        purchase_operation()

    else:
        pd.total_for_specific_product()
        TOTAL = pd.total_for_specific_product()
        AMOUNT_SPENT.append(TOTAL)

    payment()
                

def payment():
    cash = float(input('Enter the amount for payment: '))
    if cash < TOTAL:
        print('Amount not enough. Please add:'+ (TOTAL-cash))
        payment()
    elif cash >= TOTAL: 
        if cash > TOTAL:
            cash_change = int(cash) - int(TOTAL)
            print(f'''
                    Your change is = {cash_change}

                    ''')
        else:
            print(f'''
                    transaction: {order_id}
                    total spent: {TOTAL}
                    THANK YOU & WELCOME AGAIN: {pd.customer_name}

            ''')
    print_receipt()
        
def product_inventory():
    new_product_quantity = pd.product_quantity - pd.pieces_purchased
    product_id = input('Enter ID for the purchased product')
    with open('products.txt', 'w') as pl:
        for line in pl:
            if product_id in line:
                product_line = line.split('--')
                if product_id == product_line[0]:
                    product_line[2] = new_product_quantity
            pl.write(line)

def print_receipt():
    print(f'''

          -----hey, this is your receipt-----
            
            order ID           : {order_id}
            customer_name      : {pd.customer_name}
            products bought    : {PRODUCTS}
            total_amount_spent : {sum(AMOUNT_SPENT)}
            date               : {pd.date_of_purchase}
            time               : {pd.time_of_purchase}

        --------THANK YOU, WELCOME AGAIN--------
    ''')
def order_details():
    with open('order.txt', 'a', end='') as f:
        f.write(pd.order_details)
