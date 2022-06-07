
class Products:
    def __init__(self, product_name, product_id, product_type, product_price, product_quantity):
        self.product_name = product_name
        self.product_id = product_id
        self.product_price = product_price
        self.product_quantity = product_quantity
        self.product_type = product_type      
    def __str__(self):
        self.product_details =  f'{self.product_id} -- {self.product_name} -- {self.product_quantity} -- {self.product_price} -- {self.product_type} \n'
        return self.product_details

#menu to allow choosing of what product operation to perform
def product_menu():
    print('''   Select what to do with the product entry
                1. Add product information in a product list
                2. Update product details
                3. Delete product details
                4. List all products
    ''')
    selection = int(input('''\tEnter your selection: '''))

    while selection:
        if selection == 1:
            addProductinfo()
        elif selection == 2:
            updateProduct()
        elif selection == 3:
            deleteProductinfo()
        elif selection == 4:
            listAllProducts()
        else:
            print('\t Wrong input, enter value again')
        break

#adding a product entry to product text file
def addProductinfo():
    with open('products.txt', 'r') as pl:
        prod_list = pl.readlines()
        product_id = input('Enter product_id number: ')
        for line in prod_list:
            if product_id in line.split('--'):
                print('Product ID already used')
                product_menu()
        product_name = input('Enter product name: ').capitalize()
        product_type = input('Enter category of the item:').capitalize()
        product_price = input('Enter product price: ')
        product_quantity = input('Enter the number of items for the specific product: ')

    p_info = Products(product_name, product_id, product_type, product_price, product_quantity,)

    with open('products.txt', 'a') as f:
        f_contents = f.write(p_info.__str__())
        print(f_contents)
    
    product_menu()
#updating a product entry        
def updateProduct():
    with open('products.txt', 'r') as f:
        fileInfo = f.readlines()
        product_id = input("Enter id to update: ")
        for line in fileInfo:
            if product_id in line:
                line_index = fileInfo.index(line)

        new_product_name = input('Enter new or previous name: ').capitalize()
        new_product_price = input('Enter new product price: ')
        new_product_quantity = input('Enter the new number of products after being added: ')
        new_product_type = input('Enter new product category: ').capitalize()
        new_details = f'{product_id} -- {new_product_name} -- {new_product_price} -- {new_product_quantity} -- {new_product_type}\n'
    
    fileInfo[line_index] = new_details 
    
    with open('products.txt','w') as fw:
        for line in fileInfo:
            fw.write(line)


#function to delete a product entry
def deleteProductinfo():
    with open('products.txt', 'r') as fl:
        product_id = input("Enter customer id to delete: ")
        f = fl.readlines()
        p = 0
        for line in f:
            if product_id in line:
                f.pop(p)
            p += 1
    with open('customer.txt', 'w') as fs:
        for line in f:
            print(fs.write(line))

    print('Product deleted successfully')
#appending product entry to a product text file
def listAllProducts(): 
    with open('products.txt', 'r') as f:
        product_list = f.read()
        print(product_list)
        
