class Settings:
    """Class for changing the game parameters """

    def __init__(self):
        # Screen dimensions (including margin)
        # Fixed
        self.screen_width = 1000
        self.screen_height = 1000

        # Number of blocks (per row or column)
        self.block_num = 100

        # Block dimensions
        self.block_side = self.screen_width // self.block_num
        self.block_side = self.block_side - 1 # to leave space for margins

        # Board Colors
        self.bg_color = (0, 0, 0)
        self.dead_color = (255, 255, 255)
        self.alive_color = (25, 255, 0)

        # Initial Board Density
        self.board_density = 0.25