# Moa Mart program
# Program for ordering Tomorrow x Together (TXT) albums - targeted towards TXT fans


# Imports of modules from pythons library
# Module that allows program to perform tasks related to randomness
import random
# Imports the radint funciton from the random module - allows for generating random integers within a specific range
from random import randint

# Module for various system-level operations and to access command-line arguments, interact with the runtime environment, and control the Python interpreter itself.
import sys

# Imports of modules that are not in pythons library
# Module that allows program to print text in color
import simple_colors
# IMPROTANT NOTE: Please download simple_colors by pasting the following into terminal: pip3 install simple-colors    OR: pip install simple-colors

# Constants - sets the values of variables universally
# Used for choosing between 2 options
low = 1
high = 2
# Used for the min and max digits able to input for phone number
ph_low = 7
ph_high = 10

# List of random names - Names used are from the KPOP boy group TXT
names = ["Yeonjun", "Taehyun", "Huening Kai", "Beomgyu",
         "Soobin", "Steve", "Daniel ", "Ben", "Terry", "Hyuka"]

# List of album names and prices that the store offers for sale
# Album names. There are 16 albums in total
album_names = ["Mini Album 'The Dream Chapter: Star'", "Mini Album 'Minisode 1 : Blue Hour' AR ver", "Mini Album 'Minisode 1 : Blue Hour' R ver",
               "Mini Album 'Minisode 1 : Blue Hour' VR ver", "Mini Album 'The Dream Chapter : Eternity' Port ver", "Mini Album 'The Dream Chapter : Eternity' Starboard ver",
               "Full Album 'The Dream Chapter : Magic' Sanctuary ver", "Full Album 'The Dream Chapter : Magic' Arcadia ver",
               "Repackaged Album 'The Chapter of Chaos: Fight or Escape' Fight ver", "Repackaged Album 'The Chapter of Chaos: Fight or Escape' Escape ver",
               "Mini Album 'Minisode 2: Thursday's Child' Hate ver", "Mini Album 'Minisode 2: Thursday's Child' End ver", "Mini Album 'Minisode 2: Thursday's Child' Mess ver",
               "Mini Album 'The Name Chapter: TEMPTATION' Daydream ver", "Mini Album 'The Name Chapter: TEMPTATION' Nightmare ver",
               "5th Mini Album 'The Name Chapter: TEMPTATION' Farewell ver"]
# Album prices
album_prices = [59.99, 59.99, 59.99, 59.99, 59.99, 59.99, 59.99,
                59.99, 64.99, 64.99, 58.99, 58.99, 58.99, 45.99, 45.99, 45.99]

# list to store ordered albums
order_list = []
# list to store album prices
order_cost = []

# customer details dictionary - stores customer details from that the customer inputs
customer_details = {}

# Validates inputs to check if they are blank


def not_blank(question):
    '''
    Purpose: Makes sure that user input is not blank
    Parameters: Question
    Returns: The validated non-blank value as a string.(response.title()
    '''
    valid = False
    #sets up while loop
    while not valid:
        #prints out question and asks for input(string)
        response = input(question)
        #Checks if input is not blank
        if response != "":
            # if not blank, rtuense the response in the title class
            return response.title()
        #if blank
        else:
            #prints error message
            print("\nSorry, this cannot be blank")


# Validates string inputs to check if they are a string
def check_string(question):
    '''
    Purpose: Makes sure user input is only alphabetical characters
    Parameters: question
    Returns: The validated string as a title-cased version if it consists only of alphabetic characters. response.title()
    '''

    # Sets up while loop
    while True:
        # Prints questions and asks for input(string)
        response = input(question)
        # Checks that the input consists of only alphabetical characters - sets x to true if input passes requirements
        x = response.isalpha()

       # If x is False, an error message is printed
        if x == False:
            print("\nSorry, you must only input letters")
        else:
            # If true, returns the response in the title class
            return response.title()

# Validates inputs to check if they are an integer


def val_int(low, high, question):
    '''
    Purpose: Makes sure that user input as an integer within a specified range.
    Parameters: question, low, high
    Returns: The validated integer input within the specified range. num
    '''
    # Sets up while loop
    while True:
        try:
            # Prints question and asks for input(integer)
            num = int(input(question))
            # if num is inside or queal to one of the numberic boundreis it will retuern num
            if num >= low and num <= high:
                return num
            else:
                # If num does not meet requirements as it is outside of the boundries, an error message is printed
                print("\nSorry, that is not a valid number")

        except ValueError:
            # If num does not meet requirements as it is not a integer, an error message is printed
            print("\nSorry, that is not a valid number")


# Validates inputs to check if they are an integer with 7 to 10 digits
def check_phone(question, ph_low, ph_high):
    '''
    Purpose: Makes sure that user input is only an integer within a spcified range of digits
    Parameters: questions, ph_low, ph_high
    Returns: The validated phone number as a string if it consists of digits and its length is within the specified range. num
    '''
    # Sets up while loop
    while True:
        try:
            # Prints question and ask for input(integer)
            num = int(input(question))
            # Makes test_num equal to num - This allows the program to pull apart the number
            test_num = num
            count = 0
            # Sets up another while loop - test_num is greater than 0
            while test_num > 0:
                # test_num is divided by 10 to remove the last digit
                test_num = test_num//10
                # Adds 1 to the count
                count = count+1
            # Checks if count meets the requirements - Must be equal or greater than ph_low (7) and equal or lesser than ph_high (10)
            if count >= ph_low and count <= ph_high:
                # Returns num
                return num
            # if count does not meet requirements - not >= 7 and <= 10, an error message is printed and asks for input again
            else:
                print("\nSorry, that is not a valid phone number")
                print("NZ phone numbers have between 7 and 10 digits")
        # if count does not meet requirements - not an integer, an error message is printed and asks for input again
        except ValueError:
            print("\nSorry, that is not a valid phone number")
            print("NZ phone numbers have between 7 and 10 digits")

# Welcome message with random name


def welcome():
    '''
    Purpose: To generate a random name for the list of names and print out a welcome message
    Parameters: None
    Returns: None
    '''


# Sets num to randint which returns an integer number from a spcified range of numbers - 0 to 9
num = randint(0, 9)
# Makes name equal to a name that corresponds with the a number chosen from num
name = (names[num])

# Logo
print(simple_colors.yellow(""" 

       __    __     ______     ______          __    __     ______     ______     ______  
      /\ "-./  \   /\  __ \   /\  __ \        /\ "-./  \   /\  __ \   /\  == \   /\__  _\ 
      \ \ \-./\ \  \ \ \/\ \  \ \  __ \       \ \ \-./\ \  \ \  __ \  \ \  __<   \/_/\ \/ 
       \ \_\ \ \_\  \ \_____\  \ \_\ \_\       \ \_\ \ \_\  \ \_\ \_\  \ \_\ \_\    \ \_\ 
        \/_/  \/_/   \/_____/   \/_/\/_/        \/_/  \/_/   \/_/\/_/   \/_/ /_/     \/_/
    
    
    """))

# Header for welcome
print(simple_colors.blue(
    "+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+"))
print(simple_colors.yellow("          +×+"),
      "One Dream! Hello, we are TOMORROW X TOGETHER!", simple_colors.yellow("+×+"))
print(simple_colors.blue(
    "+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+"))

# welcome message - prints with random name
print("\nWelcome to Moa Mart. My name is", name)
print("I will be here to help you order your TXT album!")


# menu for click and collect or delivery

def order_type():
    '''
    Purpose: Makes user choose order type
    Parameters: None
    Returns: del_collect: A string indicating the delivery option chosen ("delivery" for delivery, "click" for click & collect).
    '''
    # Sets del_collect to empty
    del_collect = ""

    # Title header for click and collect
    print(simple_colors.blue(
        "\n\n+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+"))
    print(simple_colors.yellow("                  +×+"),
          "DELIVERY OR CLICK AND COLLECT", simple_colors.yellow("+×+"))
    print(simple_colors.blue(
        "+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+"))

    # Question asks for a number between 1 and 2
    question = (f"Please enter a number between {low} and {high}: ")

    # Print statement that gives intructions
    print("\nIs your order for click and collect or delivery?")
    print("For delivery please enter 1")
    print("For click and collect please enter 2")

    # Prints question and asks for input(integer) - sends input through integer validator
    delivery = val_int(low, high, question)

    # If user input is 1 - user chooses deilvery
    if delivery == 1:
        # print statement that lets user knows that they have chosen delivery
        print(simple_colors.green("\n+×+ "),
              "Delivery",  simple_colors.green("+×+"))
        # Print statement that lets user know about delivery fee
        print(simple_colors.magenta(
            "Please note that a delivery fee of $9 is applied when you order less than 5 albums"))
        # Sets del_collect to delivery
        del_collect = "delivery"
        # Opens and runs the delivery function
        delivery_info()

    # If user input is 2 - user chooses click and collect
    elif delivery == 2:
        # print statement that lets user know they have chosen click and collect
        print(simple_colors.green("\n+×+ "),
              "Click and Collect",  simple_colors.green("+×+"))
        # sets del_collect to collect
        del_collect = "collect"
        # opens and runs the click and collect function
        candc_info()
    # Returns information back to del_collect
    return del_collect


# Click and collect information - name and phone
def candc_info():
    '''
    Purpose: Collects the customer's information (name and phone number) which will be used for click and collect
    Parameters: None
    Returns: None
    '''
    # Title header for click and collect information
    print(simple_colors.blue(
        "\n\n+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+"))
    print(simple_colors.yellow("                    +×+"),
          "CLICK AND COLLECT DETAILS", simple_colors.yellow("+×+"))
    print(simple_colors.blue(
        "+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+"))
    # Question which asks for first name
    question = ("\nPlease enter your first name: ")
    # Prints quetsion and asks for input(string). sends input through string validator and stores input in customer details dictionary under name
    customer_details['name'] = check_string(question)
    # prints customer name
    print(simple_colors.green("\n+×+ "),
          customer_details["name"], simple_colors.green("+×+"))
    # question which asks for phone number.
    question = ("\nPlease enter your phone number: ")
    # prints question and asks for input(int). sends input through ph number validator and stores input in custoemr detials dictionary under phone
    customer_details['phone'] = check_phone(question, ph_low, ph_high)
    # prints customer ph num
    print(simple_colors.green("\n+×+ "),
          customer_details["phone"], simple_colors.green("+×+"))

# Delivery information - name, phone, address ...


def delivery_info():
    '''
    Purpose: Collects the customer's information (name, phone number, house number, street name, and suburb) which will be used for delivey
    Parameters: None
    Returns: None
    '''
    # Title header for delivery information
    print(simple_colors.blue(
        "\n\n+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+"))
    print(simple_colors.yellow("                        +×+"),
          "DELIVERY DETAILS", simple_colors.yellow("+×+"))
    print(simple_colors.blue(
        "+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+"))
    # Question which asks for first name
    question = ("\nPlease enter your first name: ")
    # Prints quetsion and asks for input(string). sends input through string validator and stores input in customer details dictionary under name
    customer_details['name'] = check_string(question)
    # prints customer name
    print(simple_colors.green("\n+×+ "),
          customer_details["name"], simple_colors.green("+×+"))
    # question which asks for phone number.
    question = ("\nPlease enter your phone number: ")
    # prints question and asks for input(int). sends input through ph number validator and stores input in custoemr detials dictionary under phone
    customer_details['phone'] = check_phone(question, ph_low, ph_high)
    # prints customer ph num
    print(simple_colors.green("\n+×+ "),
          customer_details["phone"], simple_colors.green("+×+"))
    # question which asks for house number
    question = ("\nPlease enter your house number: ")
    # prints quesiton and asks for input. sends input through not blank validator and store input in customer details dictionary under house
    customer_details['house'] = not_blank(question)
    # prints customer house number
    print(simple_colors.green("\n+×+ "),
          customer_details['house'], simple_colors.green("+×+"))
    # question which asks for street type
    question = ("\nPlease enter your street type: ")
    # prints question and asks for input(string). sends input through string validator and stored input in customer details dictionary under road
    customer_details['road'] = check_string(question)
    # prints customer street type
    print(simple_colors.green("\n+×+ "),
          customer_details['road'], simple_colors.green("+×+"))
    # questoin which asks for street name
    question = ("\nPlease enter your street name: ")
    # prints question and asks for input(string). Sends input through string validator and stores input in customer details dictionary under street
    customer_details['street'] = check_string(question)
    # prints street name
    print(simple_colors.green("\n+×+ "),
          customer_details['street'], simple_colors.green("+×+"))
    # question which asks for suburb
    question = ("\nPlease enter your suburb: ")
    # prints question and asks for input(string). Sends input through string validator and stores input in customer detials dictionary under suburb
    customer_details['suburb'] = check_string(question)
    # prints suburb
    print(simple_colors.green("\n+×+ "),
          customer_details['suburb'], simple_colors.green("+×+"))

# Album menu


def menu():
    '''
    Purpose: Displays the menu of albums - album names corresponds with item number and price
    Parameters: None
    Returns: None
    '''
    # Title header for the menu
    print(simple_colors.blue(
        "\n\n+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+"))
    print(simple_colors.yellow("                             +×+"),
          "ALBUMS", simple_colors.yellow("+×+"))
    print(simple_colors.blue(
        "+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+"))

    # sets num_albums to 16 - total amount of different albums for sale
    num_albums = 16
    # prints blank so there will be a space
    print("")

    # code will count rhough 16 times until no more numbers are left
    for count in range(num_albums):
        # Formats the item number, album name, and price and
        print(
            "-----------------------------------------------------------------------------")
        print("{} {} ${:.2f}".format(simple_colors.red(
            count+1), album_names[count], album_prices[count]))
    print("-----------------------------------------------------------------------------")

# Choose total number of albums - max 5
# Album ordering - from menu - print each album with cost


def order_albums():
    '''
    Purpose: Lets users order albums items by specifying the quantity and choosing from a menu.
    Parameters: None
    Returns: None
    '''
    # Title header for album ordering
    print(simple_colors.blue(
        "\n\n+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+"))
    print(simple_colors.yellow("                          +×+"),
          "ORDER ALBUMS", simple_colors.yellow("+×+"))
    print(simple_colors.blue(
        "+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+"))

    # sets num of albums to 0
    num_albums = 0

    # constants used in num_albums
    # max num of albums allowed to order is set to 10
    num_high = 10
    # lowest allowed album number in the menu
    menu_low = 1
    # highest allowed album number in the menu
    menu_high = 16

    # ask for total number of albums for order
    # question which asks to enter a number between 1 and 10
    question = (f"Please enter a number between {low} and {num_high}: ")
    print("\nYou can order up to max 10 albums at a time")
    print("How many albums do you want to order?")

    # prints question and asks for input(integer). sends input through int validator
    num_albums = val_int(low, num_high, question)
    # prints num of albums
    print(simple_colors.green("\n+×+ "),
          num_albums, simple_colors.green(" +×+"))

    # choose album from menu

    # code will count though the number of albums chosen
    for item in range(num_albums):
        # sets while loop where num_albums is greater than 0
        while num_albums > 0:
            # print statement for intstructions
            print("\nPlease choose your albums", simple_colors.magenta(
                "one at a time"), "by entering the numbers from the menu")
            # question which asks user to enter a num between 1 and 16
            question = (
                f"Please enter a number between {menu_low} and {menu_high}: ")
            # prints question and asks for input(integer). sends input through int validator
            album_ordered = val_int(menu_low, menu_high, question)

            # Adjust the Album index number to match the list index number
            album_ordered = album_ordered - 1
            # Add the chosen albums to the order list
            order_list.append(album_names[album_ordered])
            # add the chosen albums to the cost list
            order_cost.append(album_prices[album_ordered])
            # album_ordered decreases each time by one everytime a num is inputed - makes sure user only orders the amount of albums they wanted
            num_albums = num_albums-1

            # prints chosen album and price
            print(simple_colors.green("\n+×+ "), "{} ${:.2f}" .format(
                album_names[album_ordered], album_prices[album_ordered]), simple_colors.green("+×+"))

# print order out - inlcuding: if order is click and collect or delivery, names and prices of albums, and total cost including any delivery charge


def print_order(del_collect):
    '''
    Purpose: To display customer information, order detials and order costs
    Parameters: del_collect
    Returns: None
    '''

    # makes total_cost equal to the sum of the costs of all the ordered albums
    total_cost = sum(order_cost)

    # Customer details header title
    print(simple_colors.blue(
        "\n\n+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+"))
    print(simple_colors.yellow("                        +×+"),
          "CUSTOMER DETAILS", simple_colors.yellow("+×+"))
    print(simple_colors.blue(
        "+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+"))

    # if the user initially chose click and collect
    if del_collect == "collect":
        # prints messages that states type of order and cutstomer detials that was stored in the customer detials dictionary
        print("\nYour order is for: Pickup")
        print(
            f"Customer Name: {customer_details['name']} \nCustomer Phone Number: {customer_details['phone']}")

    # if the user intially chose delivery
    elif del_collect == "delivery":
        # prints messages that states type of order and customer details that was stored in the customer details dictionary
        print("\nYour order is for: Delivery")
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone Number: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['road']} {customer_details['suburb']}")

    # header title for order details
    print(simple_colors.blue(
        "\n\n+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+"))
    print(simple_colors.yellow("                         +×+"),
          "ORDER DETAILS", simple_colors.yellow("+×+"))
    print(simple_colors.blue(
        "+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+"))
    # sets count to 0
    count = 0
    # prints blank for spacing
    print()
    # the items stored in the order list
    for item in order_list:
        # prints in a formatted way
        print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count]))
        # Adds one to the counter variable
        count = count+1

    # prints blank for spacing
    print()
    # if user chose delivery
    if del_collect == "delivery":
        # makes subtotal equal to the sum of the costs of all the ordered albums
        sub_total = sum(order_cost)
        # prints subtotal
        print(f"Subtotal: ${sub_total:.2f}")
        # if user ordered less than 5 albums
        if len(order_list) < 5:
            # delivery fee of $9 is added to total cost
            total_cost = total_cost + 9
            # prints deliver charge
            print("Delivery charge: $9 ")
        # if user ordered more than 5
        else:
            # delivery fee of $9 is added to total cost
            total_cost = total_cost + 0
            # prints delivery caharge
            print("Delivery charge: $0 ")
    # if user chose either delivery or click and collect, total cost is printed in - it is formatted
    print(simple_colors.red(f"Total Cost: ${total_cost:.2f}", "bold"))

    # if user chose click and collect
    if del_collect == "collect":
        # print statement that tells user info
        print(simple_colors.magenta(
            "\nYou will recieve a text message when the item/s are ready for collection"))


# Ability to cancel or proceed with order

def confirm_cancel():
    '''   
    Purpose: allows user to choose to confirm or cancel their order
    Parameters: None
    Returns: None
    '''
    print(simple_colors.blue(
        "\n\n+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+"))
    print(simple_colors.yellow("                        +×+"),
          "CONFIRM OR CANCEL", simple_colors.yellow("+×+"))
    print(simple_colors.blue(
        "+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+"))

    # question which asks to enter a num between 1 and 2
    question = (f"Please enter a number between {low} and {high}: ")

    # print statements which explain the instructions
    print("\nPlease confirm your order")
    print("To confirm, please enter 1")
    print("To cancel, please enter 2")

    # prints question and asks for input(int). sends input to int validator
    confirm = val_int(low, high, question)
    # if user inputs 1 - user chooses to confirm
    if confirm == 1:
        # print statement telling user they have confirmed and that their order is now being prepared
        print(simple_colors.green("\n+×+ "),
              "Order confirmed", simple_colors.green(" +×+"))
        print(simple_colors.green("+×+ "),
              "Your order is now being prepared", simple_colors.green(" +×+"))
        # opens and starts the new_exit function

    elif confirm == 2:
        # prints statement telling user they have cancelled and gives further info
        print(simple_colors.green("\n+×+ "),
              "Order cancelled", simple_colors.green(" +×+"))
        print(simple_colors.green("+×+ "),
              "You can restart or exit the BOT", simple_colors.green(" +×+"))

    # opens and starts the new_exit function
    new_exit()


# Option for new order or to exit
def new_exit():
    '''
    Purpose: allows user to start a new order or exit the BOT
    Parameters: None
    Returns: None
    '''

    # Header title for new order or exit
    print(simple_colors.blue(
        "\n\n+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+"))
    print(simple_colors.yellow("                       +×+"),
          "NEW ORDER OR EXIT", simple_colors.yellow("+×+"))
    print(simple_colors.blue(
        "+×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×++×+"))

    # question that asks for a num between 1 and 2
    question = (f"please enter a number between {low} and {high}: ")

    # print statements which gives users instructions
    print("\nDo you want to start another order or exit?")
    print("To start another order, please enter 1")
    print("To exit the BOT, please enter 2")

    # prints question and asks for input(int). sends input through to int validator
    confirm = val_int(low, high, question)

    # if user inputs 1 - user chose new order
    if confirm == 1:
        # prints new order
        print(simple_colors.green("\n+×+ "),
              "New Order", simple_colors.green(" +×+"))
        # clears data in order list
        order_list.clear()
        # clears data in order cost
        order_cost.clear()
        # clears data in customer details dictionary
        customer_details.clear()
        # opens and starts main - the whole program restarts from the start
        main()

    # if user inputs 2 - user chose to exit
    elif confirm == 2:
        # prints exit
        print(simple_colors.green("\n+×+ "),
              "Exit", simple_colors.green(" +×+"))
        # prints thank you message
        print(simple_colors.green("\n+×+ "),
              "Thank you for shopping at Moa Mart", simple_colors.green(" +×+"))
        # clears data in order list
        order_list.clear()
        # clears data in order cost
        order_cost.clear()
        # clears data in customer details dictionary
        customer_details.clear()
        # program stops
        sys.exit()

# Main function


def main():
    '''
    Purpose: To run all functions
    Parameters: None
    Returns: None
    '''
    # Call the welcome function to welcome the customer to Moa Mart
    welcome()
    # Call the order_type function to choose between delivery or click & collect 
    del_collect = order_type()
    # Call the menu function to display the menu of albums
    menu()
    # Call the order_albums function to process the album order
    order_albums()
    # Call the print_order function to display and print out the order details
    print_order(del_collect)
    # Call the confirm_cancel function to confirm or cancel the order
    confirm_cancel()


main()
