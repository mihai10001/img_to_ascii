# Image to ASCII(text) converter.  
__A personal project made for fun.__  
__Widely known concept, implemented by me.__  
It needs a couple of optimizations, but the overall performance is fine.  

_I had to create some algorithms, that deal with pixel arrays of 1D or 3D._    
_Also other various array computations, mapping pixel to characters, etc._   

## How to run :
<br><br>

> For now, you can run the script with the command: __python3 main.py__  
> 
> It will aditionally require two well-known Python modules: __Numpy__ and __Pillow__.  
> Install them with: pip3 install numpy, pip3 install Pillow

<br><br>

## Small example :  
Input image:  
<img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="300">

<br><br>
Output text:  

                  ~~~~~~~~~~~
                ~~~~~~~~~~~~~~~
               : ~  '~~~~~~~~~~++.
               :~~~~~~~~~~~~~~++++
            "". .'~~~~~'~~++++++ ....
        ~~~~~~~~~~~~~~~~++++++++.'""^^^^  
       ~~~~~~~~~~~~~~~~~+++++++++.'^^^^^^^ 
      ~~~~~~~~~~~~~~~++++++++++++ "^^^^^^^"
      ~~~~~~~~~~~~~~~~++++++++~' '^^^^^^^^^
      ~~~~~~~~~~...'''''''''''"^^^^^^^^^^^^
      ~~~~~~~~~ """""""""""^^^^^^^^^^^^^^^^
      '~~~~~~~..""""""""""^^^^^^^^^^^^^^^^.
       :~~~~++.'"""""""""^^^^^^^^^^^^^^^^. 
         ^~~+~.'""""""^^^'''''''""""""'    
               '"""""^^^^^^^^^^^^.         
               '^""^^^^^^^^^'.'^^.         
               .^^^^^^^^^^^^. '^^.         
                 '^^^^^^^^^^^^^^.          
                    '""^^^^"'.



## Note :  
Works best with images that have a white background. Also great with logos, etc.
