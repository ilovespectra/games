import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (800, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the window title
pygame.display.set_caption("Breakout")

# Set the background color
bg_color = (0, 0, 0)

# Create the player paddle
paddle_width = 100
paddle_height = 15
paddle_color = (255, 255, 255)
paddle_x = (window_size[0] - paddle_width) // 2
paddle_y = window_size[1] - 20

# Create the ball
ball_radius = 10
ball_color = (255, 255, 255)
ball_x = window_size[0] // 2
ball_y = window_size[1] // 2
ball_dx = 4
ball_dy = 4

# Set the game clock
clock = pygame.time.Clock()

# Set the font for score and game over text
font = pygame.font.Font(None, 36)

# Set the score to 0
score = 0

# Create a list of blocks
blocks = []

# Set the block size and spacing
block_width = 50
block_height = 20
block_spacing = 5

# Set the number of rows and columns of blocks
rows = 5
columns = 10

# Set the starting position for the blocks
block_x = (window_size[0] - (columns * (block_width + block_spacing))) // 2
block_y = 50

# Create the blocks
for row in range(rows):
    for column in range(columns):
        block = {"rect": pygame.Rect(block_x, block_y, block_width, block_height), "color": (255, 0, 0), "hits": 3}
        blocks.append(block)
        block_x += block_width + block_spacing
    block_x = (window_size[0] - (columns * (block_width + block_spacing))) // 2
    block_y += block_height + block_spacing

# Set the game over flag to False
game_over = False

# Start the game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Update the paddle position based on mouse movement
    paddle_x = pygame.mouse.get_pos()[0] - paddle_width // 2

    # Keep the paddle on the screen
    if paddle_x < 0:
        paddle_x = 0
    elif paddle_x > window_size[0] - paddle_width:
        paddle_x = window_size[0] - paddle_width

    # Update the ball position
    ball_x += ball_dx
    ball_y += ball_dy

    # Check if the ball has hit the paddle
    if ball_y + ball_radius >= paddle_y and ball_x + ball_radius >= paddle_x and ball_x - ball_radius <= paddle_x + paddle_width:
    # Calculate the angle of the ricochet based on the position of the ball on the paddle
        ball_dx = (ball_x - (paddle_x + paddle_width // 2)) * 0.35
        ball_dy = -ball_dy

    # Check if the ball has hit the left or right wall
    if ball_x < 0 or ball_x > window_size[0]:
        ball_dx = -ball_dx

    # Check if the ball has hit the top wall
    if ball_y < 0:
        ball_dy = -ball_dy

    # Check if the ball has hit the bottom of the window
    if ball_y > window_size[1]:
        game_over = True

    # Check if the ball has hit a block
    for block in blocks:
        if ball_x > block["rect"].x and ball_x < block["rect"].x + block_width and ball_y > block["rect"].y and ball_y < block["rect"].y + block_height:
            ball_dy = -ball_dy
            block["hits"] -= 1
            if block["hits"] == 0:
                blocks.remove(block)
                # Increase the score
                score += 1
            elif block["hits"] == 1:
                block["color"] = (245, 210, 0)
            elif block["hits"] == 2:
                block["color"] = (255, 165, 0)
            break

    # Check if all blocks have been destroyed
    if len(blocks) == 0:
        game_over = True


    # Draw the background
    screen.fill(bg_color)

    # Draw the paddle
    pygame.draw.rect(screen, paddle_color, pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height))

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # Draw the blocks
    for block in blocks:
        pygame.draw.rect(screen, block["color"], block["rect"])

    # Draw the score
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (window_size[0] // 2, 25)
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(90)

# Game over
text = font.render("Game Over!", True, (255, 255, 255))
text_rect = text.get_rect()
text_rect.center = (window_size[0] // 2, window_size[1] // 2)
screen.blit(text, text_rect)
pygame.display.flip()

# Wait for the player to quit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            break
            if game_over:
                    break
    # Game over
    text = font.render("Game Over!", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (window_size[0] // 2, window_size[1] // 2)
    screen.blit(text, text_rect)
    pygame.display.flip()

# Quit Pygame
pygame.quit()
