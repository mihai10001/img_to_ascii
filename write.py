from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from style import get_mapping


def write_txt_from_img(img, result='result0.txt'):
    (width, height) = img.size
    mapping = get_mapping()

    with open(result, 'w') as file:
        text = ''
        for row in range(0, height):
            for col in range(0, width):
                text += ''.join(
                    element['ch'] for element in mapping if img.getpixel((col, row)) in range(element['st'], element['en'] + 1))
            text += '\n'
        file.write(text)
    return text


def write_txt_from_array(array, result='result1.txt'):
    (height, width) = array.shape
    mapping = get_mapping()

    with open(result, 'w') as file:
        text = ''
        for row in range(0, height):
            for col in range(0, width):
                text += ''.join(
                    element['ch'] for element in mapping
                    if array[row, col] in range(element['st'], element['en'] + 1))
            text += '\n'
        file.write(text)
    return text


def write_gray_img(text, result='result_gray.png'):
    image = Image.new('RGB', (1920, 1080))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 10)
    draw.text((0, 0), text, (255, 255, 255), font=font)
    image.save(result, "PNG")


def write_color_img(color, text, patch=2, result='result_color.png'):
    (height, width, z) = color.shape
    mult = 3*patch  # scale factor*patch
    image = Image.new('RGB', (1920, 1080))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 10)

    lines = text.split('\n')
    for i in range(0, height):
        for j in range(0, width):
            draw.text((j * mult, i * mult * patch), lines[i][j], tuple(color[i, j]), font=font)

    enhancer = ImageEnhance.Sharpness(image)
    enhancer2 = ImageEnhance.Brightness(image)
    factor = 1.5
    enhancer.enhance(factor)
    enhancer2.enhance(factor)

    image.save(result, "PNG")
