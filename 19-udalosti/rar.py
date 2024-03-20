import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
SPEED = 2

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the player
player = pygame.Rect(WIDTH // 2, HEIGHT // 2, 50, 50)

# Set up the game loop
running = True
while running:
    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the player
    pygame.draw.rect(screen, (255, 255, 255), player)

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= SPEED
    if keys[pygame.K_RIGHT]:
        player.x += SPEED
    if keys[pygame.K_UP]:
        player.y -= SPEED
    if keys[pygame.K_DOWN]:
        player.y += SPEED

    # Make sure the player stays on the screen
    if player.x < 0:
        player.x = 0
    if player.x > WIDTH - 50:
        player.x = WIDTH - 50
    if player.y < 0:
        player.y = 0
    if player.y > HEIGHT - 50:
        player.y = HEIGHT - 50

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Flip the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
