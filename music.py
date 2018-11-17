import pygame

from constants import *

class Music:
    def __init__(self):
        self.song = 1

        pygame.mixer.Channel(0).play(pygame.mixer.Sound("src/medieval_music.wav"), loops=-1)
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("src/present_music.wav"), loops=-1)
        pygame.mixer.Channel(2).play(pygame.mixer.Sound("src/future_music.wav"), loops=-1)
        pygame.mixer.Channel(0).set_volume(0)
        pygame.mixer.Channel(2).set_volume(0)

    def change(self, m):
        if m >= 0 and m <= 2:
            for c in range(3):
                if m == c:
                    pygame.mixer.Channel(c).set_volume(1)
                else:
                    pygame.mixer.Channel(c).set_volume(0)
