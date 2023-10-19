import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 64

# create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('chomp')

# Load Game Font
custom_font = pygame.font.Font('assets/fonts/bloodlust.ttf', 128)


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
    text = custom_font.render('Chomp', True, (255, 29, 0))
    screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 0))


def draw_fish(screen):
    # Load fish tile onto screen
    green_fish = pygame.image.load('assets/sprites/green_fish.png').convert()
    orange_fish = pygame.image.load('assets/sprites/orange_fish.png').convert()
    puffer_fish = pygame.image.load('assets/sprites/puffer_fish.png').convert()

    # Set Color Key
    green_fish.set_colorkey((0,0,0))
    orange_fish.set_colorkey((0,0,0))
    puffer_fish.set_colorkey((0,0,0))


    # Distribute fish on screen randomly
    for _ in range(1, 10):
        fish = green_fish
        fish_type = random.randint(0,3)
        if fish_type == 0:
            fish = green_fish
        elif fish_type == 1:
            fish = orange_fish
        elif fish_type == 2:
            fish = puffer_fish
        flipped_fish = pygame.transform.flip(fish, True, False)
        fish_dir = random.randint(0,2)
        if fish_dir == 0:
            fish = fish
        elif fish_dir == 1:
            fish = flipped_fish
        x = random.randint(0, SCREEN_WIDTH - TILE_SIZE)
        y = random.randint(0, SCREEN_HEIGHT - 2*TILE_SIZE)
        screen.blit(fish, (x,y))

# Main Loop
running = True
background = screen.copy()
draw_background(background)
draw_fish(background)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background
    screen.blit(background, (0, 0))

    # Update display
    pygame.display.flip()

# Quit pygame
pygame.quit()
