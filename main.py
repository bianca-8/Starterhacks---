import pygame
import random

# Variables
stick1 = 0  # Amount of sticks player 1 has
stick2 = 0  # Amount of sticks player 2 has
fences = []  # List of fence positions

# Constants
GRID_SIZE = 80
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 780

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

# Initialize positions
pos = pygame.Vector2(SCREEN_WIDTH / 2 - 120, SCREEN_HEIGHT / 2 + 50)
pos2 = pygame.Vector2(SCREEN_WIDTH / 2 + 120, SCREEN_HEIGHT / 2 + 50)
goosePos = pygame.Vector2(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))

# Random stick positions
randx = random.randint(0, SCREEN_WIDTH // GRID_SIZE - 1)
randy = random.randint(0, SCREEN_HEIGHT // GRID_SIZE - 1)

randx1 = random.randint(0, SCREEN_WIDTH // GRID_SIZE - 1)
randy1 = random.randint(0, SCREEN_HEIGHT // GRID_SIZE - 1)

randx2 = random.randint(0, SCREEN_WIDTH // GRID_SIZE - 1)
randy2 = random.randint(0, SCREEN_HEIGHT // GRID_SIZE - 1)

randx3 = random.randint(0, SCREEN_WIDTH // GRID_SIZE - 1)
randy3 = random.randint(0, SCREEN_HEIGHT // GRID_SIZE - 1)

# Function to snap to the nearest grid
def snap_to_grid(pos):
    """ Snaps a position to the nearest grid line. """
    x = round(pos.x / GRID_SIZE) * GRID_SIZE
    y = round(pos.y / GRID_SIZE) * GRID_SIZE
    return pygame.Vector2(x, y)

# Function to handle collision with sticks
def collideStick(posx, posy, stick, amount):
    global randx, randy, randx1, randy1, randx2, randy2, randx3, randy3

    if stick == 0 and (posx > randx * GRID_SIZE and posx < randx * GRID_SIZE + GRID_SIZE) and (posy > randy * GRID_SIZE and posy < randy * GRID_SIZE + GRID_SIZE):
        randx, randy = random.randint(0, SCREEN_WIDTH // GRID_SIZE - 1), random.randint(0, SCREEN_HEIGHT // GRID_SIZE - 1)
        amount += 1  # + 1 to sticks that the player has
    elif stick == 1 and (posx > randx1 * GRID_SIZE and posx < randx1 * GRID_SIZE + GRID_SIZE) and (posy > randy1 * GRID_SIZE and posy < randy1 * GRID_SIZE + GRID_SIZE):
        randx1, randy1 = random.randint(0, SCREEN_WIDTH // GRID_SIZE - 1), random.randint(0, SCREEN_HEIGHT // GRID_SIZE - 1)
        amount += 1  # + 1 to sticks that the player has
    elif stick == 2 and (posx > randx2 * GRID_SIZE and posx < randx2 * GRID_SIZE + GRID_SIZE) and (posy > randy2 * GRID_SIZE and posy < randy2 * GRID_SIZE + GRID_SIZE):
        randx2, randy2 = random.randint(0, SCREEN_WIDTH // GRID_SIZE - 1), random.randint(0, SCREEN_HEIGHT // GRID_SIZE - 1)
        amount += 1  # + 1 to sticks that the player has
    elif stick == 3 and (posx > randx3 * GRID_SIZE and posx < randx3 * GRID_SIZE + GRID_SIZE) and (posy > randy3 * GRID_SIZE and posy < randy3 * GRID_SIZE + GRID_SIZE):
        randx3, randy3 = random.randint(0, SCREEN_WIDTH // GRID_SIZE - 1), random.randint(0, SCREEN_HEIGHT // GRID_SIZE - 1)
        amount += 1  # + 1 to sticks that the player has

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
       self.images_right = []
       self.index = 0
       self.counter = 0
       for i in range(1, 4): #adds the images to a list with a loop for the animation
           img_right = pygame.image.load(f'realSprite/Goose{i}.png')
           img_right = pygame.transform.scale(img_right, (100, 60))
           self.images_right.append(img_right)
           
       self.images = self.images_right[self.index]
       self.rect = self.images.get_rect()
       self.rect.x = x
       self.rect.y = y
       self.rect.topleft = (x, y)
       self.mask = pygame.mask.from_surface(self.images)

    def update(self):
        screen.blit(self.images, self.rect)

# Initialize time for goose movement
gooseLastMoveTime = pygame.time.get_ticks()
moveInterval = 1500  # milliseconds (1.5 seconds)
goose = Goose(100, 100)
# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color
    screen.fill("white")

    # Draw background grid
    for i in range(0, SCREEN_WIDTH, GRID_SIZE):
        for j in range(0, SCREEN_HEIGHT, GRID_SIZE):
            pygame.draw.rect(screen, "black", (i, j, GRID_SIZE, GRID_SIZE), 5)

    # Draw sticks
    pygame.draw.line(screen, "black", (randx * GRID_SIZE, randy * GRID_SIZE), (randx * GRID_SIZE + GRID_SIZE, randy * GRID_SIZE + GRID_SIZE), 5)
    pygame.draw.line(screen, "black", (randx1 * GRID_SIZE, randy1 * GRID_SIZE), (randx1 * GRID_SIZE + GRID_SIZE, randy1 * GRID_SIZE + GRID_SIZE), 5)
    pygame.draw.line(screen, "black", (randx2 * GRID_SIZE, randy2 * GRID_SIZE), (randx2 * GRID_SIZE + GRID_SIZE, randy2 * GRID_SIZE + GRID_SIZE), 5)
    pygame.draw.line(screen, "black", (randx3 * GRID_SIZE, randy3 * GRID_SIZE), (randx3 * GRID_SIZE + GRID_SIZE, randy3 * GRID_SIZE + GRID_SIZE), 5)

    # Character movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and pos.y - 300 * dt > 0:
        pos.y -= 300 * dt
    if keys[pygame.K_s] and pos.y + 300 * dt < SCREEN_HEIGHT:
        pos.y += 300 * dt
    if keys[pygame.K_a] and pos.x - 300 * dt > 0:
        pos.x -= 300 * dt
    if keys[pygame.K_d] and pos.x + 300 * dt < SCREEN_WIDTH:
        pos.x += 300 * dt

    if keys[pygame.K_UP] and pos2.y - 300 * dt > 0:
        pos2.y -= 300 * dt
    if keys[pygame.K_DOWN] and pos2.y + 300 * dt < SCREEN_HEIGHT:
        pos2.y += 300 * dt
    if keys[pygame.K_LEFT] and pos2.x - 300 * dt > 0:
        pos2.x -= 300 * dt
    if keys[pygame.K_RIGHT] and pos2.x + 300 * dt < SCREEN_WIDTH:
        pos2.x += 300 * dt

    # Check character collisions with sticks
    for i in range(4):
        stick1 = collideStick(pos.x, pos.y, i, stick1)
        stick2 = collideStick(pos2.x, pos2.y, i, stick2)

    # Draw characters
    pygame.draw.circle(screen, "red", pos, 40)
    pygame.draw.circle(screen, "blue", pos2, 40)

    # Draw fences
    if keys[pygame.K_f] and stick1 > 0:
        start_pos = snap_to_grid(pos)
        end_pos = snap_to_grid(pos + pygame.Vector2(0, -80))  # Fence for character 1
        fences.append((start_pos.x, start_pos.y, end_pos.x, end_pos.y))
        stick1 -= 1
    if keys[pygame.K_SPACE] and stick2 > 0:
        start_pos = snap_to_grid(pos2)
        end_pos = snap_to_grid(pos2 + pygame.Vector2(0, -80))  # Fence for character 2
        fences.append((start_pos.x, start_pos.y, end_pos.x, end_pos.y))
        stick2 -= 1

    # Draw fences
    for fence in fences:
        pygame.draw.line(screen, "black", (fence[0], fence[1]), (fence[2], fence[3]), 5)

    # Update goose position
    currentTime = pygame.time.get_ticks()
    if currentTime - gooseLastMoveTime > moveInterval:
        gooseLastMoveTime = currentTime
        gooseMoveX = random.randint(-40, 40)
        gooseMoveY = random.randint(-40, 40)
        if goosePos.x + gooseMoveX > 0 and goosePos.x + gooseMoveX < SCREEN_WIDTH:
            goosePos.x += gooseMoveX
        if goosePos.y + gooseMoveY > 0 and goosePos.y + gooseMoveY < SCREEN_HEIGHT:
            goosePos.y += gooseMoveY

    # Draw goose
    pygame.draw.circle(screen, "green", goosePos, 40)
    goose.update() #new and updated goose

    # Update display
    pygame.display.flip()

    # Limit FPS
    dt = clock.tick(60) / 1000

pygame.quit()
