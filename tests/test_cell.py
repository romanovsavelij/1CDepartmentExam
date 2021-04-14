import unittest

from src.cell import Cell, Shape
import numpy as np


class TestCell(unittest.TestCase):

    def test_basic(self):
        # cell: Cell = Cell([])
        ...

    def test_indicator_empty(self):
        shape = Cell.shape_by_indicator(np.array([True, True, False, False, False, True]))
        self.assertEqual(shape, Shape.EMPTY)

    def test_indicator_cross(self):
        shape = Cell.shape_by_indicator(np.array([True, True, False, True, True, False, True, True]))
        self.assertEqual(shape, Shape.CROSS)

    def test_indicator_circle(self):
        shape = Cell.shape_by_indicator(np.array([False, True, False, True, False]))
        self.assertEqual(shape, Shape.CIRCLE)