from game_state import State
from constants import *
from sprites import *

class Handler:
    def __init__(self, state: State):
        self.road_next_x = WINDOW_SIZE[0] - state.scroll_length

    def tick(self, state):
        self.road_next_x -= state.scroll_length
        if self.road_next_x <= 0:
            self.add_road(state)

    def add_road(self, state: State):
        r = AnimationSprite(IMG_MEDIEVAL_ROAD, (WINDOW_SIZE[0]+self.road_next_x-state.scroll_length, LANE_START_Y))
        state.all_units.add(r)
        state.scroll_objects.add(r)
        state.graphic.add(r)
        state.graphic.change_layer(r, 0)