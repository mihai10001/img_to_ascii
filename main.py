from read import import_gray, import_gray_array, import_color, import_color_array
from traverse import set_scaling, scaled_img, scaled_gray_array, scaled_color_array
from write import write_txt_from_img, write_txt_from_array, get_gray_img, get_color_img, save_img


if __name__ == "__main__":

    print('\n\nHello, and welcome to my Image to ASCII(text) converter.',
          'In order to get started, place your image in the same folder as the main file.',
          'After that, input here the image name and press enter:', sep='\n')
    filename = 'test.jpg'  # input()

    img = import_gray(filename)
    img_c = import_color(filename)
    img_ga = import_gray_array(filename)
    img_ca = import_color_array(filename)

    print('\n\nNext, the program needs to know the scaling factor it should use.',
          'I will explain that a bit later, but for now input it', sep='\n')
    # scale = int(input())
    set_scaling(3)

    print('\n\nLastly, input the functioning mode and press enter:',
          '1. The first mode is simply creating the ASCII art in a text file.',
          '2. The second mode also creates additional images of the art', sep='\n')
    # mode = int(input())

    # if mode == 1:
    #     gray_img = scaled_img(img)
    #     text = write_txt_from_img(gray_img)
    #     print('iei')
    # elif mode == 2:
    gray_array = scaled_gray_array(img_ga)
    color_array = scaled_color_array(img_ca)
    text = write_txt_from_array(gray_array)
    save_img(get_gray_img(text), name='result_gray')
    save_img(get_color_img(color_array, text), name='result_color')

    # #  FEATURES :

    # #  ~~ 1 ~~  :
    # gray_img = scaled_img(img)
    # text = write_txt_from_img(gray_img)

    # #  ~~ OR ~~ :

    # #  ~~ 1 ~~  :
    # gray_array = scaled_gray_array(img_ga)
    # text = write_txt_from_array(gray_array)

    # #  ~~ 2 ~~  :
    # write_gray_img(text)

    # #  ~~ 3 ~~  :
    # color_array = scaled_color_array(img_ca)
    # write_color_img(color_array, text)