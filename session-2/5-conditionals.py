myShapeSize = width()

myShapeCount = 33

translate(width()/2, height()/2)

myDrawBlack = True

for myShape in range(myShapeCount):
    print(myShape)
    if myDrawBlack:
        fill(0)
        myDrawBlack = False
    else:
        fill(1)
        myDrawBlack = True
    rect(
        -myShapeSize/2, # x
        -myShapeSize/2, # y
        myShapeSize, # w
        myShapeSize # h
        )
    scale(.9)
    rotate(5)
    
        
saveImage('rectangles.pdf')