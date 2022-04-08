# define some text
myText = 'Hello world'

# set the font
font('Verdana')
# set the font size 1
# this way, the width is equal to the width:height proportion of the text as set in this particular font
fontSize(1)
# get the width of the text without drawing it to canvas
myProp = textSize(myText)[0]

# set the desired font size so that the width will fill the canvas
myFontSize = width()/myProp
# set the font size
fontSize(myFontSize)
# draw the text
text(myText, (0, 0))