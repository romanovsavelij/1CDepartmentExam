from typing import Tuple


class DrawLine:
    def __init__(self, image):
        self.image = image

    def draw_line(self, start: Tuple[int, int], end: Tuple[int, int]):
