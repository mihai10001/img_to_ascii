import numpy as np


def get_gcd(width, height):
    from fractions import gcd
    return gcd(width, height)


def get_median(arr):
    return int(np.median(arr))


def traverse_grayscale_image(image, width, height):
    patch = 2  # for viewing with a text editor, keeping aprox. the same ratio as the image
    divisor = get_gcd(width, height)  # divisor = the neighbourhood
    arr = np.zeros((height, width), dtype=np.int32)
    new_width = int(width/divisor)
    new_height = int(height/(divisor*patch))

    start_y = height
    for row in reversed(range(0, new_height)):
        start_x = 0
        start_y -= patch*divisor
        for col in range(0, new_width):
            arr[row, col] = get_median(image[start_y: start_y + patch*divisor, start_x: start_x + divisor])
            start_x += divisor

    return arr, new_width, new_height