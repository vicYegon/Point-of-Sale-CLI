

class Customer:
    def __init__(self, customer_id, customer_name, customer_town):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_town = customer_town
        
    def __str__(self):
        self.customerdetails = f"{self.customer_id}--{self.customer_name}--{self.customer_town}\n"
        return self.customerdetails
    
#customer operations menu     
def customer_menu():

    print("Select what to do with the customer entry: ")
    print("1. Add customer")
    print("2. Update customer")
    print("3. Delete customer")
    print("4. List all customer entry")
    
    selection = int(input("Enter your selection: "))
    
    while selection:
        if selection == 1:
            addCustomerinfo()
        elif selection == 2:
            updateCustomerinfo()
        elif selection == 3:
            deleteCustomerinfo()
        else:
            quit()
        break


#prints customer list in a new line at the end of the customer.txt file
def addCustomerinfo():
    customer_name = input('Enter customer full name: ').upper()
    customer_id = input('Enter customer ID number: ')
    customer_town = input('Enter customer town of residence: ').upper()

    c_info = Customer(customer_id, customer_name, customer_town)
    
    customerdetails = str(c_info)

    with open('customer.txt', 'a') as f:
        f_contents = f.write(customerdetails)
        print(f_contents)
    
        
#function to update customer entry and replace with new details
def updateCustomerinfo():
    with open('customer.txt', 'r+') as f:
        customer_id = input("Enter id to update: ")

        for line in f.readlines():
            word_in_line = line.split('--')
            if customer_id in word_in_line[0]:
                print("id found")
                customer_details = Customer(int, str, str)
                new_name = input("Enter new name: ").upper()
                new_address = input("Enter new address: ")

                c_newInfo = str(Customer(customer_id, new_name, new_address))
                word_in_line.replace(customer_details, c_newInfo)
                f_contents = f.write(c_newInfo)
                print(f_contents)
            
            else:
                print("Id not found")
                quit()
        


#method to remove specified customer entry
def deleteCustomerinfo():
    customer_id = input('Enter customer id to delete details: ')
    with open("customer.txt", "r+") as f:
        line = f.readlines()
        for line in f:
            customer_deatails_words = line.split('--')
            if customer_id not in customer_deatails_words:
                f.write(line)


#method to read all customer entry in customer file
def listAllCustomers():
    with open('customer.txt', 'r') as f:
        cus_list = f.read()
        print(cus_list)
    
#cus1 = Customer(int, str, str)

customer_menu()





    

    

