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

class Player(object):
    def __init__(self):
        self.robber= pygame.image.load("robber.PNG")
        self.robber_x = 30
        self.robber_y = 30
        self.robberSpeedX = 10
        self.robberSpeedY = 10
  

    def keys(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: robber_y -= robberSpeedY
        if pressed[pygame.K_DOWN]: robber_y += robberSpeedY
        if pressed[pygame.K_LEFT]: robber_x -= robberSpeedX
        if pressed[pygame.K_RIGHT]: robber_x += robberSpeedX

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

class Avoid(object):
    def __init__(self):
        self.detective= pygame.image.load("detective.png")
        self.judge= pygame.image.load("judge.png")
        self.money= pygame.image.load("money.png")
        self.policeDog= pygame.image.load("policeDog.png")
        self.police= pygame.image.load("police.png")


        self.detectX = 30
        self.detectY = 200
        self.judgeX = 400
        self.judgeY = 500
        self.moneyX = 850
        self.moneyY = 650
        self.policeDogX = 240
        self.policeDogY = 650
        self.policeX = 240
        self.policeY = 550

        self.detectSpeedX, detectSpeedY = 7, 7
        self.judgeSpeedX, judgeSpeedY = 7, 7
        self.moneySpeedX, moneySpeedY = 10, 10
        self.policeDogSpeedX, policeDogSpeedY = 7, 7
        self.policeSpeedX, policeSpeedY = 7, 7

    def object_draw(self, surface):
        screen.blit(self.detective, (self.detectX, self.detectY))
        screen.blit(self.judge, (self.judgeX, self.judgeY))
        screen.blit(self.money, (self.moneyX, self.moneyY))
        screen.blit(self.policeDog, (self.policeDogX, self.policeDogY))
        screen.blit(self.police, (self.policeX, self.policeY))

    def checkCollision(self, robber, detective, judge, money, policeDog, police):
        col = pygame.sprite.collide_rect(robber, detective)
        col = pygame.sprite.collide_rect(robber, judge)
        col = pygame.sprite.collide_rect(robber, money)
        col = pygame.sprite.collide_rect(robber, policeDog)
        col = pygame.sprite.collide_rect(robber, police)
        if col == True:
            sys.exit()
            
# initialize game engine
pygame.init()

window_width=1000
window_height=700

animation_increment=10

# Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

player = Player()
avoid1 = Avoid()


clock = pygame.time.Clock()
mainloop = True            
FPS = 30
playtime = 0.0
background_image = pygame.image.load("pastelBackground.png").convert()

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

    player.keys()
    avoid1.__init__()
    player.draw(screen)
    avoid.object_draw(screen)
    pygame.display.update()
    


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

    if detectX > 970 or detectX < 30 and detectX != 1000:
        detectSpeedX = detectSpeedX * -1
        
        
    elif detectY > 670 or detectY < 30:
        detectSpeedY = detectSpeedY * -1

    if judgeX > 970 or judgeX < 30 and judgeX != 1000:
        judgeSpeedX = judgeSpeedX * -1
        
        
    elif judgeY > 670 or judgeY < 30:
        judgeSpeedY = judgeSpeedY * -1

    if moneyX > 970 or moneyX < 30 and moneyX != 1000:
        moneySpeedX = moneySpeedX * -1
        
        
    elif moneyY > 670 or moneyY < 30:
        moneySpeedY = moneySpeedY * -1

    if policeDogX > 970 or policeDogX < 30 and policeDogX != 1000:
        policeDogSpeedX = policeDogSpeedX * -1
        
        
    elif policeDogY > 670 or policeDogY < 0:
        policeDogY = policeDogSpeedY * -1

    if policeX > 970 or policeX < -1 and policeX != 1000:
        policeSpeedX = policeSpeedX * -1
        
        
    elif policeY > 670 or judgeY < 0:
        policeSpeedY = policeSpeedY * -1

    if robber.Rect.colliderect(money):
        pygame.quit()

    
    screen.blit(background_image, [0, 0])
    screen.blit(robber, (robber_x, robber_y))

    

    pygame.image.tostring

    pygame.display.flip()

pygame.quit()
print("This game was played for {0:.2f} seconds".format(playtime))

    
    
