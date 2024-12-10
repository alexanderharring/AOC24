import math

board = []

with open("input.txt") as files:
    
    for line in files:
        
        board.append(line.strip())

def add(i1, j1, i2, j2):
    
    return board[i1][j1] + board[i2][j2]

goodcount = 0
for i in range(1, len(board)-1):
    for j in range(1, len(board[0])-1):
        
        if board[i][j] == "A":
            
            good = True
            
            if (add(i+1, j+1, i-1, j-1) == "MS" or add(i+1, j+1, i-1, j-1) == "SM") and (add(i-1, j+1, i+1, j-1) == "SM" or add(i-1, j+1, i+1, j-1) == "MS"):
                goodcount += 1
            

print(goodcount)