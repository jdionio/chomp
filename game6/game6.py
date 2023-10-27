import pygame
import sys
import random

# Import all our necessary files
from fish import Fish, fishes
from background import draw_background
from game_parameters import *
from player import Player

# Initialize pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('chomp!')

# Create clock
clock = pygame.time.Clock()

# Load sound into game
chomp = pygame.mixer.Sound('../assets/sounds/chomp.wav')

# Main loop
running = True
background = screen.copy()
draw_background(background)

# Draw fish on the screen
for _ in range(5):
    x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2)
    y = random.randint(0, SCREEN_HEIGHT - 2 * TILE_SIZE)
    fishes.add(Fish(x,y))

# Draw player fish
player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

# Load new font to keep score
score = 0
score_font = pygame.font.Font('../assets/fonts/Black_Crayon.ttf', 72)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # Control fish with arrow keys
        player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_up()
            if event.key == pygame.K_DOWN:
                player.move_down()
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_RIGHT:
                player.move_right()

    # Draw background
    screen.blit(background, (0,0))

    # Update fish location
    fishes.update()

    # Update player fish
    player.update()

    # Check if fish has left the screen
    for fish in fishes:  # Loop through our fishes in the sprite group
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2)
            y = random.randint(0, SCREEN_HEIGHT - 2 * TILE_SIZE)
            fishes.add(Fish(x, y))

    # Draw fish
    fishes.draw(screen)

    # Draw player
    player.draw(screen)

    # Check for collisions
    result = pygame.sprite.spritecollide(player, fishes, True)
    if result:
        # Add to score
        print(result)
        score += len(result)

        # Play chomp sound
        pygame.mixer.Sound.play(chomp)

        for _ in range(len(result)):
            fishes.add(Fish(x,y))

    # Update score on screen
    text = score_font.render(f'{score}', True, (0, 0, 0))
    screen.blit(text, (SCREEN_WIDTH - text.get_width(), 0))


    # Update display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()