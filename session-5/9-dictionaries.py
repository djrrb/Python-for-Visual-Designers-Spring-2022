# define a dictionary
myDict = {
    'key1': 'value1',
    'key2': 'value2'
    }

# could also define it like this
myDict = dict(
    key1 = 'value1',
    key2 = 'value2'
    )

# get the value for key1
print(myDict['key1'])
# get the value for key2
print(myDict['key2'])
# list all the keys
print(myDict.keys())
# list all the values
print(myDict.values())

# look for presence in a dict
if 'key1' in myDict:
    print('yes!')
else:
    print('no!')