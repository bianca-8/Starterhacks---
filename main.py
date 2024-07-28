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
charTime = 3 # character speed

# images
bg = pygame.image.load("bg.png")
charStep = 300  # character steps

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
newX = 0
newY = 0

    

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
       self.images_right = []
       self.images_left = []
       self.index = 0
       self.counter = 0
       for i in range(1, 5): #adds the images to a list with a loop for the animation
           img_right = pygame.image.load(f'realSprite/Goose{i}.png')
           img_right = pygame.transform.scale(img_right, (120, 80))
           img_left = pygame.transform.flip(img_right, True, False)
           self.images_right.append(img_right)
           self.images_left.append(img_left)
           
       self.images = self.images_right[self.index]
       self.rect = self.images.get_rect()
       self.rect.x = x
       self.rect.y = y
       self.direction = 1
       self.rect.topleft = (x, y)
       self.mask = pygame.mask.from_surface(self.images)

    def update(self):
        global gooseLastMoveTime 
        newX = self.rect.x
        newY = self.rect.y

        currentTime = pygame.time.get_ticks()
        if currentTime - gooseLastMoveTime > moveInterval:
            gooseLastMoveTime = currentTime
            gooseMove = 80
            gooseDirec = random.randint(0, 3)
            
            if gooseDirec == 0:  # up
                newY = self.rect.y - gooseMove #goose = Goose(goosePos.x-65,goosePos.y-50)
                if newY > 0:  # check if new Y position is within bounds
                    self.rect.y = newY            
            elif gooseDirec == 1:  # down
                newY = self.rect.y + gooseMove
                if newY < HEIGHT:  # check if new Y position is within bounds
                    self.rect.y = newY
            elif gooseDirec == 2:  # left
                newX = self.rect.x - gooseMove
                if newX > 0:  # check if new X position is within bounds
                    self.rect.x = newX
                    self.direction = -1
            elif gooseDirec == 3:  # right
                newX = self.rect.x + gooseMove
                if newX < WIDTH:  # check if new X position is within bounds
                    self.rect.x = newX
                    self.direction = 1

        # animating the geese
        fly_cooldown = 10
        self.counter += 1 
        if self.counter> fly_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.images = self.images_right[self.index]
            if self.direction == -1:
                self.images = self.images_left[self.index]
        screen.blit(self.images, self.rect)


#pink man image
class pinkMan(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x-25
        self.y = y-25
        self.pink_d = []
        self.pink_u = []
        self.pink_r = []
        self.pink_l = []
        self.pink = self.pink_u
        self.index = 0
        self.counter = 0
        for i in range(1, 17):
            if i/4 <= 1:
                pink_down = pygame.image.load(f'realSprite/pink{i}.png')
                # img_right = pygame.transform.scale(img_right, (100, 60))
                self.pink_d.append(pink_down)
            elif i/4 <= 2:
                pink_up = pygame.image.load(f'realSprite/pink{i}.png')
            # img_right = pygame.transform.scale(img_right, (100, 60))
                self.pink_u.append(pink_up)
                
            elif i/4 <= 3:
                pink_right = pygame.image.load(f'realSprite/pink{i}.png')
            # img_right = pygame.transform.scale(img_right, (100, 60))
                self.pink_r.append(pink_right)
            else:
                pink_left = pygame.image.load(f'realSprite/pink{i}.png')
            # img_right = pygame.transform.scale(img_right, (100, 60))
                self.pink_l.append(pink_left)
           
        self.images = self.pink_d[self.index]
        self.rect = self.images.get_rect()

        self.rect.x = x-25
        self.rect.y = y-25
        self.direction = 0
        self.rect.topleft = (x-25, y-25)
        self.mask = pygame.mask.from_surface(self.images)
        self.prevDirection = -1

    def update_x(self, new_value):
        self.x = new_value-25
        self.rect.x = new_value-25

    def update_y(self, new_value):
        self.y = new_value-25
        self.rect.y = new_value-25

    def update(self, direction):
        global keys
        
        if direction == "up":
            self.direction = 1
        elif direction == "down":
            self.direction = 2
        elif direction == "left":
            self.direction = 3
        elif direction == "right": #right
            self.direction = 4
        
        animationUpdate = 20
        self.counter += 1 
        if self.counter > animationUpdate or direction != self.prevDirection:
            self.counter = 0
            self.index += 1
            # print("len",len(self.pink_u),self.index)
            if self.index >= len(self.pink_d):
                self.index = 0
            if self.direction == 1:
                self.images = self.pink_u[self.index]
            if self.direction == 2:
                self.images = self.pink_d[self.index]
            if self.direction == 3:
                self.images = self.pink_l[self.index]
            if self.direction == 4:
                self.images = self.pink_r[self.index]
        self.prevDirection = direction
        screen.blit(self.images, self.rect)



# initialize time for goose movement
gooseLastMoveTime = pygame.time.get_ticks()
moveInterval = 1000  # milliseconds (1.5 seconds)
goose = Goose(goosePos.x-65,goosePos.y-50)
pink = pinkMan(50,50)
direction = "down"

# main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color
    screen.fill("white")

    screen.blit(bg, (0, 0))

    """
    # draw background grid - DELETE AFTER
    for i in range(0, WIDTH, GRID):
        for j in range(0, HEIGHT, GRID):
            pygame.draw.rect(screen, "black", (i, j, GRID, GRID), 5)"""

    # draw sticks
    pygame.draw.line(screen, "black", (randx * GRID, randy * GRID), (randx * GRID + GRID, randy * GRID + GRID), 5)
    pygame.draw.line(screen, "black", (randx1 * GRID, randy1 * GRID), (randx1 * GRID + GRID, randy1 * GRID + GRID), 5)
    pygame.draw.line(screen, "black", (randx2 * GRID, randy2 * GRID), (randx2 * GRID + GRID, randy2 * GRID + GRID), 5)
    pygame.draw.line(screen, "black", (randx3 * GRID, randy3 * GRID), (randx3 * GRID + GRID, randy3 * GRID + GRID), 5)

    # character movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        newCY = pos.y - GRID
        if newCY > 0:  # check if new Y position is within bounds
            pos.y = newCY
        clock.tick(charTime)
    elif keys[pygame.K_s]:
        newCY = pos.y + GRID
        if newCY < HEIGHT:  # check if new Y position is within bounds
            pos.y = newCY
        clock.tick(charTime)
    elif keys[pygame.K_a]:
        newCX = pos.x - GRID
        if newCX > 0:  # check if new X position is within bounds
            pos.x = newCX
        clock.tick(charTime)
    elif keys[pygame.K_d]:
        newCX = pos.x + GRID
        if newCX < WIDTH:  # check if new X position is within bounds
            pos.x = newCX
        clock.tick(charTime)

    if keys[pygame.K_w] and pos.y - charStep * dt > 0:
        pos.y -= charStep * dt
        direction = "up"
    elif keys[pygame.K_s] and pos.y + charStep * dt < HEIGHT:
        pos.y += charStep * dt
        direction = "down"
    elif keys[pygame.K_a] and pos.x - charStep * dt > 0:
        pos.x -= charStep * dt
        direction = "left"
    elif keys[pygame.K_d] and pos.x + charStep * dt < WIDTH:
        pos.x += charStep * dt
        direction = "right"

    if keys[pygame.K_UP]:
        newCY = pos2.y - GRID
        if newCY > 0:  # check if new Y position is within bounds
            pos2.y = newCY
        clock.tick(charTime)
    elif keys[pygame.K_DOWN]:
        newCY = pos2.y + GRID
        if newCY < HEIGHT:  # check if new Y position is within bounds
            pos2.y = newCY
        clock.tick(charTime)
    elif keys[pygame.K_LEFT]:
        newCX = pos2.x - GRID
        if newCX > 0:  # check if new X position is within bounds
            pos2.x = newCX
        clock.tick(charTime)
    elif keys[pygame.K_RIGHT]:
        newCX = pos2.x + GRID
        if newCX < WIDTH:  # check if new X position is within bounds
            pos2.x = newCX
        clock.tick(charTime)

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

    # draw goose
    goose.update()

    #PinkMan
    pink.update_x(pos.x)
    pink.update_y(pos.y)
    pink.update(direction)

    # update display
    pygame.display.flip()

    # limit FPS
    dt = clock.tick(60) / 1000

pygame.quit()
