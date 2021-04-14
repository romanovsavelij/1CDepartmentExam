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
    print(f"top_left_corner: {game_parser.top_left_corner}, cell_size: {game_parser.cell_size}")
    shapes = game_parser.parse_field()
    print(f"shapes by columns: {shapes}")

    game: Game = Game(shapes)
    line = game.get_win_line()
    print(f"Победная линия ведет от ячейки {line[0]} к ячейке {line[1]}")


