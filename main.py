from PIL import Image
import numpy as np


# convert gray, L for jpeg w/o alpha, LA for png w/ alpha
def load_image_greyscale(infilename):
    img = Image.open(infilename).convert('L')
    img.load()
    data = np.asarray(img, dtype=np.int32)
    return data


def save_image(npdata, outfilename):
    img = Image.fromarray(np.asarray(np.clip(npdata, 0, 255), dtype="uint8"), "L")
    img.save(outfilename)


pix = load_image_greyscale('test.jpg')
print(pix.size, pix.shape)  # 564 x 812 = 564 coloane, 812 randuri
width, height = pix.shape
print(width, height)

# divide part
# greatet common divisor
# from fractions import gcd
# print(gcd(600, 400))


# split in grid with cells of 4x4 values
divisor = 4
blocks_height = int(height/divisor)  # 812 / 4 = 203 blocuri
blocks_width = int(width/divisor)  # 564 / 4 = 141 blocuri
result_array = np.zeros((blocks_height, blocks_width), dtype=np.int32)
print(result_array.shape)


def get_median(nparray):
    return int(np.median(nparray))


#np.set_printoptions(threshold=np.inf)

start_x, start_y = 0, 0
for col in range(blocks_height):
    start_x = 0
    for row in range(blocks_width):
        result_array[col][row] = get_median(pix[start_x: start_x + divisor, start_y: start_y + divisor])
        start_x += divisor
    start_y += divisor


# list of characters depending on size from internet
mylist = [
          ['@', 0, 25], ['#', 26, 50], ['%', 51, 75], ['x', 76, 100], ['o', 101, 125],
          [';', 126, 150], [':', 151, 175], [',', 176, 200], ['.', 201, 225], [' ', 226, 255]
         ]

# w0w
save_image(np.transpose(result_array), 'result.jpg')

# more w0w test
result_array = np.transpose(result_array)
blocks_height, blocks_width = blocks_width, blocks_height
result = open('result.txt', 'w')

for col in range(blocks_height):
    whole_row = ''
    for row in range(blocks_width):
        check = result_array[col][row]
        char = ''
        for element in mylist:
            if check >= element[1] and check <= element[2]:
                whole_row += element[0]
    result.write(whole_row + '\n')

result.close()
