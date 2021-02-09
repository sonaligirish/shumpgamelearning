# Pygame template - skeleton for a new pygame project
import pygame
import random
import os

WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#setup assests folders
game_folder = os.path.dirname(__file__)
img_folder = os.path(.join(game_folder, "IMG")

class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       #self.image = pygame.image.load(os.path.join(img_folder, "Platformer Art Complete Pack\Extra animations and enemies\Alien sprites","alienGreen_jump.png")).convert()
       self.image = pygame.Surface((50,40))
       self.image.fill(GREEN)
       self.rect = self.image.get_rect()
       #self.rect.center = (WIDTH / 2, HEIGHT / 2)
       self.rect.center = (WIDTH / 2, HEIGHT-30)
       #self.y_speed = 5

    def update(self):
        '''
        self.rect.x +=5
        self.rect.y += self.y_speed
        if self.rect.bottom > HEIGHT - 200:
            self .y_speed = -5
        if self.rect.top < 200:
            self.y_speed = 5
        if self.rect.left > WIDTH:
            self.rect.right = 0
        '''
        pass
# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

class Mob (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.speedy = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
mobs = pygame.sprite.Group()
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

# Game loope
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything,flip the display
    pygame.display.flip()

pygame.quit()
