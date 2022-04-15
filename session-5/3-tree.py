# an example of recursion

# how many levels deep we will go into the recursion
myMaxLevels = 8
# how long to draw the branch
myBranchLength = 100

# my branch is a function that 
# draws a line
# moves to end of that line
# rotates and calls itself to draw two more lines
def myBranch(myLevel=0):
    # draw a line
    line((0, 0), (0, myBranchLength))
    # move up to the end of the line
    translate(0, 100)
    # loop through two different angles
    for myAngle in [randint(-35, -25), randint(25, 35)]:
        # save our state so the rotation stays local
        with savedState():
            # rotate and scale a little
            rotate(myAngle)
            scale(.9)
            # if we haven’t reached our number of max levels
            if myLevel < myMaxLevels:
                # set a random color
                stroke(random(), random(), random())
                # draw another branch at a deeper level
                myBranch(myLevel+1)
                
# do some formatting
lineCap('round')
stroke(0)
strokeWidth(10)
translate(width()/2, 100)
# call myBranch() once, this is enough to draw the whole tree
myBranch()