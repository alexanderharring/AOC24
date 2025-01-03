import math

board = []
with open("input.txt") as files:
    
    
    for line in files:
        
        board.append(line.strip())
        
guardPos = (-1, -1)    
guardDirection = "^"

obstacleMapI = {}
obstacleMapJ = {}

for i in range(len(board)):
    for j in range(len(board[0])):
        
        if board[i][j] == "^":
            guardPos = (i, j)
        elif board[i][j] == "#":
            
            if i not in obstacleMapI:
                obstacleMapI[i] = []
                
            if j not in obstacleMapJ:
                obstacleMapJ[j] = []
            
            obstacleMapI[i].append(j)
            obstacleMapJ[j].append(i)

directionMap = {}
directionMap["v"] = (1, 0)
directionMap["^"] = (-1, 0)
directionMap[">"] = (0, 1)
directionMap["<"] = (0, -1)

for k in obstacleMapJ.keys():
    obstacleMapJ[k].sort()

for k in obstacleMapI.keys():
    obstacleMapI[k].sort()

cycle = ["^", ">", "v", "<"]
cyclePos = 0

visited = set()
visited.add((guardPos, guardDirection))

def happy(p):
    return p[0] < len(board) and p[1] < len(board[0]) and p[0] >= 0 and p[1] >= 0

def bounce(P0, dirn):
    
    newPos = (-1, -1)
    
    if dirn == "^":

        for oi in range(len(obstacleMapJ[P0[1]])-1, -1, -1):
            
            if obstacleMapJ[P0[1]][oi] <= P0[0]:
                newPos = (obstacleMapJ[P0[1]][oi]+1, P0[1])
                break
            
    elif dirn == "v":
        
        for oi in range(len(obstacleMapJ[P0[1]])):
            if obstacleMapJ[P0[1]][oi] >= P0[0]:
                newPos = (obstacleMapJ[P0[1]][oi]-1, P0[1])
                break
            
    elif dirn == ">":   
        
        for oi in range(0, len(obstacleMapI[P0[0]])):
            if obstacleMapI[P0[0]][oi] >= P0[0]:
                newPos = (P0[0], obstacleMapI[P0[0]][oi]-1)
                break
            
    elif dirn == "<":
        
        for oi in range(len(obstacleMapI[P0[0]])-1, -1, -1):
            if obstacleMapI[P0[0]][oi] <= P0[0]:
                newPos = (P0[0], obstacleMapI[P0[0]][oi]+1)
                break
            
    return newPos
    
while guardPos != (-1, -1):
    visited.add((guardPos, guardDirection))
    guardPos = bounce(guardPos, guardDirection)
    cyclePos += 1
    guardDirection = cycle[cyclePos % 4]

changeCount = 0    

for iPOS in range(len(board)):
    for jPOS in range(len(board[0])):
        
        for d in range(4):
            dirn = cycle[d]

            checkPos = (iPOS + directionMap[dirn][0], jPOS + directionMap[dirn][1])
            
            if iPOS not in obstacleMapI:
                obstacleMapI[iPOS] = []
                
            if jPOS not in obstacleMapJ:
                obstacleMapJ[jPOS] = []
            
            obstacleMapI[iPOS].append(jPOS)
            obstacleMapJ[jPOS].append(iPOS)
            
            overDer = bounce(checkPos, dirn)
            
            if overDer != (-1, -1):
                
                if (overDer, cycle[(d+1)%4]) in visited:
                    
                    changeCount += 1
            
            obstacleMapI[iPOS].pop()
            obstacleMapJ[jPOS].pop()
            
            
            
print(changeCount)
            
            