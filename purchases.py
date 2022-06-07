import datetime
from products import *
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
    print('''Select the order operation you would want to go through:')
            1. Select for purchase operation
            2. Select for products inventory
            3. Search for a particular product
            ''') 
    
    selection = int(input('Enter your option: '))
    
    while selection:
        if selection == 1:
            purchase_operation()
        elif selection == 2:
            order_details()
        elif selection == 3:
            print_receipt()
        else:
            print('Wrong input')
            order_menu()     
        break
purch_det = Purchases(int, int, float, str, str)
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
                            Welcome {purch_det.customer_name}.\n
                ''')
    
    
    with open('products.txt', 'r') as fp:
        prod_list = fp.readlines()
        product_id = input('Enter product ID:')
        for product in prod_list:
            if product_id in product:
                prod_det = product.split('--')
                product_id = prod_det[0]
                purch_det.product_name = prod_det[1]
                purch_det.product_quantity = prod_det[2]
                purch_det.product_price = prod_det[3]
                print(f'''
                            You have selected {purch_det.product_name}\n
                    ''')
                PRODUCTS.append(purch_det.product_name)
        print('''
                ----Select an option----
                1. Purchase another product
                2. Sell product
                3. Make payment for the purchase
                0. Quit
        ''')
        pick = input('Enter your selection: ')
        while pick:
            if pick == 1:
                purchase_operation()
            elif pick ==2:
                print(purch_det.order_details)
                payment()
            elif pick == 3:
                sell_an_item()
            elif pick == 0:
                print('Enter zero to quit')
                quit()
            break
        

    def sell_an_item():
        purch_det.product_price = prod_det[3]
                    
        pieces_purchased = input('How many pieces do you require?: ')
        if int(pieces_purchased) > purch_det.product_quantity:
            print(f'''
                    Purchases is more than the stock. 
                    Products available : {purch_det.product_quantity}
            ''')
            input('Enter new amount or buy something else')
            purchase_operation()

        else:
            purch_det.total_for_specific_product()
            TOTAL = purch_det.total_for_specific_product()
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
                    THANK YOU & WELCOME AGAIN: {purch_det.customer_name}

            ''')
    print_receipt()
        
def product_inventory():
    new_product_quantity = purch_det.product_quantity - purch_det.pieces_purchased
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
            customer_name      : {purch_det.customer_name}
            products bought    : {PRODUCTS}
            total_amount_spent : {sum(AMOUNT_SPENT)}
            date               : {purch_det.date_of_purchase}
            time               : {purch_det.time_of_purchase}

        --------THANK YOU, WELCOME AGAIN--------
    ''')
def order_details():
    with open('order.txt', 'a', end='') as f:
        f.write(order_details)
