# define a function
def myLogo():
    # everything that happens in here
    # will run every time we call myLogo()
    print('hello world')
    fill(1, 0, 0)
    stroke(0, 1, 0)
    strokeWidth(10)
    rect(0, 0, 100, 100)
    
##########
##########
##########
##########
##########
##########

# now that we defined the function
# let’s use it a few times

myLogo()

newPage()
translate(100, 800)
myLogo()

newPage()
scale(5)
myLogo()