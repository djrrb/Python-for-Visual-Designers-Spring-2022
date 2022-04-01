# make a new page
newPage('Letter')

# make an inch variable to convert
# points to inches
myInch = 72

# move the canvas
translate(200, 200)

# set the fill to green
fill(0, 1, 0)


# save our state
with savedState():
    # move to the upper right and draw a red dot
    fill(1, 0, 0)
    translate(200, 400)
    rotate(45)
    scale(.5)
    # this is going to draw a 3 inch rectangle in the upper right that has been scaled by a half and rotated 45 degrees
    rect(0, 0, 3*myInch, 3*myInch)
   
# dedenting gets us back (200, 200) and a green color, with no rotation
rect(50, 50, 3*myInch, 3*myInch)
oval(0, 0, 1*myInch, 1*myInch)