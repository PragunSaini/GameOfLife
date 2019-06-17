
from random import random
import pygame

class Board:

    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen

        self.board = [[[] for i in range(self.settings.block_num)]
                            for j in range(self.settings.block_num)]


    def initialize_board(self, d):
        for y in range(self.settings.block_num):
            for x in range(self.settings.block_num):
                self.board[y][x] = random() < d


    def _make_alive(self, x, y):
        if x < 0 or x >= self.settings.block_num:
            return
        if x < 0 or x >= self.settings.block_num:
            return
        self.board[y][x] = True

    def _make_dead(self, x, y):
        if x < 0 or x >= self.settings.block_num:
            return
        if x < 0 or x >= self.settings.block_num:
            return
        self.board[y][x] = False

    def _get_status(self, x, y):
        if x < 0 or x >= self.settings.block_num:
            return False
        if y < 0 or y >= self.settings.block_num:
            return False
        return self.board[y][x]

    def _get_neightbours_count(self, x, y):
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

    def update_game(self):
        for y in range(self.settings.block_num):
            for x in range(self.settings.block_num):
                n = self._get_neightbours_count(x, y)
                if self._get_status(x, y):
                    if n < 2 or n > 3:
                        self._make_dead(x, y)
                else:
                    if n == 3:
                        self._make_alive(x, y)
        # print("Updated")


    def draw_game(self):
        for y in range(self.settings.block_num):
            for x in range(self.settings.block_num):
                rect = pygame.Rect(x*(self.settings.block_side + 1),
                                    y*(self.settings.block_side + 1),
                                    self.settings.block_side,
                                    self.settings.block_side)
                if (self._get_status(x, y)):
                    pygame.draw.rect(self.screen,
                                    self.settings.alive_color, rect)
                else:
                    pygame.draw.rect(self.screen,
                                    self.settings.dead_color, rect)
        # print("Drawn again")
