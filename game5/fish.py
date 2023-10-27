# Create a pygame sprite class for a fish
import random
import pygame
from game_parameters import *

class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.green_fish = pygame.image.load('../assets/sprites/green_fish.png').convert()
        self.orange_fish = pygame.image.load('../assets/sprites/orange_fish.png').convert()
        self.puffer_fish = pygame.image.load('../assets/sprites/puffer_fish.png').convert()

        self.fish = pygame.image.load('../assets/sprites/green_fish.png').convert() # Default fish

        self.fish_type = random.randint(0,3)
        if self.fish_type == 0:
            self.fish = self.green_fish
        elif self.fish_type == 1:
            self.fish = self.orange_fish
        elif self.fish_type == 2:
            self.fish = self.puffer_fish

        self.image = self.fish
        self.image.set_colorkey((0,0,0))

        #fish_dir = random.randint(0,2)
        #if fish_dir == 0:
        self.image = pygame.transform.flip(self.image, True, False)

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)
        self.rect.center = (x,y)

    def update(self):
        # Update the position of the fish
        self.x -= self.speed
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

fishes = pygame.sprite.Group()