import random
import time

cardNumber = []
cardShape = ["Hearts", "Spades", "Diamonds", "Clubs"] #Card Shapes
num = random.randint

for i in range(1,14):
    cardNumber.append(i)
print("You have the cards of " + str(cardNumber)) #Card number: from 1 to 13
print("We have four shapes: " + str(cardShape))

class Card:
    def __init__(MrFord, shape, number):
        MrFord.shape = shape
        MrFord.number = number
    def Func(MrFord):
        print(MrFord.shape, MrFord.number)
        #52 cards are created 

player_1 = input("Enter a name of player_1: ")
player_2 = input("Enter a name of player_2: ")
#players type their names

p1_point = 0
p2_point = 0
playAgain = 'yes'

def display(p1_point, p2_point):
    

    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        #It asks if the player wants to play again this game

        print(player_1 + "'s card is...")
        time.sleep(1)
        c1 = Card(random.choice(cardShape), random.choice(cardNumber))
        c1.Func()
    
        print(player_2 + "'s card is...")
        time.sleep(1)
        c2 = Card(random.choice(cardShape), random.choice(cardNumber))
        c2.Func()
        #The program gives one random card to each player
 
        

        if c1.number > c2.number:
            print(player_1 + " gains 1 point!")
            p1_point += 1
            print("player_1: " + str(p1_point) + " vs player_2: " + str(p2_point))
            
    
        elif c1.number < c2.number:
            print(player_2 + " gains 1 point!")
            p2_point += 1
            print(player_1 + " : " + str(p1_point) + " and " + player_2 + " : " + str(p2_point))
            

        elif c1.number == c2.number:
            print("Same number! It was a tie. Point for nobody")
            print("player_1: " + str(p1_point) + " vs player_2: " + str(p2_point))
        print('Do you want to keep playing? (yes or no)')
        playAgain = str(input())
        #This is a point system. The one who wins gets 1 point

  
display(p1_point, p2_point)
print('Good bye. See you later!')
