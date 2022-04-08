# import the csv module
import csv

# set our variables
myCSVPath = 'Business Cards - Sheet1.csv'
myInch = 72
myMargin = 20

# call the image, we only have to do this once and we can reuse it
myLogoImage = ImageObject('logo.png')

# open the CSV and get it as a file object
with open(myCSVPath) as myCSVFile:
    # read the CSV into a CSV reader object
    myReader = csv.reader(myCSVFile)
    # loop through each row in the reader
    # where myRow is a list of columns
    # and myRowIndex is what number row we are on, starting at 0
    for myRowIndex, myRow in enumerate(myReader):
        # skip the first row
        if myRowIndex == 0:
            continue
        # unpack the columns into separate variables
        myName, myAddress, myPhone, myEmail = myRow
        # make a new 3.5x2 page
        newPage(3.5*myInch, 2*myInch)
        # move our "cursor" to give the document a margin
        translate(myMargin, myMargin)
        
        # set the width of the logo
        myLogoWidth = 75
        
        # figure out how much to scale the logo in order to fit it in the logo width
        myLogoScale = myLogoWidth / myLogoImage.size()[0]
    
        # save the state, scale, and draw the logo
        with savedState():
            scale(myLogoScale)
            image(myLogoImage, (0, 0))
            # uncomment the following to draw a box instead of the logo
            #fill(1, 0, 0)
            #rect(0, 0, myLogoImage.size()[0], myLogoImage.size()[1])
            
        # define the text box based on the canvas width minus margins and the logo
        myTextBoxWidth = width() - myMargin*2 - myLogoWidth
        # define the text box height based no the height minus margins
        myTextBoxHeight = height()-myMargin*2
        # visualize the text box we will draw in
        fill(.9)
        rect(myLogoWidth, 0, myTextBoxWidth, myTextBoxHeight)
        # set the formatting
        font('Verdana', 18)
        fill(0)
        # draw the text to the text box
        # it will wrap as necessary
        textBox(myName, (myLogoWidth, 0, myTextBoxWidth, myTextBoxHeight))

# our last dedent closes the CSV file