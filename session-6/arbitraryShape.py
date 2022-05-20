myCoords = []
myPointCount = randint(3, 10)
for myPoint in range(myPointCount):
    myX = randint(0, width())
    myY = randint(0, height())
    myCoords.append( (myX, myY) )

rgb = (1, 0, 0)
fill(*rgb)    
polygon(*myCoords)

