# draw the first shape the width of the canvas
myShapeSize = width()

# how many shapes to draw
myShapeCount = 33

# move to the center of the canvas
translate(width()/2, height()/2)

# loop through the number of shapes
for myShape in range(myShapeCount):
    print(myShape)
    # make a random color
    fill(
        random(), # r
        random(), # g
        random(), # b
        )
    # draw the rectangle, offsetting x and y by half the size
    rect(
        -myShapeSize/2, # x
        -myShapeSize/2, # y
        myShapeSize, # w
        myShapeSize # h
        )
    # after drawing each rectangle, scale and rotate the canvas
    # this will draw the next rectangle smaller and slightly rotated
    scale(.9)
    rotate(5)
    
# save the image at the end if we want
# dedent this to make sure it only gets saved once
saveImage('rectangles.pdf')