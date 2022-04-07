import os
myFolder = '/Users/david/Desktop/nickelgothic2-social'
for myFileName in os.listdir(myFolder):
    myPath = os.path.join(myFolder, myFileName)
    if myFileName.endswith('.png'):
        myImage = ImageObject(myPath)
        myImage.sepiaTone()
        newPage('Letter')
        myImageWidth, myImageHeight = myImage.size()
        # myImage.size()[0]
        myScaleFactor = width()/myImageWidth
        scale(myScaleFactor)
        image(myImage, (0, 0))

