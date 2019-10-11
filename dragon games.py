import random
import time

def displayIntro(): #Explain the situation
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
    print()

def chooseWay(): #Choose one among 2 choices (Choose the way you'll go)
    way = ''
    while way != '1' and way != '2':
        print('Which way do you want to choose? (1 or 2)')
        way = input()

    return way

def checkWay (chosenWay): #It checks the way you chose
    print('You are walking down the street...')
    time.sleep(2)
    print('Now you can see the door of the entrance...')
    time.sleep(2)
    print('You are trying to open the door...')
    time.sleep(2)
   
    GoodWay = random.randint (1, 2)

    if chosenWay == str(GoodWay): #First option: The door doesn't open
        print('Oh No! The door is not open!')
        playAgain = input('Do you want to play again? (yes or no): ')
        if playAgain == 'yes' or playAgain == 'y':
            displayIntro()
            wayNumber = chooseWay()
            checkWay(wayNumber)
            caveNumber = chooseCave()
            checkCave(caveNumber)
           
            playAgain = input()
        else:
            exit()
        
    else: #Second option: The door opens
        print('Great! You opened the door!')
              
def chooseCave(): #Choose one cave among two
    cave = ''
    while cave != '1' and cave != '2':
        print('There are two caves!')
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave

   
def checkCave(chosenCave): #It checks the cave you chose
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)
          
    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave): #friendly cave
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!') #You're eaten 
    
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    wayNumber = chooseWay()
    checkWay(wayNumber)
    caveNumber = chooseCave()
    checkCave(caveNumber)
    
    print('Do you want to play again? (yes or no)') 
    playAgain = input()
   
