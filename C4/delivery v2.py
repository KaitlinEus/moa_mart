# customer detailes dictionary
customer_details = {}

def not_blank(question):
    valid = False
    while not valid: 
        response = input(question)
        if response != "":
            return response
        else:
            print("Sorry this cannot be blank")

def delivery_info():

    question = ("+×+ PPlease enter your name +×+ P")
    customer_details['name'] = not_blank(question)

    print(customer_details["name"])

    question = ("+×+ PPlease enter your phone number +×+ P")
    customer_details['phone'] = not_blank(question)

    print(customer_details["phone"])

    question = ("+×+ PPlease enter your house number +×+ P")
    customer_details['house'] = not_blank(question)

    print(customer_details['house'])

    question = ("+×+ PPlease enter your street name +×+ P")
    customer_details['street'] = not_blank(question)

    print(customer_details['street'])

    question = ("+×+ PPlease enter your suburb +×+ P")
    customer_details['suburb'] = not_blank(question)

    print(customer_details['suburb'])


delivery_info()


