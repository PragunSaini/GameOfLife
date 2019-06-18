""" Conway's Game of Life
    Made By: Pragun Saini
    Using PyGame
"""

# Imported libraries
import sys
import pygame

# User made classes
from settings import Settings
from board_logic import Board

class GameOfLife:
    """"Class to control the game"""

    def __init__(self):
        # Initialize pygame
        pygame.init()
        # Get the settings for the game
        self.settings = Settings()

        # Define a screen of given dimensions
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                                self.settings.screen_height))
        pygame.display.set_caption("The Game Of Life")

        # Build and initialize a game board
        self.board = Board(self)
        self.board.initialize_board(self.settings.board_density)

        # Clock to control game framerate
        self.clock = pygame.time.Clock()


    def _handle_mouse_clicks(self):
        """Toggles the state of a block on mouse click"""
        x, y = pygame.mouse.get_pos()
        # Convert mouse coordinates to 2-D array indexes
        x = x // self.settings.block_side
        y = y // self.settings.block_side
        self.board.toggle_block(x, y)


    def _check_events(self):
        """Handles the user generated events"""
        for event in pygame.event.get():
            # Quit the game upon pressing 'Q' key or closing the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit(0)
            # Handle mouse clicks
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_mouse_clicks()


    def _update_screen(self):
        # Fill background color
        self.screen.fill(self.settings.bg_color)
        # Draw the blocks
        self.board.draw_game()
        pygame.display.flip()


    def run_game(self):
        while True:
            # Handle events
            self._check_events()
            # Update board state
            self.board.update_game()
            # Then update the screen (re-draw the blocks)
            self._update_screen()
            # Limit framerate to 10 FPS
            self.clock.tick(10)


if __name__ == "__main__":
    # Instantiate and run game
    game = GameOfLife()
    game.run_game()