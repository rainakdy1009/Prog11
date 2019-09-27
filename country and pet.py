country = input("Where are you from?: ")
pet = input("What do you raise as your pet?: ")
if country == "Canada" and (pet == "Moose" or pet == "Beaver"):
    answer = input("Do you play hockey too?: ")
    print("Okay")
    
else:
    print("Canada is a good country to go on a trip.\nTry to raise Moose or Beaver too")
