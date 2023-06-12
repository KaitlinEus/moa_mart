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

#list to store order cost


def menu():
        num_albums = 16

        for count in range (num_albums):
            print("{} {} ${:.2f}".format(count+1, album_names[count], album_prices[count]))

menu()

########


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

menu()
order_albums()