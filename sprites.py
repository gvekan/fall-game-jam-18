import pygame
from vars import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([PLAYER_SIZE[0], PLAYER_SIZE[1]])
        self.image.fill((255,255,255))
        self.speed_mult = 21

        self.rect = self.image.get_rect()
        self.direction = Direction.STOP

    def update(self, state):
        self.rect.y += self.direction.value * state.scroll_length * self.speed_mult
        #for h in range(LANE_START_Y+LANE_HEIGHT//2, LANE_START_Y*N_LANES+LANE_HEIGHT//2, LANE_HEIGHT):
        #    if (self.direction == Direction.UP and self.rect.y < h) or (self.direction == Direction.DOWN and self.rect.y > h):
        if (self.rect.y - LANE_START_Y + LANE_HEIGHT//2 + PLAYER_SIZE[1]//2) % LANE_HEIGHT < state.scroll_length * self.speed_mult:
            self.direction = Direction.STOP


class ScrollObjects(pygame.sprite.Group):
    def __init__(self):
        super().__init__(self)

    def update(self, state):
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


