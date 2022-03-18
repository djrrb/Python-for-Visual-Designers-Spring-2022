# some basic python

# words that begin with "my" are variables and could be named anything

# print a string
print('hello world')

# do some math
print(3*5)

# make a variable
myVar = 3
print(myVar*5)

# change a variable
myVar = 'hello'
print(myVar*5)

# get the type of variable
myVar = 'hello world'
print(myVar, type(myVar))

# get the length of a sequence
myVar = 'hello world'
print(len(myVar))

# get each item from a sequence
mySequence = 'hello world'
for myItem in mySequence:
    print(myItem)

# get each item from a range of numbers
mySequence = range(10)
for myItem in mySequence:
    print(myItem)