import pygame

import controller
import game_state
import graphics
from constants import *
import generator as g

def main():
    pygame.init()

    clock = pygame.time.Clock()

    state = game_state.State()

    screen = pygame.display.set_mode(WINDOW_SIZE)

    generator = g.Generator()

    while state.running:
        clock.tick(60)

        controller.handle_events(state)

        if state.reset:
            state = game_state.State()
            generator = g.Generator()

        generator.update(state) # Has to be before state.update()

        state.update()

        graphics.update_screen(screen, state)





if  __name__ == '__main__':
    main()