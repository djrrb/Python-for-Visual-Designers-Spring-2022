import csv

myCSVPath = 'Business Cards - Sheet1.csv'
with open(myCSVPath) as myCSVFile:
    myReader = csv.reader(myCSVFile)
    for myRowIndex, myRow in enumerate(myReader):
        if myRowIndex == 0:
            continue
        myName, myAddress, myPhone, myEmail = myRow
        print(myName)

    