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
        state.graphic.draw(screen)  # units
        if DEBUG:
            for u in state.all_units:
                pygame.draw.rect(screen, (0,255,0), [u.hitbox.x, u.hitbox.y, u.hitbox.width, u.hitbox.height], 2)

        # Draw timeline
        pygame.draw.line(screen, (255,255,255), (WINDOW_SIZE[0]//2, LANE_START_Y//2), (WINDOW_SIZE[0]*3/4, LANE_START_Y//2), 5)
        for i, x in enumerate(range(WINDOW_SIZE[0]//2, (WINDOW_SIZE[0]*3)//4 +1, WINDOW_SIZE[0]//16)):
            pygame.draw.line(screen, (255, 255, 255), (x, LANE_START_Y // 2 - 10), (x, LANE_START_Y // 2 + 10), 5)
            if state.era == i:
                pygame.draw.circle(screen, (255, 0, 0), (x, LANE_START_Y//2), 20, 0)

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render('Time: {}'.format(state.time // 60), False, (255, 255, 255))
        screen.blit(textsurface, (100, LANE_START_Y//2 - 15))

    pygame.display.flip()  # update