from typing import List, Tuple

from src.cell import Shape


class Game:
    def __init__(self, field: List[List[Shape]]):
        self.field = field

    def get_win_line(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        '''Find out if someone won and return winning line's endpoints
        '''
        for i in range(3):
            if Game.is_win(self.field[i]):
                return ((i, 0), (i, 2))
        for i in range(3):
            line = [self.field[0][i], self.field[1][i], self.field[2][i]]
            if Game.is_win(line):
                return ((0, i), (2, i))
        diag = [self.field[0][0], self.field[1][1], self.field[2][2]]
        diag_inv = [self.field[2][0], self.field[1][1], self.field[0][2]]
        if Game.is_win(diag):
            return ((0, 0), (2, 2))
        if Game.is_win(diag_inv):
            return ((0, 2), (2, 0))
        return ((-1, -1), (-1, -1))

    @staticmethod
    def is_win(line: List[Shape]):
        '''Is this line winning?
        '''
        return line == 3 * [Shape.CIRCLE] or \
               line == 3 * [Shape.CROSS]
