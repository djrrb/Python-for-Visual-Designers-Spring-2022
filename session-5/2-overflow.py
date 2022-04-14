myPath = 'frankenstein.txt'
myMargin = 50
with open(myPath, 'r', encoding='utf-8') as myFile:
    myText = myFile.read()
    #myText = myText[:10000]
    myFormattedText = FormattedString(
        myText,
        font='Georgia',
        fontSize=10.5,
        lineHeight=16,
        )
    
    
    print(len(myText))
    
    while myFormattedText:
        newPage('Letter')
        myBoxWidth = width()-myMargin*2
        myBoxHeight = height()-myMargin*2
        #rect(myMargin, myMargin, myBoxWidth, myBoxHeight)
        myFormattedText = textBox(myFormattedText, (myMargin, myMargin, myBoxWidth, myBoxHeight))

    
    