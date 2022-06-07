



class Customer:
    def __init__(self, customer_id, customer_name, customer_town):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_town = customer_town
        
    def __str__(self):
        self.customerdetails = f"{self.customer_id}--{self.customer_name}--{self.customer_town}\n"
        return self.customerdetails
    
# customer operations menu    
def customer_menu():

    print('''
                Select what to do with the customer entry: 
                        1. Add customer
                        2. Update customer            
                        3. Delete customer
                        4. List all customer entry
    ''')
    
    selection = int(input("Enter your selection: "))
    
    while selection:
        if selection == 1:
            addCustomerinfo()
        elif selection == 2:
            updateCustomerinfo()
        elif selection == 3:
            deleteCustomerinfo()
        elif selection == 4:
            listAllCustomers()
        else:
            print('Invalid Option')
            quit()
        break


# prints customer list in a new line at the end of the customer.txt file
def addCustomerinfo():
    with open('customer.txt', 'r') as cus_list:
        list_items = cus_list.readlines()
        customer_id = input("Enter customer id number: ")
        for line in list_items:
            if str(customer_id) in line.split('--'):
                print('Customer id already taken')
                quit()

        customer_name = input("Enter customer name: ").upper()
        customer_address = input("Enter customer town of residence: ").upper()
    
    c_info = Customer(customer_id, customer_name, customer_address)

    with open('customer.txt', 'a') as f:
        f_contents = f.write(c_info.__str__())
        print(f_contents)
    
    customer_menu()

        
# function to update customer entry and replace with new details
def updateCustomerinfo():
    with open('customer.txt', 'r') as f:
        fileInfo = f.readlines()
        cus_id = input("Enter id to update: ")

        new_name = input('Enter new/old name: ').upper()
        new_address = input('Enter new/town: ').upper()
        new_details = f'{cus_id}--{new_name}--{new_address}\n'

        for element in fileInfo:
            if cus_id in element:
                line_index = fileInfo.index(element)

    fileInfo[line_index] = new_details
                                 
    with open('customer.txt','w') as fw:
        for line in fileInfo:
            print(fw.write(line))
    
    customer_menu()

#method to remove specified customer entry
def deleteCustomerinfo():
    with open('customer.txt', 'r') as fl:
        customer_id = input("Enter customer id to delete: ")
        f = fl.readlines()
        j = 0
        for line in f:
            if customer_id in line:
                f.pop(j)
            j += 1
    with open('customer.txt', 'w') as fs:
        for line in f:
            print(fs.write(line))

    print('''
                    -----Customer deleted successfully-----
        ''')

def listAllCustomers():
    with open('customer.txt', 'r') as f:
        cus_list = f.read()
        print(cus_list)
    
customer_menu()
