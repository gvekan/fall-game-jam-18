import pygame
from constants import *
from game_state import state

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([PLAYER_SIZE[0], PLAYER_SIZE[1]])
        self.image.fill((255,255,255))

        self.rect = self.image.get_rect()
        self.lane = 2

class ScrollObjects(pygame.sprite.Group):
    def __init__(self):
        super().__init__(self)

    def update(self, *args):
        for s in self.sprites():
            s.rect.x -= state.scroll_length
            if s.rect.x + s.rect.width <= 0:
                s.kill()

class Obstacles(pygame.sprite.Group):
    def __init__(self):
        super().__init__(self)

    def update(self, *args):
        for s in self.sprites():
            # TODO: Check collision
            return


