import pygame
import random
import sys

# Initialize pygame
pygame.init()

#Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 64

#create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('chomp')

def draw_background(screen):

    #load out tiles from assets folder
    water = pygame.image.load("assets/sprites/water.png").convert()
    sand = pygame.image.load("assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("assets/sprites/seagrass.png").convert()

    #make PNGs transparent
    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))

    #fill screen with water
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            screen.blit(water, (x,y))

    #fill bottom with sand
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(SCREEN_HEIGHT-TILE_SIZE, SCREEN_HEIGHT, TILE_SIZE):
            screen.blit(sand, (x,y))

    #place seagrass randomly along the bottom
    for _ in range(5):
        x= random.randint(0, SCREEN_WIDTH-50)
        screen.blit(seagrass, (x,SCREEN_HEIGHT-2*TILE_SIZE + 10))


#Main Loop
running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Draw the background
    screen.blit(background, (0,0))

    #Update display
    pygame.display.flip()

#Quit pygame
pygame.quit()