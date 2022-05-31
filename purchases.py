from ast import Pass
import datetime
from products import Products

WALLET = 0

class Purchases:
    def __init__(self, order_id, Products,total_amount_spent):
        self.Products = Products
        self.order_id = order_id
        self.date_of_purchase = datetime.date.today()
        self.time_of_purchase = datetime.time.hour
        self.total_amount_spent = total_amount_spent
    
    def __add__(self):
        pass

def order_menu():
    print('Select the order operation you would want to go through:')
    print('1. Select for products inventory')
    print('2. Select for purchase operation')
    print('3. Search for a particular product') 
    selection = int(input('Enter >>>'))
    while selection:
        if selection == 1:
            product_inventory()
        elif selection == 2:
            purchaseoperation()
        elif selection == 3:
            searchProduct()
        elif selection == 4:
            print_receipt()
        else:
            print('Wrong input')
        break

def product_inventory(product_quantity):
    product_quantity = ''
    purchased_products = []
    print('Do you wish to view all the products available?')
    with open('product.txt', 'r') as f:
        p_list = f.read()
        print(p_list)
    
    with open('products.txt', 'w') as pl:
        WALLET = product_quantity - purchased_products
        new_prodInfo = Products()

def purchaseoperation():
    totalAmountSpent = 0
    product_ordered = input('Enter the product you wish to buy: ')
    product_quantity = input('Enter number of pieces you require')
    with open('products.txt', 'r') as f:
        print(f.readlines())

        for product in f:
            if product_ordered <= product_quantity >= 1:
                print('Purchase can be possible: ')
            else:
                print('The order cannot be met now, do you wish to change your order: ')
                print('If yes enter 1: \n If no press any number: ')
                if str(1):
                    purchaseoperation()
                else:
                    quit()
    prod2 = Products(product_name='', product_id="", product_price='')


    totalAmountSpent = prod2.product_price * prod2.product_quantity

def searchProduct():
    product_id =  input('Enter product id: ')
    product_name = input('Enter product name: ')
    with open('products.txt', 'r+','\n') as f:
        product_list = f.readlines()  
        for line in product_list:
            if (product_id or product_name) in line:
                print('Product available: ')
                print(f.write(line))
            else:
                print('Product not available')

def print_receipt():
    pass