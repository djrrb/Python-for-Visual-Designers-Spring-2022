from interpolate import remap

myFrames = 10
for myFrame in range(myFrames):
    newPage()
    rect(0, 0, width(), height())
    fill(1)
    font('CondorVariable-VF.ttf', 200)
    minValue = listFontVariations()['wdth']['minValue']
    maxValue = listFontVariations()['wdth']['maxValue']
    myProgress = myFrame / myFrames
    mySineValue = sin(2*pi*myProgress) 
    myWeight = remap(mySineValue, -1, 1, minValue, maxValue)
    print(myProgress, myWeight)
    fontVariations(wdth=myWeight)
    translate(width()/2, 400)
    text('hello world', (0, 0), align="center")
    
saveImage('animatedText.gif')