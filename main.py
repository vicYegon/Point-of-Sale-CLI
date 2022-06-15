from purchases import*
from customer import customer_menu
from products import product_menu
from query import query_menu

#menu to call varied menus functions in different files
def operations_menu():
    while True:
        print('''
        \tWelcome to POS system \n\t        Select what you wish to do: \n
            \t 1. Customer operations
            \t 2. Product operations
            \t 3. Order operations
            \t 4. Queries section
            \t 0. Quit
                ''')
        
        pick = int(input("\n\t Enter your selection: "))
    
        if pick == 1:
            customer_menu()
        if pick ==2:
            product_menu()
        if pick == 3:
            order_menu()
        if pick == 4:
            query_menu()
        if pick == 0:
            quit()
        else:
            print('\tWrong input. Try again or press zero to quit')

if __name__=='__main__':
    operations_menu()
