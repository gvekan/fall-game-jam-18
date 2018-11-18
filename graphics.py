import pygame

from constants import *

pygame.font.init()


def death_screen(cause_of_death, era):
    if cause_of_death == Hazard.TIME_TRAVEL:
        return IMG_DEATH_TIME_TRAVEL[era]
    if cause_of_death == Hazard.FAN:
        return IMG_DEATH_FAN[era]
    if cause_of_death == Hazard.RIVER:
        return IMG_DEATH_RIVER[era]
    if cause_of_death == Hazard.CASTLE:
        return IMG_DEATH_CASTLE[era]
    return IMG_ROAD[era][0]


def update_screen(screen, state):
    screen.fill((150,0,255))  # background
    if state.game_over:

        screen.blit(death_screen(state.cause_of_death, state.era), (0,0))

        myfont = pygame.font.SysFont('Copperplate Gothic', 72)
        gameover = myfont.render('GAME OVER - Score: {}'.format(int(state.score)), False, WHITE)
        retry = myfont.render('Press SPACE to retry', False, WHITE)
        screen.blit(gameover, (100, LANE_START_Y//2-36))
        screen.blit(retry, (100, LANE_START_Y//2+36))
    else:
        state.graphic.draw(screen)  # units
        if DEBUG:
            for u in state.all_units:
                if isinstance(u.hitbox, list):
                    for h in u.hitbox:
                        pygame.draw.rect(screen, PINK, [h.x, h.y, h.width, h.height], 4)
                else:
                    pygame.draw.rect(screen, PINK, [u.hitbox.x, u.hitbox.y, u.hitbox.width, u.hitbox.height], 4)
                #pygame.draw.rect(screen, GREEN, [u.rect.x, u.rect.y, u.rect.width, u.rect.height], 1)

        # Draw timeline
        pygame.draw.line(screen,WHITE, (WINDOW_SIZE[0]//2, LANE_START_Y//2), (WINDOW_SIZE[0]*3/4, LANE_START_Y//2), 5)
        for i, x in enumerate(range(WINDOW_SIZE[0]//2+ WINDOW_SIZE[0]//16, (WINDOW_SIZE[0]*3)//4- WINDOW_SIZE[0]//16 +1, WINDOW_SIZE[0]//16)):
            pygame.draw.line(screen, WHITE, (x, LANE_START_Y // 2 - 10), (x, LANE_START_Y // 2 + 10), 5)
            if state.era == i:
                pygame.draw.circle(screen, RED, (x, LANE_START_Y//2), 20, 0)

        myfont = pygame.font.SysFont('Copperplate Gothic', 30)
        stats = myfont.render('Score: {}        Speed: {}'.format(int(state.score), int(state.scroll_length)), False, WHITE)
        controlls = myfont.render('Move: UP/DOWN        Time Travel: Z/X', False, WHITE)
        screen.blit(stats, (100, LANE_START_Y//2 - 15))
        screen.blit(controlls, (100, WINDOW_SIZE[1] - LANE_START_Y//2 - 15))

    pygame.display.flip()  # update