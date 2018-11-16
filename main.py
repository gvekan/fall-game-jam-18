import pygame
import sprites

WINDOW_SIZE = (1600, 900)

def main():
    pygame.init()

    screen = pygame.display.set_mode(WINDOW_SIZE)
    player = sprites.Player()
    player.rect.x = 40
    player.rect.y = int(sprites.LANE_SIZE * player.lane + sprites.LANE_SIZE / 2 - sprites.PLAYER_SIZE[1] / 2)
    all_units = pygame.sprite.Group()
    all_units.add(player)
    running = True  # True as long as the game should be running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.lane -= 1
                elif event.key == pygame.K_DOWN:
                    player.lane += 1
            if event.type == pygame.QUIT:
                running = False
        player.rect.y = int(sprites.LANE_SIZE * player.lane + sprites.LANE_SIZE / 2 - sprites.PLAYER_SIZE[1] / 2)

        screen.fill((0, 0, 0))
        for i in range(3):
            pygame.draw.rect(screen, [0, 255, 0], [0, (i + 1) * sprites.LANE_SIZE, WINDOW_SIZE[0], sprites.LANE_SIZE - 1])
        all_units.draw(screen)
        pygame.display.flip()


main()