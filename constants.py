from enum import Enum
import pygame

WINDOW_SIZE = (1600, 900)
PLAYER_SIZE = (180, 160)
PLAYER_HITBOX = pygame.rect.Rect((0,0), (140, 100))
SCENERY_HITBOX = pygame.rect.Rect((0,0), (0,0))
PLAYER_X = 150
LANE_HEIGHT = 200
N_LANES = 3
LANE_START_Y = 200

DEBUG = False

IMG_MEDIEVAL_ROAD = [pygame.image.load("src/medieval_road.png")]
IMG_MEDIEVAL_PLAYER = [pygame.image.load("src/tr1.png"), pygame.image.load("src/tr2.png"), pygame.image.load("src/tr1.png"), pygame.image.load("src/tr3.png")]
for i, image in enumerate(IMG_MEDIEVAL_PLAYER):
    IMG_MEDIEVAL_PLAYER[i] = pygame.transform.scale(image, PLAYER_SIZE)

BACKGROUND_LAYER = 0
OBSTACLE_LAYER = 1
PLAYER_LAYER = 2

class Direction(Enum):
    UP = -1
    STOP = 0
    DOWN = 1