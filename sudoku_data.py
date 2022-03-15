from pathlib import Path

boards = []

for p in Path('.').rglob('*.dat'):
    # print("New file")
    with p.open() as f:
        board=[]
        lines = 0

        for line in f:
            lines+=1
            if lines>2 and lines <12:
                line = line.strip()
                line = line.replace("\n","")
                newRow = line.split(" ")
                board.append(newRow)
        boards.append(board)
        fileName = p.name.replace(".dat",".txt")
        # print(fileName)
        # with open(fileName, 'w') as f:

        #     for row in board:
        #         for element in row:
        #             f.write(element)
                
        #         f.write(',')

        with open("AllBoards1.txt", 'w') as f:
            for board in boards:
                f.write("[")
                for row in board:
                    f.write("[")                    
                    for element in row:
                        f.write("\"")
                        f.write(str(element))
                        f.write("\"")
                        f.write(',')
                    f.write("]")                    
                    f.write(',')

                f.write("]")
                f.write(',')        
                f.write("\n")