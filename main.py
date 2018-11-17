import pygame

import controller
import game_state
import graphics
from constants import *

def main():
    pygame.init()

    clock = pygame.time.Clock()

    state = game_state.State()

    screen = pygame.display.set_mode(WINDOW_SIZE)

    while state.running:
        clock.tick(60)

        controller.handle_events(state)

        state.update()

        graphics.update_screen(screen, state)




if  __name__ == '__main__':
    main()