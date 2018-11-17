from game_state import State
from constants import *
from sprites import *
import random

class Generator:
    def __init__(self):
        self.road_next_x = 0
        self.part_next_x = 0
        self.obstacle_next_x = 0

    def update(self, state):
        self.road_next_x -= state.scroll_length
        if self.road_next_x <= 0:
            self.add_road(state)
            self.road_next_x = WINDOW_SIZE[0]+self.road_next_x


        self.obstacle_next_x -= state.scroll_length
        if self.obstacle_next_x <= 0:
            w = self.add_obstacle(state)
            self.obstacle_next_x = w+random.random()*3*SPACE+self.obstacle_next_x



    def add_road(self, state: State):
        r = AnimationSprite(IMG_ROAD, (WINDOW_SIZE[0]+self.road_next_x+state.scroll_length, 0))
        state.all_units.add(r)
        state.scroll_objects.add(r)
        state.graphic.add(r)
        state.graphic.change_layer(r, BACKGROUND_LAYER)


    def add_obstacle(self, state: State):
        animal = AnimationSprite(IMG_OBSTACLE,
                                 (WINDOW_SIZE[0], LANE_START_Y + (random.randint(1, N_LANES)-.5)*LANE_HEIGHT - PLAYER_SIZE[1]//2),
                                 [pygame.rect.Rect((1000,1000), (140,100)),
                                  pygame.rect.Rect((1000,1000), (140,100)),
                                  pygame.rect.Rect((1000,1000), (140,100))],
                                 [(0,0),(0,0),(0,0)])
        castle = AnimationSprite(IMG_CASTLE,
                                 (WINDOW_SIZE[0], 0),
                                 [pygame.rect.Rect((1000, 1000), (400, 600)),
                                  pygame.rect.Rect((1000, 1000), (400, 400)),
                                  pygame.rect.Rect((1000, 1000), (400, 000))],
                                 [(0, 0), (0, -200), (0, 0)])
        obj = random.choice([animal, animal, animal, animal, castle])
        state.all_units.add(obj)
        state.scroll_objects.add(obj)
        state.obstacles.add(obj)
        state.graphic.add(obj)
        state.graphic.change_layer(obj, OBSTACLE_LAYER)
        return obj.hitbox.width