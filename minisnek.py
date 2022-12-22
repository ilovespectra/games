import pygame
import random

# Initialize pygame
pygame.init()

# Set the window size
window_size = (400, 400)

# Set the window title
pygame.display.set_caption("Snake")

# Set the window background color
window_color = (0, 0, 0)

# Set the snake color
snake_color = (255, 165, 0)

# Set the snake starting position
snake_pos = [100, 50]

# Set the snake body as a list of blocks
snake_body = [[100, 50], [90, 50], [80, 50]]

# Set the food color
food_color = (255, 0, 0)

# Set the food starting position
food_pos = [random.randrange(1, (window_size[0] // 10)) * 10, random.randrange(1, (window_size[1] // 10)) * 10]
food_spawn = True

# Set the initial direction of the snake
direction = "RIGHT"

# Set the change in position for each move
change_in_pos = [10, 0]

# Set the clock speed
clock = pygame.time.Clock()
clock.tick(1) 

# Set the font
font = pygame.font.SysFont("times new roman", 20)

# Set the initial score
score = 0

# Create the game window
window = pygame.display.set_mode(window_size)

# Set the flag for when the game is over
game_over = False

# Game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        # Quit if the user closes the window
        if event.type == pygame.QUIT:
            game_over = True
            pygame.quit()
            quit()

        # Change the direction of the snake based on key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = "UP"
                change_in_pos = [0, -10]
            if event.key == pygame.K_DOWN:
                direction = "DOWN"
                change_in_pos = [0, 10]
            if event.key == pygame.K_LEFT:
                direction = "LEFT"
                change_in_pos = [-10, 0]
            if event.key == pygame.K_RIGHT:
                direction = "RIGHT"
                change_in_pos = [10, 0]

    # Update the snake position
    snake_pos[0] += change_in_pos[0]
    snake_pos[1] += change_in_pos[1]

    # Check if the snake has collided with the walls
    if snake_pos[0] < 0 or snake_pos[0] > window_size[0] - 10:
        game_over = True
    if snake_pos[1] < 0 or snake_pos[1] > window_size[1] - 10:
        game_over = True

    # Check if the snake has collided with itself
    if snake_pos in snake_body[1:]:
        game_over = True

    # Update the snake body
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Spawn food
    if not food_spawn:
        food_pos = [random.randrange(1, (window_size[0] // 10)) * 10, random.randrange(1, (window_size[1] // 10)) * 10]
    food_spawn = True

    # Draw the window
    window.fill(window_color)

    # Draw the snake
    for pos in snake_body:
        pygame.draw.rect(window, snake_color, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw the food
    pygame.draw.rect(window, food_color, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Draw the score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(score_text, (5, 5))

    # Update the display
    pygame.display.update()

    clock.tick(clock.get_fps() + 1)
# Set the high score
if score > high_score:
    high_score = score

pygame.quit()
quit()
