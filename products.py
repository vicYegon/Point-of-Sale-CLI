

class Products:
    def __init__(self, product_id, product_name, product_type, product_price, product_quantity):
        self.product_name = product_name
        self.product_id = product_id
        self.product_price = product_price
        self.product_quantity = product_quantity
        self.product_type = product_type      
    def __str__(self):
        self.product_details =  f'{self.product_id}--{self.product_name}--{self.product_quantity}--{self.product_price}--{self.product_type} \n'
        return self.product_details

#menu to allow choosing of what product operation to perform
def product_menu():
    while True:
        print('''   Select what to do with the product entry
                    1. Add product information in a product list
                    2. Update product details
                    3. Delete product details
                    4. Search product
                    5. List all products
        ''')
        selection = int(input('\tEnter your selection: '))
        #input exception handling
        try:
            int(selection)
        except ValueError:
            print('Invalid input!! Please enter a number' )

        if selection == 1:
            addProductinfo()
            break
        elif selection == 2:
            updateProduct()
            break
        elif selection == 3:
            deleteProductinfo()
            break
        elif selection == 4:
            listAllProducts()
            break
        else:
            print('\t Wrong input, enter selection again')

#adding a product entry to product text file
def addProductinfo():
    with open('products.txt', 'r') as pl:
        prod_list = pl.readlines()
        product_id = input('\tEnter product_id number: ')
        for line in prod_list:
            if product_id in line.split():
                    print('\tProduct ID already used')
                    product_menu()
        product_name = input('\tEnter product name: \n').capitalize()
        product_type = input('\tEnter category of the item: \n').capitalize()
        product_price = input('\tEnter product price: \n')
        product_quantity = input('\tEnter the number of items for the specific product: \n')

    p_info = Products(product_id, product_name, product_type, product_price, product_quantity)

    with open('products.txt', 'a') as f:
        f_contents = f.write(p_info.__str__())
        print(f_contents)
    
    product_menu()
     
def updateProduct(): #updating a product entry   
    
    with open('products.txt', 'r') as f:    # open products text file
        fileInfo = f.readlines()
        product_id = input("\tEnter id to update: \n")
        for line in fileInfo:
            if product_id in line:
                line_index = fileInfo.index(line)
                f = line.split()
                product_name = f[1]
                product_price = f[2]
                product_quantity = f[3]
                product_type = f[4]
        
        while True: #loop choices if pick is wrong
            print('''
                What would you want to update?
                    1. Change product name
                    2. Change product price
                    3. Change product quantity
                    4. Change product category
            
            ''')
            pick = int(input('\n\tPick what you would wish to change: '))
            # input exception handling
            try:
                int(pick)
            except ValueError:
                print('\n\tInvalid input!! Please enter a number' )

            if pick == 1:
                new_product_name = input('\n\t Enter new name: ').capitalize()
                new_details = f'{product_id} -- {new_product_name} -- {product_price} -- {product_quantity} -- {product_type}'
                break
            elif pick == 2:
                new_product_price = input('\n\t Enter new product price: ')
                new_details = f'{product_id} -- {product_name} -- {new_product_price} -- {product_quantity} -- {product_type}'
                break
            elif pick == 3:
                new_product_quantity = input('\n\tEnter the new number of products after being added: ')
                new_details = f'{product_id} -- {product_name} -- {product_price} -- {new_product_quantity} -- {product_type}'
                break
            elif pick == 4:
                new_product_type = input('\n\tEnter new product category: ').capitalize()
                new_details = f'{product_id} -- {product_name} -- {product_price} -- {product_quantity} -- {new_product_type}'
                break
            else:
                print('\n\tPlease select again the correct answer')
                
    fileInfo[line_index] = new_details 
    
    with open('products.txt','w') as fw:
        for line in fileInfo:
            fw.write(line)

#function to delete a product entry
def deleteProductinfo():
    with open('products.txt', 'r') as fl:
        product_id = input("\n\tEnter customer id to delete: ")
        f = fl.readlines()
        p = 0
        for line in f:
            if product_id in line:
                f.pop(p)
            p += 1
    with open('customer.txt', 'w') as fs:
        for line in f:
            print(fs.write(line))

    print('\n\t----Product deleted successfully----')

#search product either by ID/name
def searchProduct():
    with open('products.txt', 'r+') as f:
        for line in f.readlines():
            v = line.split()
            product_id = v[0]
            product_name = v[1]
        while True:    
            print('''
                    \t1. Search by ID
                    \t2. Search by Name
            ''')
            pick = int(input('\n\tEnter option to search by: '))
            if pick == 1:
                product_id = input('\n\tEnter product id: ')
                if product_id == v[0]:
                    print(line)
            elif pick == 2:
                product_name = input('\n\tEnter product name: ')
                if product_name == v[1]:
                    print(line)
            else:
                print('\n\tInvalid input. Try again!')
            
#printing product entry to a 
def listAllProducts(): 
    with open('products.txt', 'r') as f:
        product_list = f.read()
        print(product_list)
        
