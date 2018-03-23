#>> Ultimate Tic-Tac-Toe
#>> Daniel Walsh
#>> Code not to be used without written permission from Daniel Walsh.
#>> Credit must be given to Daniel Walsh if code is used once permission is given.

###############
### IMPORTS ###
###############

import tkinter as tk
import tkinter.font
import tkinter.messagebox
from functools import partial
from uTTTGetButtonPos import getBtnAddress
from uTTTGetL2 import getNextL2, getL2AddrNums

###############
### GLOBALS ###
###############

# 0 1 2 #
# 3 4 5 #
# 6 7 8 #

labelsTL = [["0" for i in range(0, 9)] for i in range(0, 9)] # lbl[Lv2][Lv1]
labelsTM = [["0" for i in range(0, 9)] for i in range(0, 9)] # lbl[Lv2][Lv1]
labelsTR = [["0" for i in range(0, 9)] for i in range(0, 9)] # lbl[Lv2][Lv1]
labelsML = [["0" for i in range(0, 9)] for i in range(0, 9)] # lbl[Lv2][Lv1]
labelsMM = [["0" for i in range(0, 9)] for i in range(0, 9)] # lbl[Lv2][Lv1]
labelsMR = [["0" for i in range(0, 9)] for i in range(0, 9)] # lbl[Lv2][Lv1]
labelsBL = [["0" for i in range(0, 9)] for i in range(0, 9)] # lbl[Lv2][Lv1]
labelsBM = [["0" for i in range(0, 9)] for i in range(0, 9)] # lbl[Lv2][Lv1]
labelsBR = [["0" for i in range(0, 9)] for i in range(0, 9)] # lbl[Lv2][Lv1]
labelsL3 = ["0", "0", "0", "0", "0", "0", "0", "0", "0"]

gameState = "PLAYING"
turn = 0 # Player 1 = X | Player 2 = O
nextL2Square = [-1, -1] #L2, L3

btnHeight = 1
btnWidth = 2
initialText = ""
systemColour = "light grey"
playerOneColour = "light blue"
playerTwoColour = "light green"
drawColour = "red"

buttons = []
labels = []

root = tk.Tk()
lblInfo = tk.Label(root, text = "Player 1's Turn", bg = systemColour)

debug = False

#################
### FUNCTIONS ###
#################

def printLabels():
    # Globals
    global labelsTL
    global labelsTM
    global labelsTR
    global labelsML
    global labelsMM
    global labelsMR
    global labelsBL
    global labelsBM
    global labelsBR
    global labelsL3

    if(debug == True):
        print(labelsTL)
        print(labelsTM)
        print(labelsTR)
        print(labelsML)
        print(labelsMM)
        print(labelsMR)
        print(labelsBL)
        print(labelsBM)
        print(labelsBR)
        print(labelsL3)

def updateBoard(btnNum, addr): # btnNum = integer | addr[Lv1, Lv2, Lv3]
    # Globals
    global labelsTL
    global labelsTM
    global labelsTR
    global labelsML
    global labelsMM
    global labelsMR
    global labelsBL
    global labelsBM
    global labelsBR
    global buttons

    if(addr[2] == 0):
        if(labelsTL[addr[1]][addr[0]] == "0"):
            buttons[btnNum].config(text = "")
        else:
            buttons[btnNum].config(text = labelsTL[addr[1]][addr[0]])
    elif(addr[2] == 1):
        if(labelsTM[addr[1]][addr[0]] == "0"):
            buttons[btnNum].config(text = "")
        else:
            buttons[btnNum].config(text = labelsTM[addr[1]][addr[0]])
    elif(addr[2] == 2):
        if(labelsTR[addr[1]][addr[0]] == "0"):
            buttons[btnNum].config(text = "")
        else:
            buttons[btnNum].config(text = labelsTR[addr[1]][addr[0]])
    elif(addr[2] == 3):
        if(labelsML[addr[1]][addr[0]] == "0"):
            buttons[btnNum].config(text = "")
        else:
            buttons[btnNum].config(text = labelsML[addr[1]][addr[0]])
    elif(addr[2] == 4):
        if(labelsMM[addr[1]][addr[0]] == "0"):
            buttons[btnNum].config(text = "")
        else:
            buttons[btnNum].config(text = labelsMM[addr[1]][addr[0]])
    elif(addr[2] == 5):
        if(labelsMR[addr[1]][addr[0]] == "0"):
            buttons[btnNum].config(text = "")
        else:
            buttons[btnNum].config(text = labelsMR[addr[1]][addr[0]])
    elif(addr[2] == 6):
        if(labelsBL[addr[1]][addr[0]] == "0"):
            buttons[btnNum].config(text = "")
        else:
            buttons[btnNum].config(text = labelsBL[addr[1]][addr[0]])
    elif(addr[2] == 7):
        if(labelsBM[addr[1]][addr[0]] == "0"):
            buttons[btnNum].config(text = "")
        else:
            buttons[btnNum].config(text = labelsBM[addr[1]][addr[0]])
    elif(addr[2] == 8):
        if(labelsBR[addr[1]][addr[0]] == "0"):
            buttons[btnNum].config(text = "")
        else:
            buttons[btnNum].config(text = labelsBR[addr[1]][addr[0]])

    if(debug == True):
        print("Board Updated")

def makeMove(addr):
    # Globals
    global labelsTL
    global labelsTM
    global labelsTR
    global labelsML
    global labelsMM
    global labelsMR
    global labelsBL
    global labelsBM
    global labelsBR
    global turn

    if((turn % 2) == 0):
        turnMarker = "X"
    else:
        turnMarker = "O"

    if(addr[2] == 0):
        labelsTL[addr[1]][addr[0]] = turnMarker
    elif(addr[2] == 1):
        labelsTM[addr[1]][addr[0]] = turnMarker
    elif(addr[2] == 2):
        labelsTR[addr[1]][addr[0]] = turnMarker
    elif(addr[2] == 3):
        labelsML[addr[1]][addr[0]] = turnMarker
    elif(addr[2] == 4):
        labelsMM[addr[1]][addr[0]] = turnMarker
    elif(addr[2] == 5):
        labelsMR[addr[1]][addr[0]] = turnMarker
    elif(addr[2] == 6):
        labelsBL[addr[1]][addr[0]] = turnMarker
    elif(addr[2] == 7):
        labelsBM[addr[1]][addr[0]] = turnMarker
    elif(addr[2] == 8):
        labelsBR[addr[1]][addr[0]] = turnMarker

    if(debug == True):
        print("Move recorded")
    

def getL1Val(addr):
    # Globals
    global labelsTL
    global labelsTM
    global labelsTR
    global labelsML
    global labelsMM
    global labelsMR
    global labelsBL
    global labelsBM
    global labelsBR
    
    if(addr[2] == 0):
        return labelsTL[addr[1]][addr[0]]
    elif(addr[2] == 1):
        return labelsTM[addr[1]][addr[0]]
    elif(addr[2] == 2):
        return labelsTR[addr[1]][addr[0]]
    elif(addr[2] == 3):
        return labelsML[addr[1]][addr[0]]
    elif(addr[2] == 4):
        return labelsMM[addr[1]][addr[0]]
    elif(addr[2] == 5):
        return labelsMR[addr[1]][addr[0]]
    elif(addr[2] == 6):
        return labelsBL[addr[1]][addr[0]]
    elif(addr[2] == 7):
        return labelsBM[addr[1]][addr[0]]
    elif(addr[2] == 8):
        return labelsBR[addr[1]][addr[0]]

### CHECK WIN ###

def checkWin(level, addr): # [Lv1, Lv2, Lv3]
    if(level == "L1"):
        return checkWinL1(addr)
    elif(level == "L2"):
        return checkWinL2(addr)
    elif(level == "L3"):
        return checkWinL3()
    else:
        raise ValueError('level not valid!')

def checkWinL1(addr): # [Lv1, Lv2, Lv3]
    # Globals
    global labelsTL
    global labelsTM
    global labelsTR
    global labelsML
    global labelsMM
    global labelsMR
    global labelsBL
    global labelsBM
    global labelsBR
    
    if(addr[2] == 0):
        return checkWinArray(labelsTL[addr[1]])
    elif(addr[2] == 1):
        return checkWinArray(labelsTM[addr[1]])
    elif(addr[2] == 2):
        return checkWinArray(labelsTR[addr[1]])
    elif(addr[2] == 3):
        return checkWinArray(labelsML[addr[1]])
    elif(addr[2] == 4):
        return checkWinArray(labelsMM[addr[1]])
    elif(addr[2] == 5):
        return checkWinArray(labelsMR[addr[1]])
    elif(addr[2] == 6):
        return checkWinArray(labelsBL[addr[1]])
    elif(addr[2] == 7):
        return checkWinArray(labelsBM[addr[1]])
    elif(addr[2] == 8):
        return checkWinArray(labelsBR[addr[1]])

def checkWinL2(addr): # [Lv1, Lv2, Lv3] 0,0,0
    # Globals
    global labelsTL
    global labelsTM
    global labelsTR
    global labelsML
    global labelsMM
    global labelsMR
    global labelsBL
    global labelsBM
    global labelsBR

    result = []
    count = 0

    if(addr[2] == 0):
        testArr = labelsTL
    elif(addr[2] == 1):
        testArr = labelsTM
    elif(addr[2] == 2):
        testArr = labelsTR
    elif(addr[2] == 3):
        testArr = labelsML
    elif(addr[2] == 4):
        testArr = labelsMM
    elif(addr[2] == 5):
        testArr = labelsMR
    elif(addr[2] == 6):
        testArr = labelsBL
    elif(addr[2] == 7):
        testArr = labelsBM
    elif(addr[2] == 8):
        testArr = labelsBR
    
    while(count < 9):
        result.append(checkWinArray(testArr[count]))
        count += 1

    return checkWinArray(result)
        

def checkWinL3():
    global labelsL3
    return checkWinArray(labelsL3)

def checkWinArray(arrBoard):
    # Check Vertical
    if(arrBoard[0] == arrBoard[3] and arrBoard[0] == arrBoard[6] and arrBoard[3] == arrBoard[6] and arrBoard[0] != "0"):
        return arrBoard[0]
    elif(arrBoard[1] == arrBoard[4] and arrBoard[1] == arrBoard[7] and arrBoard[4] == arrBoard[7] and arrBoard[1] != "0"):
        return arrBoard[1]
    elif(arrBoard[2] == arrBoard[5] and arrBoard[2] == arrBoard[8] and arrBoard[5] == arrBoard[8] and arrBoard[2] != "0"):
        return arrBoard[2]
    
    # Check Horizontal
    if(arrBoard[0] == arrBoard[1] and arrBoard[0] == arrBoard[2] and arrBoard[1] == arrBoard[2] and arrBoard[0] != "0"):
        return arrBoard[0]
    elif(arrBoard[3] == arrBoard[4] and arrBoard[3] == arrBoard[5] and arrBoard[4] == arrBoard[5] and arrBoard[3] != "0"):
        return arrBoard[3]
    elif(arrBoard[6] == arrBoard[7] and arrBoard[6] == arrBoard[8] and arrBoard[7] == arrBoard[8] and arrBoard[6] != "0"):
        return arrBoard[6]
    
    # Check Diagonal
    if(arrBoard[0] == arrBoard[4] and arrBoard[0] == arrBoard[8] and arrBoard[4] == arrBoard[8] and arrBoard[0] != "0"):
        return arrBoard[0]
    elif(arrBoard[2] == arrBoard[4] and arrBoard[2] == arrBoard[6] and arrBoard[4] == arrBoard[6] and arrBoard[2] != "0"):
        return arrBoard[2]
    
    # Check Draw
    draw = True
    for val in arrBoard:
        if(val == "0"):
            draw = False

    if(draw == True):
        return "DRAW"
    else:
        return "0"

#################

def highlightL2(addr, colour = "gold"): # addr[Lv2, Lv3]
    L3addr = getL2AddrNums(addr)
    for num in L3addr:
        buttons[num].config(bg = colour)

    if(debug == True):
        print("Highlighting Lv2: " + colour)

def dehighlightL2(addr): # addr[Lv2, Lv3]
    L3addr = getL2AddrNums(addr)
    for num in L3addr:
        buttons[num].config(bg = "SystemButtonFace")

    if(debug == True):
        print("Dehighlighting")

def highlightL3(addr, colour = "gold"): # addr = int
    if(colour != "gold"):
        for num in range(0, 9):
            highlightL2([num, addr], colour)
    else:
        for num in range(0, 9):
            if(checkWin("L1", [0, num, addr]) == "0"):
                highlightL2([num, addr], colour)

    if(debug == True):
        print("Highlighting Lv3: " + colour)

def dehighlightL3(addr): # addr = int
    for num in range(0, 9):
        if(checkWin("L1", [0, num, addr]) == "0"):
            dehighlightL2([num, addr])

    if(debug == True):
        print("Dehighlighting")

def guiLabelCalc(num):

    if(num >= 3 and num <= 5):
        num += 1
    elif(num >=6 and num <= 8):
        num += 2
    elif(num >=9 and num <= 11):
        num += 4
    elif(num >=12 and num <= 14):
        num += 5
    elif(num >=15 and num <= 17):
        num += 6
    elif(num >=18 and num <= 20):
        num += 8
    elif(num >=21 and num <= 23):
        num += 9
    elif(num >=24 and num <= 26):
        num += 10

    return num

def guiGetRow(num):
    count = 0
    while(num > 26):
        count += 1
        num -= 27

    count = guiLabelCalc(count)
        
    return count

def guiGetColumn(num):
    while(num > 26):
        num -= 27;

    num = guiLabelCalc(num)
    
    return num

def btnPress(num):
    # Globals
    global nextL2Square #L2, L3
    global turn
    global playerOneColour
    global playerTwoColour
    global drawColour
    global gameState
    
    btnAddr = getBtnAddress(num) # [Lv1, Lv2, Lv3]
    print("Button Address: " + str(btnAddr))

    if(gameState == "PLAYING"): # Is game playing?
        valid1 = False
        if(checkWin("L1", btnAddr) != "0" or checkWin("L2", btnAddr) != "0"):
            tk.messagebox.showwarning("Invalid Move", "Invalid Square [C]")
            return None
            
        if(nextL2Square[1] != -1): # Any Lv3 square?
            if(nextL2Square[0] != -1): # Any Lv2 square inside the given L3 square
                if(btnAddr[1] == nextL2Square[0] and btnAddr[2] == nextL2Square[1]): # Is the pressed btn in the next Lv2 square?
                    valid1 = True
                else:
                    tk.messagebox.showwarning("Invalid Move", "Invalid Square [L2]")
            else:
                if(btnAddr[2] == nextL2Square[1]): # Is the pressed btn in the correct next Lv3 Square but any Lv2 square?
                    valid1 = True
                else:
                    tk.messagebox.showwarning("Invalid Move", "Invalid Square [L3]")
        else:
            valid1 = True

        if(valid1 == True): # Go on to check if space is already taken
            valid2 = False
            if(getL1Val(btnAddr) == "0"): # Is the space empty?
                valid2 = True
            else:
                tk.messagebox.showwarning("Invalid Move", "Invalid Square [O]")

            if(valid2 == True):
                #>>>>> MOVE IS VALID <<<<<
                makeMove(btnAddr) # Make move

                #>>>>> DEHIGHLIGHT <<<<<
                if(nextL2Square[0] != -1): # Is Lv2 dehighlight needed?
                    dehighlightL2([btnAddr[1], btnAddr[2]]) # Dehighlight Lv2 square
                else:
                    if(nextL2Square[1] != -1): # Is Lv3 dehighlight needed?
                        dehighlightL3(btnAddr[2]) # Dehighlight Lv3 square

                #>>>>> NEXT LV2 SQUARE <<<<<
                nextL2 = getNextL2(btnAddr) # [L2, L3]
                checkAddr = [0, nextL2[0], nextL2[1]] # [L1, L2, L3]
                lvOneCheck = checkWin("L1", checkAddr)
                lvThreeCheck = checkWin("L2", checkAddr)
                if(lvOneCheck != "0"): # Is Lv2 square available?
                    if(lvThreeCheck != "0"): # Is Lv3 square available?
                        nextL2Square = [-1, -1]
                    else:
                        nextL2Square = [-1, nextL2[1]]
                else:
                    if(lvThreeCheck != "0"): # Is Lv3 square available?
                        nextL2Square = [-1, -1]
                    else:
                        nextL2Square = nextL2
                if(debug == True):
                    print("CL1: " + lvOneCheck)
                    print("CL2: " + lvThreeCheck)
                    print("NLV2 ADDR: " + str(nextL2))
                    print("NLV2: " + str(nextL2Square))

                #>>>>> CHECK WINS <<<<<
                lvOne = checkWin("L1", btnAddr)
                if(lvOne != "0"):
                    # Win / draw found on Lv1 board
                    if(lvOne == "DRAW"):
                        highlightL2([btnAddr[1], btnAddr[2]], drawColour)
                    else:
                        if(lvOne == "X"):
                            highlightL2([btnAddr[1], btnAddr[2]], playerOneColour)
                        else:
                            highlightL2([btnAddr[1], btnAddr[2]], playerTwoColour)

                lvTwo = checkWin("L2", btnAddr)
                if(lvTwo != "0"):
                    # Win / draw found on Lv2 board
                    if(lvTwo == "DRAW"):
                        highlightL3(btnAddr[2], drawColour)
                    else:
                        if(lvTwo == "X"):
                            highlightL3(btnAddr[2], playerOneColour)
                        else:
                            highlightL3(btnAddr[2], playerTwoColour)
                lvThree = checkWin("L3", btnAddr)
                if(lvThree != "0"):
                    # GAME OVER
                    if(lvThree == "DRAW"):
                        lblInfo.configure(text = "Game ended in a DRAW")
                    else:
                        if(lvThree == "X"):
                            lblInfo.configure(text = "Player 1 WINS")
                        else:
                            lblInfo.configure(text = "Player 2 WINS")
                    gameState = "GAME OVER"
                    return None

                #>>>>> HIGHLIGHT NEXT LV2 SQUARE <<<<<
                if(nextL2Square[0] != -1): # [Lv2, Lv3]
                    highlightL2(nextL2Square)
                else:
                    if(nextL2Square[1] != -1):
                        highlightL3(nextL2Square[1])

                #>>>>> NEXT TURN <<<<<
                turn += 1
                if((turn % 2) == 0):
                    lblInfo.configure(text = "Player 1's Turn")
                else:
                    lblInfo.configure(text = "Player 2's Turn")

                #>>>>> UPDATE BOARD <<<<<
                updateBoard(num, btnAddr)

###########
### GUI ###
###########

root.configure(background = systemColour)
root.resizable(0,0)

root.title("Ultimate Ultimate Tic-Tac-Toe")

for num in range(0, 729):
    button = tk.Button(root, text = initialText, height = btnHeight, width = btnWidth, command = lambda num = num: btnPress(num))
    buttons.append(button)

for num in range(0, 20):
    lbl = tk.Label(root, text = " ", font = ("Helvetica", 13), bg = systemColour)
    labels.append(lbl)

pos = [3, 7, 11, 12, 16, 20, 24, 25, 29, 33]
for num in range(0, 20):
    if(num < 10):
        labels[num].grid(row = 0, column = pos[num])
        if(num == 2 or num == 3 or num == 6 or num == 7):
            labels[num].configure(text = "   ")
    else:
        labels[num].grid(row = pos[num - 10], column = 0)
        if(num == 12 or num == 13 or num == 16 or num == 17):
            labels[num].configure(text = "   ")

for num in range(0, 729):
    buttons[num].grid(row = guiGetRow(num), column = guiGetColumn(num))

lblP1 = tk.Label(root, text="Player 1", bg = playerOneColour)
lblP1.grid(row = 37, column = 0, columnspan = 11)
lblInfo.grid(row = 37, column = 13, columnspan = 11)
lblP2 = tk.Label(root, text="Player 2", bg = playerTwoColour)
lblP2.grid(row = 37, column = 26, columnspan = 11)

root.mainloop()

############
### GAME ###
############

while(True):
    #>> Play the game

    #endGame = input("End game? [Y/N]: ")
    endGame = "y"
    if(endGame == "Y" or endGame == "y"):
        break
