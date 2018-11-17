from enum import Enum

WINDOW_SIZE = (1600, 900)
PLAYER_SIZE = (40, 20)
LANE_HEIGHT = 200
N_LANES = 3
LANE_START_Y = 200

class Direction(Enum):
    UP = -1
    STOP = 0
    DOWN = 1