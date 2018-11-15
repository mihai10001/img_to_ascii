from read import import_grayscale, import_grayscale_array, import_color, import_color_array
from traverse import return_grayscale_img, return_grayscale_array
from write import write_txt_from_img, write_txt_from_array


if __name__ == "__main__":

    filename = 'test.jpg'
    img = import_grayscale(filename)
    img_ga = import_grayscale_array(filename)
    img_c = import_color(filename)
    img_ca = import_color_array(filename)

    #  FEATURES :

    #  ~~ 1 ~~  :
    gray_img = return_grayscale_img(img)
    text = write_txt_from_img(gray_img)
    #  ~~ OR ~~ :
    gray_array = return_grayscale_array(img_ga)
    text2 = write_txt_from_array(gray_array)

    #img3 = write_img_gray(text)
    #img4 = write_img_color(new_img2, text, new_w2, new_h2)
