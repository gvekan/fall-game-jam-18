import pygame

from constants import Direction


def handle_keydown(event, state):
    if event.key == pygame.K_UP:
        state.player.set_direction(Direction.UP)
    elif event.key == pygame.K_DOWN:
        state.player.set_direction(Direction.DOWN)
    elif event.key == pygame.K_z:
        state.time_travel(Direction.DOWN)
    elif event.key == pygame.K_x:
        state.time_travel(Direction.UP)
    elif event.key == pygame.K_r:
        state.reset()


def handle_events(state):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            handle_keydown(event, state)
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            state.running = False