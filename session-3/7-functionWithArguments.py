# define a function
def myOtherLogo(mySize=100, myColor=(0, 0, 0, 1) ):
    myOffset = 2
    myShapeCount = 10
    # this function accepts two arguments with default values
    # mySize and myColor variables will be created 
    # it then uses those arguments to draw the logo at a certain size
    
    # save the state, so the formatting only applies to this logo
    with savedState():
        fill(*myColor)
        for myShape in range(myShapeCount):
            oval(-mySize/2, -mySize/2+myOffset*mySize, mySize, mySize)
            rotate(360/myShapeCount)
    

# draw the logo a couple times
translate(width()/2, height()/2)
myOtherLogo(180)

newPage()
translate(width()/2, height()/2)

myOtherLogo(myColor=(0, 1, 1, 1))

newPage()

# draw the logo big and transparent like a watermak
translate(0, height()/2)
myOtherLogo(220, (0, 0, 0, 0.1))
translate(width()/2)

# now draw it small and magenta
myOtherLogo(50, (1, 0, 1, 1))