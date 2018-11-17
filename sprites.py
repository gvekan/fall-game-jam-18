import pygame
from constants import *

class All(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)

    def update(self, *args):
        for s in self.sprites():
            s.update()

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
            self.count = 0

class Player(pygame.sprite.Sprite, Animation):
    def __init__(self):
        """ Test
        images = []
        rgb = [(255,0,0), (0,255,0), (0,0,255)]
        for c in rgb:
            image = pygame.Surface([PLAYER_SIZE[0], PLAYER_SIZE[1]])
            image.fill(c)
            images.append(image)
        """

        images = [pygame.image.load("src/tr1.png"), pygame.image.load("src/tr2.png"), pygame.image.load("src/tr1.png"), pygame.image.load("src/tr3.png")]
        for i, image in enumerate(images):
            images[i] = pygame.transform.scale(image, PLAYER_SIZE)

        pygame.sprite.Sprite.__init__(self)
        Animation.__init__(self, images, 5)

        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.direction = Direction.STOP
        self.buffer = Direction.STOP
        self.speed_mult = 21

    def set_direction(self, d):
        if self.direction == Direction.STOP:
            self.direction = d
        else:
            if self.buffer == Direction.STOP:
                self.buffer = d
            elif self.buffer == (Direction.UP and d == Direction.DOWN) or (self.buffer == Direction.DOWN and d == Direction.UP):
                self.buffer = Direction.STOP

    def update(self, state):
        Animation.update(self, self)
        self.rect.y += self.direction.value * state.scroll_length * self.speed_mult
        if (self.rect.y - LANE_START_Y + LANE_HEIGHT//2 + PLAYER_SIZE[1]//2) % LANE_HEIGHT < state.scroll_length * self.speed_mult:
            if self.rect.y + PLAYER_SIZE[1]//2 < LANE_START_Y or self.rect.y + PLAYER_SIZE[1]//2 > LANE_START_Y + LANE_HEIGHT*N_LANES:
                state.game_over = True
            self.direction = self.buffer
            self.buffer = Direction.STOP




class ScrollObjects(pygame.sprite.Group):
    def __init__(self):
        super().__init__(self)

    def update(self, state):
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




