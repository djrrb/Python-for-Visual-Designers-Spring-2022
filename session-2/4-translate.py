myShapeSize = width()

myShapeCount = 33

translate(width()/2, height()/2)

for myShape in range(myShapeCount):
    print(myShape)
    fill(
        random(), # r
        random(), # g
        random(), # b
        1
        )
    rect(
        -myShapeSize/2, # x
        -myShapeSize/2, # y
        myShapeSize, # w
        myShapeSize # h
        )
    scale(.9)
    rotate(5)
    print(myShapeSize)
    
        
saveImage('rectangles.pdf')