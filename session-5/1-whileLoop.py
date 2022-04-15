# a while loop is a mix of a "for" loop and an "if" statement
# for item in sequence:
# if thing is True:
# ... becomes ...
# while thing is True:
#     ...

# set a number
myNumber = 10

# make a condition that will run the loop while the number is greater than five
while myNumber > 5:
    # print the number
    print(myNumber)
    # take one off the number
    # it’s important to whittle this number down, otherwise the loop will run forever!
    myNumber -= 1
# the loop will stop once myNumber is less than 5
print('done')
    
