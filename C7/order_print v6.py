#list to store ordered albums
order_list =["Mini Album 'The Dream Chapter: Star'", "Mini Album 'Minisode 1 : Blue Hour' AR ver", 
             "Mini Album 'Minisode 1 : Blue Hour' R ver", "5th Mini Album 'The Name Chapter: TEMPTATION' Farewell ver"]
#list to store album prices
order_cost =[59.99, 59.99, 59.99, 45.99]

customer_details = {'name': 'Denzelle', 'phone': '1234567890', 'house': '1a', 'street': 'broadhurst road', 'suburb': 'Flat Bush'}

def print_order():
    total_cost = sum(order_cost)

    print("+×+ Customer Details +×+")
    print(f"Customer Name: +×+  {customer_details['name']}  +×+ \nCustomer Phone Number: +×+  {customer_details['phone']}  +×+ \nCustomer Address: +×+  {customer_details['house']} {customer_details['street']} {customer_details['suburb']}  +×+")
    print()

    print("+×+ Order Details +×+")
    count = 0
    for item in order_list:
        print("Ordered: +×+  {}  +×+ Cost: +×+  ${:.2f}  +×+".format(item, order_cost[count]))
        count = count+1
    print()
        
    print("+×+ Total Cost +×+")
    print(f"+×+  ${total_cost:.2f}  +×+")

print_order()