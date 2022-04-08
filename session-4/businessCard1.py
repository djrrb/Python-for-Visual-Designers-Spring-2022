import csv

myCSVPath = 'Business Cards - Sheet1.csv'
myInch = 72
myMargin = 20

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
        print(myLogoScale)
        with savedState():
            scale(myLogoScale)
            image(myLogoImage, (0, 0))
            #fill(1, 0, 0)
            #rect(0, 0, myLogoImage.size()[0], myLogoImage.size()[1])
            
        myTextBoxWidth = width() - myMargin*2 - myLogoWidth
        myTextBoxHeight = height()-myMargin*2
        fill(.9)
        rect(myLogoWidth, 0, myTextBoxWidth, myTextBoxHeight)
        font('Verdana', 14)
        fill(0)
        textBox(myName, (myLogoWidth, 0, myTextBoxWidth, myTextBoxHeight))

    