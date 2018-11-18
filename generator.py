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
            self.obstacle_next_x = w+self.obstacle_next_x+250*(1+random.random())



    def add_road(self, state: State):
        r = AnimationSprite(IMG_ROAD, (WINDOW_SIZE[0]+self.road_next_x+state.scroll_length, 0))
        state.all_units.add(r)
        state.scroll_objects.add(r)
        state.graphic.add(r)
        state.graphic.change_layer(r, BACKGROUND_LAYER)


    def add_obstacle(self, state: State):
        obj = random.choices([self.get_hazard(Hazard.FAN),
                              self.get_hazard(Hazard.CASTLE),
                              self.get_hazard(Hazard.RIVER)],
                             weights=[4, 1, 1])[0]
        state.all_units.add(obj)
        state.scroll_objects.add(obj)
        state.obstacles.add(obj)
        state.graphic.add(obj)
        state.graphic.change_layer(obj, OBSTACLE_LAYER)
        return obj.hitbox.width


    def get_hazard(self, hazard: Hazard, version=0) -> AnimationSprite:
        if version < 0 or version > 3:
            raise AttributeError("Version number needs to be 0 (random) or 1-3")
        if version == 0:
            version = random.randint(1, 3)

        if hazard == Hazard.FAN:
            y = LANE_START_Y + (version-.5)*LANE_HEIGHT - PLAYER_SIZE[1]//2
            return AnimationSprite(IMG_OBSTACLE,
                                   (WINDOW_SIZE[0], y),
                                   pygame.rect.Rect((1000, 1000), (140, 100)),
                                   type=hazard)

        if hazard == Hazard.CASTLE:
            return AnimationSprite(IMG_CASTLE,
                                   (WINDOW_SIZE[0], 0),
                                   [pygame.rect.Rect((1000, 1000), (400, 600)),
                                    pygame.rect.Rect((1000, 1000), (400, 400)),
                                    pygame.rect.Rect((1000, 1000), (400, 000))],
                                   [(0, 0), (0, -200), (0, 0)],
                                   type=hazard)

        if hazard == Hazard.RIVER:
            if version == 1:
                past_hitbox = pygame.rect.Rect((1000, 1000), (200, 600))
                past_offset = (0,0)
            elif version == 2:
                past_hitbox = [pygame.rect.Rect((1000, 1000), (200, 400)),pygame.rect.Rect((1000, 1000), (200, 400))]
                past_offset = [(0,0),(0,-600)]
            elif version == 3:
                past_hitbox = pygame.rect.Rect((1000, 1000), (200, 600))
                past_offset = (0,-400)
            return AnimationSprite(self.test_sprite((400,1000)),
                                   (WINDOW_SIZE[0], 0),
                                   [past_hitbox,
                                    pygame.rect.Rect((1000, 1000), (200, 1000)),
                                    pygame.rect.Rect((1000, 1000), (200, 1000))],
                                   [past_offset, (0, 0), (0, 0)],
                                   type=hazard)

    def test_sprite(self, size):
        return pygame.transform.scale(IMG_TEST, size)