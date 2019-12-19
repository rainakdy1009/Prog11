import pygame
import os
import time

_image_library = {}
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pg.image.load(canonicalized_path)
        _image_library[path] = image
    return image

# initialize game engine
pygame.init()

window_width=1000
window_height=700

animation_increment=10

# Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
mainloop = True            
FPS = 30
playtime = 0.0
background_image = pygame.image.load("pastelBackground.png").convert()


##robber: player

robber_x = 30
robber_y = 30
detectX = 51
detectY = 200
judgeX = 400
judgeY = 500
moneyX = 850
moneyY = 640
policeDogX = 240
policeDogY = 600
policeX = 240
policeY = 550
robberSpeedX, robberSpeedY = 10, 10
detectSpeedX, detectSpeedY = 7, 7
judgeSpeedX, judgeSpeedY = 7, 7
moneySpeedX, moneySpeedY = 10, 10
policeDogSpeedX, policeDogSpeedY = 7, 7
policeSpeedX, policeSpeedY = 7, 7
robber= pygame.image.load("robber.PNG")
detective= pygame.image.load("detective.png")
judge= pygame.image.load("judge.png")
money= pygame.image.load("money.png")
policeDog= pygame.image.load("policeDog.png")
police= pygame.image.load("police.png")

objects = [detective, judge, money, policeDog, police]
        
while mainloop:
    milliseconds = clock.tick(FPS) 
    playtime += milliseconds / 1000.0

    for event in pygame.event.get():
        pygame.time.delay(3)
        if event.type == pygame.QUIT: 
            mainloop = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False


    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: robber_y -= robberSpeedY
    if pressed[pygame.K_DOWN]: robber_y += robberSpeedY
    if pressed[pygame.K_LEFT]: robber_x -= robberSpeedX
    if pressed[pygame.K_RIGHT]: robber_x += robberSpeedX



    text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), playtime)
    pygame.display.set_caption(text)

    detectX += detectSpeedX
    detectY += detectSpeedY
    judgeX += judgeSpeedX
    judgeY += judgeSpeedY
    moneyX += moneySpeedX
    moneyY += moneySpeedY
    policeDogX += policeDogSpeedX
    policeDogY += policeDogSpeedY
    policeX += policeSpeedX
    policeY += policeSpeedY

    if detectX > 950 or detectX < 50 and detectX != 1000:
        detectSpeedX = detectSpeedX * -1
        
        
    elif detectY > 650 or detectY < 50:
        detectSpeedY = detectSpeedY * -1

    if judgeX > 950 or judgeX < 50 and judgeX != 1000:
        judgeSpeedX = judgeSpeedX * -1
        
        
    elif judgeY > 650 or judgeY < 50:
        judgeSpeedY = judgeSpeedY * -1

    if moneyX > 950 or moneyX < 50 and moneyX != 1000:
        moneySpeedX = moneySpeedX * -1
        
        
    elif moneyY > 650 or moneyY < 30:
        moneySpeedY = moneySpeedY * -1

    if policeDogX > 950 or policeDogX < 50 and policeDogX != 1000:
        policeDogSpeedX = policeDogSpeedX * -1
        
        
    elif policeDogY > 670 or policeDogY < 50:
        policeDogY = policeDogSpeedY * -1

    if policeX > 950 or policeX < 50 and policeX != 1000:
        policeSpeedX = policeSpeedX * -1
        
        
    elif policeY > 650 or judgeY < 50:
        policeSpeedY = policeSpeedY * -1

    
    screen.blit(background_image, [0, 0])
    screen.blit(robber, (robber_x, robber_y))
    screen.blit(detective, (detectX, detectY))
    screen.blit(judge, (judgeX, judgeY))
    screen.blit(money, (moneyX, moneyY))
    screen.blit(policeDog, (policeDogX, policeDogY))
    screen.blit(police, (policeX, policeY))

    

    pygame.image.tostring

    pygame.display.flip()

pygame.quit()
print("This game was played for {0:.2f} seconds".format(playtime))

    
    
