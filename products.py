
class Products:
    def __init__(self, product_name, product_id, product_price, product_quantity):
        self.product_name = product_name
        self.product_id = product_id
        self.product_price = product_price
        self.product_quantity = product_quantity
    
    def __str__(self):
        self.productdetails =  str(f'{self.product_id} -- {self.product_name} --{self.product_quantity}pieces--Ksh.{self.product_price}each, end=')
        return self.productdetails

#menu to allow choosing of what product operation to perform
def product_menu():
    print("Select what to do with the product entry")
    print("1. Add product")
    print("2. Update product")
    print("3. Delete product")
    print('4. List all products')
    selection = int(input("Enter your selection: "))

    while selection:
        if selection == 1:
            addProduct()
        elif selection == 2:
            updateProduct()
        elif selection == 3:
            deleteProduct()
        elif selection == 4:
            listAllProducts()
        else:
            print('Wrong input, enter value again')
        break

#adding a product entry to product text file
def addProduct():
    product_name = input('Enter product name: ').upper()
    product_id = input('Enter product_id number: ')
    product_price = input('Enter product price: ')

    p_info = Products(product_name, product_id, product_price)
    
    product_details = str(p_info)

    with open('products.txt', 'a', '\n') as f:
        f_contents = f.write(product_details)
        print(f_contents)
    

#updating a product entry        
def updateProduct():
   with open('products.txt', 'r') as f:
        fileInfo = f.readlines()
        product_id = input("Enter id to update: ")

        new_product_name = input('Enter new or previous name: ').upper()
        new_product_price = input('Enter new product price: ')
        product_quantity = input('Enter the new number of products after being added: ')
        new_details = f'{product_id}--{new_product_name}--{new_product_price}--{product_quantity}\n'

        for element in fileInfo:
            if product_id in element:
                line_index = fileInfo.index(element)

    fileInfo[line_index] = new_details

    with open('products.txt','w') as f:
        f.writelines(new_details)

#function to delete a product entry
def deleteProduct():
    with open('products.txt', 'r') as fr:
    product_id = input("Enter product id to delete: ")
    f = fr.readlines()
    for line in f:
        if product_id not in line:
            with open('products.txt', 'w') as fw:
                fw.write(line)
print('Product details deleted')

#appending product entry to a product text file
def listAllProducts(): 
    with open('products.txt', 'r') as f:
        product_list = f.read()
        print(product_list)
