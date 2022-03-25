# loop through 20 pages
for myPage in range(20):
    newPage()
    # slow down the gif, only 5 FPS
    frameDuration(1/5)
    # black background
    fill(0)
    rect(0, 0, width(), height())
    # set fill to white
    fill(1)
    
    # how many points will this shape have?
    # a random number between 3 and 20
    myPointCount = randint(3, 20)
    
    # make an empty list that we will fill
    myPointList = []

    for myPoint in range(myPointCount):
        # get random x, y coordinates
        # within the bounds of the canvas
        myX = randint(0, width())
        myY = randint(0, height())
        # combine those into a tuple
        myXY = (myX, myY)
        # add those to the end of our point list
        myPointList.append(myXY)
    
    # let’s see our list of points
    print(myPointList)
    
    # the polygon() function doesn’t expect a list
    # so we use the asterisk to “unpack” that list
    # and feed polygon() the list’s contents instead of the list itself. I’ll talk about this next week
    polygon(*myPointList)
    
# save the image
saveImage('randomPolygon.gif')
    