from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from style import get_mapping

font_path = '/usr/share/fonts/truetype/freefont/FreeMono.ttf'


def write_txt_from_img(image, result='result.txt'):
    (width, height) = image.size
    mapping = get_mapping()

    with open(result, 'w') as file:
        text = ''
        for row in range(0, height):
            for col in range(0, width):
                text += ''.join(element['ch'] for element in mapping if image.getpixel((col, row)) in range(element['st'], element['en'] + 1))
            text += '\n'
        file.write(text)
    return text


def write_txt_from_array(array, result='result.txt'):
    (height, width) = array.shape
    mapping = get_mapping()
    text = ''

    with open(result, 'w') as file:
        for row in range(0, height):
            line = ''
            for col in range(0, width):
                line += [element['ch'] for element in mapping if array[row, col] in range(element['st'], element['en'] + 1)].pop()
            text += line + '\n'
        file.write(text)
        return text


# inspired algorithm(simplified)
def font_scale(s, width):
    fontsize = 1
    font = ImageFont.truetype(font_path, fontsize)
    while font.getsize(s)[0] < width:
        fontsize += 1
        font = ImageFont.truetype(font_path, fontsize)
    fontsize -= 1
    return fontsize


def get_gray_img(text):
    width, height = 1920, 1080
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)
    fontsize = font_scale(text.splitlines()[0], width)
    font = ImageFont.truetype(font_path, fontsize)
    draw.text((0, 0), text, (255, 255, 255), font=font)
    return image


# def get_color_img(color, text, patch=2):
#     width, height = 1920, 1080
#     image = Image.new('RGB', (width, height))
#     draw = ImageDraw.Draw(image)
#     lines = text.splitlines()

#     fontsize = font_scale(lines[0], width)
#     font = ImageFont.truetype(font_path, fontsize)

#     (arrayh, arrayw, z) = color.shape
#     ratio = int(arrayw/arrayh)/2
#     for i in range(0, arrayh):
#         for j in range(0, arrayw):
#             draw.text((j*1**3, i*1*patch**3), lines[i][j], tuple(color[i, j]), font=font)
#     return image

def enhance_img(image):
    factor = 1.5
    sharpen = ImageEnhance.Sharpness(image)
    brighten = ImageEnhance.Brightness(image)
    sharpen.enhance(factor), brighten.enhance(factor)
    return image


def save_img(image, enhance=False, name='result.png'):
    if enhance is True:
        image = enhance_img(image)
    image.save(name, 'PNG')
