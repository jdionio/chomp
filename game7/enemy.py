# Create a pygame sprite class for a fish
import random
import pygame
from game_parameters import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.enemy = pygame.image.load('../assets/sprites/puffer_fish.png').convert()  # Default fish

        self.image = self.enemy
        self.image.set_colorkey((0, 0, 0))

        self.image = pygame.transform.flip(self.image, True, False)

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = MAX_SPEED
        self.rect.center = (x, y)

    def update(self):
        # Update the position of the fish
        self.x -= self.speed
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)


enemies = pygame.sprite.Group()