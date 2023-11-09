import pygame
import sys
import random

# Import all our necessary files
from fish import Fish, fishes
from background import draw_background, add_fish, add_enemies
from game_parameters import *
from player import Player
from enemy import Enemy,enemies

# Initialize pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('chomp!')

# Create clock
clock = pygame.time.Clock()

# Load sound into game
chomp = pygame.mixer.Sound('../assets/sounds/chomp.wav')
hurt = pygame.mixer.Sound("../assets/sounds/hurt.wav")
bubbles = pygame.mixer.Sound("../assets/sounds/bubbles.wav")

# add alternate and game over
life_icon = pygame.image.load("../assets/sprites/orange_fish_alt.png")
life_icon.set_colorkey((0,0,0))

# Set number of lives
lives = NUM_LIVES


# Main loop
running = True
background = screen.copy()
draw_background(background)

# Draw fish on the screen
add_fish(5)
add_enemies(5)
# Draw player fish
player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

# Load new font to keep score
score = 0
score_font = pygame.font.Font('../assets/fonts/Black_Crayon.ttf', 72)


while lives > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # Control fish with arrow keys
        # player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_up()
            if event.key == pygame.K_DOWN:
                player.move_down()
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_RIGHT:
                player.move_right()
        if event.type == pygame.KEYUP:
            player.stop()
# Check if player collides with enemies
    # Draw background
    screen.blit(background, (0,0))

    # Update fish location
    fishes.update()
    enemies.update()

    # Update player fish
    player.update()

    # Check if fish has left the screen
    for fish in fishes:  # Loop through our fishes in the sprite group
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2)
            y = random.randint(0, SCREEN_HEIGHT - 2 * TILE_SIZE)
            fishes.add(Fish(x, y))

    # Check if enemy has left the screen
    for enemy in enemies:  # Loop through our fishes in the sprite group
        if enemy.rect.x < -fish.rect.width:
            enemies.remove(enemy)
            x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2)
            y = random.randint(0, SCREEN_HEIGHT - 2 * TILE_SIZE)
            enemies.add(Enemy(x, y))

    # Draw fish
    fishes.draw(screen)

    # Draw player
    player.draw(screen)

    # Check for collisions
    result = pygame.sprite.spritecollide(player, fishes, True)
    result1 = pygame.sprite.spritecollide(player, enemies, True)
    if result:
         print('nom')
         # Add to score
         score += len(result)

        # Play chomp sound
        pygame.mixer.Sound.play(chomp)
        add_fish(len(result))

    if result1:
        print('ow')
        lives -= len(result1)
        pygame.mixer.Sound.play(hurt)
        add_enemies(len(result1))


    # Update score on screen
    text = score_font.render(f'{score}', True, (0, 0, 0))
    screen.blit(text, (SCREEN_WIDTH - text.get_width(), 0))

    for i in range(lives):
        screen.blit(life_icon, (i * TILE_SIZE, SCREEN_HEIGHT-TILE_SIZE))


    # Update display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Create new background when game over
screen.blit(background, (0,0))

# Show game over message
message = score_font.render("GAME OVER", True, (0,0,0))
screen.blit(message, (SCREEN_WIDTH/2 - message.get_width(), SCREEN_HEIGHT/2))

# Show final score
score_text = score_font.render(f"Score: {score}", True, (0,0,0))
screen.blit(score_text, (SCREEN_WIDTH/2 - score_text.get_width() /2, SCREEN_HEIGHT/2 + score_text.get_height()))

pygame.display.flip()

pygame.mixer.Sound.play(bubbles)

