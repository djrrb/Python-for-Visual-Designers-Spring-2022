newPage()

def myZigZag():
    
    myDivisions = 10
    myX = 0
    myUpDown = 1
    myAmplitude = 280# base number
    myAmpVar = 80 # volatility 

    
    bp = BezierPath()
    bp.moveTo((myX, 0))
    myX += width()/myDivisions

    for myDivision in range(myDivisions-1):
        thisAmplitude = myAmplitude + randint(-myAmpVar, myAmpVar)
        print(thisAmplitude)
        bp.lineTo((myX, myUpDown*thisAmplitude))
        myUpDown *= -1
        myX += width()/myDivisions
    
    bp.lineTo((myX, 0))
    bp.lineTo((myX, -5000))
    bp.lineTo((0, -5000))
    return bp

myRows = 8
myFill = 1

translate(0, height()*1.5)
for myRow in range(myRows):

    fill(myFill)

    drawPath(myZigZag())
    translate(0, -200)
    myFill *= -1