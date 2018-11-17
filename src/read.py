from PIL import Image
import numpy as np


def import_gray(filename):
    img = Image.open(filename).convert('L')
    return img


def import_color(filename):
    img = Image.open(filename).convert('RGB')
    return img


def import_gray_array(filename):
    img = Image.open(filename).convert('L')
    data = np.asarray(img, dtype=np.uint8)
    return data


def import_color_array(filename):
    img = Image.open(filename).convert('RGB')
    data = np.asarray(img, dtype=np.uint8)
    return data
