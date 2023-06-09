# menu so that user can choose either pickup or delivery

print("+×+ Is your order for pickup or delivery? +×+")

print("+×+ For deliver please enter 1 +×+")
print("+×+ For pickup please enter 2 +×+")

while True: 
    try:
        delivery = int(input("+×+ Please enter a number +×+ "))
        if delivery >= 1 and delivery <= 2:

            if delivery == 1:
                print("+×+ Delivery +×+")
                break

            elif delivery == 2:
                print("+×+ Pickup +×+")
                break
        else: 
            print("+×+ Number must be 1 or 2 +×+ ")

    except ValueError:
        print("+×+ That is not a valid number +×+")
        print("+×+ Please enter 1 or 2 +×+ ")
