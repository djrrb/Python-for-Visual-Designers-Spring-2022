bp = BezierPath()

bp.moveTo((0, 0))
bp.lineTo((width(), 0))
bp.lineTo((width(), 100))

#bp.lineTo((0, 100))

myHandle = 460
myWiggle = randint(-myHandle, myHandle)
myWiggle2 = randint(-myHandle, myHandle)

bp.curveTo(
    (width(), 100+myWiggle),
    (0, 100+myWiggle2),
    (0, 100)
    )

# bp.closePath()
# bp.moveTo((20, 20))
# bp.lineTo((20, 50))
# bp.lineTo((50, 50))

drawPath(bp)
