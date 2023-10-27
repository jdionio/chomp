import random
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 64

# Speed of fish in pixels per frame
MIN_SPEED = 0.5
MAX_SPEED = 3.0

# Speed of player
PLAYER_SPEED = 3.0

# Random fish coords
x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2)
y = random.randint(0, SCREEN_HEIGHT - 2 * TILE_SIZE)