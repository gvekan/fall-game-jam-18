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

test1 = pygame.Surface((WINDOW_SIZE[0], LANE_HEIGHT*N_LANES))
test2 = pygame.Surface((WINDOW_SIZE[0], LANE_HEIGHT*N_LANES))
test1.fill((169,169,169))
test2.fill((0,255,255))

IMG_ROAD = [[pygame.image.load("src/medieval_road.png")], [pygame.image.load("src/present_road.bmp")], [test2]]
DEBUG = True

IMG_MEDIEVAL_PLAYER = [pygame.image.load("src/tr1.png"), pygame.image.load("src/tr2.png"), pygame.image.load("src/tr1.png"), pygame.image.load("src/tr3.png")]
for i, image in enumerate(IMG_MEDIEVAL_PLAYER):
    IMG_MEDIEVAL_PLAYER[i] = pygame.transform.scale(image, PLAYER_SIZE)


IMG_PLAYER = [IMG_MEDIEVAL_PLAYER for _ in range(3)]

IMG_OBSTACLE = [[pygame.image.load("src/sheep.png")], [pygame.image.load("src/car.png")], [pygame.image.load("src/alien.png")]]
for i, image in enumerate(IMG_OBSTACLE):
    IMG_OBSTACLE[i][0] = pygame.transform.scale(image[0], PLAYER_SIZE)

BACKGROUND_LAYER = 0
OBSTACLE_LAYER = 1
PLAYER_LAYER = 2

class Direction(Enum):
    UP = -1
    STOP = 0
    DOWN = 1