from typing import Tuple, List

from solution import Solution
import numpy as np
import pandas as pd
from scipy import stats

import numpy as np
from skimage.io import imread

from src.cell import Shape, Cell


class GameParser:
    def __init__(self, field: np.ndarray):
        self.field: np.ndarray = field

    def find_border(self):
        ''' Calculates top left corner and cell size
        '''
        leftest = (-1, -1)
        for i in range(0, self.field.shape[1]):
            # Iterate throw verticals
            # Search for black cell
            has_black = False
            for j in range(0, self.field.shape[0]):
                # print(parser.field[j][i][:])
                if self.field[j][i]:
                    leftest = (i, j)
                    has_black = True
                    break
            if has_black:
                break

        rightest = (-1, -1)

        for i in range(self.field.shape[1] - 1, -1, -1):
            has_black = False
            for j in range(0, self.field.shape[0]):
                if self.field[j][i]:
                    rightest = (i, j)
                    has_black = True
                    break
            if has_black:
                break

        print(leftest)
        print(rightest)

        self.size = rightest[0] - leftest[0] + 1
        self.cell_size = self.size // 3
        self.top_left_corner = (max(leftest[0], 0), max(leftest[1] - self.cell_size, 0))
        print(f"top_left_corner: {self.top_left_corner}, cell_size: {self.cell_size}")

    def parse_cell(self, corner: Tuple[int, int]) -> Shape:
        square = self.field[corner[1]:corner[1]+self.cell_size, corner[0]:corner[0]+self.cell_size]
        cell: Cell = Cell(square)
        shape = cell.identify_shape()
        return shape

    def parse_field(self) -> List[List[Shape]]:
        # Iterate throw all the cells
        shapes = [[Shape.EMPTY for i in range(3)] for j in range(3)]
        for i in range(3):
            for j in range(3):
                corner = (self.top_left_corner[0] + i * self.cell_size,
                                self.top_left_corner[1] + j * self.cell_size)
                shapes[i][j] = self.parse_cell(corner)
        return shapes
