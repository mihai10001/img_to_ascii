## Image to ASCII (text) converter
A personal project made for fun  
It needs optimizations  

### How to run:
Requires two Python modules: __Numpy__ and __Pillow__  
Run the script with the command: __python3 main.py__  

### Output examples:  

| Original Image | Output color | Output black & white |
| ----------- | ----------- | ----------- |
| <img src="examples/apple.jpg" width="180"> | <img src="examples/result_apple_color.png" width="180"> | <img src="examples/result_apple_gray.png" width="180"> |
| <img src="examples/dogs.jpg" width="180"> | <img src="examples/result_dogs_color.png" width="180"> | <img src="examples/result_dogs_gray.png" width="180"> |

### Note:  
Works best with images that have a white background. Also great with logos, etc

### To do:
Better CLI interface  
Pre-process images that don't have a high contrast ratio before computing (and other pre-processing methods)  
Automatically pick the best scaling ratio based on original dimension of the image as another user option  
Later add other useful user options, create a user interface

_Contains functions that deal with pixel arrays of 1D or 3D. Also other various array computations, mapping pixel to characters, etc_
