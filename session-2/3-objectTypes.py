# some basic object types

# TUPLE
# an unmutable sequence of objects
# https://docs.python.org/3/library/stdtypes.html#tuple
myTuple = (500, 100)
print(myTuple)
print(type(myTuple)) # print the object type
print(myTuple[1]) # slice it to get the second item
print()
# STRING
# a sequence of characters
# https://docs.python.org/3/library/stdtypes.html#string-methods
myString = 'hello world'
print(myString)
print(type(myString)) # print the object type
print(myString[1])  # slice it to get the second item
print(myString.upper()) # use a string method
print()

# LIST
# a mutable sequence of objects
# https://docs.python.org/3/library/stdtypes.html#list
myList = ['apples', 'oranges', 'bananas']
myList.append('grapefruit') # add something to the end of the list
myList.reverse() # reverse the list order
print(myList)
print(type(myList))
print(myList[1])
