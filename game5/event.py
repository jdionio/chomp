import pygame
import sys
from game_parameters import *
from background import draw_background # Import draw background function

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('chomp!')

# Main loop
running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('You pressed they key up key!')
            if event.key == pygame.K_DOWN:
                print('You pressed the down key!')


    # Draw background
    screen.blit(background, (0,0))

    # Update display
    pygame.display.flip()


pygame.QUIT
sys.exit()