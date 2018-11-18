import pygame

from constants import *

pygame.font.init()
def update_screen(screen, state):
    screen.fill((150,0,255))  # background
    if state.game_over:

        screen.blit(IMG_ROAD[state.era][0], (0,0))
        myfont = pygame.font.SysFont('Comic Sans MS', 72)
        gameover = myfont.render('GAME OVER - Score: {} (Death by {})'.format(int(state.score), state.cause_of_death.name), False, (255, 255, 255))
        retry = myfont.render('Press SPACE to retry', False, (255, 255, 255))
        screen.blit(gameover, (100, LANE_START_Y//2-36))
        screen.blit(retry, (100, LANE_START_Y//2+36))
    else:
        state.graphic.draw(screen)  # units
        if DEBUG:
            for u in state.all_units:
                if isinstance(u.hitbox, list):
                    for h in u.hitbox:
                        pygame.draw.rect(screen, (255, 0, 127), [h.x, h.y, h.width, h.height], 4)
                else:
                    pygame.draw.rect(screen, (255,0,127), [u.hitbox.x, u.hitbox.y, u.hitbox.width, u.hitbox.height], 4)

        # Draw timeline
        pygame.draw.line(screen, (255,255,255), (WINDOW_SIZE[0]//2, LANE_START_Y//2), (WINDOW_SIZE[0]*3/4, LANE_START_Y//2), 5)
        for i, x in enumerate(range(WINDOW_SIZE[0]//2+ WINDOW_SIZE[0]//16, (WINDOW_SIZE[0]*3)//4- WINDOW_SIZE[0]//16 +1, WINDOW_SIZE[0]//16)):
            pygame.draw.line(screen, (255, 255, 255), (x, LANE_START_Y // 2 - 10), (x, LANE_START_Y // 2 + 10), 5)
            if state.era == i:
                pygame.draw.circle(screen, (255, 0, 0), (x, LANE_START_Y//2), 20, 0)

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        stats = myfont.render('Time: {}, Speed: {}'.format(int(state.score), int(state.scroll_length)), False, (255, 255, 255))
        controlls = myfont.render('Move: UP/DOWN         Time Travel: Z/X', False, (255, 255, 255))
        screen.blit(stats, (100, LANE_START_Y//2 - 15))
        screen.blit(controlls, (100, WINDOW_SIZE[1] - LANE_START_Y//2 - 15))

    pygame.display.flip()  # update