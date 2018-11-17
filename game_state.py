import random

import pygame

import sprites
from constants import *
from music import Music


class State:
    def __init__(self):
        self.time = 0
        self.era = 1
        self.player = sprites.Player()
        self.player.rect.x = PLAYER_X
        self.player.rect.y = LANE_START_Y + 1.5*LANE_HEIGHT - PLAYER_SIZE[1] + self.player.hitbox.height//2

        self.all_units = pygame.sprite.Group()

        self.obstacles = sprites.Obstacles()

        self.scroll_objects = sprites.ScrollObjects()

        self.graphic = pygame.sprite.LayeredUpdates()
        self.graphic.layers()

        road1 = sprites.AnimationSprite(IMG_ROAD, (0, LANE_START_Y))

        self.scroll_objects.add(road1)
        self.all_units.add(road1, self.player)
        self.graphic.add(road1, self.player)

        self.set_bottom()

        self.graphic.change_layer(self.player, 2)
        self.graphic.change_layer(road1, 0)

        self.music = Music()
        self.music.change(self.era)

        self.running = True  # True as long as the game should be running
        self.game_over = False
        self.reset = False
        self.kill = set()

    @property
    def score(self):
        return self.time//30

    @property
    def scroll_length(self):
        return 14 + self.time//300

    def update(self):
        if not self.game_over:
            self.all_units.update(self)
            self.obstacles.update(self)
            self.scroll_objects.update(self)
            self.graphic.update(self)
            for unit in self.kill:
                unit.kill()
            self.time += 1


    def time_travel(self, d):
        if d == Direction.DOWN:
            self.era -= 1
        elif d == Direction.UP:
            self.era += 1
        self.music.change(self.era)
        if self.era < 0 or self.era > 2:
            self.game_over = True

    def set_bottom(self):
        for x in range(0,WINDOW_SIZE[0], 200):
            a = sprites.AnimationSprite(IMG_BOTTOM_PART, (x, WINDOW_SIZE[1]-LANE_HEIGHT))
            self.scroll_objects.add(a)
            self.all_units.add(a, self.player)
            self.graphic.add(a, self.player)
            self.graphic.change_layer(a, BACKGROUND_LAYER)


