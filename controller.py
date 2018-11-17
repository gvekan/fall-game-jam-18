import pygame

from vars import Direction


def handle_keydown(event, state):
    if event.key == pygame.K_UP:
        state.player.direction = Direction.UP
    elif event.key == pygame.K_DOWN:
        state.player.direction = Direction.DOWN
    elif event.key == pygame.K_z and state.era > 0:
        state.era -= 1
    elif event.key == pygame.K_x and state.era < 4:
        state.era += 1


def handle_events(state):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            handle_keydown(event, state)
        if event.type == pygame.QUIT:
            state.running = False