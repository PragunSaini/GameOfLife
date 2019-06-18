
from random import random
import pygame

class Board:
    """Class to store the board state
        True means block is alive
        False means block is dead"""

    def __init__(self, game):
        # Get Screen and setting parameters
        self.settings = game.settings
        self.screen = game.screen

        # Create a 2-D board filled with boolean values
        self.board = [[[] for i in range(self.settings.block_num)]
                            for j in range(self.settings.block_num)]


    def initialize_board(self, d):
        """Randomly initialize various blocks as alive or dead
            based on density parametter d"""
        for y in range(self.settings.block_num):
            for x in range(self.settings.block_num):
                self.board[y][x] = random() < d


    def _make_alive(self, x, y):
        try:
            self.board[y][x] = True
        except IndexError:
            return

    def _make_dead(self, x, y):
        try:
            self.board[y][x] = False
        except IndexError:
            return

    def _get_status(self, x, y):
        try:
            return self.board[y][x]
        except IndexError:
            return False


    def _get_neightbours_count(self, x, y):
        """Get the number of neighbours alive of a block
            A block has 8 neighbours"""
        n = 0
        n += 1 if self._get_status(x-1, y-1) else 0
        n += 1 if self._get_status(x-1, y) else 0
        n += 1 if self._get_status(x-1, y+1) else 0
        n += 1 if self._get_status(x, y+1) else 0
        n += 1 if self._get_status(x, y-1) else 0
        n += 1 if self._get_status(x+1, y-1) else 0
        n += 1 if self._get_status(x+1, y) else 0
        n += 1 if self._get_status(x+1, y+1) else 0
        return n


    def toggle_block(self, x, y):
        """If a block is dead, then make it alive
            otherwise kill it"""
        if (self._get_status(x, y)):
            self._make_dead(x, y)
        else:
            self._make_alive(x, y)


    def update_game(self):
        """Checks each block in the game,
            and according to game rules
            updates the board"""
        for y in range(self.settings.block_num):
            for x in range(self.settings.block_num):
                n = self._get_neightbours_count(x, y)
                if self._get_status(x, y):
                    if n < 2 or n > 3:
                        self._make_dead(x, y)
                else:
                    if n == 3:
                        self._make_alive(x, y)


    def draw_game(self):
        """Draws the blocks on the game screen"""
        for y in range(self.settings.block_num):
            for x in range(self.settings.block_num):
                # Make a rectangle of given size at given position
                rect = pygame.Rect(x*(self.settings.block_side + 1),
                                    y*(self.settings.block_side + 1),
                                    self.settings.block_side,
                                    self.settings.block_side)
                # Draw it with the appropriate color
                if (self._get_status(x, y)):
                    pygame.draw.rect(self.screen,
                                    self.settings.alive_color, rect)
                else:
                    pygame.draw.rect(self.screen,
                                    self.settings.dead_color, rect)
