# use an if statement to compare two strings
myString1 = 'hello'
myString2 = 'world'
if myString1 != myString2:
    print('yay my strings are the same')
else:
    print('boo they are not the same')

######
# draw a different shape depending on the results of a string
myShape = 'circle'
if myShape == 'circle':
    print('draw a circle')
    oval(0, 0, 100, 100)
else:
    print('draw a square')
    rect(0, 0, 100, 100)
    