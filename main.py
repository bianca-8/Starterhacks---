# import
import pygame

#colors


# set up
pygame.init()
screen = pygame.display.set_mode((1280, 780))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_pos2 = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

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

    # characters
    pygame.draw.circle(screen, "red", player_pos, 40)
    pygame.draw.circle(screen, "blue", player_pos2, 40)

    # stick
    pygame.draw.line(screen,"black", (0,0), (0,80), 5)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    if keys[pygame.K_UP]:
        player_pos2.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player_pos2.y += 300 * dt
    if keys[pygame.K_LEFT]:
        player_pos2.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos2.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()