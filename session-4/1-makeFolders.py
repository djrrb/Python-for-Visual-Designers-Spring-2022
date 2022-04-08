# import the OS module
# https://docs.python.org/3/library/os.html
import os

# drag in an absolute path
# this won’t work for you
myFolder = '/Users/david/Desktop/testFolder/'

# do a simple loop
for myItem in range(100):
    # make a new path by joining together myFolder with something else
    myNewFolder = os.path.join(myFolder, 'something'+str(myItem))
    # print our new path
    print(myNewFolder)
    # make our new folder exist on the computer
    os.mkdir(myNewFolder)
    