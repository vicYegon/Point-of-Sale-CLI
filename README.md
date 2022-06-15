# Point-of-Sale CLI system

  This is a point of sale system where a user can manage customer, product and purchases information which are stored 
  in varied text files, and this is through the command line interface. 

## How to use the system
1. To be able to use the system. you have to run the [main.py](https://github.com/vicYegon/Point-of-Sale/blob/main/main.py) file

## Features
  The system has four files:
  They include:-
  ##### - The main.py (Contains an `operations menu` that directs to all other files menus)  
  ##### - The customer.py /customer file
  ##### - The products.py /products file
  ##### - The purchases.py /purchases file

### 1. The customer file 
  This file has a customer class and `customer operations menu function` which directs to various functions in the file. 
  These functions help to, 
        - __Add new customer information__ 
        - __Delete customer information__
        - __Update customer information__ 
        
  This are done in the customer text file. 
  More so, the user can list all the customer information in the terminal through the `listallcustomers function`. 
  *However it is not advised to use in cases where the information is large*

### 2. The products file
  Just like the customer file, the products file has a class Products and also the `products-operation-menu function` 
  which directs to various fuctions that manipulate the products text file. These functions include the addproductinfo, 
  deleteproductinfo, updateproductinfo and also the listallproductdetails functions/methods.
  
### 3. The purchases files
  This file is used by the system be able to incorporate the use of all the files. This file contains a purchase class 
  and `purchase operations menu function` to direct to different functions in the file. They include, 
        - __The purchase operations__
        In the purchase operations function, the user can identify a customer, product to sell and also be able to make 
        a successful sell of a product(s). 
        - __Search transaction through transaction ID__ 
 
## Language used
  `PYTHON` language.
  
