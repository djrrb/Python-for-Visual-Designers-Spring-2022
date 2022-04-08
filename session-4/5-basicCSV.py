# import the csv library
import csv

# set the CSV filename as a variable
# this is a relative path so it will look in the current folder
myCSVPath = 'Business Cards - Sheet1.csv'

# open the file and assign the file object to the myCSVFile variable
with open(myCSVPath) as myCSVFile:
    # use the csv reader function to get a CSV reader object
    myReader = csv.reader(myCSVFile)
    # loop through each row in the reader
    # use enumerate() to get an extra variable
    # telling us which item we are on
    for myRowIndex, myRow in enumerate(myReader):
        # skip the first row since it is the headers
        if myRowIndex == 0:
            # continue will move to the next item in the loop
            continue
        # unpack the columns row into separate variables 
        myName, myAddress, myPhone, myEmail = myRow
        # print the name
        print(myName)

# our last dedent closes the CSV file    