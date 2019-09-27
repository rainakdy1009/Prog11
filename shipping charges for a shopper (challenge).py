totalPurchase = input("Enter the amount of your total purchase: $")
if float(totalPurchase) < 50 :
    CostWShip = (float(totalPurchase))+10
    print("$10 is added for shipping costs.\nIncluding shipping fee, You have to pay {0:.2f}".format(CostWShip))
else:
    totalPurchase = (float(totalPurchase))
    print("No shipping costs!\nYou have to pay {0:.2f}".format(totalPurchase))
