import random
import pygame
from game_parameters import *


# Draw background function
def draw_background(screen):
    # load out tiles from assets folder
    water = pygame.image.load("../assets/sprites/water.png").convert()
    sand = pygame.image.load("../assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("../assets/sprites/seagrass.png").convert()

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
    custom_font = pygame.font.Font('../assets/fonts/bloodlust.ttf', 128)
    text = custom_font.render('Chomp', True, (255, 29, 0))
    screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 0))
