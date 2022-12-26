import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (1800, 2000)

# Create the window
screen = pygame.display.set_mode(window_size, pygame.FULLSCREEN)

# Set the window title
pygame.display.set_caption("Snow Day")

# Set the background color
bg_color = (0, 0, 0)

# Set the number of stars
num_stars = 500

# Create the list of stars
stars = []
for i in range(num_stars):
    x = random.randint(0, window_size[0])
    y = random.randint(0, window_size[1])
    size = random.randint(1, 3)
    stars.append([x, y, size])

# Set the game clock
clock = pygame.time.Clock()

# Set the speed of the stars
speed = 100

# Set the game loop flag
running = True

# Start the game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(bg_color)

    # Update the position of the stars
    for star in stars:
        star[1] += speed * clock.get_time() / 1000
        if star[1] > window_size[1]:
            star[1] = 0
            star[0] = random.randint(0, window_size[0])

    # Draw the stars
    for star in stars:
        pygame.draw.circle(screen, (255, 255, 255), (star[0], int(star[1])), star[2])

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
