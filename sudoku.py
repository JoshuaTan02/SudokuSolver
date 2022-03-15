board = [
    [1,2,3,0,0,0,0,0,0],
    [4,5,6,0,0,0,0,0,0],
    [7,8,9,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
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

def isValid(board,coordinate,number):
    #check the row 
    for j in range(len(board[0])):
        print(board[coordinate[0]][j])
        if board[coordinate[0]][j] == number and coordinate[1] != j:
            return False

    #check the col
    for i in range(len(board)):
        print(board[i][coordinate[1]])
        if board[i][coordinate[1]] == number and coordinate[0] != i:
            return False

    #check the 3x3 box
    #we need to mod the coordinate in order to know which box it is in
    xBox = coordinate[1]//3
    yBox = coordinate[0]//3
    print(xBox,yBox)
    for i in range(yBox*3,yBox*3+3): 
        for j in range(xBox*3,xBox*3+3):
            if (board[i][j] == number and (i,j) != coordinate):
                return False
    return True




