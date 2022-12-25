# This is a screen saver, you can use any png you'd like.

import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (1920, 1080)

# Create the window
screen = pygame.display.set_mode(window_size, pygame.FULLSCREEN)

# Set the window title
pygame.display.set_caption("Space Screensaver")

# Load the PNG image
png = pygame.image.load("/images/BOP.png")

# Set the background color
bg_color = (0, 0, 0)

# Set the object size
obj_size = 10

# Set the falling speed
fall_speed = 1.2

# Create a list to store the falling objects
objects = []

# Set the game clock
clock = pygame.time.Clock()

# Start the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(bg_color)

    # Add a new object to the list if there are less than 10 objects
    if len(objects) < 14:
        objects.append([random.randint(0, window_size[0] - obj_size), 0, random.uniform(0.6, 3)])

    # Update the position of each object and remove it if it goes off the screen
    for i, obj in enumerate(objects):
        obj[1] += obj[2]
        if obj[1] > window_size[1]:
            objects.pop(i)

    # Draw each object
    for obj in objects:
        screen.blit(png, (obj[0], obj[1]))

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)
