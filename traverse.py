from PIL import Image
import numpy as np


def get_gcd(width, height):
    from fractions import gcd
    return gcd(width, height)


def get_median(arr):
    return int(np.median(arr))


def return_grayscale_img(image):
    patch = 2  # for viewing with a text editor, keeping aprox. the same ratio as the image
    maxsize = (256, 256)
    image.thumbnail(maxsize, Image.ANTIALIAS)
    (width, height) = image.size
    new_height = int(height/patch)
    new_image = image.resize((width, new_height))
    return new_image


def return_grayscale_array(array):
    (width, height) = array.shape
    patch = 1  # for viewing with a text editor, keeping aprox. the same ratio as the image
    divisor = get_gcd(width, height)  # divisor = the neighbourhood
    new_width = int(width/divisor)
    new_height = int(height*patch/(divisor*patch))
    new_array = np.zeros((new_height, new_width), dtype=np.uint8)

    start_y = height
    for row in reversed(range(0, new_height)):
        start_x = 0
        start_y -= patch*divisor
        for col in range(0, new_width):
            new_array[row, col] = get_median(array[start_x: start_x + divisor, start_y: start_y + patch*divisor])
            start_x += divisor

    return new_array


def return_color_array(array):
    (width, height, z) = array.shape
    patch = 2  # for viewing with a text editor, keeping aprox. the same ratio as the image
    divisor = get_gcd(width, height)  # divisor = the neighbourhood
    new_width = int(width/divisor)
    new_height = int(height/(divisor*patch))
    new_array = np.zeros((new_height, new_width, z), dtype=np.uint8)

    start_y = height
    for row in reversed(range(0, new_height)):
        start_x = 0
        start_y -= patch*divisor
        for col in range(0, new_width):
            r = get_median(array[start_y: start_y + patch*divisor, start_x: start_x + divisor, :1])
            g = get_median(array[start_y: start_y + patch*divisor, start_x: start_x + divisor, 1:2])
            b = get_median(array[start_y: start_y + patch*divisor, start_x: start_x + divisor, 2:3])
            new_array[row, col] = [r, g, b]
            start_x += divisor

    return new_array
