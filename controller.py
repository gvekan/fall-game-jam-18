import pygame


def handle(event, player, state):
    if event.key == pygame.K_UP and player.lane > 0:
        player.lane -= 1
    elif event.key == pygame.K_DOWN and player.lane < 4:
        player.lane += 1
    elif event.key == pygame.K_z and state.era > 0:
        state.era -= 1
    elif event.key == pygame.K_x and state.era < 4:
        state.era += 1