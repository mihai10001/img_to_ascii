from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from src.traverse import get_scaling, get_patch
from src.style import get_mapping

#  !~~~~~~~~~~~~~~~~~~~~~~~ GUIDE ~~~~~~~~~~~~~~~~~~~~~~~!

#  FONT_PATH = path to the font you wish to use
#  MAXIFY => arbitrary size for a better visible output image, can be changed to any integer

font_path = '/usr/share/fonts/truetype/freefont/FreeMono.ttf'
maxify = 3


def write_txt_from_img(image, result='result.txt'):
    (width, height) = image.size
    mapping = get_mapping()
    text, line = '', ''

    for row in range(0, height):
        line = ''
        for col in range(0, width):
            line += [element['ch'] for element in mapping if image.getpixel((col, row)) in range(element['st'], element['en'] + 1)].pop()
        text += line + '\n'
    if result:
        with open(result, 'w') as file:
            file.write(text)
            print('\nWrote ASCII art to "%s" !' % result)
    return text


def write_txt_from_array(array, result='result.txt'):
    (height, width) = array.shape
    mapping = get_mapping()
    text, line = '', ''

    for row in range(0, height):
        line = ''
        for col in range(0, width):
            line += [element['ch'] for element in mapping if array[row, col] in range(element['st'], element['en'] + 1)].pop()
        text += line + '\n'
    if result:
        with open(result, 'w') as file:
            file.write(text)
            print('\nWrote ASCII art to "%s" !' % result)
    return text


# inspired algorithm(simplified)
def font_scale(line, width):
    fontsize = 1
    font = ImageFont.truetype(font_path, fontsize)
    while font.getsize(line)[0] < width:
        fontsize += 1
        font = ImageFont.truetype(font_path, fontsize)
    fontsize -= 1
    return fontsize


def get_gray_img(text, orig_h, orig_w):
    scale, patch = get_scaling(), get_patch()
    image = Image.new('RGB', (orig_w*maxify, orig_h*maxify))
    draw = ImageDraw.Draw(image)
    lines = text.splitlines()
    fontsize = font_scale(lines[0], orig_w*maxify) + 1
    font = ImageFont.truetype(font_path, fontsize)

    h, w = len(lines), len(lines[0])
    for i in range(0, h):
        for j in range(0, w):
            draw.text((j*scale*maxify, i*scale*patch*maxify), lines[i][j], (255, 255, 255), font=font)
    return image


def get_color_img(color, text, orig_h, orig_w):
    scale, patch = get_scaling(), get_patch()
    image = Image.new('RGB', (orig_w*maxify, orig_h*maxify))
    draw = ImageDraw.Draw(image)
    lines = text.splitlines()
    fontsize = font_scale(lines[0], orig_w*maxify) + 3
    font = ImageFont.truetype(font_path, fontsize)

    (h, w, z) = color.shape
    for i in range(0, h):
        for j in range(0, w):
            draw.text((j*scale*maxify, i*scale*patch*maxify), lines[i][j], tuple(color[i, j]), font=font)
    return image


def enhance_img(image):
    factor = 1.7
    modified = image
    contrast = ImageEnhance.Contrast(modified)
    modified = contrast.enhance(factor)
    brighten = ImageEnhance.Brightness(modified)
    modified = brighten.enhance(factor)
    # color = ImageEnhance.Color(image)
    # modified = color.enhance(factor)
    return modified


def save_img(image, name, enhance=True):
    if enhance is True:
        image = enhance_img(image)
    image.save(name, 'PNG')
    print('\nCreated image out of ASCII art to "%s" !' % name)
