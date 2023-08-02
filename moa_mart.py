# Moa Mart program

import random
from random import randint
import sys

# Constants
low = 1
high =2
ph_low = 7
ph_high = 10

# List of random names
names = ["Yeonjun", "Taehyun", "Huening Kai", "Beomgyu", "Soobin", "Steve", "Daniel ", "Ben", "Terry", "Hyuka"]

# list of album names and prices
album_names = ["Mini Album 'The Dream Chapter: Star'", "Mini Album 'Minisode 1 : Blue Hour' AR ver", "Mini Album 'Minisode 1 : Blue Hour' R ver", 
               "Mini Album 'Minisode 1 : Blue Hour' VR ver", "Mini Album 'The Dream Chapter : Eternity' Port ver", "Mini Album 'The Dream Chapter : Eternity' Starboard ver", 
               "Full Album 'The Dream Chapter : Magic' Sanctuary ver", "Full Album 'The Dream Chapter : Magic' Arcadia ver", 
               "Repackaged Album 'The Chapter of Chaos: Fight or Escape' Fight ver", "Repackaged Album 'The Chapter of Chaos: Fight or Escape' Escape ver", 
               "Mini Album 'Minisode 2: Thursday's Child' Hate ver", "Mini Album 'Minisode 2: Thursday's Child' End ver", "Mini Album 'Minisode 2: Thursday's Child' Mess ver", 
               "Mini Album 'The Name Chapter: TEMPTATION' Daydream ver", "Mini Album 'The Name Chapter: TEMPTATION' Nightmare ver", 
               "5th Mini Album 'The Name Chapter: TEMPTATION' Farewell ver"]
album_prices = [59.99, 59.99, 59.99, 59.99, 59.99, 59.99, 59.99, 59.99, 64.99, 64.99, 58.99, 58.99, 58.99, 45.99, 45.99, 45.99]

#list to store ordered albums
order_list =[]
#list to store album prices
order_cost =[]

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
            print("")
            print("Sorry this cannot be blank")


# Validates to check if they are a string
def check_string(question):
    while True:
        response = input(question)
        x = response.isalpha()

        if x == False:
            print("")
            print("Sorry, you must only input letters")
        else:
            return (response.title())

# Validates inputs to check if they are an integer
def val_int(low, high, question):


    while True: 
        try:
            num = int(input(question))
            if num >= low and num <= high:
                return num
            else:
                print("")
                print("That is not a valid number")

        except ValueError:
            print("")
            print("That is not a valid number")


# Validates inputs to check if they are an integer with 7 to 10 digits
def check_phone(question, ph_low, ph_high):
    while True:
        try:
            num = int(input(question))
            test_num = num
            count = 0
            while test_num > 0:
                test_num = test_num//10
                count = count+1
            if count >= ph_low and count <= ph_high:
                return num
            else:
                print("")
                print("NZ phone numbers have between 7 and 10 digits")
        except ValueError:
            print("")
            print("NZ phone numbers have between 7 and 10 digits")

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

# Header for welcome
print("+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+")
print("+×+           One Dream! Hello, we are TOMORROW X TOGETHER!          +×+")
print("+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+")
# welcome message 
print("")
print("Welcome to Moa Mart. My name is",name)
print("I will be here to help you order your TXT album!")
print("")



# menu for click and collect or delivery

print()

def order_type():
    del_collect = ""

    question = (f"Please enter a number between {low} and {high}: ")

    # Title header for click and collect
    print("+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+")
    print("+×+                  DELIVERY OR CLICK AND COLLECT                   +×+")
    print("+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+")

    print("")
    print("Is your order for click and collect or delivery?")
    print("For delivery please enter 1")
    print("For click and collect please enter 2")


    delivery = val_int(low, high, question)

    if delivery == 1:
        print("")
        print("+×+  Delivery  +×+")
        print("")
        delivery_info()
        del_collect = "delivery"

    elif delivery == 2:
        print("")
        print("+×+  Click and Collect  +×+")
        print("")
        candc_info()
        del_collect = "collect"

    return del_collect



# Click and collect information - name and phone
def candc_info():
    # Title header for click and collect information
    print("+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+")
    print("+×+                      CLICK AND COLLECT DETAILS                   +×+")
    print("+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+")

    print("")
    question = ("Please enter your name: ")
    customer_details['name'] = check_string(question)

    print("")
    print("+×+ ",customer_details["name"]," +×+ ")
    print("")

    question = ("Please enter your phone number: ")
    customer_details['phone'] = check_phone(question, ph_low, ph_high)

    print("")
    print("+×+ ",customer_details["phone"]," +×+ ")
    print("")

# Delivery information - name, phone, address ...

def delivery_info():

    # Title header for delivery information
    print("+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+")
    print("+×+                          DELIVERY DETAILS                        +×+")
    print("+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+")

    print("")
    question = ("Please enter your name: ")
    customer_details['name'] = check_string(question)

    print("")
    print("+×+ ",customer_details["name"]," +×+ ")
    print("")

    question = ("Please enter your phone number: ")
    customer_details['phone'] = check_phone(question, ph_low, ph_high)

    print("")
    print("+×+ ",customer_details["phone"]," +×+ ")
    print("")

    question = ("Please enter your house number: ")
    customer_details['house'] = not_blank(question)

    print("")
    print("+×+ ",customer_details['house']," +×+ ")
    print("")

    question = ("Please enter your street name: ")
    customer_details['street'] = check_string(question)

    print("")
    print("+×+ ",customer_details['street']," +×+ ")
    print("")

    question = ("Please enter your suburb: ")
    customer_details['suburb'] = check_string(question)

    print("")
    print("+×+ ",customer_details['suburb']," +×+ ")
    print("")



# Album menu
def menu():
        # Title header for the menu
        print("+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+")
        print("+×+                              ALBUMS                              +×+")
        print("+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+")

        num_albums = 16

        for count in range (num_albums):
            print("")
            print("-----------------------------------------------------------------------------")
            print("{} {} ${:.2f}".format(count+1, album_names[count], album_prices[count]))
            print("-----------------------------------------------------------------------------")

# Choose total number of albums - max 5
# Album ordering - from menu - print each album with cost

def order_albums():

    # Title header for album ordering
    print("")
    print("+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+")
    print("+×+                            ORDER ALBUMS                          +×+")
    print("+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+")

    #ask for total number of albums for order
    num_albums = 0
    num_high = 10
    menu_low = 1
    menu_high = 16

    question = (f"Please enter a number between {low} and {num_high}: ")
    print("")
    print("You can order up to max 10 albums at a time")
    print("How many albums do you want to order?")

    num_albums = val_int(low, num_high, question)

    print("")
    print("+×+  ", num_albums, "  +×+")
    print("")

    #choose album from menu
    for item in range(num_albums):
        while num_albums > 0: 
            print("Please choose your albums by entering the numbers from the menu")
            question = (f"Please enter a number between {menu_low} and {menu_high}: ")
            album_ordered = val_int(menu_low, menu_high, question)

        
            album_ordered = album_ordered -1
            order_list.append(album_names[album_ordered])
            order_cost.append(album_prices[album_ordered])
            num_albums = num_albums-1

            print("")
            print("+×+","{} ${:.2f}" .format(album_names[album_ordered],album_prices[album_ordered]),"+×+")
            print("")

# print order out - inlcuding: if order is click and collect or delivery, names and prices of albums, and total cost including any delivery charge

def print_order(del_collect):
    print()
    total_cost = sum(order_cost)

    print("+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+")
    print("+×+                          CUSTOMER DETAILS                        +×+")
    print("+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+")
    if del_collect == "collect":
            print("Your order is for: Pickup")
            print(f"Customer Name: {customer_details['name']} \nCustomer Phone Number: {customer_details['phone']}")
            print("You will recieve a text message when the item/s are ready for collection")
    
    elif del_collect == "delivery":
        print("Your order is for: Delivery")
        
        
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone Number: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()

    print("+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+")
    print("+×+                            ORDER DETAILS                         +×+")
    print("+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
        


    if del_collect == "delivery":

        sub_total = sum(order_cost)
        print(f"Subtotal: ${sub_total:.2f}")

        if len(order_list) < 5:
                total_cost = total_cost + 9
                print("Delivery charge: $9 ")
        else:
            total_cost = total_cost + 0
            print("Delivery charge: $0 ")

    print(f"Total Cost: ${total_cost:.2f}")
    
    print("")


# Ability to cancel or proceed with order

def confirm_cancel():

    question = (f"Please enter a number between {low} and {high}: ")

    print("+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+")
    print("+×+                          CONFIRM OR CANCEL                       +×+")
    print("+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+")

    print("Please confirm your order")

    print("To confirm, please enter 1")
    print("To cancel, please enter 2")

    confirm = val_int(low, high, question)
    if confirm >= low and confirm <= high:

        if confirm == 1:
            print("")
            print("+×+  Order confirmed  +×+")
            print("+×+ Your order is now being prepared +×+")
            print("")
            new_exit()

        elif confirm == 2:
            print("")
            print("+×+  Order cancelled  +×+")
            print("+×+ You can restart or exit the BOT +×+")
            print("")
            new_exit()
                    
            
# Option for new order or to exit
def new_exit():

    print("+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+")
    print("+×+                         NEW ORDER OR EXIT                        +×+")
    print("+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+")

    question = (f"please enter a number between {low} and {high}: ")

    print("Do you want to start another order or exit?")
    print("To start another order, please enter 1")
    print("To exit the BOT, please enter 2")

    confirm = val_int(low, high, question)
    if confirm >= 1 and confirm <= 2:

        if confirm == 1:
            print("")
            print("+×+  New Order  +×+")
            print("")
            order_list.clear()
            order_cost.clear()
            customer_details.clear()
            main()


        elif confirm == 2:
            print("")
            print("+×+  Exit  +×+")
            print("")
            order_list.clear()
            order_cost.clear()
            customer_details.clear()
            sys.exit()
                 
# Main function

def main():
     
    '''
    Purpose: To generate a random name from the list and print out a welcome message
    Parameters: None
    Returns: None
    '''
     
    welcome()
    del_collect = order_type()
    menu()
    order_albums()
    print_order(del_collect)
    confirm_cancel()
    

main()
