import pygame

import sprites
from constants import *


class State:
    def __init__(self):
        self.era = 2
        self.scroll_length = 2
        self.player = sprites.Player()
        self.player.rect.x = PLAYER_X
        self.player.rect.y = LANE_START_Y + 1.5*LANE_HEIGHT - PLAYER_SIZE[1]//2

        self.all_units = pygame.sprite.Group()

        self.obstacles = sprites.Obstacles()

        self.scroll_objects = sprites.ScrollObjects()

        self.graphic = pygame.sprite.LayeredUpdates()
        self.graphic.layers()

        images = [pygame.image.load("src/medieval_road.png")]
        road1 = sprites.AnimationSprite(images, (0, LANE_START_Y))

        images = [pygame.image.load("src/tr1.png")]
        images[0] = pygame.transform.scale(images[0], PLAYER_SIZE)
        test = sprites.AnimationSprite(images, (WINDOW_SIZE[0], LANE_START_Y + 1.5*LANE_HEIGHT - PLAYER_SIZE[1]//2))

        self.obstacles.add(test)
        self.scroll_objects.add(test, road1)
        self.all_units.add(test, road1, self.player)
        self.graphic.add(test, road1, self.player)

        self.graphic.change_layer(self.player, 2)
        self.graphic.change_layer(road1, 0)
        self.graphic.change_layer(test, 1)


        self.running = True  # True as long as the game should be running
        self.game_over = False
        self.kill = set()

    def reset(self):
        self.__init__()

    def update(self):
        self.all_units.update(self)
        self.obstacles.update(self)
        self.scroll_objects.update(self)
        self.graphic.update(self)

    def time_travel(self, d):
        if d == Direction.DOWN:
            self.era -= 1
        elif d == Direction.UP:
            self.era += 1
        if self.era < 1 or self.era > 3:
            self.game_over = True
