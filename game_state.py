import pygame

import sprites
from constants import *


class State:
    def __init__(self):
        self.era = 2
        self.scroll_length = 1
        self.player = sprites.Player()
        self.player.rect.x = PLAYER_X
        self.player.rect.y = LANE_START_Y + 1.5*LANE_HEIGHT - PLAYER_SIZE[1]//2
        self.all_units = pygame.sprite.Group()
        self.all_units.add(self.player)
        self.running = True  # True as long as the game should be running
        self.game_over = False
        self.kill = set()

    def reset(self):
        self.__init__()

    def time_travel(self, d):
        if d == Direction.DOWN:
            self.era -= 1
        elif d == Direction.UP:
            self.era += 1
        if self.era < 1 or self.era > 3:
            self.game_over = True
