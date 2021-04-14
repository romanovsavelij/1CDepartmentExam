from typing import Tuple, List

import numpy as np

from src.cell import Shape, Cell


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class GameParser:
    def __init__(self, field: np.ndarray):
        self.field: np.ndarray = field

    def find_border(self):
        ''' Calculates top left corner and cell size
        '''
        # Find leftest corner
        leftest = Point(-1, -1)
        for i in range(0, self.field.shape[1]):
            # Iterate throw verticals
            # Search for black cell
            has_black = False
            for j in range(0, self.field.shape[0]):
                if self.field[j][i]:
                    leftest = Point(i, j)
                    has_black = True
                    break
            if has_black:
                break

        # No time to remove copy paste. Sorry for that.
        # Better to implement without loops, using np.
        # Find rightest corner
        rightest = Point(-1, -1)
        for i in range(self.field.shape[1] - 1, -1, -1):
            has_black = False
            for j in range(0, self.field.shape[0]):
                if self.field[j][i]:
                    rightest = Point(i, j)
                    has_black = True
                    break
            if has_black:
                break

        self.size = rightest.x - leftest.x + 1
        self.cell_size = self.size // 3
        self.top_left_corner = (max(leftest.x, 0), max(leftest.y - self.cell_size, 0))

    def parse_cell(self, corner: Tuple[int, int]) -> Shape:
        '''Parse shape of a cell. Cell is given by it's
        top left corner. Cell size is self.cell_size
        '''
        square = self.field[corner[1]:corner[1]+self.cell_size, corner[0]:corner.x+self.cell_size]
        cell: Cell = Cell(square)
        shape = cell.identify_shape()
        return shape

    def parse_field(self) -> List[List[Shape]]:
        '''Parse shapes on given field
        '''
        # Iterate throw all the cells
        shapes = [[Shape.EMPTY for i in range(3)] for j in range(3)]
        for i in range(3):
            for j in range(3):
                corner = (self.top_left_corner.x + i * self.cell_size,
                                self.top_left_corner.y + j * self.cell_size)
                shapes[i][j] = self.parse_cell(corner)
        return shapes

    def cell_coords_to_image_coords(self, start: Point, end: Point) -> Tuple[Point, Point]:
        '''Gets coords of the sell and translates
        them into line coords in the image
        '''
        p1 = Point(-1, -1)
        p2 = Point(-1, -1)
        if start.x == end.x:
            # Vertical line
            delta_x = start.x * self.cell_size + self.cell_size // 2
            delta_y = (start.y + 1) * self.cell_size

            x = self.top_left_corner.x + delta_x
            p1 = Point(x, 0)
            p2 = Point(x, self.top_left_corner.y + delta_y)
            return p1, p2
        # And so on...
        return Point(-1, -1), Point(-1, -1)
