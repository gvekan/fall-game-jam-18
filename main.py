import pygame

import controller
import sprites
from game_state import state
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    player = sprites.Player()
    player.rect.x = 40
    player.rect.y = int(LANE_HEIGHT * player.lane + LANE_HEIGHT / 2 - PLAYER_SIZE[1] / 2)
    all_units = pygame.sprite.Group()
    all_units.add(player)
    running = True  # True as long as the game should be running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                controller.handle(event, player, state)
            if event.type == pygame.QUIT:
                running = False
        player.rect.y = int(LANE_HEIGHT * player.lane + LANE_HEIGHT / 2 - PLAYER_SIZE[1] / 2)

        screen.fill((50*state.era, 5*state.era, 20*state.era)) # background
        for i in range(3):
            pygame.draw.rect(screen, [128 - 32*state.era, 127 + 32*state.era, 0], [0, (i + 1) * LANE_HEIGHT, WINDOW_SIZE[0], LANE_HEIGHT - 1]) # lanes
        all_units.draw(screen) # units
        pygame.display.flip() # update

        clock.tick(60)


if  __name__ == '__main__':
    main()