import random
cardNumber = []
cardShape = ["Hearts", "Spades", "Diamonds", "Clubs"]
num = random.randint

for i in range(1,14):
    cardNumber.append(i)
print("You have the cards of " + str(cardNumber))
print("We have four shapes: " + str(cardShape))

class Card:
    def __init__(MrFord, shape, number):
        MrFord.shape = shape
        MrFord.number = number
    def Func(MrFord):
        print(MrFord.shape, MrFord.number)

player_1= input("What is your name?: ")
print("Hello, "  + player_1 + ". Your card is...")

c1 = Card(random.choice(cardShape), random.choice(cardNumber))
c1.Func()

player_2= input("What is your name?: ")
print("Hello, "  + player_2 + ". Your card is...")

c2 = Card(random.choice(cardShape), random.choice(cardNumber))
c2.Func()

if c1.number > c2.number:
    print(player_1 + " won!")
    
elif c1.number < c2.number:
    print(player_2 + " won!")

else:
    print("Same number! It was a tie.")
