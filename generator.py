from game_state import State
from constants import *
from sprites import *
import random

class Generator:
    def __init__(self):
        self.road_next_x = 0
        self.part_next_x = 0

    def update(self, state):
        self.road_next_x -= state.scroll_length
        if self.road_next_x <= 0:
            self.add_road(state)
            self.road_next_x = WINDOW_SIZE[0]+self.road_next_x

        self.part_next_x -= state.scroll_length
        if self.part_next_x <= 0:
            # TODO: add big obstacle or background part as add_road()
            self.add_obstacle(state)
            self.part_next_x = LANE_HEIGHT*2+self.part_next_x


    def add_road(self, state: State):
        r = AnimationSprite(IMG_ROAD, (WINDOW_SIZE[0]+self.road_next_x+state.scroll_length, LANE_START_Y))
        state.all_units.add(r)
        state.scroll_objects.add(r)
        state.graphic.add(r)
        state.graphic.change_layer(r, BACKGROUND_LAYER)


    def add_obstacle(self, state: State):
        obj = AnimationSprite(IMG_OBSTACLE, (WINDOW_SIZE[0], LANE_START_Y + (random.randint(1, N_LANES)-.5)*LANE_HEIGHT - PLAYER_SIZE[1]//2))
        state.all_units.add(obj)
        state.scroll_objects.add(obj)
        state.obstacles.add(obj)
        state.graphic.add(obj)
        state.graphic.change_layer(obj, OBSTACLE_LAYER)