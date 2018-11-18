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
DEBUG = False

pygame.display.init()
pygame.display.set_mode()

IMG_ROAD = [[pygame.image.load("src/past_road.bmp").convert_alpha()],
            [pygame.image.load("src/present_road.bmp").convert_alpha()],
            [pygame.image.load("src/future_road2.bmp").convert_alpha()]]

IMG_MEDIEVAL_PLAYER = [pygame.image.load("src/tr1.png").convert_alpha(),
                       pygame.image.load("src/tr2.png").convert_alpha(),
                       pygame.image.load("src/tr1.png").convert_alpha(),
                       pygame.image.load("src/tr3.png").convert_alpha()]
for i, image in enumerate(IMG_MEDIEVAL_PLAYER):
    IMG_MEDIEVAL_PLAYER[i] = pygame.transform.scale(image, PLAYER_SIZE)

IMG_PRESENT_PLAYER = [pygame.image.load("src/tr_nu.png").convert_alpha(),
                       pygame.image.load("src/tr_nu2.png").convert_alpha(),
                       pygame.image.load("src/tr_nu3.png").convert_alpha(),
                       pygame.image.load("src/tr_nu4.png").convert_alpha()]
for i, image in enumerate(IMG_PRESENT_PLAYER):
    IMG_PRESENT_PLAYER[i] = pygame.transform.scale(image, PLAYER_SIZE)

IMG_FUTURE_PLAYER = [pygame.image.load("src/tr_sen1.png").convert_alpha(),
                       pygame.image.load("src/tr_sen2.png").convert_alpha(),
                       pygame.image.load("src/tr_sen3.png").convert_alpha(),
                       pygame.image.load("src/tr_sen2.png").convert_alpha()]
for i, image in enumerate(IMG_FUTURE_PLAYER):
    IMG_FUTURE_PLAYER[i] = pygame.transform.scale(image, PLAYER_SIZE)

IMG_PLAYER = [IMG_MEDIEVAL_PLAYER, IMG_PRESENT_PLAYER, IMG_FUTURE_PLAYER]

IMG_FAN = [[pygame.image.load("src/past_fans.png").convert_alpha()],
           [pygame.image.load("src/present_fans.png").convert_alpha()],
           [pygame.image.load("src/future_fans.png").convert_alpha()]]
for i, image in enumerate(IMG_FAN):
    IMG_FAN[i][0] = pygame.transform.scale(image[0], PLAYER_SIZE)

IMG_CASTLE = [[pygame.image.load("src/castle1.png").convert_alpha()],
              [pygame.image.load("src/castle2.png").convert_alpha()],
              [pygame.image.load("src/castle3.png").convert_alpha()]]

IMG_TEST = pygame.image.load("src/test.png").convert_alpha()
IMG_START = pygame.image.load("src/start_screen.png").convert_alpha()

IMG_GLITCH = [pygame.image.load("src/glitch1.bmp").convert_alpha(),
              pygame.image.load("src/glitch2.bmp").convert_alpha(),
              pygame.image.load("src/glitch3.bmp").convert_alpha()]

IMG_RIVER1 = [[pygame.image.load("src/bridge1.bmp").convert_alpha()],
              [pygame.image.load("src/river1.bmp").convert_alpha()],
             IMG_GLITCH]
IMG_RIVER2 = [[pygame.image.load("src/bridge2.bmp").convert_alpha()],
              [pygame.image.load("src/river2.bmp").convert_alpha()],
             IMG_GLITCH]
IMG_RIVER3 = [[pygame.image.load("src/bridge3.bmp").convert_alpha()],
              [pygame.image.load("src/river3.bmp").convert_alpha()],
             IMG_GLITCH]

IMG_DEATH_TIME_TRAVEL = [pygame.image.load("src/past_cod_tt.bmp").convert_alpha(),
                         None,
                         pygame.image.load("src/death_by_future.bmp").convert_alpha()]
IMG_DEATH_FAN = [pygame.image.load("src/past_cod_fans.bmp").convert_alpha(),
                 pygame.image.load("src/present_cod_fans.bmp").convert_alpha(),
                 pygame.image.load("src/future_cod_fans.bmp").convert_alpha()]
IMG_DEATH_RIVER = [pygame.image.load("src/past_cod_river.bmp").convert_alpha(),
                 pygame.image.load("src/present_cod_river.bmp").convert_alpha(),
                 pygame.image.load("src/future_cod_river.bmp").convert_alpha()]
IMG_DEATH_CASTLE = [pygame.image.load("src/past_cod_castle.bmp").convert_alpha(),
                 pygame.image.load("src/present_cod_castle.bmp").convert_alpha(),
                 None]

BACKGROUND_LAYER = 0
OBSTACLE_LAYER = 1
PLAYER_LAYER = 2

class Direction(Enum):
    UP = -1
    STOP = 0
    DOWN = 1

class Hazard(Enum):
    TIME_TRAVEL = -1
    CRASH = 0
    FAN = 1
    CASTLE = 2
    RIVER = 3

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
PINK=(255,0,255)
TURQUOISE=(0,255,255)