# set the length of a handle
myHandle = 300

# define a new bezier path
bp = BezierPath()

# take a list of commands for the drawing
# move to the loewr left
bp.moveTo((0, 0))
# draw a line to the lower right
bp.lineTo((width(), 0))
# draw a line up
bp.lineTo((width(), 100))

# each handle can wiggle separately by a random amount
myWiggle = randint(-myHandle, myHandle)
myWiggle2 = randint(-myHandle, myHandle)

# draw a curve from the right to the left
bp.curveTo(
    (width(), 100+myWiggle), # handle 1
    (0, 100+myWiggle2), # handle 2
    (0, 100) # destination point
    )

drawPath(bp)
