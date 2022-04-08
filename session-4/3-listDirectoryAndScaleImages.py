# a variant where we scale the image to fit the page size

# import the os module
import os

# get a folder of images
myFolder = '/Users/david/Desktop/nickelgothic2-social'
# loop through the folder
for myFileName in os.listdir(myFolder):
    # get the full path
    myPath = os.path.join(myFolder, myFileName)
    # if the path ends with png
    if myFileName.endswith('.png'):
        # make an image object
        myImage = ImageObject(myPath)
        # do formatting
        myImage.sepiaTone()
        # make the new page at a particular size
        newPage('Letter')
        # get the dimensions of the image
        myImageWidth, myImageHeight = myImage.size()
        # i could also get that using
        # myImageWidth = myImage.size()[0]
        
        # determine the amount we need to scale by dividing the image width by the canvas width
        myScaleFactor = width()/myImageWidth
        # do the scale transformation
        scale(myScaleFactor)
        # draw the image
        image(myImage, (0, 0))

