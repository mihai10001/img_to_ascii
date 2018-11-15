from read import import_gray, import_gray_array, import_color, import_color_array
from traverse import scaled_img, scaled_gray_array, scaled_color_array
from write import write_txt_from_img, write_txt_from_array, write_gray_img, write_color_img


if __name__ == "__main__":

    filename = 'test.jpg'

    img = import_gray(filename)
    img_c = import_color(filename)
    img_ga = import_gray_array(filename)
    img_ca = import_color_array(filename)

    #  FEATURES :

    #  ~~ 1 ~~  :
    gray_img = scaled_img(img)
    text = write_txt_from_img(gray_img)
    #  ~~ OR ~~ :
    gray_array = scaled_gray_array(img_ga)
    text = write_txt_from_array(gray_array)

    #  ~~ 2 ~~  :
    write_gray_img(text)

    #  ~~ 3 ~~  :
    color_array = scaled_color_array(img_ca)
    write_color_img(color_array, text)
