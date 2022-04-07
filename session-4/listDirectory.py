import os
myFolder = '/Users/david/Desktop/nickelgothic2-social'
for myFileName in os.listdir(myFolder):
    myPath = os.path.join(myFolder, myFileName)
    if myFileName.endswith('.png'):
        myImage = ImageObject(myPath)
        myImage.sepiaTone()
        newPage(*myImage.size())
        image(myImage, (0, 0))

