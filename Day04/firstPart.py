import math

board = []

with open("input.txt") as files:
    
    for line in files:
        
        board.append(line.strip())
        
pain = []
pain.append([(0, 0), (0, 1), (0, 2), (0, 3)])
pain.append([(0, 0), (0, -1), (0, -2), (0, -3)])
pain.append([(0, 0), (1, 1), (2, 2), (3, 3)])
pain.append([(0, 0), (1, -1), (2, -2), (3, -3)])

pain.append([(0, 0), (1, 0), (2, 0), (3, 0)])
pain.append([(0, 0), (-1, 0), (-2, 0), (-3, 0)])
pain.append([(0, 0), (-1, 1), (-2, 2), (-3, 3)])
pain.append([(0, 0), (-1, -1), (-2, -2), (-3, -3)])

goodcount = 0
for i in range(0, len(board)):
    for j in range(0, len(board[0])):
        
        if board[i][j] == "X":   
            
            for path in pain:
                
                word = ""
                good = True
                
                for step in path:
                    newPos = (i + step[0], j + step[1])
                    
                    if newPos[0] >= len(board) or newPos[1] >= len(board[0]):
                        good = False
                    elif newPos[0] < 0 or newPos[1] < 0:
                        good = False
                    else:
                        word += board[newPos[0]][newPos[1]]
                        
                if good:
                    if word=="XMAS":
                        goodcount += 1
                    
                
            
print(goodcount)