import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
BALL_SIZE = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 80
BALL_SPEED = 2
PADDLE_SPEED = 2

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the ball and paddles
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)
paddle1 = pygame.Rect(0, HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - PADDLE_WIDTH, HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Set up the ball direction
ball_dx = BALL_SPEED
ball_dy = BALL_SPEED

# Set up the game loop
running = True
while running:
    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the ball and paddles
    pygame.draw.rect(screen, (255, 255, 255), ball)
    pygame.draw.rect(screen, (255, 255, 255), paddle1)
    pygame.draw.rect(screen, (255, 255, 255), paddle2)

    # Move the ball
    ball.x += ball_dx
    ball.y += ball_dy

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.y -= PADDLE_SPEED
    if keys[pygame.K_s]:
        paddle1.y += PADDLE_SPEED
    if keys[pygame.K_UP]:
        paddle2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN]:
        paddle2.y += PADDLE_SPEED

    # Collide with the top and bottom
    if ball.y < 0 or ball.y > HEIGHT - BALL_SIZE:
        ball_dy *= -1

    # Collide with the paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_dx *= -1

    # Make sure the paddles don't go off screen
    if paddle1.y < 0:
        paddle1.y = 0
    if paddle1.y > HEIGHT - PADDLE_HEIGHT:
        paddle1.y = HEIGHT - PADDLE_HEIGHT
    if paddle2.y < 0:
        paddle2.y = 0
    if paddle2.y > HEIGHT - PADDLE_HEIGHT:
        paddle2.y = HEIGHT - PADDLE_HEIGHT

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Flip the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
