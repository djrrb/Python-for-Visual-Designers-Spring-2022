# draw a sine wave

# how many shapes to draw
myShapeCount = 60
# how big to draw them
myShapeSize = 50

newPage()
# move to the vertical middle
translate(0, height()/2)
# loop through the shapes
for myShape in range(myShapeCount):
    # how far are we through the circle
    # divided by 1
    myProgress = myShape / myShapeCount
    # 2*pi is a full circle
    # get the sine of our progress through a circle
    myYValue = sin(2*pi*myProgress)
    # now multiply that by half our height, and we will get waves that go above and below the middle
    myY = myYValue * height()/2
    # draw the oval
    oval(0, myY, 50, 50)
    # move to the right to draw the next circle
    translate(width()/myShapeCount)

saveImage('sineWave.gif')