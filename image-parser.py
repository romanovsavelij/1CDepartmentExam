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