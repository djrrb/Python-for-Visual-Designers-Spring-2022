# import the OS module
import os
# drag on an absolute path
# you gotta change this
myFolder = '/Users/david/Desktop/nickelgothic2-social'

# use listdir to get a list of all files in the directory
# then loop through it
for myFileName in os.listdir(myFolder):
    # myFileName is now equal to just the filename of the current file
    # add the folder path to get the full path for the file
    myPath = os.path.join(myFolder, myFileName)
    # test to see if it’s a png
    if myFileName.endswith('.png'):
        # if so make an image object
        myImage = ImageObject(myPath)
        # do some formatting
        myImage.sepiaTone()
        # make a new page equal to the size of the image
        newPage(*myImage.size())
        # draw the image to canvas
        image(myImage, (0, 0))

