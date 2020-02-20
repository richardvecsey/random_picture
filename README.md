# random_picture

Create a random RGB image in the given resolution
------------------------------------------------------------------------------
## Input:<br>
**height**  *(int)*       height of final picture<br>
**width**   *(int)*       width of final picture<br>
**save**    *(boolean)*   Picture save if *True* (default: *False*)<br>
**show**    *(boolean)*   Picture show if *True* (default: *True*)<br>

## Output:<br>
**picture**  (image)
- If save is *True*: myrndpic.png
- If show is *True*: picture is on the display

## Requested packages:<br>
- Pillow
- Numpy

## Possible usage:<br>
- testing screen
- make noise to neural network training process
- create unique wallpaper
- understand image processing and image creation from array

------------------------------------------------------------------------------

Feel free to rewrite the code and play with it. Change the integer values in
the np.random.randint function between 0 and 255 to get other result. Lower
value means darker colours, higher value means lighter colours.
- RGB   0,  0,  0 = black
- RGB 255,255,255 = white
