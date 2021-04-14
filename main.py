from solution import Solution
import numpy as np
import pandas as pd
from scipy import stats

import numpy as np
from skimage.io import imread


class ImageParser:
    def __init__(self, filename: str):
        self.name: str = filename

    def parse_image(self) -> np.ndarray:
        self.image = imread(self.name)

    def parse_game(self):
        print(self.image[0][0])
        print(type(self.image[0][0]))
        print(ImageParser.is_black(self.image[0][0]))

    def find_border(self):
        ''' Calculates top left corner and cell size
        '''
        leftest = (-1, -1)
        for i in range(0, parser.image.shape[1]):
            # Iterate throw verticals
            # Search for black cell
            has_black = False
            for j in range(0, parser.image.shape[0]):
                # print(parser.image[j][i][:])
                if ImageParser.is_black(parser.image[j][i][:]):
                    leftest = (i, j)
                    has_black = True
            if has_black:
                break

        rightest = (-1, -1)

        for i in range(parser.image.shape[1] - 1, -1, -1):
            has_black = False
            for j in range(0, parser.image.shape[0]):
                # print(parser.image[j][i][:])
                if ImageParser.is_black(parser.image[j][i][:]):
                    rightest = (i, j)
                    has_black = True
            if has_black:
                break

        # print(leftest)
        # print(rightest)

        self.size = rightest[0] - leftest[0]
        self.cell_size = self.size / 3
        self.top_left_corner = (leftest[0], leftest[1] - cell_size)
        # print(parser.top_left_corner, cell_size)

    @staticmethod
    def is_black(cell: np.ndarray):
        return np.array_equal(cell, [0, 0, 0, 255])


if __name__ == '__main__':
    parser = ImageParser("images/image1.png")
    parser.parse_image()
    parser.parse_game()
    parser.find_border()
