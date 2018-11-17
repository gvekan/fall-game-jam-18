import pygame

import sprites
from vars import *


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
        self.kill = set()

