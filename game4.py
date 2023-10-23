import pygame
import random
import sys

# Import sprite class and sprite group
from fish import Fish, fishes

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 64

# Add pygame clock
clock = pygame.time.Clock() # Allows us to set the frames per second

# create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('chomp')


def draw_background(screen):
    # load out tiles from assets folder
    water = pygame.image.load("assets/sprites/water.png").convert()
    sand = pygame.image.load("assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("assets/sprites/seagrass.png").convert()

    # make PNGs transparent
    sand.set_colorkey((0, 0, 0))
    seagrass.set_colorkey((0, 0, 0))

    # fill screen with water
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            screen.blit(water, (x, y))

    # fill bottom with sand
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(SCREEN_HEIGHT - TILE_SIZE, SCREEN_HEIGHT, TILE_SIZE):
            screen.blit(sand, (x, y))

    # place seagrass randomly along the bottom
    for _ in range(5):
        x = random.randint(0, SCREEN_WIDTH - 50)
        screen.blit(seagrass, (x, SCREEN_HEIGHT - 2 * TILE_SIZE + 10))

    # draw text
    custom_font = pygame.font.Font('assets/fonts/bloodlust.ttf', 128)
    text = custom_font.render('Chomp', True, (255, 29, 0))
    screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 0))

# Main Loop

running = True
background = screen.copy()
draw_background(background)

# Draw fish on the screen
for _ in range(5):
    x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2)
    y = random.randint(0, SCREEN_HEIGHT - 2 * TILE_SIZE)
    fishes.add(Fish(x,y))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background
    screen.blit(background, (0, 0))

    # Update fish position
    fishes.update()

    # Check if fish has left the screen
    for fish in fishes: # Loop through our fishes in the sprite group
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2)
            y = random.randint(0, SCREEN_HEIGHT - 2 * TILE_SIZE)
            fishes.add(Fish(x,y))

    # Draw fish
    fishes.draw(screen)

    # Update display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()