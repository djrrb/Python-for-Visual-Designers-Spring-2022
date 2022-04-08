# demoing the enumerate function

# it will turn a sequence into list of tuples pairing the item with what number we are on in the sequence

myString = 'hello'
print(list(enumerate(myString)))

# a demo of how to use enumrate in a loop
# to keep track of what number we are on
for myIndex, myChar in enumerate(myString):
    print(myChar, 'is the', myIndex, 'th character')