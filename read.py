from PIL import Image
import numpy as np


def import_grayscale(filename):
    img = Image.open(filename).convert('L')
    data = np.asarray(img, dtype=np.uint8)
    return data, data.shape


def import_color(filename):
    img = Image.open(filename)
    data = np.asarray(img, dtype=np.uint8)
    return data, data.shape
