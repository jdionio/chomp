# Create a pygame sprite class for a fish
import random
import pygame

MIN_SPEED = 0.5
MAX_SPEED = 3

class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        green_fish = pygame.image.load('assets/sprites/green_fish.png').convert()
        orange_fish = pygame.image.load('assets/sprites/orange_fish.png').convert()
        puffer_fish = pygame.image.load('assets/sprites/puffer_fish.png').convert()

        fish = pygame.image.load('assets/sprites/green_fish.png').convert() # Default fish

        fish_type = random.randint(0,3)
        if fish_type == 0:
            fish = green_fish
        elif fish_type == 1:
            fish = orange_fish
        elif fish_type == 2:
            fish = puffer_fish

        self.image = fish
        self.image.set_colorkey((0,0,0))

        fish_dir = random.randint(0,2)
        if fish_dir == 0:
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

    def draw(self, screen):
        screen.blit(self.image, self.rect)

fishes = pygame.sprite.Group()