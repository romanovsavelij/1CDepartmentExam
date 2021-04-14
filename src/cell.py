from enum import Enum

import numpy as np


class Shape(Enum):
    CIRCLE = 1
    CROSS = 2
    EMPTY = 3


class Cell:
    def __init__(self, field: np.ndarray):
        self.field = field

    def identify_shape(self):
        row = self.field.shape[0] // 2
        indicator = self.field[[row], :][0, :]
        return self.shape_by_indicator(indicator)

    @staticmethod
    def shape_by_indicator(indicator: np.array):
        '''Indicator is a row. We can indentify shape by this row.
        '''
        # Remove leading and trailing True's
        prefix = 0
        while prefix < len(indicator) and indicator[prefix]:
            prefix += 1
        indicator = indicator[prefix:]

        suffix = len(indicator) - 1
        while suffix > 0 and indicator[suffix]:
            suffix -= 1
        indicator = indicator[:suffix+1]

        # Get indices of all True's in indicator
        inds = np.where(indicator)[0]
        if inds.size == 0:
            return Shape.EMPTY

        # Cross's indicator should look like that:
        # False, ..., False, True, ..., True, False, ..., False
        for i in range(min(inds) + 1, max(inds)):
            if i not in inds:
                return Shape.CIRCLE
        return Shape.CROSS



