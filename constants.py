import random
from enum import Enum
import pygame

from sprites import AnimationSprite

WINDOW_SIZE = (1600, 900)
PLAYER_SIZE = (180, 160)
PLAYER_HITBOX = pygame.rect.Rect((0,0), (140, 100))
SCENERY_HITBOX = pygame.rect.Rect((0,0), (0,0))
PLAYER_X = 150
LANE_HEIGHT = 200
N_LANES = 3
LANE_START_Y = 200

DEBUG = True

test1 = pygame.Surface((WINDOW_SIZE[0], LANE_HEIGHT*N_LANES))
test2 = pygame.Surface((200, 800))
test1.fill((169,169,169))
test2.fill((0,255,255))

IMG_ROAD = [[pygame.image.load("src/medieval_road.png")], [test1], [pygame.image.load("src/future_road.bmp")]]

IMG_MEDIEVAL_PLAYER = [pygame.image.load("src/tr1.png"), pygame.image.load("src/tr2.png"), pygame.image.load("src/tr1.png"), pygame.image.load("src/tr3.png")]
for i, image in enumerate(IMG_MEDIEVAL_PLAYER):
    IMG_MEDIEVAL_PLAYER[i] = pygame.transform.scale(image, PLAYER_SIZE)

IMG_PLAYER = [IMG_MEDIEVAL_PLAYER for _ in range(3)]

IMG_OBSTACLE = [[pygame.image.load("src/sheep.png")], [pygame.image.load("src/car.png")], [pygame.image.load("src/alien.png")]]
for i, image in enumerate(IMG_OBSTACLE):
    IMG_OBSTACLE[i][0] = pygame.transform.scale(image[0], PLAYER_SIZE)

#OBSTACLES = [AnimationSprite(IMG_OBSTACLE,
#                             (WINDOW_SIZE[0], LANE_START_Y + (random.randint(1, N_LANES)-.5)*LANE_HEIGHT - PLAYER_SIZE[1]//2),
#                             [pygame.rect.Rect((1000,1000), (140,100)),pygame.rect.Rect((1000,1000), (140,100)),pygame.rect.Rect((1000,1000), (140,100))],
#                             [(0,0),(0,0),(0,0)]),
             #AnimationSprite(IMG_PLAYER,
             #                (WINDOW_SIZE[0], 0),
             #                [pygame.rect.Rect((1000, 1000), (140, 600)), pygame.rect.Rect((1000, 1000), (140, 400)), pygame.rect.Rect((1000, 1000), (140, 0))],
             #                [(0,0), (0,-200), (0,0)])
    #         ]

BACKGROUND_LAYER = 0
OBSTACLE_LAYER = 1
PLAYER_LAYER = 2

class Direction(Enum):
    UP = -1
    STOP = 0
    DOWN = 1