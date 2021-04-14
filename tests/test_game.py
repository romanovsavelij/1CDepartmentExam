import unittest

from src.cell import Cell, Shape
import numpy as np

from src.game import GameParser


class TestGame(unittest.TestCase):

    def test_basic(self):
        game: GameParser = GameParser(np.array([
            [False, False, True, False],
            [False, True, True, True],
            [False, True, True, True],
            [False, False, True, False]]))
        game.find_border()
        self.assertEqual(game.top_left_corner, (1, 0))
