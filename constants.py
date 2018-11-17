from enum import Enum
import pygame




WINDOW_SIZE = (1600, 1000)
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


pygame.display.init()
pygame.display.set_mode()

IMG_ROAD = [[pygame.image.load("src/medieval_road.png").convert_alpha()],
            [pygame.image.load("src/present_road.bmp").convert_alpha()],
            [pygame.image.load("src/future_road.bmp").convert_alpha()]]
DEBUG = True

IMG_MEDIEVAL_PLAYER = [pygame.image.load("src/tr1.png").convert_alpha(),
                       pygame.image.load("src/tr2.png").convert_alpha(),
                       pygame.image.load("src/tr1.png").convert_alpha(),
                       pygame.image.load("src/tr3.png").convert_alpha()]
for i, image in enumerate(IMG_MEDIEVAL_PLAYER):
    IMG_MEDIEVAL_PLAYER[i] = pygame.transform.scale(image, PLAYER_SIZE)

SPACE = 200
IMG_BOTTOM_PART = [[pygame.image.load("src/medieval_bottom_part.bmp").convert_alpha()],
                   [pygame.image.load("src/medieval_bottom_part.bmp").convert_alpha()],
                   [pygame.image.load("src/medieval_bottom_part.bmp").convert_alpha()]]


IMG_PLAYER = [IMG_MEDIEVAL_PLAYER for _ in range(3)]

IMG_OBSTACLE = [[pygame.image.load("src/sheep.png").convert_alpha()],
                [pygame.image.load("src/car.png").convert_alpha()],
                [pygame.image.load("src/alien.png").convert_alpha()]]
for i, image in enumerate(IMG_OBSTACLE):
    IMG_OBSTACLE[i][0] = pygame.transform.scale(image[0], PLAYER_SIZE)

IMG_CASTLE = [[pygame.image.load("src/castle1.png").convert_alpha()],
              [pygame.image.load("src/castle2.png").convert_alpha()],
              [pygame.image.load("src/castle3.png").convert_alpha()]]

BACKGROUND_LAYER = 0
OBSTACLE_LAYER = 1
PLAYER_LAYER = 2

class Direction(Enum):
    UP = -1
    STOP = 0
    DOWN = 1
