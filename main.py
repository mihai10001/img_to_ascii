from PIL import Image
import numpy as np
np.set_printoptions(threshold=np.inf)


def import_greyscale(filename):
    img = Image.open(filename).convert('L')
    data = np.asarray(img, dtype=np.int32)
    return data, data.shape


def get_gcd(width, height):
    from fractions import gcd
    return gcd(width, height)


def get_median(arr):
    return (np.median(arr)).astype('int32')


def traverse_image(divisor, width, height):
    patch = 2  # for viewing with a text editor, keeping aprox. the same ratio as the image
    arr = np.zeros((height, width), dtype=np.int32)
    new_width = int(width/divisor)
    new_height = int(height/(divisor*patch))

    start_y = height
    for row in reversed(range(0, new_height)):
        start_x = 0
        start_y -= patch*divisor
        for col in range(0, new_width):
            arr[row, col] = get_median(pix[start_y: start_y + patch*divisor, start_x: start_x + divisor])
            start_x += divisor

    return arr, new_width, new_height


def write_text(arr, mylist, width, height, result='result3.txt'):
    with open(result, 'w') as text:
        for row in range(0, height):
            whole_row = ''
            for col in range(0, width):
                check = arr[row, col]
                for element in mylist:
                    if element['st'] <= check <= element['en']:
                        whole_row += element['ch']
            text.write(whole_row + '\n')


def get_style():
    return " .`'\"^,:;Il!i><~+jrdbk*#M@"


def get_mapping():
    style = get_style()
    mapping, start, part = [], 0, int(255/len(style))
    print(mapping, start, part)
    mapping = [{'ch': x, 'st': start, 'en': start+part} for start, x in enumerate(style[::-1], start+part)]
    #mapping[-1][2] = 255
    print(mapping)
    return mapping


if __name__ == "__main__":
    pix, (h, w) = import_greyscale('test1.jpg')
    hood = 4  # get_gcd(w, h)
    arr, new_w, new_h = traverse_image(hood, w, h)
    mapp = get_mapping()
    #write_text(arr, mapp, new_w, new_h)

# STEPS:
# IMPORT IMAGE(CONVERTED TO GREYSCALE)
# SELECT NEIGHBOURHOOD (4 = 4X4 = 16 PIXELS) get_gcd(w, h)
# SELECT MAPPING BASED OF STYLE
# WRITE TEXT