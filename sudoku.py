########### Sudoku boards ##############################

small = [[1, 0, 0, 0],
         [0, 4, 1, 0],
         [0, 0, 0, 3],
         [4, 0, 0, 0]]

small2 = [[0, 0, 1, 0],
          [4, 0, 0, 0],
          [0, 0, 0, 2],
          [0, 3, 0, 0]]

big = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [4, 0, 0, 7, 8, 9, 0, 0, 0],
       [7, 8, 0, 0, 0, 0, 0, 5, 6],
       [0, 2, 0, 3, 6, 0, 8, 0, 0],
       [0, 0, 5, 0, 0, 7, 0, 1, 0],
       [8, 0, 0, 2, 0, 0, 0, 0, 5],
       [0, 0, 1, 6, 4, 0, 9, 7, 0],
       [0, 0, 0, 9, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 3, 0, 0, 0, 2]]

big2 = [[7, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 5, 0, 0, 0, 9, 0, 0, 0],
        [8, 0, 0, 0, 3, 0, 0, 4, 0],
        [0, 0, 0, 7, 6, 0, 0, 0, 8],
        [6, 2, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 7, 0],
        [0, 0, 0, 6, 0, 0, 9, 8, 0],
        [0, 0, 0, 0, 2, 7, 3, 0, 0],
        [0, 0, 2, 0, 8, 0, 0, 5, 0]]

big3 = [[0, 0, 8, 1, 9, 0, 0, 0, 6],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 6, 0, 0, 1, 3, 0],
        [0, 0, 6, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 2, 0, 0, 5],
        [0, 0, 0, 0, 3, 0, 9, 0, 0],
        [0, 1, 0, 4, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 5, 7]]

big4 = [[0, 0, 0, 6, 0, 0, 2, 0, 0],
        [8, 0, 4, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [4, 0, 5, 0, 0, 0, 0, 0, 7],
        [7, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 5, 0, 0, 0, 8],
        [3, 0, 0, 0, 7, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 1, 9, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 6, 0]]

giant = [[ 0,  0, 13,  0,  0,  0,  0,  0,  2,  0,  8,  0,  0,  0, 12, 15],
         [ 7,  8, 12,  2, 10,  0,  0, 13,  0,  0, 14, 11,  6,  9,  0,  4],
         [11, 10,  0,  0,  0,  6, 12,  5,  0,  3,  0,  0,  0, 14,  0,  8],
         [ 1,  0,  0,  0, 14,  0,  2,  0,  0,  4,  6,  0, 16,  3,  0, 13],
         [12,  6,  0,  3,  0,  0, 16, 11,  0, 10,  1,  7, 13, 15,  0,  0],
         [ 0, 13,  0,  0,  0, 15,  8,  0, 14,  0,  0,  0,  0, 16,  5, 11],
         [ 8,  0, 11,  9, 13,  0,  7,  0,  0,  0,  0,  3,  2,  4,  0, 12],
         [ 5,  0,  0, 16, 12,  9,  0, 10, 11,  2, 13,  0,  0,  0,  8,  0],
         [ 0,  0,  0,  0, 16,  8,  9, 12,  0,  0,  0,  0,  0,  6,  3,  0],
         [ 2, 16,  0,  0,  0, 11,  0,  0,  7,  0, 12,  6,  0, 13, 15,  0],
         [ 0,  0,  4,  0,  0, 13,  0,  7,  3, 15,  0,  5,  0,  0,  0,  0],
         [ 0,  7,  0, 13,  4,  5, 10,  0,  1,  0, 11, 16,  9,  0, 14,  2],
         [ 0,  2,  8,  0,  9,  0,  0,  0,  4,  0,  7,  0,  0,  5,  0,  0],
         [14,  0,  0,  0, 15,  2, 11,  4,  9, 13,  3,  0, 12,  0,  0,  0],
         [ 0,  1,  9,  7,  0,  0,  5,  0,  0, 11, 15, 12,  0,  0,  0,  0],
         [16,  3, 15,  0,  0, 14, 13,  6, 10,  1,  0,  2,  0,  8,  4,  9]]

giant2 = [[ 0,  5,  0,  0,  0,  4,  0,  8,  0,  6,  0,  0,  0,  0,  9, 16],
          [ 1,  0,  0,  0,  0,  0,  0, 13,  4,  0,  0,  7, 15,  0,  8,  0],
          [13,  0,  0,  0,  0,  7,  3,  0,  0,  0,  0,  9,  5, 10,  0,  0],
          [ 0, 11, 12, 15, 10,  0,  0,  0,  0,  0,  5,  0,  3,  4,  0, 13],
          [15,  0,  1,  3,  0,  0,  7,  2,  0,  0,  0,  0,  0,  5,  0,  0],
          [ 0,  0,  0, 12,  0,  3,  0,  5,  0, 11,  0, 14,  0,  0,  0,  9],
          [ 4,  7,  0,  0,  0,  0,  0,  0, 12,  0, 15, 16,  0,  0,  0,  0],
          [ 0,  0,  0,  0, 14,  0, 15,  0,  6,  9,  0,  0,  0,  0, 12,  0],
          [ 3,  0, 15,  4,  0, 13, 14,  0,  0,  0,  0,  1,  0,  0,  7,  8],
          [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  9, 10,  0,  0,  0,  0],
          [11,  0, 16, 10,  0,  0,  0,  0,  0,  7,  0,  0,  0,  3,  5,  0],
          [ 0,  0, 13,  0,  0,  0,  0,  0, 14,  0, 16, 15,  0,  9,  0,  1],
          [ 9,  0,  2,  0,  0, 14,  0,  4,  8,  0,  0,  0,  0,  0,  0,  0],
          [ 0, 14,  0,  0,  0,  0,  0, 10,  9,  0,  3,  0,  0,  0,  1,  7],
          [ 8,  0,  0,  0, 16,  0,  0,  1,  2, 14, 11,  4,  0,  0,  0,  3],
          [ 0,  0,  0,  1,  0,  0,  5,  0,  0, 16,  0,  6,  0, 12,  0,  0]]

giant3 = [[ 0,  4,  0,  0,  0,  0,  0, 12,  0,  1,  0,  0,  9,  0,  8,  0],
          [15, 14,  0,  0,  9,  0,  0, 13,  8,  0,  0, 10,  1,  0,  0,  0],
          [ 0,  7,  0,  0,  0,  0,  0,  8, 16,  0, 14,  0,  0,  2,  0,  0],
          [ 0,  0,  0,  9,  0,  0, 11,  0,  0,  0,  0,  0,  5,  0,  0, 15],
          [ 3,  0, 12,  0,  7,  0, 10,  0,  0, 11,  2,  0,  0,  0,  0,  6],
          [14,  8,  0,  0,  0, 12,  0,  6,  0,  0,  0, 16,  0,  0,  0, 10],
          [ 0, 16,  0,  0, 13,  0,  0,  0,  0,  0,  0,  0,  0,  0, 12,  0],
          [ 6,  0,  0,  0,  0,  8,  0,  5,  1,  7, 13,  0, 11,  0,  0, 14],
          [ 0,  0,  0,  2,  0,  0, 16,  0, 15, 12,  0,  3, 10,  7,  0,  0],
          [ 0,  9,  0,  5, 11,  0,  3,  0,  4, 13, 16,  0,  0, 15,  6,  0],
          [ 0,  0,  0,  0,  5,  4,  0,  0,  9,  6,  0,  2,  0,  0,  0,  0],
          [ 1,  0,  0,  0,  0, 15, 12,  0,  0,  0,  5,  0,  0,  0,  9,  0],
          [12, 10,  0, 15,  0,  1,  0,  0,  2,  9,  3,  4,  0,  0,  5,  0],
          [ 0,  0,  0,  3, 10,  0,  4,  0,  0, 15,  0,  0,  0,  0,  0,  0],
          [ 0,  0,  0,  0, 16,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10, 11],
          [11,  6,  8,  0,  0,  0, 15,  0, 14,  0,  0,  0,  0, 13,  0,  2]]

sudokus = [[], [], [small, small2], [big, big2, big3, big4], [giant, giant2, giant3]]

#Module functions#

from math import sqrt

def print_board(board):
    """
    Prints a given board to the console in a way that aligns the content of columns and makes
    the subgrids visible.

    Input : a Sudoku board (board) of size 4x4, 9x9, or 16x16
    Effect: prints the board to the console 
    """
    L = len(board)**2
    topsmall = '------'
    topbig = '------------'
    topgiant = '-------------'
#Small board
    if L == 16:
        print(" " + topsmall*2 + "-")
        for i in range(4):#row
            for j in range(4):#column
                if ((i == 2 or i == 4) and j == 0):
                    print(" " + topsmall*2 + "-")
                if (j == 0 or j == 2 or j == 4):
                    print(" " + "|", end="")
                if board[i][j] > 0:
                    print(" " + str(board[i][j]), end="")#str to add space
                elif board[i][j] < 1:
                    print( " " + " ", end="")
                if (j == 3):
                      print(" " + "|")
        print(" " + topsmall*2 + "-")
        return
#Big board
    if L == 81:
        print(" " + topbig*2 + "-")
        for i in range(9):
            for j in range(9):
                if ((i == 3 or i == 6) and j == 0):
                    print(" " + topbig*2 + "-")
                if (j == 0 or j == 3 or j == 6):
                    print(" " + "|", end="")
                print(" " + str(board[i][j]), end="")
                if (j == 8):
                      print(" " + "|")
        print(" " + topbig*2 + "-")
        return
#Giant board
    if L == 256:
        print(" " + topgiant*3 + "--")
        for i in range(16):
            for j in range(16):
                if ((i == 4 or i == 8 or i == 12) and j == 0):
                    print(" " + topgiant*3 + "--")
                if (j == 0 or j == 4 or j == 8 or j == 12):
                    print(" " + "|", end="")
                if board[i][j] > 0 and board[i][j] < 10:
                    print(" " + str(board[i][j]), end="")
                elif board[i][j] < 1:
                    print(" " + " ", end="")
                elif board[i][j] == 10:
                    print(" " + "A", end="")
                elif board[i][j] == 11:
                    print(" " + "B", end="")
                elif board[i][j] == 12:
                    print(" " + "C", end="")
                elif board[i][j] == 13:
                    print(" " + "D", end="")
                elif board[i][j] == 14:
                    print(" " + "E", end="")
                elif board[i][j] == 15:
                    print(" " + "F", end="")
                elif board[i][j] == 16:
                    print(" " + "G", end="")
                if (j == 15):
                      print(" " + "|")
        print(" " + topgiant*3 + "--")
        return


def subgrid_values(board, r, c):
    """
    Input : Sudoku board (board), row index (r), and column index (c)
    Output: list of all numbers that are present in the subgrid of the board related to the
            field (r, c)
    """
    n = len(board)
    k = round(sqrt(n))
    res = []
    for i in range((r // k) * k, ((r // k) + 1) * k):
        for j in range((c // k) * k, ((c // k) + 1) * k):
            if board[i][j]:
                res.append(board[i][j])
    return res 
    pass


def options(board, i, j):
    """
    Input : Sudoku board (board), row index (r), and column index (c)
    Output: list of all numbers that player is allowed to place on field (r, c),
            i.e., those that are not already present in row r, column c,
            and subgrid related to field (r, c)
    """
    L = len(board)**2

    #Small----------------------------
    if L == 16:
        rsec = i//2
        csec = j//2
        lst = [1, 2, 3, 4]#a list of available options, if number is detected, number from list is removed. leaving only available options
        #row
        for r in range(4):
            if(board[r][j] == 1):
               lst.remove(1)
            if(board[r][j] == 2):
               lst.remove(2)
            if(board[r][j] == 3):
                lst.remove(3)
            if(board[r][j] == 4):
                lst.remove(4)
            if(board[r][j] == 0):
                continue
        #column
        for c in range(4):
            if(board[i][c] == 1):
                if 1 in lst:
                    lst.remove(1)
            if(board[i][c] == 2):
                if 2 in lst:
                    lst.remove(2)
            if(board[i][c] == 3):
                if 3 in lst:
                    lst.remove(3)
            if(board[i][c] == 4):
                if 4 in lst:
                    lst.remove(4)
            if(board[i][c] == 0):
                continue
        #subgrid
        for r in range(2):
            for c in range(2):
                if(board[rsec * 2 + r][csec * 2 + c] == 1):
                    if 1 in lst:
                        lst.remove(1)
                if(board[rsec * 2 + r][csec * 2 + c] == 2):
                    if 2 in lst:
                        lst.remove(2)
                if(board[rsec * 2 + r][csec * 2 + c] == 3):
                    if 3 in lst:
                        lst.remove(3)
                if(board[rsec * 2 + r][csec * 2 + c] == 4):
                    if 4 in lst:
                        lst.remove(4)
                if(board[rsec * 2 + r][csec * 2 + c] == 0):
                    continue
        return lst

    #Big--------------------------------------------
    if L == 81:
        rsec = i//3
        csec = j//3
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #row
        for r in range(9):
            if(board[r][j] == 1):
                lst.remove(1)
            if(board[r][j] == 2):
                lst.remove(2)
            if(board[r][j] == 3):
                lst.remove(3)
            if(board[r][j] == 4):
                lst.remove(4)
            if(board[r][j] == 5):
                lst.remove(5)
            if(board[r][j] == 6):
                lst.remove(6)
            if(board[r][j] == 7):
                lst.remove(7)
            if(board[r][j] == 8):
                lst.remove(8)
            if(board[r][j] == 9):
                lst.remove(9)
            if(board[r][j] == 0):
                continue
        #column
        for c in range(9):
            if(board[i][c] == 1):
                if 1 in lst:
                    lst.remove(1)
            if(board[i][c] == 2):
                if 2 in lst:
                    lst.remove(2)
            if(board[i][c] == 3):
                if 3 in lst:
                    lst.remove(3)
            if(board[i][c] == 4):
                if 4 in lst:
                    lst.remove(4)
            if(board[i][c] == 5):
                if 5 in lst:
                    lst.remove(5)
            if(board[i][c] == 6):
                if 6 in lst:
                    lst.remove(6)
            if(board[i][c] == 7):
                if 7 in lst:
                    lst.remove(7)
            if(board[i][c] == 8):
                if 8 in lst:
                    lst.remove(8)
            if(board[i][c] == 9):
                if 9 in lst:
                    lst.remove(9)
            if(board[i][c] == 0):
                continue
        #subgrid
        for r in range(3):
            for c in range(3):
                if(board[rsec * 3 + r][csec * 3 + c] == 1):
                    if 1 in lst:
                        lst.remove(1)
                if(board[rsec * 3 + r][csec * 3 + c] == 2):
                    if 2 in lst:
                        lst.remove(2)
                if(board[rsec * 3 + r][csec * 3 + c] == 3):
                    if 3 in lst:
                        lst.remove(3)
                if(board[rsec * 3 + r][csec * 3 + c] == 4):
                    if 4 in lst:
                        lst.remove(4)
                if(board[rsec * 3 + r][csec * 3 + c] == 5):
                    if 5 in lst:
                        lst.remove(5)
                if(board[rsec * 3 + r][csec * 3 + c] == 6):
                    if 6 in lst:
                        lst.remove(6)
                if(board[rsec * 3 + r][csec * 3 + c] == 7):
                    if 7 in lst:
                        lst.remove(7)
                if(board[rsec * 3 + r][csec * 3 + c] == 8):
                    if 8 in lst:
                        lst.remove(8)
                if(board[rsec * 3 + r][csec * 3 + c] == 9):
                    if 9 in lst:
                        lst.remove(9)
                if(board[rsec * 3 + r][csec * 3 + c] == 0):
                    continue
        return lst
    #Giant--------------------------------------------------
    if L == 256:
        rsec = i//4
        csec = j//4
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        #row
        for r in range(16):
            if(board[r][j] == 1):
                lst.remove(1)
            if(board[r][j] == 2):
                lst.remove(2)
            if(board[r][j] == 3):
                lst.remove(3)
            if(board[r][j] == 4):
                lst.remove(4)
            if(board[r][j] == 5):
                lst.remove(5)
            if(board[r][j] == 6):
                lst.remove(6)
            if(board[r][j] == 7):
                lst.remove(7)
            if(board[r][j] == 8):
                lst.remove(8)
            if(board[r][j] == 9):
                lst.remove(9)
            if(board[r][j] == 10):
                lst.remove(10)
            if(board[r][j] == 11):
                lst.remove(11)
            if(board[r][j] == 12):
                lst.remove(12)
            if(board[r][j] == 13):
                lst.remove(13)
            if(board[r][j] == 14):
                lst.remove(14)
            if(board[r][j] == 15):
                lst.remove(15)
            if(board[r][j] == 16):
                lst.remove(16)
            if(board[r][j] == 0):
                continue
        #column
        for c in range(16):
            if(board[i][c] == 1):
                if 1 in lst:
                    lst.remove(1)
            if(board[i][c] == 2):
                if 2 in lst:
                    lst.remove(2)
            if(board[i][c] == 3):
                if 3 in lst:
                    lst.remove(3)
            if(board[i][c] == 4):
                if 4 in lst:
                    lst.remove(4)
            if(board[i][c] == 5):
                if 5 in lst:
                    lst.remove(5)
            if(board[i][c] == 6):
                if 6 in lst:
                    lst.remove(6)
            if(board[i][c] == 7):
                if 7 in lst:
                    lst.remove(7)
            if(board[i][c] == 8):
                if 8 in lst:
                    lst.remove(8)
            if(board[i][c] == 9):
                if 9 in lst:
                    lst.remove(9)
            if(board[i][c] == 10):
                if 10 in lst:
                    lst.remove(10)
            if(board[i][c] == 11):
                if 11 in lst:
                    lst.remove(11)
            if(board[i][c] == 12):
                if 12 in lst:
                    lst.remove(12)
            if(board[i][c] == 13):
                if 13 in lst:
                    lst.remove(13)
            if(board[i][c] == 14):
                if 14 in lst:
                    lst.remove(14)
            if(board[i][c] == 15):
                if 15 in lst:
                    lst.remove(15)
            if(board[i][c] == 16):
                if 16 in lst:
                    lst.remove(16)
            if(board[i][c] == 0):
                continue
            
        for r in range(4):
            for c in range(4):
                if(board[rsec * 4 + r][csec * 4 + c] == 1):
                    if 1 in lst:
                        lst.remove(1)
                if(board[rsec * 4 + r][csec * 4 + c] == 2):
                    if 2 in lst:
                        lst.remove(2)
                if(board[rsec * 4 + r][csec * 4 + c] == 3):
                    if 3 in lst:
                        lst.remove(3)
                if(board[rsec * 4 + r][csec * 4 + c] == 4):
                    if 4 in lst:
                        lst.remove(4)
                if(board[rsec * 4 + r][csec * 4 + c] == 5):
                    if 5 in lst:
                        lst.remove(5)
                if(board[rsec * 4 + r][csec * 4 + c] == 6):
                    if 6 in lst:
                        lst.remove(6)
                if(board[rsec * 4 + r][csec * 4 + c] == 7):
                    if 7 in lst:
                        lst.remove(7)
                if(board[rsec * 4 + r][csec * 4 + c] == 8):
                    if 8 in lst:
                        lst.remove(8)
                if(board[rsec * 4 + r][csec * 4 + c] == 9):
                    if 9 in lst:
                        lst.remove(9)
                if(board[rsec * 4 + r][csec * 4 + c] == 10):
                    if 10 in lst:
                        lst.remove(10)
                if(board[rsec * 4 + r][csec * 4 + c] == 11):
                    if 11 in lst:
                        lst.remove(11)
                if(board[rsec * 4 + r][csec * 4 + c] == 12):
                    if 12 in lst:
                        lst.remove(12)
                if(board[rsec * 4 + r][csec * 4 + c] == 13):
                    if 13 in lst:
                        lst.remove(13)
                if(board[rsec * 4 + r][csec * 4 + c] == 14):
                    if 14 in lst:
                        lst.remove(14)
                if(board[rsec * 4 + r][csec * 4 + c] == 15):
                    if 15 in lst:
                        lst.remove(15)
                if(board[rsec * 4 + r][csec * 4 + c] == 16):
                    if 16 in lst:
                        lst.remove(16)
                if(board[rsec * 4 + r][csec * 4 + c] == 0):
                    continue
        return lst
    pass

def empty_fields(board):
    """
    Input : Sudoku board
    Output: list of fields, i.e., pairs of row and column indices, that are not
            empty (i.e., value is not equal to 0)
    """
    n = len(board)
    k = int(sqrt(n))
    res = []
    for i in range(n):
        for j in range(n):
            if not board[i][j]:
                res.append((i, j))
                
def play(board):
    """
    Input : Sudoku board
    Effect: Allows user to play board via console
    """
    import copy
    copy = copy.deepcopy(board)#made a copy of the board which is used to restart.
    print_board(board)
    while True:
        inp = input().split(' ')
        if len(inp) == 3 and inp[0].isdecimal() and inp[1].isdecimal() and inp[2].isdecimal():
            i = int(inp[0])
            j = int(inp[1])
            x = int(inp[2])
            if x in options(board, i, j):
                board[i][j] = x
            print_board(board)
        elif len(inp)==3 and (inp[0] == 'n' or inp[0] == 'new') and inp[1].isdecimal() and inp[2].isdecimal():
            k = int(inp[1])
            d = int(inp[2])
            if k < len(sudokus) and 0 < d <= len(sudokus[k]):
                board = sudokus[k][d-1]
                print_board(board)
            else:
                print('board not found')
        elif (inp[0] == 'g' and inp[1]) or (inp[0] == 'generate' and inp[1]):
            k = int(inp[1])
            if k >= 1:
                randomboard = [[0 for i in range(k**2)] for j in range(k**2)]
                generate_solution(randomboard)
                board = randomboard
                print_board(board)
        elif (inp[0] == 's') or (inp[0] == 'solve'):
            print_board(solve(board))
            
        elif inp[0] == 'q' or inp[0] == 'quit':
            return
        elif inp[0] == 'r' or inp[0] == 'restart':
            print_board(copy)
        elif (inp[0] == 'i') or (inp[0] == 'infer'):
            print_board(inferred(board))
        else:
            print('Invalid input')
    for num1 in range(len(board)):
            for num2 in range(len(board)):
                if(board[i][num2] != 0 and board[num1][j] != 0):
                    return('You win.')

import copy
import random

def valid(board, i, j, num):
    """
    Input: Board, row, column, and a number.
    Output: Returns a boolean to determine whether num is valid in the cell.
    """
    for x in range(len(board)):
        if board[i][x] == num:
            return False
    
    for x in range(len(board)):
        if board[x][j] == num:
            return False
 
    row = i - i // int(sqrt(len(board)))
    col = j - j // int(sqrt(len(board)))
    for x in range(int(sqrt(len(board)))):
        for y in range(int(sqrt(len(board)))):
            if board[x + row][y + col] == num:
                return False
    return True

def value_by_single(board, i, j):
    """
    Input : board, row, and column index
    Output: The correct value for field (i, j) in board if it can be inferred as
            either a forward or a backward single; or None otherwise. 
    """
    if len(options(board, i, j)) == 1:
        return options(board, i, j).pop() #if only one possible option, that is the true value of that square.

    grid = copy.deepcopy(board) #Filled in all spaces that are 100% known with options which are equal to 1 element.
    any_fill = True
    while any_fill: #essentially only proceeds if any_fill is equalt to true 
        any_fill = False
        for x in range(len(grid[0])):
            for y in range(len(grid[0])):
                candidates = options(grid, x, y)
                if len(candidates) == 1 and grid[x][y] == 0: #made by this if statement
                    grid[x][y] = candidates.pop()
                    options(board, x, y)
                    any_fill = True
    if grid[i][j] == 0:
        return None
    else:
        return grid[i][j]
    pass


def get_options(board):
    grid = copy.deepcopy(board)
    for i in range(len(board[0])):
            for j in range(len(board[0])):
                grid[i][j] = options(board, i, j)
    return grid
pass

def inferred(board):
    """
    Input : Sudoku board
    Output: new Soduko board with all values field from input board plus
            all values that can be inferred by repeated application of 
            forward and backward single rule
    """
    grid = copy.deepcopy(board)
    true = True
    candidates = get_options(grid)
    while true:
        true = False
        for i in range(len(board[0])):
            for j in range(len(board[0])):
                if len(candidates[i][j]) == 1 and grid[i][j] == 0 and valid(grid, i, j, candidates[i][j]):
                    grid[i][j] = candidates[i][j][0]
                    candidates = get_options(grid)
                    true = True
    return grid
    pass

#SOLVE BACKTRACKING#
def is_solution(board):
    """
    Input: A sudoku grid
    Effect: Determines if the grid has a solution.
    """
    for i in range(len(board)):
        lst = subgrid_values(board, i, 0)
        if range(0, len(lst)) != range(0, len(board[0])):
            return False
    return True


def valid_board(board):
    """
    Input: A sudoku grid
    Effect: Determines if the board is valid, i.e. does not break any rules.
    """
    candidates = get_options(board)
    for i in range(len(board)):
        for j in range(len(board)):
            if len(candidates[i][j]) == 0:
                return True
    return False


def g(board):
    """
    Was not finished.
    """
    grid = copy.deepcopy(board)
    candidates = get_options(grid)
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            for guess in candidates[i][j]:
                grid[i][j] = guess
                solution = solve(grid)
                if solution is not None:
                    return solution
                grid[i][j] = 0


def solve(board):
    '''
    Used 3 seperate functions as a means of backtracking.
    One to ask if the grid is solved.
    Two to ask if the board is valid.
    Three to make a guess for those unkown numbers.
    '''
    '''
    The inferred board reduces extra guessing.
    The inferred board implements 100% correct values.
    This limits the amount of guessing by the algorithm, reducing computational cost.
    '''
    grid = inferred(copy.deepcopy(board))
    if is_solution(grid):
        return grid
    if not valid_board(grid):
        return None
    return g(grid)


#GENERATE BOARD#
def generate_solution(randomboard):
    '''
    Generate solution creates a solution to a generated sodoku board
    '''
    '''
    This randomises numbers from the sodoku board and creates a playable
    board.
    '''
    lst = list(range(1, len(randomboard[0])))
    for i in range(len(randomboard)):
        for j in range(len(randomboard)):
            if randomboard[i][j] == 0:
                cow = random.randrange(1, len(randomboard[0]))      
                if valid(randomboard, i, j, cow):
                    randomboard[i][j] = cow
                    if not empty_fields(randomboard):
                        True
                    else:
                        if generate_solution(randomboard):
                            True 
    False
pass
