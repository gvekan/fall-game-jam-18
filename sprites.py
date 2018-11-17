import pygame
from constants import *
from game_state import state

class All(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)

    def update(self, *args):
        for s in self.sprites():
            s.update()


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

    def update(self, state, *args):
        for s in self.sprites():
            s.rect.x -= state.scroll_length
            if s.rect.x + s.rect.width <= 0:
                state.kill.add(s)


class Obstacles(pygame.sprite.Group):
    def __init__(self):
        super().__init__(self)

    def update(self, *args):
        for s in self.sprites():
            # TODO: Check collision
            return


class Animation:
    def __init__(self, images, speed):
        self.index = 0
        self.images = images
        self.speed = speed
        self.count = 0

    def update(self, sprite: pygame.sprite.Sprite):
        self.count += 1
        if self.count == self.speed:
            self.index += 1
            if self.index == len(self.images):
                self.index = 0
            sprite.image = self.images[self.index]

