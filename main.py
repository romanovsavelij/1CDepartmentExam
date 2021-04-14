from solution import Solution
import numpy as np
import pandas as pd
from scipy import stats

import numpy as np
from skimage.io import imread

from src.game import GameParser
from src.image import ImageParser

if __name__ == '__main__':
    image_parser = ImageParser("images/image1.png")
    print(image_parser.parse_image())
    game_parser: GameParser = GameParser(image_parser.parse_image())
    game_parser.find_border()
    game_parser.parse_field()
