from pathlib import Path

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
            
        fileName = p.name.replace(".dat",".txt")
        print(fileName)
        with open(fileName, 'w') as f:
            for row in board:
                for element in row:
                    f.write(element)
                
                f.write(',')
        

