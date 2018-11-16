import pygame

def main():
    pygame.init()

    WINDOW_SIZE = (1024,768)
    screen = pygame.display.set_mode(WINDOW_SIZE)

    running = True  # True as long as the game should be running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

main()