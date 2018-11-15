from PIL import Image, ImageDraw, ImageFont
from style import get_mapping


def write_txt_from_img(img, result='result0.txt'):
    (width, height) = img.size
    mapping = get_mapping()
    text = ''
    with open(result, 'w') as file:
        for row in range(0, height):
            for col in range(0, width):
                text += ''.join(element['ch'] for element in mapping if img.getpixel((col, row)) in range(element['st'], element['en'] + 1))
            text += '\n'
        file.write(text)
    return text


def write_txt_from_array(array, result='result1.txt'):
    (width, height) = array.shape
    print(array.shape)
    mapping = get_mapping()
    text = ''
    with open(result, 'w') as file:
        for row in range(0, height):
            for col in range(0, width):
                text += ''.join(element['ch'] for element in mapping if array[col, row] in range(element['st'], element['en'] + 1))
            text += '\n'
        file.write(text)
    return text


# def write_img_gray(text, result='result_gray.png'):
#     new_image = Image.new('RGB', (1920, 1080))
#     draw = ImageDraw.Draw(new_image)
#     font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 10)
#     draw.text((0, 0), text, (255, 255, 255), font=font)
#     new_image.save(result, "PNG")
#     return new_image


# def write_img_color(img, text, width, height,  result='result_color.png'):
#     new_image = Image.new('RGB', (1920, 1080))
#     draw = ImageDraw.Draw(new_image)
#     font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 9)

#     lines = text.split('\n')
#     for i in range(0, height):
#         for j in range(0, width):
#             a = (img[i, j, 0], img[i, j, 1], img[i, j, 2])
#             draw.text((j*6, i*12), lines[i][j], a, font=font)

#     new_image.save(result, "PNG")
#     return new_image
