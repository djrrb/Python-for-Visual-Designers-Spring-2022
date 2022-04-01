# get an image object
myImage = ImageObject('black-raspberries.jpg')

# draw the image
image(myImage, (0, 0))

# eyedrop (500, 500)
# returns a (r,g,b,a) tuple
myColor = imagePixelColor(myImage, (500, 500))

# set the fill color to myColor, unpacking it
fill(*myColor)
# draw a swatch at the lower left
rect(0, 0, 100, 100)