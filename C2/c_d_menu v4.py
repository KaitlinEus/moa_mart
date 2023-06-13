# menu so that user can choose either pickup or delivery
# bug - need to make it so that it only accepts 1 or 2

print("Is your order for pickup or delivery?")

print("For deliver please enter 1")
print("For pickup please enter 2")

low = 1
high = 2

while True: 
    try:
        delivery = int(input("Please enter a number"))

        if delivery == 1:
            print("Delivery")
            break

        elif delivery == 2:
            print("Pickup")
            break

    except ValueError:
        print("That is not a valid number")
        print("Please enter 1 or 2")
