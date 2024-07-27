# imports
import pygame
import random

#colors


# set up
pygame.init()
screen = pygame.display.set_mode((1280, 780))
clock = pygame.time.Clock()
running = True
dt = 0

pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
pos2 = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# stick positions
randx = random.randint(0, 15)
randy = random.randint(0, 9)

randx1 = random.randint(0, 15)
randy1 = random.randint(0, 9)

randx2 = random.randint(0, 15)
randy2 = random.randint(0, 9)

randx3 = random.randint(0, 15)
randy3 = random.randint(0, 9)

#create goose sprite
class Goose(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        '''self.image = pygame.image.load() <-- when we get the image
       self.rect = self.image.get_rect()
       self.rect.topleft = (x, y)
       self.mask = pygame.mask.from_surface(self.image)'''

while running:
    # user didn't press quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("green")
    """
    bg = pygame.image.load("background.png")
    bg = pygame.transform.scale(bg, (1280, 800))
    screen.blit(bg, (0, 0))
    """
    # background guidelines - delete after
    for i in range(0, 1280, 80):
        for j in range(0, 780, 80):
            pygame.draw.rect(screen, "black", (i, j, 80, 80), 5)

    # sticks
    pygame.draw.line(screen, "black", (randx * 80,randy * 80), (randx * 80 + 80,randy * 80 + 80), 5)
    pygame.draw.line(screen, "black", (randx1 * 80,randy1 * 80), (randx1 * 80 + 80,randy1 * 80 + 80), 5)
    pygame.draw.line(screen, "black", (randx2 * 80,randy2 * 80), (randx2 * 80 + 80,randy2 * 80 + 80), 5)
    pygame.draw.line(screen, "black", (randx3 * 80,randy3 * 80), (randx3 * 80 + 80,randy3 * 80 + 80), 5)

    # character 1 moving
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        pos.y -= 300 * dt
    if keys[pygame.K_s]:
        pos.y += 300 * dt
    if keys[pygame.K_a]:
        pos.x -= 300 * dt
    if keys[pygame.K_d]:
        pos.x += 300 * dt
    # character 2 moving
    if keys[pygame.K_UP]:
        pos2.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        pos2.y += 300 * dt
    if keys[pygame.K_LEFT]:
        pos2.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        pos2.x += 300 * dt
    
    # character 1 collide with stick 0
    if (pos.x > randx * 80 and pos.x < randx * 80 + 80) and (pos.y > randy * 80 and pos.y < randy * 80 + 80):
        pygame.draw.rect(screen, "black", (randx * 80, randy * 80, 80, 80), 5) # REPLACE WITH BG OF THAT SQUARE
        randx = random.randint(0, 15)
        randy = random.randint(0, 9)
        if (randx == randx1 or randx == randx2 or randx == randx3):
            randx = random.randint(0, 15)
        if (randy == randy1 or randy == randy2 or randy == randy3):
            randy = random.randint(0, 9)
    # character 1 collide with stick 1
    if (pos.x > randx1 * 80 and pos.x < randx1 * 80 + 80) and (pos.y > randy1 * 80 and pos.y < randy1 * 80 + 80):
        pygame.draw.rect(screen, "black", (randx1 * 80, randy1 * 80, 80, 80), 5) # REPLACE WITH BG OF THAT SQUARE
        randx1 = random.randint(0, 15)
        randy1 = random.randint(0, 9)
        if (randx1 == randx or randx1 == randx2 or randx1 == randx3):
            randx1 = random.randint(0, 15)
        if (randy1 == randy or randy1 == randy2 or randy1 == randy3):
            randy1 = random.randint(0, 9)
    # character 1 collide with stick 2
    if (pos.x > randx2 * 80 and pos.x < randx2 * 80 + 80) and (pos.y > randy2 * 80 and pos.y < randy2 * 80 + 80):
        pygame.draw.rect(screen, "black", (randx2 * 80, randy2 * 80, 80, 80), 5) # REPLACE WITH BG OF THAT SQUARE
        randx2 = random.randint(0, 15)
        randy2 = random.randint(0, 9)
        if (randx2 == randx or randx2 == randx1 or randx2 == randx3):
            randx2 = random.randint(0, 15)
        if (randy2 == randy or randy2 == randy1 or randy2 == randy3):
            randy2 = random.randint(0, 9)
    # character 1 collide with stick 3
    if (pos.x > randx3 * 80 and pos.x < randx3 * 80 + 80) and (pos.y > randy3 * 80 and pos.y < randy3 * 80 + 80):
        pygame.draw.rect(screen, "black", (randx3 * 80, randy3 * 80, 80, 80), 5) # REPLACE WITH BG OF THAT SQUARE
        randx3 = random.randint(0, 15)
        randy3 = random.randint(0, 9)
        if (randx3 == randx or randx3 == randx1 or randx3 == randx2):
            randx3 = random.randint(0, 15)
        if (randy3 == randy or randy3 == randy1 or randy3 == randy2):
            randy3 = random.randint(0, 9)
    
    # characters
    pygame.draw.circle(screen, "red", pos, 40)
    pygame.draw.circle(screen, "blue", pos2, 40)

    # display on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()