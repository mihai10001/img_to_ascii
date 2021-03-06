from math import ceil
from PIL import Image
import numpy as np

#  !~~~~~~~~~~~~~~~~~~~~~~~ GUIDE ~~~~~~~~~~~~~~~~~~~~~~~!

#  SCALE = SCALE FACTOR ( NEIGHBOURHOOD )
#  MAXSIZE => arbitrary optimal size for viewing with a text editor


#  !~~~~~~~~~~~~~~~~~~~~~~~ GUIDE~~~~~~~~~~~~~~~~~~~~~~~~!

#  PATCH = 2 => for viewing with a text editor, keeping ~ the same ratio
#            => for reconstructing the original photo

maxsize = (256, 256)
scale = None
patch = 2


def set_scaling(factor, height=None, width=None):
    global scale
    if factor:
        scale = factor
    else:
        from fractions import gcd
        scale = gcd(height, width)


def get_scaling():
    return scale


def get_patch():
    return patch


def get_median(array):
    return int(np.median(array))


def scaled_img(image):
    new_image = image
    new_image.thumbnail(maxsize, Image.BICUBIC)
    return new_image.resize((new_image.size[0], int(new_image.size[1]/patch)))


def scaled_gray_array(array):
    (height, width) = array.shape
    new_array = np.zeros((ceil(height/(scale*patch)), ceil(width/scale)), dtype=np.uint8)

    for i, col in enumerate(range(0, height, scale*patch)):
        for j, row in enumerate(range(0, width, scale)):
            new_array[i, j] = get_median(array[col: col + patch*scale, row: row + scale])

    return new_array


def scaled_color_array(array):
    (height, width, z) = array.shape
    new_array = np.zeros((ceil(height/(scale*patch)), ceil(width/scale), z), dtype=np.uint8)

    for i, col in enumerate(range(0, height, scale*patch)):
        for j, row in enumerate(range(0, width, scale)):
            r = get_median(array[col: col + patch*scale, row: row + scale, :1])
            g = get_median(array[col: col + patch*scale, row: row + scale, 1:2])
            b = get_median(array[col: col + patch*scale, row: row + scale, 2:3])
            new_array[i, j] = [r, g, b]

    return new_array
