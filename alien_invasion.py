""" Alien Invasion game """
import sys
import pygame


class AlienInvasion:
    """ Main class"""
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Alien Invasion")

    @staticmethod
    def run_game():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
