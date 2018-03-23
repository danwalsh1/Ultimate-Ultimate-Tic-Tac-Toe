#>> Ultimate Tic-Tac-Toe
#>> Daniel Walsh
#>> Code not to be used without written permission from Daniel Walsh.
#>> Credit must be given to Daniel Walsh if code is used once permission is given.

def getNextL2(clickedAddr):
    # Should return [L2, L3]
    nextL2 = [clickedAddr[0], clickedAddr[1]]
    
    return nextL2

def getL2AddrNums(L2addr):
    # Should return array of nine integers
    L2RC = getL2RandC(L2addr)
    sn = (L2RC[0] * 81) + (L2RC[1] * 3)
    addrNums = [sn, sn + 1, sn + 2, sn + 27, sn + 28, sn + 29, sn + 54, sn + 55, sn  + 56]

    return addrNums

def getL2RandC(L2addr):
    rc = [0, 0]
    # Get column
    if(L2addr[1] in [0, 3, 6]):
        if(L2addr[0] in [0, 3, 6]):
            rc[1] = 0
        elif(L2addr[0] in [1, 4, 7]):
            rc[1] = 1
        else:
            rc[1] = 2
    elif(L2addr[1] in [1, 4, 7]):
        if(L2addr[0] in [0, 3, 6]):
            rc[1] = 3
        elif(L2addr[0] in [1, 4, 7]):
            rc[1] = 4
        else:
            rc[1] = 5
    else:
        if(L2addr[0] in [0, 3, 6]):
            rc[1] = 6
        elif(L2addr[0] in [1, 4, 7]):
            rc[1] = 7
        else:
            rc[1] = 8
            
    # Get row
    if(L2addr[1] in [0, 1, 2]):
        if(L2addr[0] in [0, 1, 2]):
            rc[0] = 0
        elif(L2addr[0] in [3, 4, 5]):
            rc[0] = 1
        else:
            rc[0] = 2
    elif(L2addr[1] in [3, 4, 5]):
        if(L2addr[0] in [0, 1, 2]):
            rc[0] = 3
        elif(L2addr[0] in [3, 4, 5]):
            rc[0] = 4
        else:
            rc[0] = 5
    else:
        if(L2addr[0] in [0, 1, 2]):
            rc[0] = 6
        elif(L2addr[0] in [3, 4, 5]):
            rc[0] = 7
        else:
            rc[0] = 8
    return rc
