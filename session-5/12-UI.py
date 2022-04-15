# define our variables in a UI
Variable([
    # this is the myBranchLength slider
    dict(name="myBranchLength", ui="Slider",
            args=dict(
                value=100, # default value
                minValue=50, # minimum
                maxValue=300)), # maximum
                
    # this is the myMaxLevels slider
    dict(name="myMaxLevels", ui="Slider",
            args=dict(
                value=3,
                minValue=0,
                maxValue=6)),
                
    # a variable wiggle, this will be the amount of randomness
    dict(name="myWiggle", ui="Slider",
            args=dict(
                value=10,
                minValue=0,
                maxValue=40)),
                
    # a variable wiggle, this will be the amount of randomness
    dict(name="myStrokeWidth", ui="Slider",
            args=dict(
                value=10,
                minValue=1,
                maxValue=50)),
    # dashed line variable
    dict(name="dashedLine", ui="CheckBox"),
    # choose the color of the tree
    dict(name="myColor", ui="ColorWell"),
    dict(name="myText", ui="EditText")
    ], globals())

# this is a function that draws a branch
def myBranch(myLevel=0):
    # draw a line
    stroke(myColor)
    line((0, 0), (0, myBranchLength))
    # move up to the end of the line
    translate(0, myBranchLength)
    # loop through two different angles
    # we’ll hardcode them as -30 and +30
    # myWiggle is a float so we gotta convert to int
    # to work with randint()
    myAngleList = [
        randint(int(-30-myWiggle), int(-30+myWiggle)), 
        randint(int(30-myWiggle), int(30+myWiggle)), 
        ]
    # loop through our angles
    for myAngle in myAngleList:
        # save state so that we always rotate from the source
        # and don't keep amping up the rotation
        with savedState():
            # do the rotation and a slight scale
            rotate(myAngle)
            scale(.9)
            # if we haven’t reached our maximum levels yet
            if myLevel < myMaxLevels:
                # draw the branch and augment the level variable
                myBranch(myLevel+1)
                
# do our formatting
lineCap('round')
stroke(0)
strokeWidth(myStrokeWidth)
# the dashed line checkbox will return True or False
# so we can do a conditional for it
if dashedLine:
    lineDash(20)

# move to the middle and a little up
translate(width()/2, 100)
# draw the first branch
# this will trigger a chain reaction
# that keeps drawing branches until we 
myBranch()
stroke(None)

# also draw some text using the UI variable myText 
# just because we can
fill(1, 0, 0)
font('Verdana', 100)
text(myText, (0, -100), align="center")
