from style import get_mapping


def write_img_as_txt(img, width, height, result='result.txt'):
    mapping = get_mapping()
    with open(result, 'w') as text:
        for row in range(0, height):
            line = ''
            for col in range(0, width):
                line += ''.join(element['ch'] for element in mapping if img[row, col] in range(element['st'], element['en'] + 1))
            text.write(line + '\n')
    return text
