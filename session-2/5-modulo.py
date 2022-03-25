for myItem in range(50):
    # if we divide this number by 2, is there a remainder?
    if myItem % 2:
        myOddEvenResult = 'odd'
    else:
        myOddEvenResult = 'even'
    
    print(
    myItem, 
    'is an', 
    myOddEvenResult.upper(), 
    'number because its modulo/remainder is', 
    myItem % 2
    )