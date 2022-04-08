import os
import random as randomLib

# set an absolute path
# every mac has this wordlist
myPath = '/usr/share/dict/words'

# confirm the path exists
print(os.path.exists(myPath))

# open the file in read mode using the UTF-8 unicode encoding
# call the file object myFile
with open(myPath, 'r', encoding="utf-8") as myFile:
    # read the file as a list of lines
    myWords = myFile.readlines()
    # print how many lines there are
    print(len(myWords))
    # now do the following twenty times
    for myItem in range(20):
        # choose a random word from the wordList
        myWord = randomLib.choice(myWords)
        # get a random position on the canvas
        myX = randint(0, width())
        myY = randint(0, height())
        # set a random fill color
        fill(random(), random(), random())
        # set the formatting
        font('Verdana', 100)
        # draw the text centered at the coordinates
        text(myWord, (myX, myY), align="center")