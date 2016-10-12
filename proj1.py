# Project 1 - Michael C. Butts

import sys

# ========== Functions ==========

# prints the board

def print_board(board):
    print ()
    for i in range(0, len(board), 1):
        for j in range(0, len(board[i]), 1):
            print (board[i][j],end = "")
        print ()
    print("",end="\n")

# fills in the piece in the appropriate place

def fill_in(move,color,board):
    i = 5
    while(i > -1):
        if(board[i][move - 1] == '*'):
            board[i][move - 1] = color
            return
        i -= 1

# for checking if moves are correct

def check_move(turns,board):
    if(turns % 2 == 1): # blue goes
        temp_move = int(input("Blue player, what is your move?\n"))
        if(bad_move(temp_move,board)):
            temp_move = do_it_again(temp_move,board)
    else: # red goes
        temp_move = int(input("Red player, what is your move?\n"))
        if(bad_move(temp_move,board)):
            temp_move = do_it_again(temp_move,board)
    return temp_move

def bad_move(move,board):
    return ((move >= 8 or move <= 0) or board[0][move - 1] != '*')

def do_it_again(move,board):
    while(bad_move(move,board)):
        move = int(input("Bad move. Try again: "))
    return move

# decides what to do with a player's piece

def evaluate_move(move, board, turns):
    if(turns % 2 == 0):
        # do red eval
        fill_in(move,'R',board)
        if(check_winner('R',board)):
            return False
    else:
        # do blue eval
        fill_in(move,'B',board)
        if(check_winner('B',board)):
            return False
    return True

# check for seeing if there's 4 in row, column, or diagonal

def check_winner(color,board):
    return frwd_check(color,board) or hori_check(color,board) or veri_check(color,board) or back_check(color,board)

def hori_check(color,board):
    victor = 0
    for i in range(0, len(board), 1):
        victor = 0
        for j in range(0, len(board[i]), 1):
            if(board[i][j] == color):
                victor += 1
                if(victor == 4):
                    return True
            else:
                victor = 0
    return False

def veri_check(color,board):
    victor = 0
    for i in range(0, 6, 1):
        victor = 0
        for j in range(5, 0, -1):
            if(board[j][i] == color):
                victor += 1
                if(victor == 4):
                    return True
            else:
                victor = 0
    return False

# backwards diagonal

def back_check(color,board):

    victor = 0

    for i in range (5, 1, -1):
        if(board[i][i - 2] == color):
            victor += 1
            if(victor == 4):
                return True
        else:
            victor = 0

    for i in range (5, 0, -1):
        if(board[i][i - 1] == color):
            victor += 1
            if(victor == 4):
                return True
        else:
            victor = 0

    for i in range (5,-1,-1):
        if(board[i][i] == color):
            victor += 1
            if(victor == 4):
                return True
        else:
            victor = 0

    for i in range (5,-1,-1):
        if(board[i][i + 1] == color):
            victor += 1
            if(victor == 4):
                return True
        else:
            victor = 0

    for i in range (4,-1,-1):
        if(board[i][i + 2] == color):
            victor += 1
            if(victor == 4):
                return True
        else:
            victor = 0

    for i in range (3,-1,-1):
        if(board[i][i + 3] == color):
            victor += 1
            if(victor == 4):
                return True
        else:
            victor = 0

    return victor == 4

# forward diagonal

def frwd_check(color,board):

    victor = 0
# http://stackoverflow.com/questions/18648626/python-for-loop-with-two-variables
    for i, j in zip(range (3, -1, -1), range(0, 4, 1)):
        if(board[i][j] == color):
            victor += 1
            if(victor == 4):
                return True
        else:
            victor = 0

    for i, j in zip(range(4, -1, -1), range(0, 5, 1)):
            if(board[i][j] == color):
                #print ("just work")
                victor += 1
                if(victor == 4):
                    return True
            else:
                victor = 0

    for i, j in zip(range(5, -1, -1), range(0, 6, 1)):
            if(board[i][j] == color):
                #print ("just work")
                victor += 1
                if(victor == 4):
                    return True
            else:
                victor = 0

    for i, j in zip(range(5, -1, -1), range(1, 7, 1)):
            if(board[i][j] == color):
                #print ("just work")
                victor += 1
                if(victor == 4):
                    return True
            else:
                victor = 0

    for i, j in zip(range(5, 0, -1), range(2, 7, 1)):
            if(board[i][j] == color):
                #print ("just work")
                victor += 1
                if(victor == 4):
                    return True
            else:
                victor = 0

    for i, j in zip(range (5, 1, -1),range(3, 7, 1)):
            if(board[i][j] == color):
                #print ("just work")
                victor += 1
                if(victor == 4):
                    return True
            else:
                victor = 0

    return victor == 4


# ========= Main ===========

board = []

for i in range(7):  # make the board
    board.append([])
    for j in range(7):
        board[i].append('*')

board[6] = ['1','2','3','4','5','6','7']

print_board(board)
turns = 0
move = check_move(turns,board) # red goes first

while(evaluate_move(move,board,turns)):

    print_board(board)
    turns += 1

    if(turns % 2 == 1): # blue goes
        move = check_move(turns,board)
    else: # red goes
        move = check_move(turns,board)

print_board(board)

if(turns % 2 == 0):
    print("Red wins!", end = "\n")
else:
    print("Blue wins!", end = "\n")
