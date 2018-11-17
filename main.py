import pygame

import controller
import game_state
import graphics
from constants import *
import generator as g
import os
import ctypes
def main():
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (screensize[0]//2-WINDOW_SIZE[0]//2 , screensize[1]//2-WINDOW_SIZE[1]//2-10)

    pygame.init()
    pygame.mixer.init()

    clock = pygame.time.Clock()

    state = game_state.State()

    screen = pygame.display.set_mode(WINDOW_SIZE)
    generator = g.Generator()

    while state.running:
        clock.tick(30)

        controller.handle_events(state)

        if state.reset:
            state = game_state.State()
            generator = g.Generator()

        generator.update(state) # Has to be before state.update()

        state.update()

        graphics.update_screen(screen, state)





if  __name__ == '__main__':
    main()