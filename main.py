from read import import_grayscale
from traverse import traverse_grayscale_image
from write import write_img_as_txt


if __name__ == "__main__":
    img, (h, w) = import_grayscale('py.png')
    new_img, new_w, new_h = traverse_grayscale_image(img, w, h)
    text = write_img_as_txt(new_img, new_w, new_h)
