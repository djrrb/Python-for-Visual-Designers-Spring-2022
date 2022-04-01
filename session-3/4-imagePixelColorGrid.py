# get the image, but don’t draw it
myImage = ImageObject('black-raspberries.jpg')

# how many rows and columns to draw
# this is essentially our "resolution"
myRows = 30
myCols = 30

# automatically calculate the width and height of each grid element
myRowHeight = width()/myRows
myColWidth = height()/myCols

# we gotta keep track of x and y
# so we know what coordinates to eyedrop
# from the image
myX, myY = 0, 0

# loop through the rows
for myRow in range(myRows):
    # remember where we are so we can
    # go back to the beginning of each row
    with savedState():
        # now loop through the columns
        for myCol in range(myCols):
            # get the color at (myX, myY)
            # starting at 0, 0 but we will augment
            myColor = imagePixelColor(myImage, (myX, myY))
            # set the fill color and draw the shape
            # unpacking the tuple using *
            fill(*myColor)
            oval(0, 0, myColWidth, myRowHeight)
            # move canvas to the right
            translate(myColWidth, 0)
            # also keep track of x position
            myX += myColWidth
        # this indent shows the end of each column
    # ALSO, exit the saved State so we snap back to the left
    # forgetting all of our translates above  
    
    # at the end of each row, move the canvas up
    translate(0, myRowHeight)
    # also keep track of myY and reset myX to 0
    myY += myRowHeight
    myX = 0

# save the image
saveImage('berries.pdf')