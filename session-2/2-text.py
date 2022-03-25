# import the random library
from random import choice

# choose a random font from the ones we have installed
myFontChoice = choice(installedFonts())

print(myFontChoice)
# set the font
font(myFontChoice, 130)
# change the tracking
tracking(-5)
# change the canvas settings
fill(1, 0, 0)
strokeWidth(2)
stroke(0, 0, 1)

# center the text in the center of the canvas (width()/2)
# raise the text vertically by its descender
text(
    'happy birthday', # the string to draw
    (width()/2, -fontDescender()), # (x, y) tuple
    'center' # alignment (left, center, right)
)