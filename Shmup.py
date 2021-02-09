# Pygame template - skeleton for a new pygame project
# Frozen Jam by tgfcoder <https://twitter.com/tgfcoder> licensed under CC-BY-3
# Art from Kenny.nl
import pygame
import random
import os

img_dir = os.path.join(os.path.dirname(__file__), 'PNG')
snd_dir = os.path.join(os.path.dirname(__file__), 'snd')
WIDTH = 400
HEIGHT = 600
FPS = 30

# define colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255,0)
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "PNG")

class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       #self.image = pygame.image.load(os.path.join(img_folder, "Platformer Art Complete Pack\Extra animations and enemies\Alien sprites","alienGreen_jump.png")).convert()
       self.image = pygame.transform.scale(player_img, (50, 38))
       self.image.set_colorkey(BLACK)
       self.rect = self.image.get_rect()
       self.radius = 20
       # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
       self.rect.center = (WIDTH / 2, HEIGHT - 10)
       self.y_speed = 5
       self.speedx = 0
       self.shield = 100

    def update(self):

        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        shoot_sound.play()
        shoot_sound.set_volume(0.4)

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

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(meteor_images)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85  / 2)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.y = random.randrange(-150, -100)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()

# initialize pygame and create window
pygame.init()
pygame.mixer.init(44100,16,2,4096)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 100)
    BAR_HEIGHT = 10
    fill = (pct / 100)* BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect,2)

# Load all game graphics
background = pygame.image.load(os.path.join(img_folder, "Backgrounds/back.png"))
background = pygame.transform.scale(background, (WIDTH, HEIGHT)).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(os.path.join(img_dir, "playerShip1_orange.png")).convert()
bullet_img = pygame.image.load(os.path.join(img_dir, "lasers/laserRed16.png")).convert()
meteor_images = []
meteor_list = ['meteorBrown_big1.png', 'meteorBrown_big2.png', 'meteorBrown_med1.png',
               'meteorBrown_med1.png', 'meteorBrown_small1.png', 'meteorBrown_small2.png',
               'meteorBrown_tiny1.png']
for img in meteor_list:
    meteor_images.append(pygame.image.load(os.path.join(img_dir, "Meteors/"+img)).convert())
# Load all game sounds
shoot_sound = pygame.mixer.Sound(os.path.join(snd_dir, 'Laser.wav'))
expl_sounds = []
for snd in ['exl3.wav', 'exl16.wav']:
    expl_sounds.append(pygame.mixer.Sound(os.path.join(snd_dir, snd)))
    background_music = pygame.mixer.music.load(os.path.join(snd_dir, 'tgfcoder-FrozenJam-SeamlessLoop.mp3'))
    pygame.mixer.music.set_volume(0.9)

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    newmob()

score = 0
pygame.mixer.music.play(loops=-1)
# Game loope
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # process input
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Update
    all_sprites.update()

    #check to see if a bullet hit the mob
    hits =pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        score  += 50 - hit.radius
        random.choice(expl_sounds).play()
        newmob()

    #check to see if a mob hit the player
    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    for hit in hits:
        player.shield -= hit.radius * 2
        newmob()
        if player.shield <= 0:
            running = False

    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH / 2, 10)
    draw_shield_bar (screen, 5, 5, player.shield)
    # *after* drawing everything,flip the display
    pygame.display.flip()

pygame.quit()