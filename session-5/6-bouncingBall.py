myShapeCount = 50
myShapeSize = 50
myFrames = myShapeCount
for myFrame in range(myFrames):
    newPage()
    frameDuration(1/12)
    translate(width()/2, height()/2)
    for myShape in range(myShapeCount):
        myProgress = myShape / myShapeCount
        myYValue = sin(2*pi*myProgress)
        myY = myYValue * height()/2
        if myShape == myFrame:
            oval(0, myY, 50, 50)
        #translate(width()/myShapeCount)
        

saveImage('movingOval.gif')