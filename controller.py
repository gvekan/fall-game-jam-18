import pygame

from constants import Direction

def handle_keydown(event, state):

    if not state.game_over:
        if event.key == pygame.K_UP:
            state.player.set_direction(Direction.UP)
        elif event.key == pygame.K_DOWN:
            state.player.set_direction(Direction.DOWN)
        elif event.key == pygame.K_z:
            state.time_travel(Direction.DOWN)
        elif event.key == pygame.K_x:
            state.time_travel(Direction.UP)
    if event.key == pygame.K_r or (event.key == pygame.K_SPACE and state.game_over):
        state.reset = True


def handle_events(state):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            handle_keydown(event, state)
        if event.type == pygame.QUIT:
            state.running = False
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            if is_playing(state):
                state.cause_of_death = None
            else:
                state.running = False

def is_playing(state):
    return (state.game_over and state.cause_of_death) or (not state.game_over)