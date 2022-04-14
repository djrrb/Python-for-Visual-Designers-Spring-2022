myMaxLevels = 8
myBranchLength = 100


def myBranch(myLevel=0):
    # draw a line
    line((0, 0), (0, myBranchLength))
    # move up to the end of the line
    translate(0, 100)
    # loop through two different angles
    for myAngle in [randint(-35, -25), randint(25, 35)]:
        with savedState():
            rotate(myAngle)
            scale(.9)
            if myLevel < myMaxLevels:
                stroke(random(), random(), random())
                myBranch(myLevel+1)
                
        
lineCap('round')
stroke(0)
strokeWidth(10)
translate(width()/2, 100)
myBranch()