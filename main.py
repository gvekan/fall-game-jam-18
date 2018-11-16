import pygame
import sprites

WINDOW_SIZE = (1600,900)

def main():
    pygame.init()

    screen = pygame.display.set_mode(WINDOW_SIZE)
    player = sprites.Player()
    player.rect.x = 40
    player.rect.y = int(WINDOW_SIZE[1] / 2 + sprites.PLAYER_SIZE[1] / 2)
    all = pygame.sprite.Group()
    all.add(player)
    running = True  # True as long as the game should be running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        all.draw(screen)
        pygame.display.flip()


main()