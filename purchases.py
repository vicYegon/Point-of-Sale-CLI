from datetime import date
from customer import Customer, updateCustomerinfo
from products import Products, updateProduct
import random

order_id = random.randint(100, 1000)
pieces_purchased = 0
TOTAL = 0
PRODUCTS = []
AMOUNT_SPENT = []

today = date.today()
t1 = today.strftime('%B %d %Y')

class Purchases:
    def __init__(self, order_id, product_quantity, product_price, product_name, customer_name):
        self.customer_name = customer_name
        self.product_name = product_name
        self.product_quantity = product_quantity
        self.product_price = product_price
        self.order_id = order_id
        
    def __str__(self):#function to print purchase details
        self.order_details = f'{order_id}--{self.customer_name}--{PRODUCTS}--{TOTAL}'
        return self.order_details


def order_menu():#function to direct what to do in the purchase file
    while True:
        print('''\n Select the order operation you would want to go through:
                \t1. Purchase operation \n
                \t2. Search Purchase transaction \n
                \t3. Quit
                ''') 
        
        selection = int(input('\t Enter your option: '))  

        try:
            int(selection)
        except ValueError:
            print('Invalid input!! Please enter a number' )   
    
        if selection == 1:
            purchase_operation()
        elif selection == 2:
            search_transaction()
        elif selection == 3:
            from main import operations_menu
            operations_menu()
        else:
            print('\t Wrong input, try again')


# make purchase function
def purchase_operation():
    continue_purchase = True #initializing variable to be used later in code
    with open('customer.txt', 'r') as fc:
        cus_list = fc.readlines()
        customer_id = input('\t Enter customer id: ') #picks first customer by default
                
        for line in cus_list:
            if customer_id in line:
                cus_details = line.split('--')
                customer_id = cus_details[0]
                customer_name = cus_details[1]
                print(f'''
                            Welcome {customer_name}.\n
                ''')
                break
        else:
            print('Customer not available')

    while continue_purchase:
        with open('products.txt', 'r') as fp:#open products file to perform various operations
            prod_list = fp.readlines()
            product_id = input('\t Enter product ID:')
            for product_line in prod_list:
                if product_id in product_line:
                    line_index = prod_list.index(product_line)
                    prod_det = product_line.split('--')
                    product_id = prod_det[0]
                    product_name = prod_det[1]
                    product_quantity = prod_det[2]
                    product_price = prod_det[3]
                    product_type = prod_det[4]
                    print(f'''
                                You have selected {product_name}\n
                                It costs Ksh. {product_price}\n
                                There are {product_quantity} pieces in stock
                        ''')
                    PRODUCTS.append(product_name)
                    break
            else: 
                print("\n\tProduct not available")

        #Condition to enable purchase of another product
        pick = input('\n\tEnter Yes to purchase another item or No continue').capitalize()
        if pick == 'Yes':
            continue_purchase = True
        else:
            #select amount of pieces to purchase
            pieces_purchased = int(input('\n\tHow many pieces do you require?: '))
            if int(pieces_purchased) > int(product_quantity):
                print(f'''
                        Purchases is more than the stock. 
                        Products available : {product_quantity}
                ''')
                input('\n\tEnter new amount or buy something else')
                purchase_operation()

            else:
                TOTAL = pieces_purchased * int(product_price)
                AMOUNT_SPENT.append(TOTAL)
                print(f'\n\tYou have spent Ksh.{TOTAL}')

            # making payments
            cash = float(input('\n\tEnter the amount for payment: '))
            if cash < TOTAL:
                print('\n\t Amount not enough. Please add:'+ (TOTAL-cash))
            else: 
                if cash >= TOTAL:
                    cash_change = int(cash) - int(TOTAL)
                    print(f'''
                            Transaction: {order_id}
                            Your Name: {customer_name}
                            Your change: {cash_change}
                            Total spent: {sum(AMOUNT_SPENT)}
                    ''')

    #object to instatiate the class
    pd = Purchases(order_id, product_quantity, product_price, product_name, customer_name)

    #stock update inventory in product.txt
    pd.product_quantity = prod_det[2]
    new_product_quantity = int(product_quantity) - int(pieces_purchased)
    new_product_details = f'{product_id}--{product_name}--{new_product_quantity}--{product_price}--{product_type}'

    prod_list[line_index] = new_product_details
    with open('products.txt', 'a+') as fq:
        for line in fq.read():
            p_contents = fq.write(line)
            print(p_contents)

    # print order details to order.txt
    with open('order.txt', 'a') as f:
        f.write(pd.__str__())

    # printing receipt
    total_spent = sum(AMOUNT_SPENT)
    print(f'''
        -----This is the receipt for the transaction-----
                
            Order ID           : {order_id}
            Customer_name      : {customer_name}
            Products bought    : {PRODUCTS}
            Total_amount_spent : {total_spent}
            Date               : {t1}
        --------THANK YOU, WELCOME AGAIN--------
    ''')
    from main import operations_menu
    operations_menu()

#search for a transaction using ID
def search_transaction():
    purchase_ID = input('\tEnter the purchase id to search transaction: ')
    with open('order.txt', 'r') as f:
        f_list = f.readlines()
        for line in f_list:
            if purchase_ID in line:
                print(line)
