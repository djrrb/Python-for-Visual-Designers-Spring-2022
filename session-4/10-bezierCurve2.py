# what's the longest a handle can be
myHandle = 300
# the height of the shape
myHeight = 1000
# how many shapes
myShapeCount = 15
# how much to scale each time draw a shape
# so that each successive one gets taller
myScale = .9

newPage()
rect(0, 0, width(), height())

# draw a certain number of shapes
for myStripe in range(myShapeCount):
    # define a new bezier path
    bp = BezierPath()

    # take a list of commands for the drawing
    # move to the loewr left
    bp.moveTo((0, 0))
    # draw a line to the lower right
    bp.lineTo((width(), 0))
    # draw a line up
    bp.lineTo((width(), myHeight))

    # each handle can wiggle separately by a random amount
    myWiggle = randint(-myHandle, myHandle)
    myWiggle2 = randint(-myHandle, myHandle)

    # draw a curve from the right to the left
    bp.curveTo(
        (width(), myHeight+myWiggle), # handle 1
        (0, myHeight+myWiggle2), # handle 2
        (0, myHeight) # destination point
        )

    # make each shape a random color
    fill(random(), random(), random(), .2)
    # draw the path
    drawPath(bp)
    # scale down a little each time
    scale(1, myScale)