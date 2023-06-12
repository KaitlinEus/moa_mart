# Moa Mart program

import random
from random import randint

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

    print("+×+ For delivery please enter 1 +×+")
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

# Pizza menu

def menu():
        num_albums = 16

        for count in range (num_albums):
            print("{} {} ${:.2f}".format(count+1, album_names[count], album_prices[count]))

# Choose total number of albums - max 5
# Album ordering - from menu - print each album with cost

def order_albums():
    #ask for total number of albums for order
    num_albums = 0

    while True:
        try:
            num_albums = int(input("How many albums do you want to order? "))
            if num_albums >= 1 and num_albums <= 5:
                break
            else:
                print("Your order must be between 1 and 5")
        except ValueError:
            print("That is not a valid number")
            print("Please enter a number between 1 and 5")


    #choose album from menu

    for item in range(num_albums):
        while num_albums > 0: 
                while True:
                    try:
                        album_ordered = int(input("Please choose your albums by entering the number from the menu "))
                        if album_ordered >= 1 and album_ordered <= 16:
                            break
                        else:
                            print("You order must be between 1 and 12")
                    except ValueError:
                        print("That is not a valid number")
                        print("Please enter a number from the menu")
        
                    
                album_ordered = album_ordered -1
                order_list.append(album_names[album_ordered])
                order_cost.append(album_prices[album_ordered])
                num_albums = num_albums-1
                print("{} ${:.2f}" .format(album_names[album_ordered],album_prices[album_ordered]))




# Main function

def main():
     
    '''
    Purpose: To generate a random name from the list and print out a welcome message
    Parameters: None
    Returns: None
    '''
     
    welcome()
    order_type()
    menu()
    order_albums()


main()


