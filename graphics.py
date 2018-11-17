import pygame

import vars


def update_screen(screen, state):
    screen.fill((50 * state.era, 5 * state.era, 20 * state.era))  # background
    for i in range(3):
        pygame.draw.rect(screen, [128 - 32 * state.era, 127 + 32 * state.era, 0],
                         [0, (i + 1) * vars.LANE_HEIGHT, vars.WINDOW_SIZE[0], vars.LANE_HEIGHT - 1])  # lanes
    state.all_units.draw(screen)  # units
    pygame.display.flip()  # update