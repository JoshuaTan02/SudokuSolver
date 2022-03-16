import os, random
startingBoard = [
    [0,0,0,5,0,0,0,7,9],
    [0,0,5,0,7,9,0,4,8],
    [7,0,8,6,0,4,0,0,0],
    [0,0,7,0,0,0,0,1,2],
    [6,0,4,0,0,0,8,0,3],
    [8,2,0,0,0,0,4,0,0],
    [0,0,0,7,0,5,3,0,6],
    [4,7,0,8,3,0,1,0,0],
    [2,5,0,0,0,1,0,0,0],
]

def printBoard(board):
    for i in range(len(board)):
        if i % 3 ==0:
            print("- - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def solveBoard(board):
    square = findSquare(board)
    if not square:
        return True
    else:
        row,col = square
    # now with an empty square, we will try every possible number
    for i in range(1,10):
        if isValid(board,(row,col),i):
            # print("Trying number " + str(i) + " at position: " + str(row) + " "+str(col))
            board[row][col] = i
            if solveBoard(board):
                return True
            board[row][col]  = 0
    return False




def isValid(board,coordinate,number):
    #check the row 
    for j in range(len(board[0])):
        if board[coordinate[0]][j] == number and coordinate[1] != j:
            return False

    #check the col
    for i in range(len(board)):
        if board[i][coordinate[1]] == number and coordinate[0] != i:
            return False

    #check the 3x3 box
    #we need to mod the coordinate in order to know which box it is in
    xBox = coordinate[1]//3
    yBox = coordinate[0]//3
    for i in range(yBox*3,yBox*3+3): 
        for j in range(xBox*3,xBox*3+3):
            if (board[i][j] == number and (i,j) != coordinate):
                return False
    return True

def findSquare(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row,col)    
    return None

# def getBoard(path):
#     randomFile  = random.choice(os.listdir(path))
#     # print(randomFile)
#     board = []
#     with open(path +"\\" +randomFile, 'r') as f:
#         line = f.readline()
#         line = line.split(",", 9)
#         for i in range(0,9):
#             row = line[i]
#             row =  list(map(int,list(row)))
#             board.append(row)
#             print(row)
#     # print (board)
#     return board

startingBoard = getBoard("D:\\SudokuSolver\\sudoku_dataset")

solveBoard(startingBoard)
printBoard(startingBoard)
