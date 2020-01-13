import pygame
 
# Global constants
 
# Colors
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
PINK = (255,192,203)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
 
 
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
        controls. """
 
  
    def __init__(self):
    
 
        super().__init__()
 
        # Create an image of the block
        width = 40
        height = 60
        self.image = pygame.Surface([width, height])
        self.image.fill(PINK)
 
        # Set a referance to the image rect
        self.rect = self.image.get_rect()
 
        # Set speed
        self.change_x = 0
        self.change_y = 0
 
        self.level = None
 
    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
 
        # Move left/right
        self.rect.x += self.change_x
 
        # when we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # If we are moving left, do the opposite.
                self.rect.left = block.rect.right
 

        self.rect.y += self.change_y
 
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
 
    def calc_grav(self):

        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
 
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
 
    def jump(self):
 
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
 
    
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10
 
    def go_left(self):
        self.change_x = -6
 
    def go_right(self):
        self.change_x = 6
 
    def stop(self):
        self.change_x = 0
 
 
class Platform(pygame.sprite.Sprite):
 
    def __init__(self, width, height):

        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(ORANGE)
 
        self.rect = self.image.get_rect()
 
 
class Level(object):
 
    def __init__(self, player):
        
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
         
        # Background image
        self.background = None
 
    def update(self):
        self.platform_list.update()
        self.enemy_list.update()
 
    def draw(self, screen):

 
        # Draw the background
        screen.fill(BLACK)
 
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
 
 
class Level_01(Level):
 
    def __init__(self, player):
 
        Level.__init__(self, player)
 
        level = [[50, 50, 50, 500],
                 [50, 50, 250, 450],
                 [50, 50, 450, 350],
                 [50, 50, 230, 250],
                 [50, 50, 500, 100]
                 ]
 

        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
 
 
def main():
    pygame.init()
 
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("DAYOUNG KIM")
 
    player = Player()
 
    level_list = []
    level_list.append( Level_01(player) )
 
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
 
    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)
 
    done = False
 
    clock = pygame.time.Clock()
 
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
 
        active_sprite_list.update()
 
        current_level.update()
 
        if player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH
 
        if player.rect.left < 0:
            player.rect.left = 0

        current_level.draw(screen)
        active_sprite_list.draw(screen)
        clock.tick(60)
        pygame.display.flip()
 

    pygame.quit()
 
if __name__ == "__main__":
    main()
