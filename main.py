# imports
import pygame
import random

# variables
stick1 = 0 # amount of sticks player 1 has
stick2 = 0 # amount of sticks player 2 has

# initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1280, 780))
clock = pygame.time.Clock()
running = True
dt = 0

# initialize positions
pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
pos2 = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# random stick positions
randx = random.randint(0, 15)
randy = random.randint(0, 9)

randx1 = random.randint(0, 15)
randy1 = random.randint(0, 9)

randx2 = random.randint(0, 15)
randy2 = random.randint(0, 9)

randx3 = random.randint(0, 15)
randy3 = random.randint(0, 9)

# character collision with sticks
def collideStick(posx, posy, stick, amount):
    global randx, randy, randx1, randy1, randx2, randy2, randx3, randy3

    if stick == 0 and (posx > randx * 80 and posx < randx * 80 + 80) and (posy > randy * 80 and posy < randy * 80 + 80):
        randx, randy = random.randint(0, 15), random.randint(0, 9)
        amount += 1 # + 1 to sticks that the player has
    elif stick == 1 and (posx > randx1 * 80 and posx < randx1 * 80 + 80) and (posy > randy1 * 80 and posy < randy1 * 80 + 80):
        randx1, randy1 = random.randint(0, 15), random.randint(0, 9)
        amount += 1 # + 1 to sticks that the player has
    elif stick == 2 and (posx > randx2 * 80 and posx < randx2 * 80 + 80) and (posy > randy2 * 80 and posy < randy2 * 80 + 80):
        randx2, randy2 = random.randint(0, 15), random.randint(0, 9)
        amount += 1 # + 1 to sticks that the player has
    elif stick == 3 and (posx > randx3 * 80 and posx < randx3 * 80 + 80) and (posy > randy3 * 80 and posy < randy3 * 80 + 80):
        randx3, randy3 = random.randint(0, 15), random.randint(0, 9)
        amount += 1 # + 1 to sticks that the player has

    return amount
    
#create character sprite
class CharacterMale(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        '''self.image = pygame.image.load() <-- when we get the image
       self.rect = self.image.get_rect()
       self.rect.topleft = (x, y)
       self.mask = pygame.mask.from_surface(self.image)'''
        
#create goose sprite
class Goose(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        '''self.image = pygame.image.load() <-- when we get the image
       self.rect = self.image.get_rect()
       self.rect.topleft = (x, y)
       self.mask = pygame.mask.from_surface(self.image)'''

# main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color
    screen.fill("white")

    # draw background grid - DELETE AFTER
    for i in range(0, 1280, 80):
        for j in range(0, 780, 80):
            pygame.draw.rect(screen, "black", (i, j, 80, 80), 5)

    # draw sticks
    pygame.draw.line(screen, "black", (randx * 80, randy * 80), (randx * 80 + 80, randy * 80 + 80), 5)
    pygame.draw.line(screen, "black", (randx1 * 80, randy1 * 80), (randx1 * 80 + 80, randy1 * 80 + 80), 5)
    pygame.draw.line(screen, "black", (randx2 * 80, randy2 * 80), (randx2 * 80 + 80, randy2 * 80 + 80), 5)
    pygame.draw.line(screen, "black", (randx3 * 80, randy3 * 80), (randx3 * 80 + 80, randy3 * 80 + 80), 5)

    # character movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and pos.y - 300 * dt > 0:
        pos.y -= 300 * dt
    if keys[pygame.K_s] and pos.y + 300 * dt < 780:
        pos.y += 300 * dt
    if keys[pygame.K_a] and pos.x - 300 * dt > 0:
        pos.x -= 300 * dt
    if keys[pygame.K_d] and pos.x + 300 * dt < 1280:
        pos.x += 300 * dt

    if keys[pygame.K_UP] and pos2.y - 300 * dt > 0:
        pos2.y -= 300 * dt
    if keys[pygame.K_DOWN] and pos2.y + 300 * dt < 780:
        pos2.y += 300 * dt
    if keys[pygame.K_LEFT] and pos2.x - 300 * dt > 0:
        pos2.x -= 300 * dt
    if keys[pygame.K_RIGHT] and pos2.x + 300 * dt < 1280:
        pos2.x += 300 * dt

    # check character collisions with sticks
    for i in range(4):
        stick1 = collideStick(pos.x, pos.y, i, stick1)
        stick2 = collideStick(pos2.x, pos2.y, i, stick2)

    # draw characters
    pygame.draw.circle(screen, "red", pos, 40)
    pygame.draw.circle(screen, "blue", pos2, 40)
    if keys[pygame.K_f]: # planting fence
        pygame.draw.line(screen, "black", (pos.x, pos.y - 40), (pos.x, pos.y + 40), 5)
    if keys[pygame.K_SPACE]: # planting fence
        pygame.draw.line(screen, "black", (pos2.x, pos2.y-40), (pos2.x, pos2.y + 40), 5)

    # goose
    #pygame.draw.circle(screen, "red", pos, 40)
    #random.randint(0, 15)

    # update display
    pygame.display.flip()

    # limit FPS
    dt = clock.tick(60) / 1000

pygame.quit()
