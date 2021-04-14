import numpy as np
from skimage.io import imread


class ImageParser:
    def __init__(self, filename: str):
        self.name: str = filename

    def parse_image(self) -> np.ndarray:
        image: np.ndarray = imread(self.name)
        image = np.array([[ImageParser.is_black(image[i][j]) for j in range(image.shape[1])] for i in range(image.shape[0])])
        return image

    @staticmethod
    def is_black(cell: np.ndarray) -> bool:
        return np.array_equal(cell, [0, 0, 0, 255])
