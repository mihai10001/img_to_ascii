from PIL import Image
import numpy as np
np.set_printoptions(threshold=np.inf)


def load_image_greyscale(filename):
    img = Image.open(filename).convert('L')
    data = np.asarray(img, dtype=np.float)
    return data, data.shape


def get_gcd(width, height):
    from fractions import gcd
    return gcd(width, height)


def get_median(arr):
    return int(np.median(arr))


def return_traversed_image(divisor, width, height):
    arr = np.zeros((height, width), dtype=np.float)
    new_width = int(width/divisor)
    new_height = int(height/(divisor*2))

    start_y = height
    for row in reversed(range(0, new_height)):
        start_x = 0
        start_y -= 2*divisor
        for col in range(0, new_width):
            arr[row, col] = get_median(pix[start_y: start_y + 2*divisor, start_x: start_x + divisor])
            start_x += divisor

    return arr, new_width, new_height


def write_text(arr, mylist, width, height, result='result.txt'):
    with open(result, 'w') as text:
        for row in range(0, height):
            whole_row = ''
            for col in range(0, width):
                check = arr[row, col]
                for element in mylist:
                    if check >= element['start'] and check <= element['end']:
                        whole_row += element['char']
            text.write(whole_row + '\n')


def get_style():
    # style = " .:-=+*#%@"
    style = " .`'\"^,:;Il!i><~+jrdbk*#M@"
    mil = []
    start = 0
    part = int(255/len(style))

    for c in reversed(style):
        mydict = {}
        mydict['char'] = c
        mydict['start'] = start
        mydict['end'] = start + part
        mil.append(mydict)
        start += part + 1

    mil[-1]['end'] = 255
    return mil


if __name__ == "__main__":
    pix, (h, w) = load_image_greyscale('test1.jpg')
    hood = 4
    arr, new_w, new_h = return_traversed_image(hood, w, h)
    style = get_style()
    write_text(arr, style, new_w, new_h)

# STEPS:
# IMPORT IMAGE(CONVERTED TO GREYSCALE)
# SELECT NEIGHBOURHOOD (4 = 4X4 = 16 PIXELS) get_gcd(w, h)
# SELECT STYLE
# WRITE TEXT