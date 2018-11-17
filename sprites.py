import pygame
from constants import *

class Animation:
    def __init__(self, animation, speed):
        self.index = 0
        self.animation = animation
        self.speed = speed
        self.count = 0


    def update(self, sprite: pygame.sprite.Sprite):
        if len(self.animation) > 1:
            self.count += 1
            if self.count == self.speed:
                self.index += 1
                if self.index == len(self.animation):
                    self.index = 0
                sprite.image = self.animation[self.index]
                self.count = 0


class AnimationSprite(pygame.sprite.Sprite, Animation):
    def __init__(self, images, pos):
        Animation.__init__(self, images[1], 5)
        pygame.sprite.Sprite.__init__(self)

        self.images = images
        self.image = self.animation[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.era = 1

    def update(self, state):
        if state.era != self.era: #TODO: Change rect for obstacles
            self.era = state.era
            self.animation = self.images[self.era]
            self.image = self.animation[0]
            print(str(self.era) + "\n")
        Animation.update(self, self)



class Player(pygame.sprite.Sprite, Animation):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        Animation.__init__(self, IMG_PLAYER[1], 5)
        print(str(IMG_PLAYER))
        self.image = self.animation[0]
        self.rect = self.image.get_rect()
        self.direction = Direction.STOP
        self.buffer = Direction.STOP
        self.speed = 10
        self.era = 1

    def set_direction(self, d):
        if self.direction == Direction.STOP:
            self.direction = d
        else:
            if self.buffer == Direction.STOP:
                self.buffer = d
            elif self.buffer == (Direction.UP and d == Direction.DOWN) or (self.buffer == Direction.DOWN and d == Direction.UP):
                self.buffer = Direction.STOP

    def update(self, state):
        if state.era != self.era:
            self.era = state.era
            self.animation = IMG_PLAYER[self.era]
            self.image = self.animation[0]
        Animation.update(self, self)
        self.rect.y += self.direction.value * self.speed
        if (self.rect.y - LANE_START_Y + LANE_HEIGHT//2 + PLAYER_SIZE[1]//2) % LANE_HEIGHT < self.speed:
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

    def update(self, state):
        for s in self.sprites():
            if s.rect.colliderect(state.player.rect):
                state.game_over = True





