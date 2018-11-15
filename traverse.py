from math import ceil
from PIL import Image
import numpy as np


def get_gcd(height, width):
    from fractions import gcd
    return gcd(width, height)


def get_median(arr):
    return int(np.median(arr))

#  !~~~~~~~~~~~~~~~~~~~~~~~ GUIDE ~~~~~~~~~~~~~~~~~~~~~~~!:

#  MAXSIZE = optimal size for viewing with a text editor
#  PATCH = 2 => for viewing with a text editor, keeping aprox. the same ratio as the image
#  DIVISOR = NEIGHBOURHOOD = SCALING FACTOR


def scaled_img(image, maxsize=(256, 256), patch=2):
    new_image = image
    new_image.thumbnail(maxsize, Image.ANTIALIAS)
    new_image = new_image.resize((new_image.size[0], int(new_image.size[1]/patch)))
    return new_image


def scaled_gray_array(array, patch=2):
    (height, width) = array.shape
    divisor = get_gcd(height, width)
    new_array = np.zeros((ceil(height/(divisor*patch)), ceil(width/divisor)), dtype=np.uint8)

    for i, col in enumerate(range(0, height, divisor*patch)):
        for j, row in enumerate(range(0, width, divisor)):
            new_array[i, j] = get_median(array[col: col + patch*divisor, row: row + divisor])

    return new_array


def scaled_color_array(array, patch=2):
    (height, width, z) = array.shape
    divisor = get_gcd(width, height)
    new_array = np.zeros((ceil(height/(divisor*patch)), ceil(width/divisor), z), dtype=np.uint8)

    for i, col in enumerate(range(0, height, divisor*patch)):
        for j, row in enumerate(range(0, width, divisor)):
            r = get_median(array[col: col + patch*divisor, row: row + divisor, :1])
            g = get_median(array[col: col + patch*divisor, row: row + divisor, 1:2])
            b = get_median(array[col: col + patch*divisor, row: row + divisor, 2:3])
            new_array[i, j] = [r, g, b]

    return new_array
