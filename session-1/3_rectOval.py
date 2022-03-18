# make a new page
newPage()
# set the fill color (r, g, b)
# if using Adobe values, divide by 255
fill(9/255, 92/255, 211/255)
# make a green stroke
stroke(0, 1, 0)
# make the stroke thicker
strokeWidth(10)
# draw a rectangle (x, y, width, height)
rect(0, 0, 100, 100)
# change the fill
fill(1, 0, 0)
# remove the stroke
stroke()
# now draw an oval
oval(300, 300, 100, 100)

saveImage('rectOval.gif')