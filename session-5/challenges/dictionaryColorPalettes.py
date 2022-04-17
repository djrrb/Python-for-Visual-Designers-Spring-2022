# import choice() in order to choose a random font later
from random import choice

# set a global margin
myMargin = 100

# define the dictionary of color palettes
# each color palette gets a name, which is mapped to a dictionary of roles. Within each sub dictionary, the role is mapped to an RGB sequence

myColorPalettes = {
    'lightMode':
        {
            'foreground': (0, 0, 0),
            'background': (1, 1, 1),
            'highlight': (0, 0, 1)
            },
    'darkMode':
        {
            'foreground': (1, 1, 1),
            'background': (0, 0, 0),
            'highlight': (0, 1, 0)
            },
            
    'funkyMode':
        {
            'foreground': (.8, 1, .8),
            'background': (1, 0, 1),
            'highlight': (1, 1, 0)
            },
    }

# render our design in each of the predefined palettes
# loop through the dictionary
# myPaletteName will be equal to the key of each palette
for myPaletteName in myColorPalettes:
    # make a new page
    newPage()
    # define the font size and position relative to the canvas height
    myFontSize = height()/8 # font is 1/8th of the page
    myTextY = height()/2 # positioned at 1/3 of the page high 
    myLineOffset = -100 # the line will appear X pts below the text
    
    # get the value of each palette by querying the palettes dictionary
    # my palette is now a dictionary with 'foreground', 'background', and 'highlight' keys
    myPalette = myColorPalettes[myPaletteName]

    # call the background color of the current palette
    fill(*myPalette['background'])
    # draw a background
    rect(0, 0, width(), height())
    # call the foreground color
    fill(*myPalette['foreground'])
    # set the font to a random font
    font(choice(installedFonts()), myFontSize)
    # set our text
    text('hello world', (width()/2, myTextY), align="center")
    # set the highlight color
    stroke(*myPalette['highlight'])
    # draw a thick dotted line below the text
    strokeWidth(30)
    lineDash(5)
    line(
        (myMargin, myTextY+myLineOffset), 
        (width()-myMargin, myTextY+myLineOffset)
    )