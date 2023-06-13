# menu so that user can choose either pickup or delivery

print("Is your order for pickup or delivery?")

print("For deliver please enter 1")
print("For pickup please enter 2")

delivery = int(input())

if delivery == 1:
    print("Delivery")

elif delivery == 2:
    print("Pickup")

else:
    print("That was not a valid input")