""" Alien Invasion game """
import sys
import pygame

from settings import Settings


class AlienInvasion:
    """ Main class"""
    def __init__(self):
        """ Default constructor initializer"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,
            self.settings.screen_height))


    def run_game(self):
        """ Main loop for the game """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            """ redraw the screen """
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
