# this is like the previous script 
# but we break it up into separate frames
myShapeCount = 50
myShapeSize = 50
myFrames = myShapeCount
for myFrame in range(myFrames):
    newPage()
    frameDuration(1/12)
    translate(0, height()/2)
    for myShape in range(myShapeCount):
        myProgress = myShape / myShapeCount
        myYValue = sin(2*pi*myProgress)
        myY = myYValue * height()/2
        # use the if statement to only draw the shape
        # if we are on the corresponding frame
        # so we get one shape per frame
        # rather than them all at once
        if myShape == myFrame:
            oval(0, myY, 50, 50)
        translate(width()/myShapeCount)
        
saveImage('animatedSineWave.gif')