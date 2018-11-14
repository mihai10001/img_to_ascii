from read import import_grayscale, import_color
from traverse import traverse_grayscale_image, traverse_color_image
from write import write_img_as_txt, write_img_gray, write_img_color


if __name__ == "__main__":

    filename = 'test.jpg'
    img, (h, w) = import_grayscale(filename)
    img2, (h, w, z) = import_color(filename)

    new_img, new_w, new_h = traverse_grayscale_image(img, w, h)
    new_img2, new_w2, new_h2, z = traverse_color_image(img2, w, h, z)

    #  FEATURES :
    text = write_img_as_txt(new_img, new_w, new_h)
    img3 = write_img_gray(text)
    img4 = write_img_color(new_img2, text, new_w2, new_h2)
