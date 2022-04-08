myText = 'Hello world'

myFontSize = 100

font('Verdana')
fontSize(1)
lineHeight(1)
myProp = textSize(myText)[0]
myFontSize = width()/myProp
lineHeight(myFontSize)
fontSize(myFontSize)
text(myText, (0, 0))