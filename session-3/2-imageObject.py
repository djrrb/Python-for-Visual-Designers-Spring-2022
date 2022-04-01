# define the image object
# using the image file in our folder
myImage = ImageObject('black-raspberries.jpg')

# apply some filters
# SO MANY to explore
# https://drawbot.com/content/image/imageObject.html

myImage.sepiaTone(3)
myImage.kaleidoscope(10)

# draw a page at the image size
# myImage.size() is a tuple, so we unpack it and feed to newPage()
newPage(*myImage.size())

# draw the image at 0, 0
image(myImage, (0, 0))