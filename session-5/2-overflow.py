# set some variables
myPath = 'frankenstein.txt'
myMargin = 50

# open the file
with open(myPath, 'r', encoding='utf-8') as myFile:
    # read the text from the file
    myText = myFile.read()
    # get the first 10k characters from the book
    # so this doesn’t take forever to run
    myText = myText[:10000]
    # format the text
    myFormattedText = FormattedString(
        myText,
        font='Georgia',
        fontSize=10.5,
        lineHeight=16,
        )
    # print the number of characters to render
    print(len(myText))
    
    # while there is content in myFormattedText, make a new page and draw the content
    while myFormattedText:
        # make the page and calculate the text box
        newPage('Letter')
        myBoxWidth = width()-myMargin*2
        myBoxHeight = height()-myMargin*2
        #rect(myMargin, myMargin, myBoxWidth, myBoxHeight)
        # draw the text in a text box 
        # and reassign myFormattedText to be the overflow from the text box
        # this way we whittle the variable down until it is empty
        myFormattedText = textBox(myFormattedText, (myMargin, myMargin, myBoxWidth, myBoxHeight))

    
    