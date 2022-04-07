import os
myFolder = '/Users/david/Desktop/testFolder/'

for myItem in range(100):
    myNewFolder = os.path.join(myFolder, 'something'+str(myItem))
    print(myNewFolder)
    os.mkdir(myNewFolder)
    