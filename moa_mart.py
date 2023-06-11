# Moa Mart program

import random
from random import randint

# List of random names
names = ["Yeonjun", "Taehyun", "Huening Kai", "Beomgyu", "Soobin", "Steve", "Daniel ", "Ben", "Terry", "Hyuka"]

# customer detailes dictionary
customer_details = {}

# Validates inputs to check if they are blank
def not_blank(question):
    valid = False
    while not valid: 
        response = input(question)
        if response != "":
            return response
        else:
            print("+×+ Sorry this cannot be blank +×+")

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
                    print("+×+  Delivery  +×+")
                    delivery_info()
                    break

                elif delivery == 2:
                    print("+×+  Pickup  +×+")
                    pickup_info()
                    break
            else: 
                print("+×+ Number must be 1 or 2 +×+ ")

        except ValueError:
            print("+×+ That is not a valid number +×+")
            print("+×+ Please enter 1 or 2 +×+ ")



# Pick up information - name and phone
def pickup_info():

    question = ("+×+ Please enter your name +×+ ")
    customer_details['name'] = not_blank(question)

    question = ("+×+ Please enter your phone number +×+ ")
    customer_details['phone'] = not_blank(question)


    print("+×+ ",customer_details," +×+")

# Delivery information - name, phone, address ...

# customer detailes dictionary
def delivery_info():

    question = ("+×+ Please enter your name +×+ ")
    customer_details['name'] = not_blank(question)

    print("+×+ ",customer_details["name"]," +×+ ")

    question = ("+×+ Please enter your phone number +×+ ")
    customer_details['phone'] = not_blank(question)

    print("+×+ ",customer_details["phone"]," +×+ ")

    question = ("+×+ Please enter your house number +×+ ")
    customer_details['house'] = not_blank(question)

    print("+×+ ",customer_details['house']," +×+ ")

    question = ("+×+ Please enter your street name +×+ ")
    customer_details['street'] = not_blank(question)

    print("+×+ ",customer_details['street']," +×+ ")

    question = ("+×+ Please enter your suburb +×+ ")
    customer_details['suburb'] = not_blank(question)

    print("+×+ ",customer_details['suburb']," +×+ ")






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


