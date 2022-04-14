myShapeCount = 30
myShapeSize = 50
myFrames = 1
for myFrame in range(myFrames):
    newPage()
    frameDuration(1/12)
    translate(0, height()/2)
    for myShape in range(myShapeCount):
        myProgress = myShape / myShapeCount
        myYValue = sin(2*pi*myProgress)
        myY = myYValue * height()/2
        oval(0, myY, 50, 50)
        translate(width()/myShapeCount)
        
saveImage('movingOval.gif')