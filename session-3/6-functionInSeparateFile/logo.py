# this file stores 

# because this file is not being run directly in drawbot, we need to import drawbot in order to let it use drawbot functions
from drawBot import *

# define the myLogo function
def myLogo():
    print('hello world')
    fill(1, 0, 0)
    stroke(0, 1, 0)
    strokeWidth(10)
    rect(0, 0, 100, 100)