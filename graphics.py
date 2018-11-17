import pygame

from constants import *

pygame.font.init()
def update_screen(screen, state):
    screen.fill((150,0,255))  # background
    if state.game_over:
        if state.era == -1:
            e = 0
        elif state.era ==3:
            e = 2
        else:
            e = state.era
        screen.blit(IMG_ROAD[e][0], (0,0))
        myfont = pygame.font.SysFont('Comic Sans MS', 72)
        textsurface = myfont.render('GAME OVER, score: {}'.format(state.score), False, (255, 255, 255))
        screen.blit(textsurface, (100, 100))
    else:
        state.graphic.draw(screen)  # units
        if DEBUG:
            for u in state.all_units:
                pygame.draw.rect(screen, (255,0,127), [u.hitbox.x, u.hitbox.y, u.hitbox.width, u.hitbox.height], 4)

        # Draw timeline
        pygame.draw.line(screen, (255,255,255), (WINDOW_SIZE[0]//2, LANE_START_Y//2), (WINDOW_SIZE[0]*3/4, LANE_START_Y//2), 5)
        for i, x in enumerate(range(WINDOW_SIZE[0]//2+ WINDOW_SIZE[0]//16, (WINDOW_SIZE[0]*3)//4- WINDOW_SIZE[0]//16 +1, WINDOW_SIZE[0]//16)):
            pygame.draw.line(screen, (255, 255, 255), (x, LANE_START_Y // 2 - 10), (x, LANE_START_Y // 2 + 10), 5)
            if state.era == i:
                pygame.draw.circle(screen, (255, 0, 0), (x, LANE_START_Y//2), 20, 0)

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render('Time: {}'.format(state.score), False, (255, 255, 255))
        screen.blit(textsurface, (100, LANE_START_Y//2 - 15))

    pygame.display.flip()  # update