# how many shapes to draw
myShapeCount = 30
# how big to make em
myShapeSize = 50
# draw as many frames as we have shapes
myFrames = myShapeCount

# loop through the frames
for myFrame in range(myFrames):
    # draw a new page for each frame and set the frame rate
    newPage()
    frameDuration(1/12)
    # draw a background
    fill(1)
    rect(0, 0, width(), height())
    # set the fill
    fill(0)
    # move to the vertical center
    translate(0, height()/2)
    # now draw all of our shapes
    for myShape in range(myShapeCount):
        # but since we are animating
        # only draw the shape if we are on the frame that corresponds to the shape to draw
        if myFrame == myShape:
            oval(0, 0, 50, 50)
        translate(width()/myShapeCount)
        
# save it as a gif
saveImage('basicAnimation.gif')