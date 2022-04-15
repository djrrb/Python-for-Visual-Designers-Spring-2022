# import our handy remap function to scale one range to another
from interpolate import remap

# how many frames to draw
myFrames = 48
for myFrame in range(myFrames):
    newPage(2000, 1000)
    frameDuration(1/24)
    # black background
    rect(0, 0, width(), height())
    fill(1)
    # set the font
    font('CondorVariable-VF.ttf', 200)
    # query the font for its min and max width value
    # these are ditionaries within dictionaries so we can slice to drill in and get the data we need
    minValue = listFontVariations()['wdth']['minValue']
    maxValue = listFontVariations()['wdth']['maxValue']
    # determine our progress through the cycle
    # a number between 0 and 1
    myProgress = myFrame / myFrames
    # use sine to get our relative value on the circle (2*pi is full circle)
    mySineValue = sin(2*pi*myProgress) 
    # remap that value between -1 and 1 to or variable font’s scale
    myWidth = remap(mySineValue, -1, 1, minValue, maxValue)
    print(myProgress, myWidth)
    # set the font Variations
    fontVariations(wdth=myWidth)
    # move to the middle
    translate(width()/2, 450)
    # draw the text
    text('hello world', (0, 0), align="center")

saveImage('animatedText.gif')