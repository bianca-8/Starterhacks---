# imports
import pygame
import random

# constants
GRID = 80
WIDTH = 1280
HEIGHT = 780

# variables
stick1 = 0 # amount of sticks player 1 has
stick2 = 0 # amount of sticks player 2 has
fences = [] # list of fence positions
charStep = 400  # character steps

# initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

# initialize positions
pos = pygame.Vector2(WIDTH / 2 - 120, HEIGHT / 2 + 50)
pos2 = pygame.Vector2(WIDTH / 2 + 120, HEIGHT / 2 + 50)
gooseRandx = random.randint(0, WIDTH // GRID - 1)
gooseRandy = random.randint(0, HEIGHT // GRID - 1)
goosePos = pygame.Vector2(gooseRandx * GRID + GRID // 2, gooseRandy * GRID + GRID // 2)

# random stick positions
randx = random.randint(0, WIDTH // GRID - 1)
randy = random.randint(0, HEIGHT // GRID - 1)

randx1 = random.randint(0, WIDTH // GRID - 1)
randy1 = random.randint(0, HEIGHT // GRID - 1)

randx2 = random.randint(0, WIDTH // GRID - 1)
randy2 = random.randint(0, HEIGHT // GRID - 1)

randx3 = random.randint(0, WIDTH // GRID - 1)
randy3 = random.randint(0, HEIGHT // GRID - 1)

# Snap fence to the nearest grid
def snapToGrid(pos):
    x = round(pos.x / GRID) * GRID + GRID // 2
    y = round(pos.y / GRID) * GRID
    return pygame.Vector2(x, y)

# character collision with sticks
def collideStick(posx, posy, stick, amount):
    global randx, randy, randx1, randy1, randx2, randy2, randx3, randy3

    if stick == 0 and (posx > randx * GRID and posx < randx * GRID + GRID) and (posy > randy * GRID and posy < randy * GRID + GRID):
        randx, randy = random.randint(0, WIDTH // GRID - 1), random.randint(0, HEIGHT // GRID - 1)
        amount += 1 # + 1 to sticks that the player has
    elif stick == 1 and (posx > randx1 * GRID and posx < randx1 * GRID + GRID) and (posy > randy1 * GRID and posy < randy1 * GRID + GRID):
        randx1, randy1 = random.randint(0, WIDTH // GRID - 1), random.randint(0, HEIGHT // GRID - 1)
        amount += 1 # + 1 to sticks that the player has
    elif stick == 2 and (posx > randx2 * GRID and posx < randx2 * GRID + GRID) and (posy > randy2 * GRID and posy < randy2 * GRID + GRID):
        randx2, randy2 = random.randint(0, WIDTH // GRID - 1), random.randint(0, HEIGHT // GRID - 1)
        amount += 1 # + 1 to sticks that the player has
    elif stick == 3 and (posx > randx3 * GRID and posx < randx3 * GRID + GRID) and (posy > randy3 * GRID and posy < randy3 * GRID + GRID):
        randx3, randy3 = random.randint(0, WIDTH // GRID - 1), random.randint(0, HEIGHT // GRID - 1)
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

# initialize time for goose movement
gooseLastMoveTime = pygame.time.get_ticks()
moveInterval = 1000  # milliseconds (1.5 seconds)

# main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color
    screen.fill("white")

    # draw background grid - DELETE AFTER
    for i in range(0, WIDTH, GRID):
        for j in range(0, HEIGHT, GRID):
            pygame.draw.rect(screen, "black", (i, j, GRID, GRID), 5)

    # draw sticks
    pygame.draw.line(screen, "black", (randx * GRID, randy * GRID), (randx * GRID + GRID, randy * GRID + GRID), 5)
    pygame.draw.line(screen, "black", (randx1 * GRID, randy1 * GRID), (randx1 * GRID + GRID, randy1 * GRID + GRID), 5)
    pygame.draw.line(screen, "black", (randx2 * GRID, randy2 * GRID), (randx2 * GRID + GRID, randy2 * GRID + GRID), 5)
    pygame.draw.line(screen, "black", (randx3 * GRID, randy3 * GRID), (randx3 * GRID + GRID, randy3 * GRID + GRID), 5)

    # character movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and pos.y - charStep * dt > 0:
        pos.y -= charStep * dt
    elif keys[pygame.K_s] and pos.y + charStep * dt < HEIGHT:
        pos.y += charStep * dt
    elif keys[pygame.K_a] and pos.x - charStep * dt > 0:
        pos.x -= charStep * dt
    elif keys[pygame.K_d] and pos.x + charStep * dt < WIDTH:
        pos.x += charStep * dt

    if keys[pygame.K_UP] and pos2.y - charStep * dt > 0:
        pos2.y -= charStep * dt
    elif keys[pygame.K_DOWN] and pos2.y + charStep * dt < HEIGHT:
        pos2.y += charStep * dt
    elif keys[pygame.K_LEFT] and pos2.x - charStep * dt > 0:
        pos2.x -= charStep * dt
    elif keys[pygame.K_RIGHT] and pos2.x + charStep * dt < WIDTH:
        pos2.x += charStep * dt

    # check character collisions with sticks
    for i in range(4):
        stick1 = collideStick(pos.x, pos.y, i, stick1)
        stick2 = collideStick(pos2.x, pos2.y, i, stick2)

    # draw characters
    pygame.draw.circle(screen, "red", pos, 40)
    pygame.draw.circle(screen, "blue", pos2, 40)

    # draw fences
    print(stick1, stick2)
    if keys[pygame.K_f] and stick1 > 0:
        fencePos = snapToGrid(pos)
        end_pos = snapToGrid(pos + pygame.Vector2(0, -80))  # character 1 fence
        fences.append((fencePos.x, fencePos.y, end_pos.x, end_pos.y))
        stick1 -= 1

    if keys[pygame.K_SPACE] and stick2 > 0:
        fencePos = snapToGrid(pos2)
        end_pos = snapToGrid(pos2 + pygame.Vector2(0, -80))  # character 2 fence
        fences.append((fencePos.x, fencePos.y, end_pos.x, end_pos.y))
        stick2 -= 1
    
    for fence in fences:
        pygame.draw.line(screen, "black", (fence[0], fence[1]), (fence[2], fence[3]), 5)

     # update goose position
    currentTime = pygame.time.get_ticks()
    if currentTime - gooseLastMoveTime > moveInterval:
        gooseLastMoveTime = currentTime
        gooseMove = 80
        gooseDirec = random.randint(0, 3)
        
        if gooseDirec == 0:  # up
            newY = goosePos.y - gooseMove
            if newY > 0:  # check if new Y position is within bounds
                goosePos.y = newY
        elif gooseDirec == 1:  # down
            newY = goosePos.y + gooseMove
            if newY < HEIGHT:  # check if new Y position is within bounds
                goosePos.y = newY
        elif gooseDirec == 2:  # left
            newX = goosePos.x - gooseMove
            if newX > 0:  # check if new X position is within bounds
                goosePos.x = newX
        elif gooseDirec == 3:  # right
            newX = goosePos.x + gooseMove
            if newX < WIDTH:  # check if new X position is within bounds
                goosePos.x = newX

    # draw goose
    pygame.draw.circle(screen, "green", goosePos, 40)

    # update display
    pygame.display.flip()

    # limit FPS
    dt = clock.tick(60) / 1000

pygame.quit()
