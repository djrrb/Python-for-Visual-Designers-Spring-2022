translate(0, height()/2)

myCount = 20
myDirection = 1
myX = 0

myPath = BezierPath()
myPath.moveTo((0, 0))

for myLine in range(myCount):
    myAdvance = randint(0, 100)
    myAdvance = 100
    myZag = randint(0, 500)
    myPath.lineTo((myX, myZag*myDirection))
    myDirection *= -1
    myX += myAdvance
    
fill(None)
stroke(0)
strokeWidth(10)
drawPath(myPath)
    