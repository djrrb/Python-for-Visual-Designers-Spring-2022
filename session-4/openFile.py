import os
import random as randomLib

myPath = '/usr/share/dict/words'

print(os.path.exists(myPath))

with open(myPath, 'r', encoding="utf-8") as myFile:
    myWords = myFile.readlines()
    print(len(myWords))
    for myItem in range(20):
        myWord = randomLib.choice(myWords)
        myX = randint(0, width())
        myY = randint(0, height())
        fill(random(), random(), random())
        font('Verdana', 100)
        text(myWord, (myX, myY))