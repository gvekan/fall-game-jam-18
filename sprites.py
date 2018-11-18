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
    def __init__(self, images, pos, hitboxes=SCENERY_HITBOX, offsets = [(0,0), (0,0), (0,0)], type:Hazard=None):
        if not isinstance(images, list):
            self.images = [[images], [images], [images]]
        else:
            self.images = images
        Animation.__init__(self, self.images[1], 5)
        pygame.sprite.Sprite.__init__(self)
        if not isinstance(hitboxes, list):
            self.hitboxes = [hitboxes, hitboxes, hitboxes]
        elif len(hitboxes) != 3:
            raise AttributeError("Hitboxes list needs three elements.")
        else:
            self.hitboxes = hitboxes

        self.offsets = offsets
        self.type = type
        self.image = self.animation[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.era = 1
        self.hitbox = self.hitboxes[1]
        self.offset = self.offsets[1]
        if isinstance(self.hitbox, list):
            for h in self.hitbox:
                h.midbottom = self.rect.midbottom
        else:
            self.hitbox.midbottom = self.rect.midbottom


    def update(self, state):
        if state.era != self.era: #TODO: Change rect for obstacles
            self.era = state.era
            self.animation = self.images[self.era]
            self.image = self.animation[0]
            self.hitbox = self.hitboxes[self.era]
            self.offset = self.offsets[self.era]

        if isinstance(self.hitbox, list):
            for i, h in enumerate(self.hitbox):
                h.midbottom = (self.rect.midbottom[0] + self.offset[i][0], self.rect.midbottom[1] + self.offset[i][1])
        else:
            self.hitbox.midbottom = (self.rect.midbottom[0] + self.offset[0], self.rect.midbottom[1] + self.offset[1])
        Animation.update(self, self)

    def collision(self, other):
        if isinstance(self.hitbox, list):
            for h in self.hitbox:
                if h.colliderect(other.hitbox):
                    return True
            return False
        else:
            return self.hitbox.colliderect(other.hitbox)



class Player(pygame.sprite.Sprite, Animation):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        Animation.__init__(self, IMG_PLAYER[1], 5)
        self.image = self.animation[0]
        self.rect = self.image.get_rect()
        self.direction = Direction.STOP
        self.buffer = Direction.STOP
        self.era = 1
        self.speed = 30
        self.hitbox = PLAYER_HITBOX
        self.hitbox.midbottom = self.rect.midbottom

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

        self.rect.y += self.direction.value * self.speed
        self.hitbox.midbottom = self.rect.midbottom
        Animation.update(self, self)
        if (self.hitbox.center[1] - LANE_START_Y + LANE_HEIGHT//2) % LANE_HEIGHT < self.speed:
            # Check if outside road
            if self.hitbox.y + PLAYER_SIZE[1]//2 < LANE_START_Y or self.rect.y + PLAYER_SIZE[1]//2 > LANE_START_Y + LANE_HEIGHT*N_LANES:
                state.game_over = True
                state.cause_of_death = Hazard.CRASH
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
            if s.collision(state.player):
                state.game_over = True
                if s.type:
                    state.cause_of_death = s.type





