#list to store ordered albums
order_list =["Mini Album 'The Dream Chapter: Star'", "Mini Album 'Minisode 1 : Blue Hour' AR ver", 
             "Mini Album 'Minisode 1 : Blue Hour' R ver", "5th Mini Album 'The Name Chapter: TEMPTATION' Farewell ver"]
#list to store album prices
order_cost =[59.99, 59.99, 59.99, 45.99]

cust_details = {'name': 'Denzelle', 'phone': '1234567890', 'house': '1a', 'street': 'broadhurst road', 'suburb': 'Flat Bush'}


print(f"Customer Name : {cust_details['name']} \nCustomer Phone Number :{cust_details['phone']} \nCustomer Address :{cust_details['house']} {cust_details['street']} {cust_details['suburb']}")



count = 0
for item in order_list:
    print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count]))
    count = count+1
    