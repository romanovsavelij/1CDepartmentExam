from solution import Solution
import numpy as np
import pandas as pd
from scipy import stats

import numpy as np
from skimage.io import imread

from src.game_parser import GameParser
from src.game import Game
from src.image import ImageParser

if __name__ == '__main__':
    image_parser = ImageParser("images/image1.png")

    game_parser: GameParser = GameParser(image_parser.parse_image())
    game_parser.find_border()
    shapes = game_parser.parse_field()
    print(f"shapes by columns: {shapes}")

    game: Game = Game(shapes)
    print(game.get_win_line())
