from src.read import import_gray, import_gray_array, import_color, import_color_array
from src.traverse import set_scaling, scaled_img, scaled_gray_array, scaled_color_array
from src.write import write_txt_from_img, write_txt_from_array, get_gray_img, get_color_img, save_img

if __name__ == "__main__":

    print('\n\nHello, and welcome to my Image to ASCII(text) converter.\n',
          'In order to get started, place your image in the same folder as the main file.\n',
          'After that, input the full image name (with the format) and press enter.\n', sep='')
    filename = input('Image name: ')
    img = import_gray(filename)
    img_c = import_color(filename)
    img_ga = import_gray_array(filename)
    img_ca = import_color_array(filename)

    print('\n\nNext, the program needs to know the scaling factor it should use, input any integer from (0, infinity) and press enter.\n',
          'I would suggest picking a scaling factor of 2, 3, or 4 for acceptable results.\n',
          'A one scaling factor, or 1:1 means that the result will have as many characters as there are pixels in the input image.\n',
          'A three scaling factor, or 1:3x3 means that the result will have a character for every 3x3 grid of pixels from the input image.\n'
          'You can, in theory, use any scaling factor, but keep in mind that it is inversely proportional with the quality of the result.\n', sep='')
    set_scaling(int(input('Scaling factor: ')))

    print('\n\nLastly, specify the functioning mode number.\n',
          '1. Express:  The first mode is simply creating the ASCII art in a text file called "results.txt", using a fast computing method.\n',
          '2. Extended: The second mode creates the ASCII art and also creates two additional images(gray, color).\n', sep='')
    mode = int(input('Functioning mode number: '))
    if mode == 1:
        gray_img = scaled_img(img)
        text = write_txt_from_img(gray_img)
    elif mode == 2:
        gray_array = scaled_gray_array(img_ga)
        color_array = scaled_color_array(img_ca)
        text = write_txt_from_array(gray_array)
        save_img(get_gray_img(text, img_ga.shape[0], img_ga.shape[1]), name='result_gray.png')
        save_img(get_color_img(color_array, text, img_ga.shape[0], img_ga.shape[1]), name='result_color.png')