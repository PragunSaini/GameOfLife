import sys
from time import sleep

import pygame

from settings import Settings
from board_logic import Board

class GameOfLife:

    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                                self.settings.screen_height))

        pygame.display.set_caption("The Game Of Life")

        self.board = Board(self)
        self.board.initialize_board(0.1)


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.board.draw_game()
        pygame.display.flip()


    def run_game(self):
        while True:
            self._check_events()
            self.board.update_game()
            self._update_screen()
            sleep(0.1)


if __name__ == "__main__":
    game = GameOfLife()
    game.run_game()