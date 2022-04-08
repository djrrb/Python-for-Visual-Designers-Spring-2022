# import the csv module
import csv

# set the variables
myCSVPath = 'Business Cards - Sheet1.csv'
myInch = 72
myMargin = 20
myCenterMargin = 10
debug = False

# define the logo image
myLogoImage = ImageObject('logo.png')

# open the csv as a file
with open(myCSVPath) as myCSVFile:
    # read the file using the csv reader
    myReader = csv.reader(myCSVFile)
    # loop through each row in the csv
    # where myRow is a list of columns
    # and myRowIndex is what number row we are on, starting at 0
    for myRowIndex, myRow in enumerate(myReader):
        # skip the first row
        if myRowIndex == 0:
            continue
        # unpack the columns into variables
        myName, myAddress, myPhone, myEmail = myRow
    
        # make a new page
        newPage(3.5*myInch, 2*myInch)
        # move to the margin
        translate(myMargin, myMargin)
        
        # draw the logo
        myLogoWidth = 75
        myLogoScale = myLogoWidth / myLogoImage.size()[0]
        with savedState():
            # save the state so the change in scale is only temporary
            scale(myLogoScale)
            image(myLogoImage, (0, -1))
        # calculate the text box
        myTextBoxWidth = width() - myMargin*2 - myLogoWidth
        myTextBoxHeight = height()-myMargin*2
        # draw the text box in debug mode
        fill(.9)
        if debug: rect(myLogoWidth, 0, myTextBoxWidth, myTextBoxHeight)

        # make a new formatted string 
        myText = FormattedString(
            myName, 
            font='ComicSansMS',
            fill=(1, 0, 0)
        )
        # append new text with new formatting
        myText.append(
            '\n\n'+myAddress.strip(), 
            font='MinionPro-Regular',
            openTypeFeatures=dict(smcp=True),
            fill=(0, 0, 0)
            )
        # and more text
        myText.append('\n\n'+myPhone)
        # and more text
        myText.append(
            '\n\n'+myEmail.lower(), 
            openTypeFeatures=dict(resetFeatures=True), 
            font="Minion Pro Italic"
        )

        if debug: print(myText)
        
        # now draw the text box
        # it takes the string (or FormattedString) to draw
        # and also a (x,y,w,h) tuple 
        textBox(myText, 
            (
                myLogoWidth+myCenterMargin,  # x
                0, # y
                myTextBoxWidth, # width
                myTextBoxHeight # height
            )
        )
        
# our last dedent closes the CSV file
    