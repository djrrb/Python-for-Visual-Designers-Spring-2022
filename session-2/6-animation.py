# how many pages to draw
myPages = 40
# code that is dedented all the way will run once
print('this will run once')

# draw the shape at the full width
myShapeSize = width()

# how many shapes to draw
myShapeCount = 40

# the starting angle of rotation
myAngle = 0

# each time, let’s bump the angle by a certain amount
# this amount should add up to 360 over the sequence of pages
# so each bump is equal to 360/myPages
myAngleAugment = 360/myPages

# loop through the pages
for myPage in range(myPages):
    # code that is indented once will run on each page
    # \t is a tab
    print('\tthis will run once per page')
    # make a new page
    newPage()
    # set the frame duration
    frameDuration(1/15)
    
    # move to the center of the canvas
    translate(width()/2, height()/2)

    # loop through each shape
    for myShape in range(myShapeCount):
        # now we are double indented
        # this could will run once per page per shape
        # that’s a lot of times!
        print('\t\tthis will run once per shape', myShape)
        
        # if the shape is not even, make it black
        # otherwise, make it white
        if not myShape % 2:
            fill(0)
        else:
            fill(1)
        
        # draw the rectangle offset by half its size
        # so it draws from the center
        rect(
            -myShapeSize/2, # x
            -myShapeSize/2, # y
            myShapeSize, # w
            myShapeSize # h
            )
        # shrink it by 90% each time
        scale(.9)
        # rotate the canvas using our angle variable
        rotate(myAngle)
    # this will run once per page again
    # bump up the angle so it spins more on the next frame
    myAngle += myAngleAugment
    
# dedent again, this code is run once total
# at the very end, save our gif!
saveImage('rectangles.gif')