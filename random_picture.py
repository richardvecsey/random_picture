"""
Create a random RGB image in the given resolution
------------------------------------------------------------------------------
Input:  height  (int)       height of final picture
        width   (int)       width of final picture
        save    (boolean)   Picture save if True
                            default: False
        show    (boolean)   Picture show if True
                            default: True

Output: picture (image)     If save is True: myrndpic.png
                            If show is True: picture is on the display
------------------------------------------------------------------------------
Requested packages:
    - Pillow
    - Numpy

Possible usage:
    - testing screen
    - make noise to neural network training process
    - create unique wallpaper
    - understand image processing and image creation from array
------------------------------------------------------------------------------
Feel free to rewrite the code and play with it. Change the integer values in
the np.random.randint function between 0 and 255 to get other result. Lower
value means darker colours, higher value means lighter colours.
    RGB   0,  0,  0 = black
    RGB 255,255,255 = white
"""
# IMPORT SECTION
from PIL import Image
import numpy as np

# VARIABLES
height = 1920
width = 1080
save = False
show = True

# Create array in the final size filled with zeros
picture_array = np.zeros((width, height, 3))

# Create arrays and filled with random number between 0 and 255
red_layer = np.zeros((width, height))
red_layer = np.random.randint(0, 255, (width, height))
green_layer = np.zeros((width, height))
green_layer = np.random.randint(0, 255, (width, height))
blue_layer = np.zeros((width, height))
blue_layer = np.random.randint(0, 255, (width, height))

# Separate layers and move into the final array
picture_array[:,:,0] = red_layer
picture_array[:,:,1] = green_layer
picture_array[:,:,2] = blue_layer

# Convert array to image
image = Image.fromarray(picture_array.astype(int), 'RGB')

# Save image
if save:
    image.save('myrndpic.png')
    
# Show image    
if show:
    image.show()
