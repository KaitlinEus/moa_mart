# Moa Mart program

import random
from random import randint

# List of random names
names = ["Yeonjun", "Taehyun", "Huening Kai", "Beomgyu", "Soobin", "Steve", "Daniel ", "Ben", "Terry", "Hyuka"]



#welcome message with random name
def welcome():

    '''
    Purpose: To run all functions
    Parameters: None
    Returns: None
    '''

num = randint(0,9)
name = (names[num])

# Logo
print(""" 

     __    __     ______     ______          __    __     ______     ______     ______  
    /\ "-./  \   /\  __ \   /\  __ \        /\ "-./  \   /\  __ \   /\  == \   /\__  _\ 
    \ \ \-./\ \  \ \ \/\ \  \ \  __ \       \ \ \-./\ \  \ \  __ \  \ \  __<   \/_/\ \/ 
     \ \_\ \ \_\  \ \_____\  \ \_\ \_\       \ \_\ \ \_\  \ \_\ \_\  \ \_\ \_\    \ \_\ 
      \/_/  \/_/   \/_____/   \/_/\/_/        \/_/  \/_/   \/_/\/_/   \/_/ /_/     \/_/
      
      
      """)
# welcome message
print("+×+ One Dream! Hello, we are TOMORROW X TOGETHER! +×+")
print("+×+ Welcome to Moa Mart +×+")
print("+×+ My name is",name, "+×+")
print("+×+ I will be here to help you order your TXT album! +×+")


# menu for pickup or delivery

def order_type():

    print("+×+ Is your order for pickup or delivery? +×+")

    print("+×+ For deliver please enter 1 +×+")
    print("+×+ For pickup please enter 2 +×+")

    while True: 
        try:
            delivery = int(input("+×+ Please enter a number +×+ "))
            if delivery >= 1 and delivery <= 2:

                if delivery == 1:
                    print("+×+ Delivery +×+")
                    break

                elif delivery == 2:
                    print("+×+ Pickup +×+")
                    break
            else: 
                print("+×+ Number must be 1 or 2 +×+ ")

        except ValueError:
            print("+×+ That is not a valid number +×+")
            print("+×+ Please enter 1 or 2 +×+ ")














# Main function
def main():
     
    '''
    Purpose: To generate a random name from the list and print out a welcome message
    Parameters: None
    Returns: None
    '''
     
    welcome()
    order_type()


main()


