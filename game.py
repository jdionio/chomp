import pygame
import sys

# Initialize pygame
pygame.init()

#Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Colors
BLUE = (0,0,255)
SANDY = (196, 183, 67)
OCEAN_BLUE = (67, 149, 196)

#Creating the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('chomp')

#Main loop
running = True #set flag to True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fill screen with blue
    screen.fill(OCEAN_BLUE)

    #add sandy bottom
    RECT_HEIGHT = 100
    pygame.draw.rect(screen, SANDY, (0, SCREEN_HEIGHT - RECT_HEIGHT, SCREEN_WIDTH, RECT_HEIGHT))

    #update the display
    pygame.display.flip()

pygame.quit()