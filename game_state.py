import random

import pygame

import sprites
from constants import *
from music import Music


class State:
    def __init__(self, go, music):
        self.time = 0
        self.era = 1
        self.score = 0
        self.cause_of_death = None
        self.player = sprites.Player()
        self.player.rect.x = PLAYER_X
        self.player.rect.y = LANE_START_Y + 1.5*LANE_HEIGHT - PLAYER_SIZE[1] + self.player.hitbox.height//2

        self.all_units = pygame.sprite.Group()

        self.obstacles = sprites.Obstacles()

        self.scroll_objects = sprites.ScrollObjects()

        self.graphic = pygame.sprite.LayeredUpdates()
        self.graphic.layers()

        road1 = sprites.AnimationSprite(IMG_ROAD, (0, 0))

        self.scroll_objects.add(road1)
        self.all_units.add(road1, self.player)
        self.graphic.add(road1, self.player)

        self.graphic.change_layer(self.player, 2)
        self.graphic.change_layer(road1, 0)

        self.music = music
        self.music.change(self.era)

        self.running = True  # True as long as the game should be running
        self.game_over = go
        self.reset = False
        self.kill = set()

    @property
    def time_sec(self):
        return self.time/30

    @property
    def scroll_length(self):
        start = 20
        top = 80
        div = 100  # lower div -> faster increase
        return int(start + (top-start) * self.time_sec / (div + self.time_sec) + self.era)

    def update(self):
        if not self.game_over:
            self.all_units.update(self)
            self.obstacles.update(self)
            self.scroll_objects.update(self)
            self.graphic.update(self)
            for unit in self.kill:
                unit.kill()
            self.time += 1
            self.score += self.scroll_length/100


    def time_travel(self, d):
        if d == Direction.DOWN:
            self.era -= 1
        elif d == Direction.UP:
            self.era += 1
        self.music.change(self.era)
        if self.era < 0:
            self.era = 0
            self.game_over = True
            self.cause_of_death = Hazard.TIME_TRAVEL
        elif self.era > 2:
            self.era = 2
            self.game_over = True
            self.cause_of_death = Hazard.TIME_TRAVEL




