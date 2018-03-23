#>> Ultimate Tic-Tac-Toe
#>> Daniel Walsh
#>> Code not to be used without written permission from Daniel Walsh.
#>> Credit must be given to Daniel Walsh if code is used once permission is given.

def getBtnAddress(num): #>> Btn array number
    row = getRow(num)
    column = getColumn(num)
    btnAddress = [0, 0, 0]
    btnAddress[0] = getBtnAddrL1(row, column)
    btnAddress[1] = getBtnAddrL2(row, column)
    btnAddress[2] = getBtnAddrL3(row, column)

    return btnAddress

def getBtnAddrL1(row, column):
    while(row > 2):
        row -= 3
    while(column > 2):
        column -= 3

    if(row == 0):
        if(column == 0):
            return 0
        elif(column == 1):
            return 1
        else:
            return 2
    elif(row == 1):
        if(column == 0):
            return 3
        elif(column == 1):
            return 4
        else:
            return 5
    else:
        if(column == 0):
            return 6
        elif(column == 1):
            return 7
        else:
            return 8

def getBtnAddrL2(row, column):
    while(row > 8):
        row -= 9
    while(column > 8):
        column -= 9

    if(row < 3):
        if(column < 3):
            return 0
        elif(column < 6):
            return 1
        else:
            return 2
    elif(row < 6):
        if(column < 3):
            return 3
        elif(column < 6):
            return 4
        else:
            return 5
    else:
        if(column < 3):
            return 6
        elif(column < 6):
            return 7
        else:
            return 8

def getBtnAddrL3(row, column):
    if(row < 9):
        if(column < 9):
            return 0
        elif(column < 18):
            return 1
        else:
            return 2
    elif(row < 18):
        if(column < 9):
            return 3
        elif(column < 18):
            return 4
        else:
            return 5
    else:
        if(column < 9):
            return 6
        elif(column < 18):
            return 7
        else:
            return 8
    

def getRow(num):
    count = 0
    while(num > 26):
        count += 1
        num -= 27

    return count


def getColumn(num):
    while(num > 26):
        num -= 27

    return num

    
