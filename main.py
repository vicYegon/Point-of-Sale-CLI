
from purchases import*
from customer import*
from products import*

def operations_menu():
    print("Welcome, select what you wish to do: ")
    print("1. Customer operations")
    print("2. Product operations")
    print("3. Order operations")
    pick = int(input("Enter your selection: "))
    while pick:
        if pick == 1:
            customer_menu()
        if pick ==2:
            product_menu()
        if pick == 3:
            order_menu()
        else:
            print('Wrong input. Try again')
            print('If you wish to try again, press 1: ')
            if 1:
                operations_menu()
            else:
                quit()
        break

if __name__=='__main__':
    operations_menu()