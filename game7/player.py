# Pygame sprite class for a player fish

import pygame
from game_parameters import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/orange_fish.png").convert()
        self.image.set_colorkey((0,0,0))
        self.image = pygame.transform.flip(self.image, False, False)
        self.forward_image = pygame.transform.flip(self.image, False, False)
        self.backwards_image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0
        self.rect.center = (x, y)

    def move_up(self):
        self.y_speed = -PLAYER_SPEED

    def move_down(self):
        self.y_speed = PLAYER_SPEED

    def move_left(self):
        self.x_speed = -PLAYER_SPEED
        self.image = self.backwards_image

    def move_right(self):
        self.x_speed = PLAYER_SPEED
        self.image = self.forward_image

    def stop(self):
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y
        # Check if player has reached edge of screen and stop it
        if self.rect.x < 0:
            self.x_speed = 0
            self.rect.x = 0
        if self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.x_speed = 0
            self.rect.x = SCREEN_WIDTH - self.rect.width
        if self.rect.y < 0:
            self.y_speed = 0
            self.rect.y = 0
        if self.rect.y > SCREEN_HEIGHT - self.rect.height:
            self.y_speed = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def draw(self, screen):
        screen.blit(self.image, self.rect)