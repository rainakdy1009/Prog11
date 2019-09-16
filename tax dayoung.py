item1 = input("What is the cost of item1?: ")
item2 = input("What is the cost of item2?: ")
item3 = input("What is the cost of item3?: ")
SalesTaxes = (float(item1)+float(item2)+float(item3))*0.12
TotalCost = (float(item1)+float(item2)+float(item3))*1.12
print("The sales taxes of the items is {0:.2f}".format(SalesTaxes))
print("The total cost of the items is {0:.2f}".format(TotalCost))
