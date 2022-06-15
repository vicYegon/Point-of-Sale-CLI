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
    while True:
        print('''
                    Select what to do with the customer entry: 
                            1. Add customer
                            2. Update customer            
                            3. Delete customer
                            4. List all customer entry
                            5. Search for specific customer details
                            0. To main menu
        ''')
        
        selection = input("\tEnter your selection: ")
        try:
            int(selection)
        except ValueError:
            print('Invalid input!! Please enter a number' )
        
        if selection == 1:
            addCustomerinfo()
        elif selection == 2:
            updateCustomerinfo()
        elif selection == 3:
            deleteCustomerinfo()
        elif selection == 4:
            listAllCustomers()
        elif selection == 5:
            search_customer_details()
        elif selection == 0:
            from main import operations_menu
            operations_menu()
        else:
            print('''\tInvalid Option, 
                       Please try again or press zero to quit to main menu!''')
        
# prints customer list in a new line at the end of the customer.txt file
def addCustomerinfo():
    with open('customer.txt', 'r') as f:
        list_items = f.readlines()
        print(list_items)
        customer_id = input("\t Enter customer id number: ")
        for line in list_items:
            if str(customer_id) in line.split('--'):
                print('\t Customer id already taken')
                quit()

        customer_name = input("\t Enter customer name: ").upper()
        customer_address = input("\n\t Enter customer town of residence: ").upper()
    
    c_info = Customer(customer_id, customer_name, customer_address)

    with open('customer.txt', 'a') as f:
        f_contents = f.write(c_info.__str__())
        print(f_contents)
    
    customer_menu()
      
# function to update customer entry and replace with new details
def updateCustomerinfo():
    with open('customer.txt', 'r') as f:
        fileInfo = f.readlines()
        cus_id = input("\t Enter id to update: ")

        for element in fileInfo:
            if cus_id in element:
                line_index = fileInfo.index(element)
                v = fileInfo[line_index]
                l = v.split('--')
                customer_name = l[1]
                customer_address =l[2]
                break

        print('''
                \t1. Change customer name
                \t2. Change customer address
        ''')
        
        pick = input('\n\t Select what to change: ')
        try:
            int(pick)
        except ValueError:
            print('Invalid input!! Please enter a number' )
        if pick == 1:    
            new_name = input('\n\tEnter new name: ').upper()
            l[1] = new_name
            new_details = f'{cus_id}--{new_name}--{customer_address}'
        elif pick == 2:
            new_address = input('\n\tEnter new town: ').upper()
            l[2] = new_address
            new_details = f'{cus_id}--{customer_name}--{new_address}'    
        else:
            print('Invalid option')

        fileInfo[line_index] = new_details
                                 
    with open('customer.txt','w') as fw:
        for line in fileInfo:
            fw.write(line)
    print('''
            ------Customer Updated Successfuly------
    ''')
    
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

def search_customer_details():
    with open('customer.txt', 'r') as f:
        customer_id = input('\tEnter customer ID to search: ')
        for line in f:
            line_list = line.split()
            if customer_id == line_list[0]:
                print(line)

def listAllCustomers():
    with open('customer.txt', 'r') as f:
        cus_list = f.read()
        print(cus_list)
