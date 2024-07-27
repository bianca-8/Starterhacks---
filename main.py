import pygame
import random

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
def collideStick(posx, posy, stick):
    global randx, randy, randx1, randy1, randx2, randy2, randx3, randy3

    if stick == 0 and (posx > randx * 80 and posx < randx * 80 + 80) and (posy > randy * 80 and posy < randy * 80 + 80):
        randx, randy = random.randint(0, 15), random.randint(0, 9)
    elif stick == 1 and (posx > randx1 * 80 and posx < randx1 * 80 + 80) and (posy > randy1 * 80 and posy < randy1 * 80 + 80):
        randx1, randy1 = random.randint(0, 15), random.randint(0, 9)
    elif stick == 2 and (posx > randx2 * 80 and posx < randx2 * 80 + 80) and (posy > randy2 * 80 and posy < randy2 * 80 + 80):
        randx2, randy2 = random.randint(0, 15), random.randint(0, 9)
    elif stick == 3 and (posx > randx3 * 80 and posx < randx3 * 80 + 80) and (posy > randy3 * 80 and posy < randy3 * 80 + 80):
        randx3, randy3 = random.randint(0, 15), random.randint(0, 9)

# main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color
    screen.fill("green")

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
    if keys[pygame.K_w]:
        pos.y -= 300 * dt
    if keys[pygame.K_s]:
        pos.y += 300 * dt
    if keys[pygame.K_a]:
        pos.x -= 300 * dt
    if keys[pygame.K_d]:
        pos.x += 300 * dt

    if keys[pygame.K_UP]:
        pos2.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        pos2.y += 300 * dt
    if keys[pygame.K_LEFT]:
        pos2.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        pos2.x += 300 * dt

    # check character collisions with sticks
    collideStick(pos.x, pos.y, 0)
    collideStick(pos.x, pos.y, 1)
    collideStick(pos.x, pos.y, 2)
    collideStick(pos.x, pos.y, 3)
    collideStick(pos2.x, pos2.y, 0)
    collideStick(pos2.x, pos2.y, 1)
    collideStick(pos2.x, pos2.y, 2)
    collideStick(pos2.x, pos2.y, 3)

    # draw characters
    pygame.draw.circle(screen, "red", pos, 40)
    pygame.draw.circle(screen, "blue", pos2, 40)

    # update display
    pygame.display.flip()

    # limit FPS
    dt = clock.tick(60) / 1000

pygame.quit()
