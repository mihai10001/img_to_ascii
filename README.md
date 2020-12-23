# Image to ASCII(text) converter.  
__A personal project made for fun. Widely known concept, reimagined.__  
_I had to create some algorithms, that deal with pixel arrays of 1D or 3D. Also other various array computations, mapping pixel to characters, etc._   
It needs a couple of optimizations, but the overall performance is fine.  

## Output examples :  

| Original Image | Output Color | Output BW |
| ----------- | ----------- | ----------- |
|![Orig apple](examples/apple.jpg?raw=true "Title") | ![Color apple](examples/result_apple_color.png?raw=true "Title") | ![BW apple](examples/result_apple_gray.png?raw=true "Title") |
|![Orig dog](examples/dogs.jpg?raw=true "Title") | ![Color dog](examples/result_dogs_color.png?raw=true "Title") | ![BW apple](examples/result_dogs_gray.png?raw=true "Title") |


## How to run :
For now, you can run the script with the command: __python3 main.py__  
It will aditionally require two well-known Python modules: __Numpy__ and __Pillow__  

## Note :  
Works best with images that have a white background. Also great with logos, etc.

## To do:
Pre-process images that don't have a high contrast ratio before computing (and other prep-rocessing methods)  
Automatically pick the best scaling ratio based on original dimension of the image as another user optionn
