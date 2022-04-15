# path to font file
fontPath = '/Users/david/Desktop/FitVF.ttf'

# text to set
myText = 'Hello'

grayColor = (119/255,119/255,114/255)
greenColor = (222/255,252/255,88/255)
greenColor = (229/255,252/255,104/255)


fgColor = greenColor
bgColor = grayColor

# constants
margin = 50
# width axis values
defaultValue = 110
minValue = 1
maxValue = 1000 
sizeMultiplier = 1000/750 # fit’s capitals are 75% of the em height
fps = 5 # frames per second
holdFrames = 3 # how many frames to hold at either extreme

# MATH HELPERS
def lerp(start, stop, amt):
	"""
	Return the interpolation factor (between 0 and 1) of a VALUE between START and STOP.
	https://processing.org/reference/lerp_.html
	"""
	return float(amt-start) / float(stop-start)
	
def norm(value, start, stop):
	"""
	Interpolate using a value between 0 and 1
	See also: https://processing.org/reference/norm_.html
	"""
	return start + (stop-start) * value

def remap(value, start1, stop1, start2, stop2, withinBounds=False):
    """
    Re-maps a number from one range to another.
    See also: https://processing.org/reference/map_.html
    (called remap to avoid conflict with map() function)
    """
    factor = lerp(start1, stop1, value)
    if withinBounds:
        if factor < 0: factor = 0
        if factor > 1: factor = 1
    return norm(factor, start2, stop2)

# parse myText into frames
textFrames = []
for i, letter in enumerate(myText):
    textFrames.append(myText[:i+1])
for i in range(holdFrames):
    textFrames.append(myText)
topIndex = len(myText)-1
for i in range(topIndex, 1, -1):
    print(i)
    textFrames.append(myText[:i])

for i in range(holdFrames):
    textFrames.append(myText[0])
    
# loop through each letter in myText
for frameText in textFrames:
    # skip wordspace frames
    if frameText.endswith(' '):
        continue

    # new frame
    newPage(2500, 2000)
    # set the frames per second
    frameDuration(1/fps)
    # black background
    fill(*bgColor)
    rect(0, 0, width(), height())

    # get desired width and height of text
    marginWidth = width()-margin*2
    marginHeight = height()-margin*2

    
    # get the desired font size to fill the space
    theSize = marginHeight * sizeMultiplier
    
    
    # measure the min, max, and default settings
    fsMin = FormattedString(frameText, font=fontPath, fontVariations={'wdth': minValue}, fontSize=theSize)
    fsMax = FormattedString(frameText, font=fontPath, fontVariations={'wdth': maxValue}, fontSize=theSize)
    fsDef = FormattedString(frameText, font=fontPath, fontVariations={'wdth': defaultValue}, fontSize=theSize)
    widthMin = textSize(fsMin)[0]
    widthMax = textSize(fsMax)[0]
    widthDef = textSize(fsDef)[0]
    
    # interpolate between min and default, or default and max, depending
    if marginWidth < widthDef:
        axisValue = remap(marginWidth, widthMin, widthDef, minValue, defaultValue)
    else:
        axisValue = remap(marginWidth, widthDef, widthMax, defaultValue, maxValue)

    # set the text with the interpolated value and draw it
    fs = FormattedString(frameText, font=fontPath, fill=fgColor, fontVariations={'wdth': axisValue}, fontSize=theSize)
    text(fs, (margin, margin))


# save as a gif
saveImage('fit-devanagari-animated-website-1.gif')
