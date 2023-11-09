# Create a pygame sprite class for a fish
import random
import pygame
from game_parameters import *


class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.fish = pygame.image.load('../assets/sprites/orange_fish.png').convert()

        self.image = self.fish
        self.image.set_colorkey((0, 0, 0))

        self.image = pygame.transform.flip(self.image, True, False)

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)
        self.rect.center = (x, y)

    def update(self):
        # Update the position of the fish
        self.x -= self.speed
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)


fishes = pygame.sprite.Group()