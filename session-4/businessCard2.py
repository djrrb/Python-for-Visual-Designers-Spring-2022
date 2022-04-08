import csv

myCSVPath = 'Business Cards - Sheet1.csv'
myInch = 72
myMargin = 20
myCenterMargin = 10
debug = False

myLogoImage = ImageObject('logo.png')

with open(myCSVPath) as myCSVFile:
    myReader = csv.reader(myCSVFile)
    for myRowIndex, myRow in enumerate(myReader):
        if myRowIndex == 0:
            continue
        myName, myAddress, myPhone, myEmail = myRow
    
        newPage(3.5*myInch, 2*myInch)
        translate(myMargin, myMargin)
        myLogoWidth = 75
        
        myLogoScale = myLogoWidth / myLogoImage.size()[0]
        with savedState():
            scale(myLogoScale)
            rotate(0)
            image(myLogoImage, (0, -1))

        myTextBoxWidth = width() - myMargin*2 - myLogoWidth
        myTextBoxHeight = height()-myMargin*2
        fill(.9)
        if debug: rect(myLogoWidth, 0, myTextBoxWidth, myTextBoxHeight)
        font('Papyrus', 14)
        fill(1, 0, 0)
        
        myText = FormattedString(
            myName, 
            font='ComicSansMS',
            fill=(1, 0, 0)
        )
        myText.append(
            '\n\n'+myAddress.strip(), 
            font='MinionPro-Regular',
            openTypeFeatures=dict(smcp=True),
            fill=(0, 0, 0)
            )
        myText.append('\n\n'+myPhone)
        myText.append('\n\n'+myEmail.lower(), openTypeFeatures=None)

        if debug: print(myText)
        myText = textBox(myText, (myLogoWidth+myCenterMargin, 0, myTextBoxWidth, myTextBoxHeight))
    print(myText)
    

    