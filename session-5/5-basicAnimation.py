myShapeCount = 30
myShapeSize = 50
myFrames = myShapeCount
for myFrame in range(myFrames):
    newPage()
    frameDuration(1/12)
    translate(0, height()/2)
    for myShape in range(myShapeCount):
        if myFrame == myShape:
            oval(0, 0, 50, 50)
        translate(width()/myShapeCount)
        
saveImage('movingOval.gif')