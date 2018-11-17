from enum import Enum
import pygame

WINDOW_SIZE = (1600, 900)
PLAYER_SIZE = (180, 160)
PLAYER_X = 150
LANE_HEIGHT = 200
N_LANES = 3
LANE_START_Y = 200

IMG_MEDIEVAL_ROAD = [pygame.image.load("src/medieval_road.png")]

BACKGROUND_LAYER = 0
OBSTACLE_LAYER = 1
PLAYER_LAYER = 2

class Direction(Enum):
    UP = -1
    STOP = 0
    DOWN = 1