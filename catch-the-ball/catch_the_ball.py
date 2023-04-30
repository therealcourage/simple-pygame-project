import pygame
import random

# Initialize Pygame
pygame.init()

icon = pygame.image.load("shit.png")

# Set up the game screen
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catch the Ball")
pygame.display.set_icon(icon)

# Set up the paddle
paddle_width = 80
paddle_height = 10
paddle_x = (screen_width - paddle_width) // 2
paddle_y = screen_height - 50
paddle_speed = 2

# Set up the ball
ball_radius = 10
ball_x = random.randint(ball_radius, screen_width - ball_radius)
ball_y = -ball_radius
ball_speed = 1

# Set up the font
font = pygame.font.Font(None, 30)

# Main game loop
game_over = False
score = 0

while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_d] and paddle_x < screen_width - paddle_width:
        paddle_x += paddle_speed

    # Move the ball
    ball_y += ball_speed

    # Check for collision with paddle
    if ball_y + ball_radius >= paddle_y and ball_x + ball_radius >= paddle_x and ball_x - ball_radius <= paddle_x + paddle_width:
        ball_y = -ball_radius
        ball_x = random.randint(ball_radius, screen_width - ball_radius)
        score += 1

    # Check for game over
    if ball_y - ball_radius > screen_height:
        game_over = True

    # Draw the game objects
    screen.fill((0, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius)
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

# Clean up Pygame
pygame.quit()
