# imports
import pygame
import random

# constants
GRID = 80
WIDTH = 1280
HEIGHT = 780

# initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

# fonts
font = pygame.font.SysFont("Times New Roman", 25)

# variables
stick = 0 # amount of sticks player 1 has
poop = 0 # amount of poop player 1 has
fences = [] # list of fence positions
charTime = 3 # character speed
lastDirect = "w" # last direction character was facing (w is up, s is down, a is left, d is right)

# images
bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (1280, 780))


# initialize positions
pos = pygame.Vector2(WIDTH / 2 - 40, HEIGHT / 2 + 50)
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

# random poop positions
randpx = 0
randpy = 0

randpx1 = 0
randpy1 = 0

randpx2 = 0
randpy2 = 0

randpx3 = 0
randpy3 = 0

def updatePoopPos(num):
    global randpx, randpy, randpx1, randpy1, randpx2, randpy2, randpx3, randpy3
    if num == 0:
        randpx = random.randint(0, WIDTH // GRID - 1)
        randpy = random.randint(0, HEIGHT // GRID - 1)

        if randpx * GRID - GRID // 2 > 0:
            randpx = randpx * GRID - GRID // 2
        else:
            randpx = randpx * GRID + GRID // 2

        if randpy * GRID - GRID // 2 > 0:
            randpy = randpy * GRID - GRID // 2
        else:
            randpy = randpy * GRID + GRID // 2

    elif num == 1:
        randpx1 = random.randint(0, WIDTH // GRID - 1)
        randpy1 = random.randint(0, HEIGHT // GRID - 1)

        if randpx1 * GRID - GRID // 2 > 0:
            randpx1 = randpx1 * GRID - GRID // 2
        else:
            randpx1 = randpx1 * GRID + GRID // 2

        if randpy1 * GRID - GRID // 2 > 0:
            randpy1 = randpy1 * GRID - GRID // 2
        else:
            randpy1 = randpy1 * GRID + GRID // 2

    elif num == 2:
        randpx2 = random.randint(0, WIDTH // GRID - 1)
        randpy2 = random.randint(0, HEIGHT // GRID - 1)

        if randpx2 * GRID - GRID // 2 > 0:
            randpx2 = randpx2 * GRID - GRID // 2
        else:
            randpx2 = randpx2 * GRID + GRID // 2

        if randpy2 * GRID - GRID // 2 > 0:
            randpy2 = randpy2 * GRID - GRID // 2
        else:
            randpy2 = randpy2 * GRID + GRID // 2

    elif num == 3:
        randpx3 = random.randint(0, WIDTH // GRID - 1)
        randpy3 = random.randint(0, HEIGHT // GRID - 1)

        if randpx3 * GRID - GRID // 2 > 0:
            randpx3 = randpx3 * GRID - GRID // 2
        else:
            randpx3 = randpx3 * GRID + GRID // 2

        if randpy3 * GRID - GRID // 2 > 0:
            randpy3 = randpy3 * GRID - GRID // 2
        else:
            randpy3 = randpy3 * GRID + GRID // 2

# random poop positions
updatePoopPos(0)
updatePoopPos(1)
updatePoopPos(2)
updatePoopPos(3)

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

# character collision with poop
def collidePoop(posx, posy, poop, amount):
    global randpx, randpy, randpx1, randpy1, randpx2, randpy2, randpx3, randpy3

    def check_collision(px, py):
        return (posx > px - GRID // 2 and posx < px + GRID // 2) and (posy > py - GRID // 2 and posy < py + GRID // 2)

    if poop == 0 and check_collision(randpx, randpy):
        updatePoopPos(0)
        amount += 1
    elif poop == 1 and check_collision(randpx1, randpy1):
        updatePoopPos(1)
        amount += 1
    elif poop == 2 and check_collision(randpx2, randpy2):
        updatePoopPos(2)
        amount += 1
    elif poop == 3 and check_collision(randpx3, randpy3):
        updatePoopPos(3)
        amount += 1

    return amount

# check if new fence overlaps with any existing fences
def checkFenceOverlap(new_fence):
    for fence in fences:
        if (fence[0] == new_fence[0] and fence[1] == new_fence[1] and fence[2] == new_fence[2] and fence[3] == new_fence[3]):
            return True
    return False
        
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
            
        screen.blit(self.images, self.rect)
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

# initialize time for poop movement
poopLastMoveTime = pygame.time.get_ticks()
poopMoveInterval = 10000  # milliseconds (10 seconds)

# main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color
    screen.fill("white")

    # draw background
    screen.blit(bg, (0, 0))

    # background grid - DELETE AFTER
    for i in range(0, WIDTH, GRID):
        for j in range(0, HEIGHT, GRID):
            pygame.draw.rect(screen, "black", (i, j, GRID, GRID), 5)

    # stick text
    text = font.render(f"Sticks: {stick}", True, "black")
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2 + 120, 30) # center text
    pygame.draw.rect(screen, "white", textRect) # stick text border
    screen.blit(text, textRect) # stick text

    # point text
    text2 = font.render(f"Points: {poop}", True, "black")
    textRect2 = text2.get_rect()
    textRect2.center = (WIDTH // 2 - 120, 30) # center text
    pygame.draw.rect(screen, "white", textRect2) # points text border
    screen.blit(text2, textRect2) # points text

    # draw sticks
    pygame.draw.line(screen, "black", (randx * GRID, randy * GRID), (randx * GRID + GRID, randy * GRID + GRID), 5)
    pygame.draw.line(screen, "black", (randx1 * GRID, randy1 * GRID), (randx1 * GRID + GRID, randy1 * GRID + GRID), 5)
    pygame.draw.line(screen, "black", (randx2 * GRID, randy2 * GRID), (randx2 * GRID + GRID, randy2 * GRID + GRID), 5)
    pygame.draw.line(screen, "black", (randx3 * GRID, randy3 * GRID), (randx3 * GRID + GRID, randy3 * GRID + GRID), 5)

    # draw poop
    pygame.draw.circle(screen, "brown", (randpx, randpy), 20)
    pygame.draw.circle(screen, "brown", (randpx1, randpy1), 20)
    pygame.draw.circle(screen, "brown", (randpx2, randpy2), 20)
    pygame.draw.circle(screen, "brown", (randpx3, randpy3), 20)
    #print(randpx, randpy, randpx1, randpy1, randpx2, randpy2, randpx3, randpy3)

    # character movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        newCY = pos.y - GRID
        if newCY > 0:  # check if new Y position is within bounds
            # check for collision with fences
            collision = False
            for fence in fences:
                if (pos.x >= fence[0] and pos.x <= fence[2] and
                    newCY >= fence[1] and newCY <= fence[3]):
                    collision = True
                    break
            if not collision:
                pos.y = newCY
        clock.tick(charTime)
        lastDirect = "w"
        direction = "up"
    elif keys[pygame.K_s]:
        newCY = pos.y + GRID
        if newCY < HEIGHT:  # check if new Y position is within bounds
            # check for collision with fences
            collision = False
            for fence in fences:
                if (pos.x >= fence[0] and pos.x <= fence[2] and
                    newCY >= fence[1] and newCY <= fence[3]):
                    collision = True
                    break
            if not collision:
                pos.y = newCY
        clock.tick(charTime)
        lastDirect = "s"
        direction = "down"
    elif keys[pygame.K_a]:
        newCX = pos.x - GRID
        if newCX > 0:  # check if new X position is within bounds
            # check for collision with fences
            collision = False
            for fence in fences:
                if (newCX >= fence[0] and newCX <= fence[2] and
                    pos.y >= fence[1] and pos.y <= fence[3]):
                    collision = True
                    break
            if not collision:
                pos.x = newCX
        clock.tick(charTime)
        lastDirect = "a"
        direction = "left"
    elif keys[pygame.K_d]:
        newCX = pos.x + GRID
        if newCX < WIDTH:  # check if new X position is within bounds
            # check for collision with fences
            collision = False
            for fence in fences:
                if (newCX >= fence[0] and newCX <= fence[2] and
                    pos.y >= fence[1] and pos.y <= fence[3]):
                    collision = True
                    break
            if not collision:
                pos.x = newCX
        clock.tick(charTime)
        lastDirect = "d"
        direction = "right"

    if keys[pygame.K_UP]:
        newCY = pos.y - GRID
        if newCY > 0:  # check if new Y position is within bounds
            # check for collision with fences
            collision = False
            for fence in fences:
                if (pos.x >= fence[0] and pos.x <= fence[2] and
                    newCY >= fence[1] and newCY <= fence[3]):
                    collision = True
                    break
            if not collision:
                pos.y = newCY
        clock.tick(charTime)
        lastDirect = "w"
        direction = "up"
    elif keys[pygame.K_DOWN]:
        newCY = pos.y + GRID
        if newCY < HEIGHT:  # check if new Y position is within bounds
            # check for collision with fences
            collision = False
            for fence in fences:
                if (pos.x >= fence[0] and pos.x <= fence[2] and
                    newCY >= fence[1] and newCY <= fence[3]):
                    collision = True
                    break
            if not collision:
                pos.y = newCY
        clock.tick(charTime)
        lastDirect = "s"
        direction = "down"
    elif keys[pygame.K_LEFT]:
        newCX = pos.x - GRID
        if newCX > 0:  # check if new X position is within bounds
            # check for collision with fences
            collision = False
            for fence in fences:
                if (newCX >= fence[0] and newCX <= fence[2] and
                    pos.y >= fence[1] and pos.y <= fence[3]):
                    collision = True
                    break
            if not collision:
                pos.x = newCX
        clock.tick(charTime)
        lastDirect = "a"
        direction = "left"
    elif keys[pygame.K_RIGHT]:
        newCX = pos.x + GRID
        if newCX < WIDTH:  # check if new X position is within bounds
            # check for collision with fences
            collision = False
            for fence in fences:
                if (newCX >= fence[0] and newCX <= fence[2] and
                    pos.y >= fence[1] and pos.y <= fence[3]):
                    collision = True
                    break
            if not collision:
                pos.x = newCX
        clock.tick(charTime)
        lastDirect = "d"
        direction = "right"

    # check character collisions with sticks
    for i in range(4):
        stick = collideStick(pos.x, pos.y, i, stick)

    # check character collisions with poop
    for i in range(4):
        poop = collidePoop(pos.x, pos.y, i, poop)

    # draw characters
    pygame.draw.circle(screen, "red", pos, 40)

    # draw fences
    if keys[pygame.K_SPACE] and stick > 0:
        if (lastDirect == "w"):
            fencePos = pygame.Vector2(pos.x, pos.y - GRID - GRID // 2)
        elif (lastDirect == "s"):
            fencePos = pygame.Vector2(pos.x, pos.y + GRID // 2)
        elif (lastDirect == "a"):
            fencePos = pygame.Vector2(pos.x - GRID, pos.y - GRID // 2)
        elif (lastDirect == "d"):
            fencePos = pygame.Vector2(pos.x + GRID, pos.y - GRID // 2)
        endPos = fencePos + pygame.Vector2(0, 80)
        newFence = (fencePos.x, fencePos.y, endPos.x, endPos.y)
        if not checkFenceOverlap(newFence):
            fences.append(newFence)
            stick -= 1  # only reduce stick if placing fence in valid place
        clock.tick(3) 
    
    for fence in fences:
        pygame.draw.line(screen, "pink", (fence[0], fence[1]), (fence[2], fence[3]), 5)

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
