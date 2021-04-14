from typing import Tuple

from src.game_parser import Point


class DrawLine:
    def __init__(self, new_image_name: str, old_image: np.ndarray):
        self.new_image_name = new_image_name
        self.old_image = old_image

    def draw_line(self, start: Point, end: Point) -> None:
        '''Create a new image with a line drawn on it.
        Line is drawn by given endpoints' coords on the image.
        '''
        # TODO
        # Iterate throw cells from start to end, coloring
        # cells with black. Iteration should be done with some width
        # for line not to be one pixel width.
