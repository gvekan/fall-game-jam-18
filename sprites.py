import pygame

PLAYER_SIZE = (40, 20)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([PLAYER_SIZE[0], PLAYER_SIZE[1]])
        self.image.fill((255,255,255))

        self.rect = self.image.get_rect()

class Obstacles(pygame.sprite.Group):
    def __init__(self):
        super().__init__(self)