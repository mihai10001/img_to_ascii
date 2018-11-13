from PIL import Image
import numpy as np


def import_grayscale(filename):
    img = Image.open(filename).convert('L')
    data = np.asarray(img, dtype=np.int32)
    return data, data.shape
