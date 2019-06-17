class Settings:

    def __init__(self):
        # Screen dimensions (including margin)
        self.screen_width = 1000
        self.screen_height = 1000

        # Block dimensions
        self.block_side = 5

        # Number of blocks (per row or column)
        self.block_num = 500

        # Board Colors
        self.bg_color = (0, 0, 0)
        self.dead_color = (255, 255, 255)
        self.alive_color = (24, 255, 0)

        # Initial Board Density
        self.board_density = 0.5