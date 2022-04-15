# same as previous script
# but get rid of the X change
myShapeCount = 100
myShapeSize = 50
myFrames = myShapeCount
for myFrame in range(myFrames):
    newPage()
    fill(1)
    rect(0, 0, width(), height())
    fill(0)
    frameDuration(1/24)
    translate(width()/2, height()/2)
    for myShape in range(myShapeCount):
        myProgress = myShape / myShapeCount
        myYValue = sin(2*pi*myProgress)
        myY = myYValue * height()/2
        if myShape == myFrame:
            # the X value remains contsant
            # i centered it by subtracting the radius
            oval(-25, myY-25, 50, 50)
        

saveImage('bouncingBall.gif')