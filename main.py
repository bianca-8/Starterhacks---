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
    
    # character 1 collide with stick
    if (pos.x > randx * 80 and pos.x < randx * 80 + 80) and (pos.y > randy * 80 and pos.y < randy * 80 + 80):
        pygame.draw.rect(screen, "black", (randx * 80, randy * 80, 80, 80), 5)
        randx = random.randint(0, 15)
        randy = random.randint(0, 9)
        if (randx == randx1 or randx == randx2 or randx == randx3):
            randx = random.randint(0, 15)
        if (randy == randy1 or randy == randy2 or randy == randy3):
            randy = random.randint(0, 9)
        print(randx, randy)
    
    # characters
    pygame.draw.circle(screen, "red", pos, 40)
    pygame.draw.circle(screen, "blue", pos2, 40)

    # display on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()