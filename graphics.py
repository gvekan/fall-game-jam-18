import pygame

from constants import *

pygame.font.init()
def update_screen(screen, state):
    screen.fill((50 * state.era, 5 * state.era, 20 * state.era))  # background
    if state.game_over:
        myfont = pygame.font.SysFont('Comic Sans MS', 72)
        textsurface = myfont.render('GAME OVER, score: {}'.format(state.time//60), False, (255, 255, 255))
        screen.blit(textsurface, (100, 100))
    else:
        for i in range(3):
            pygame.draw.rect(screen, [128 - 32 * state.era, 127 + 32 * state.era, 0],
                [0, (i + 1) * LANE_HEIGHT, WINDOW_SIZE[0], LANE_HEIGHT - 1])  # lanes
        state.graphic.draw(screen)  # units

        pygame.draw.line(screen, (255,255,255), (WINDOW_SIZE[0]//2, LANE_START_Y//2), (WINDOW_SIZE[0]*3/4, LANE_START_Y//2), 5)
        for i, x in enumerate(range(WINDOW_SIZE[0]//2, (WINDOW_SIZE[0]*3)//4 +1, WINDOW_SIZE[0]//16)):
            pygame.draw.line(screen, (255, 255, 255), (x, LANE_START_Y // 2 - 10), (x, LANE_START_Y // 2 + 10), 5)
            if state.era == i:
                pygame.draw.circle(screen, (255, 0, 0), (x, LANE_START_Y//2), 20, 0)

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render('Time: {}'.format(state.time // 60), False, (255, 255, 255))
        screen.blit(textsurface, (100, 100))

    pygame.display.flip()  # update