from purchases import*
from customer import*
from products import*

#menu to call varied menus functions in different files
def operations_menu():
    while True:
        print('''
        \tWelcome to POS, select what you wish to do: \n
            \t 1. Customer operations
            \t 2. Product operations
            \t 3. Order operations
            \t 0. Quit
                ''')
        
        pick = int(input("\n\t Enter your selection: "))
    
        if pick == 1:
            customer_menu()
        if pick ==2:
            product_menu()
        if pick == 3:
            order_menu()
        if pick == 0:
            quit()
        else:
            print('\tWrong input. Try again or press zero to quit')

if __name__=='__main__':
    operations_menu()
